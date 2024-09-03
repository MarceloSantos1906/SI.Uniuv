import { Body, Controller, Delete, Get, Param, Patch, Post, Put } from '@nestjs/common';
import { TasksService } from './tasks.service';
import { Task } from './task.entity';

@Controller('tasks')
export class TasksController {
    constructor(private readonly tasksService: TasksService) {}

    @Get()
    getAllTasks(): Task[] {
        return this.tasksService.getAllTasks();
    }

    @Get(':id')
    getTaskById(@Param('id') id: string): Task {
        return this.tasksService.getTaskById(Number(id));
    }

    @Post()
    createTask(@Body('title') title: string, @Body('description') description: string): Task {
        return this.tasksService.createTask(title, description);
    }

    @Put(':id')
    updateTask(
        @Param('id') id: string,
        @Body('title') title: string,
        @Body('description') description: string,
        @Body('completed') completed: boolean,
    ): Task {
        return this.tasksService.updateTask(Number(id), title, description, completed);
    }

    @Patch(':id')
    partialUpdateTask(
        @Param('id') id: string,
        @Body() partialTask: Partial<Task>,
    ): Task {
        return this.tasksService.partialUpdateTask(Number(id), partialTask);
    }

    @Delete(':id')
    deleteTask(@Param('id') id: string): void {
        this.tasksService.deleteTask(Number(id));
    }
}
