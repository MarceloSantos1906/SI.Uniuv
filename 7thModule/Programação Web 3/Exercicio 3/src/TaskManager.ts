export interface Task {
    id: number;
    title: string;
    description: string;
    completed: boolean;
}

export type RouteResponse = {
    success: boolean;
    message: string;
    data?: Task | Task[];
};

export class TaskManager {
    private tasks: Task[] = [];

    public getAllTasks(): RouteResponse {
        return {
            success: true,
            message: "All tasks retrieved successfully.",
            data: this.tasks,
        };
    }

    public getTaskById(id: number): RouteResponse {
        const task = this.tasks.find(t => t.id === id);
        if (task) {
            return {
                success: true,
                message: "Task retrieved successfully.",
                data: task,
            };
        }
        return {
            success: false,
            message: `Task with id ${id} not found.`,
        };
    }

    public addTask(title: string, description: string): RouteResponse {
        const newTask: Task = {
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

    public updateTask(id: number, title: string, description: string, completed: boolean): RouteResponse {
        const task = this.tasks.find(t => t.id === id);
        if (task) {
            task.title = title;
            task.description = description;
            task.completed = completed;
            return {
                success: true,
                message: "Task updated successfully.",
                data: task,
            };
        }
        return {
            success: false,
            message: `Task with id ${id} not found.`,
        };
    }

    public partiallyUpdateTask(id: number, partialTask: Partial<Task>): RouteResponse {
        const task = this.tasks.find(t => t.id === id);
        if (task) {
            task.title = partialTask.title ?? task.title;
            task.description = partialTask.description ?? task.description;
            task.completed = partialTask.completed ?? task.completed;
            return {
                success: true,
                message: "Task partially updated successfully.",
                data: task,
            };
        }
        return {
            success: false,
            message: `Task with id ${id} not found.`,
        };
    }

    public deleteTask(id: number): RouteResponse {
        const index = this.tasks.findIndex(t => t.id === id);
        if (index !== -1) {
            const deletedTask = this.tasks.splice(index, 1)[0];
            return {
                success: true,
                message: "Task deleted successfully.",
                data: deletedTask,
            };
        }
        return {
            success: false,
            message: `Task with id ${id} not found.`,
        };
    }
}
