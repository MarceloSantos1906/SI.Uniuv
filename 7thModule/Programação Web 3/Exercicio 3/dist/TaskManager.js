"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.TaskManager = void 0;
class TaskManager {
    constructor() {
        this.tasks = [];
    }
    getAllTasks() {
        return {
            success: true,
            message: "All tasks retrieved successfully.",
            data: this.tasks,
        };
    }
    addTask(title, description) {
        const newTask = {
            id: this.tasks.length + 1,
            title,
            description,
            completed: false,
        };
        this.tasks.push(newTask);
        return {
            success: true,
            message: "Task added successfully.",
            data: newTask,
        };
    }
}
exports.TaskManager = TaskManager;
