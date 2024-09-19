import { Controller } from '@nestjs/common';

@Controller('order')
export class OrderController {}

@UseGuards(AuthGuard('jwt'))
@Get()
async findAll() {
  return this.productService.findAll();
}
