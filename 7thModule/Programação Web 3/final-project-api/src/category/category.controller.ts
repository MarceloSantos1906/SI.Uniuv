import { Controller } from '@nestjs/common';

@Controller('category')
export class CategoryController {}

@UseGuards(AuthGuard('jwt'))
@Get()
async findAll() {
  return this.productService.findAll();
}
