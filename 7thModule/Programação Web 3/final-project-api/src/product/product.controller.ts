import { Controller } from '@nestjs/common';

@Controller('product')
export class ProductController {}

@UseGuards(AuthGuard('jwt'))
@Get()
async findAll() {
  return this.productService.findAll();
}
