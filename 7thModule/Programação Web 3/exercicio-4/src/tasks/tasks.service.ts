import { Injectable, NotFoundException } from '@nestjs/common';
import { Task } from './task.entity';

@Injectable()
export class TasksService {
    private tasks: Task[] = [];

    getAllTasks(): Task[] {
        return this.tasks;
    }

    getTaskById(id: number): Task {
        const task = this.tasks.find((task) => task.id === id);
        if (!task) {
            throw new NotFoundException(`Task with ID ${id} not found`);
        }
        return task;
    }

    createTask(title: string, description: string): Task {
        const newTask: Task = {
            id: this.tasks.length + 1,
            title,
            description,
            completed: false,
        };
        this.tasks.push(newTask);
        return newTask;
    }

    updateTask(id: number, title: string, description: string, completed: boolean): Task {
        const task = this.getTaskById(id);
        task.title = title;
        task.description = description;
        task.completed = completed;
        return task;
    }

    partialUpdateTask(id: number, partialTask: Partial<Task>): Task {
        const task = this.getTaskById(id);
        task.title = partialTask.title ?? task.title;
        task.description = partialTask.description ?? task.description;
        task.completed = partialTask.completed ?? task.completed;
        return task;
    }

    deleteTask(id: number): void {
        const index = this.tasks.findIndex((task) => task.id === id);
        if (index === -1) {
            throw new NotFoundException(`Task with ID ${id} not found`);
        }
        this.tasks.splice(index, 1);
    }
}
