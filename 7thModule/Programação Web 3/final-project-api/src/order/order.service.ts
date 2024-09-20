import { Injectable, NotFoundException } from '@nestjs/common';
import { PrismaService } from '../prisma/prisma.service';
import { CreateOrderDto } from './dto/order.dto';
import { Order } from '@prisma/client';
import { UpdateOrderDto } from './dto/order.dto';

@Injectable()
export class OrderService {
  constructor(private prisma: PrismaService) {}

  async createOrder(data: CreateOrderDto): Promise<Order> {
    return this.prisma.order.create({
      data: {
        productId: data.productId,
        quantity: data.quantity,
        customer: data.customer,
      },
    });
  }

  async findAll(): Promise<Order[]> {
    return this.prisma.order.findMany();
  }

  async findOne(id: number): Promise<Order> {
    return this.prisma.order.findUnique({ where: { id } });
  }

  async update(id: number, data: UpdateOrderDto): Promise<Order> {
    const idExists = await this.prisma.order.findUnique({
      where: { id: id },
    });

    if (!idExists) {
      throw new NotFoundException('Invalid id.');
    }

    return this.prisma.order.update({ where: { id }, data });
  }

  async remove(id: number): Promise<Order> {
    const idExists = await this.prisma.order.findUnique({
      where: { id: id },
    });

    if (!idExists) {
      throw new NotFoundException('Invalid id.');
    }

    return this.prisma.order.delete({ where: { id } });
  }
}
