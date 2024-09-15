import { Injectable, NotFoundException, InternalServerErrorException } from '@nestjs/common';
import { PrismaService } from '../prisma/prisma.service';
import { Product } from '@prisma/client';

@Injectable()
export class ProductsService {
  constructor(private prisma: PrismaService) {}

  async getProducts(): Promise<Product[]> {
    try {
      return this.prisma.product.findMany();
    } catch (error) {
      throw new InternalServerErrorException('Failed to fetch products');
    }
  }

  async createProduct(data: { name: string; description: string; price: number }): Promise<Product> {
    try {
      return this.prisma.product.create({
        data,
      });
    } catch (error) {
      throw new InternalServerErrorException('Failed to create product');
    }
  }

  async updateProduct(id: number, data: { name?: string; description?: string; price?: number }): Promise<Product> {
    const product = await this.prisma.product.findUnique({
      where: { id },
    });

    if (!product) {
      throw new NotFoundException(`Product with ID ${id} not found`);
    }

    try {
      return this.prisma.product.update({
        where: { id },
        data,
      });
    } catch (error) {
      throw new InternalServerErrorException('Failed to update product');
    }
  }

  async deleteProduct(id: number): Promise<Product> {
    const product = await this.prisma.product.findUnique({
      where: { id },
    });

    if (!product) {
      throw new NotFoundException(`Product with ID ${id} not found`);
    }

    try {
      return this.prisma.product.delete({
        where: { id },
      });
    } catch (error) {
      throw new InternalServerErrorException('Failed to delete product');
    }
  }
}
