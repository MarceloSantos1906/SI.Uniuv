import {
  Body,
  Controller,
  Delete,
  Get,
  Param,
  Post,
  Put,
} from '@nestjs/common';
import { OrderService } from './order.service';
import { Order } from '@prisma/client';
import {
  UpdateOrderDto,
  OrderResponseDto,
  CreateOrderDto,
} from './dto/order.dto';
import { ApiResponse, ApiTags } from '@nestjs/swagger';

@ApiTags('Orders')
@Controller('orders')
export class OrderController {
  constructor(private readonly orderService: OrderService) {}

  @Post()
  @ApiResponse({
    status: 201,
    type: OrderResponseDto,
  })
  async register(@Body() createOrderDto: CreateOrderDto) {
    return this.orderService.createOrder(createOrderDto);
  }

  @Get()
  @ApiResponse({
    status: 200,
    type: [OrderResponseDto],
  })
  async findAll() {
    return this.orderService.findAll();
  }

  @Get(':id')
  @ApiResponse({
    status: 200,
    type: OrderResponseDto,
  })
  async findOne(@Param('id') id: number): Promise<Order> {
    return this.orderService.findOne(Number(id));
  }

  @Put(':id')
  @ApiResponse({
    status: 200,
    type: OrderResponseDto,
  })
  @ApiResponse({
    status: 404,
    description: 'Order not found.',
  })
  async update(
    @Param('id') id: string,
    @Body() updateOrderDto: UpdateOrderDto,
  ) {
    return this.orderService.update(Number(id), updateOrderDto);
  }

  @Delete(':id')
  @ApiResponse({
    status: 200,
    type: OrderResponseDto,
  })
  @ApiResponse({
    status: 404,
    description: 'Order not found.',
  })
  async remove(@Param('id') id: string) {
    return this.orderService.remove(Number(id));
  }
}
