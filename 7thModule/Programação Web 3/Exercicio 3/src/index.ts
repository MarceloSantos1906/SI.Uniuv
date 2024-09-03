import express from 'express';
import { TaskManager } from './TaskManager';

const app = express();
const taskManager = new TaskManager();

app.use(express.json());

app.get('/task', (req, res) => {
    const response = taskManager.getAllTasks();
    res.json(response);
});

app.get('/task/:id', (req, res) => {
    const id = parseInt(req.params.id, 10);
    const response = taskManager.getTaskById(id);
    res.json(response);
});

app.post('/post-task', (req, res) => {
    const { title, description } = req.body;
    const response = taskManager.addTask(title, description);
    res.json(response);
});

app.put('/put-task/:id', (req, res) => {
    const id = parseInt(req.params.id, 10);
    const { title, description, completed } = req.body;
    const response = taskManager.updateTask(id, title, description, completed);
    res.json(response);
});

app.patch('/patch-task/:id', (req, res) => {
    const id = parseInt(req.params.id, 10);
    const partialTask = req.body;
    const response = taskManager.partiallyUpdateTask(id, partialTask);
    res.json(response);
});

app.delete('/delete-task/:id', (req, res) => {
    const id = parseInt(req.params.id, 10);
    const response = taskManager.deleteTask(id);
    res.json(response);
});

const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Server is running at http://localhost:${PORT}`);
});
