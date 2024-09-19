import { Controller, Get, Post, Body } from '@nestjs/common';
import { CreateProductDto } from './product/dto/create-product.dto';
import { ProductService } from './product/product.service';
import { CreateCategoryDto } from './category/dto/create-category.dto';
import { CategoryService } from './category/category.service';

@Controller('products')
export class ProductController {
  constructor(private readonly productService: ProductService) {}

  @Post()
  async create(@Body() createProductDto: CreateProductDto) {
    return this.productService.create(createProductDto);
  }

  @Get()
  async findAll() {
    return this.productService.findAll();
  }
}

@Controller('categories')
export class CategoryController {
  constructor(private readonly categoryService: CategoryService) {}

  @Post()
  async create(@Body() createCategoryDto: CreateCategoryDto) {
    return this.categoryService.createCategory(createCategoryDto);
  }

  @Get()
  async findAll() {
    return this.categoryService.findAll();
  }
}
