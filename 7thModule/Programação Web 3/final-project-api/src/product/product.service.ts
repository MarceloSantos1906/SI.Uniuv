import {
  Injectable,
  NotFoundException,
  BadRequestException,
} from '@nestjs/common';
import { PrismaService } from '../prisma/prisma.service';
import { CreateProductDto } from './dto/product.dto';
import { UpdateProductDto } from './dto/product.dto';
import { Product } from '@prisma/client';

@Injectable()
export class ProductService {
  constructor(private prisma: PrismaService) {}

  async create(data: CreateProductDto): Promise<Product> {
    this.validateProductData(data);
    return this.prisma.product.create({ data });
  }

  async findAll(): Promise<Product[]> {
    return this.prisma.product.findMany();
  }

  async findOne(id: number): Promise<Product> {
    const product = await this.prisma.product.findUnique({ where: { id } });
    if (!product) {
      throw new NotFoundException('Product not found');
    }
    return product;
  }

  async update(id: number, data: UpdateProductDto): Promise<Product> {
    const product = await this.prisma.product.findUnique({ where: { id } });
    if (!product) {
      throw new NotFoundException('Product not found');
    }
    this.validateProductData(data);
    return this.prisma.product.update({ where: { id }, data });
  }

  async remove(id: number): Promise<Product> {
    const product = await this.prisma.product.findUnique({ where: { id } });
    if (!product) {
      throw new NotFoundException('Product not found');
    }
    return this.prisma.product.delete({ where: { id } });
  }

  private validateProductData(data: CreateProductDto | UpdateProductDto) {
    if (typeof data.price !== 'number' || isNaN(data.price) || data.price < 0) {
      throw new BadRequestException('Invalid price value');
    }
    if (
      typeof data.userId !== 'number' ||
      isNaN(data.userId) ||
      data.userId <= 0
    ) {
      throw new BadRequestException('Invalid userId value');
    }
    if (
      typeof data.categoryId !== 'number' ||
      isNaN(data.categoryId) ||
      data.categoryId <= 0
    ) {
      throw new BadRequestException('Invalid categoryId value');
    }
  }
}
