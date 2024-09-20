import { ApiProperty } from '@nestjs/swagger';
import {
  IsString,
  IsNumber,
  IsOptional,
  IsNotEmpty,
  Min,
} from 'class-validator';

export class ProductResponseDto {
  @ApiProperty()
  @IsString()
  @IsNotEmpty()
  name: string;

  @ApiProperty()
  @IsString()
  @IsNotEmpty()
  description: string;

  @ApiProperty()
  @IsNumber()
  @Min(0)
  price: number;

  @ApiProperty()
  @IsNumber()
  @Min(1)
  userId: number;

  @ApiProperty()
  @IsNumber()
  @Min(1)
  categoryId: number;
}

export class CreateProductDto {
  @ApiProperty()
  @IsString()
  @IsNotEmpty()
  name: string;

  @ApiProperty()
  @IsString()
  @IsNotEmpty()
  description: string;

  @ApiProperty()
  @IsNumber()
  @Min(0)
  price: number;

  @ApiProperty()
  @IsNumber()
  @Min(1)
  userId: number;

  @ApiProperty()
  @IsNumber()
  @Min(1)
  categoryId: number;
}

export class UpdateProductDto {
  @ApiProperty()
  @IsString()
  @IsOptional()
  @IsNotEmpty()
  name?: string;

  @ApiProperty()
  @IsString()
  @IsOptional()
  @IsNotEmpty()
  description?: string;

  @ApiProperty()
  @IsNumber()
  @IsOptional()
  @Min(0)
  price?: number;

  @ApiProperty()
  @IsNumber()
  @IsOptional()
  @Min(1)
  userId?: number;

  @ApiProperty()
  @IsNumber()
  @IsOptional()
  @Min(1)
  categoryId?: number;
}
