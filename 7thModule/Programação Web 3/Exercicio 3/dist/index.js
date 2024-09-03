"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const express_1 = __importDefault(require("express"));
const TaskManager_1 = require("./TaskManager");
const app = (0, express_1.default)();
const taskManager = new TaskManager_1.TaskManager();
app.use(express_1.default.json());
app.get('/tasks', (req, res) => {
    const response = taskManager.getAllTasks();
    res.json(response);
});
app.post('/tasks', (req, res) => {
    const { title, description } = req.body;
    const response = taskManager.addTask(title, description);
    res.json(response);
});
const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Server is running at http://localhost:${PORT}`);
});
