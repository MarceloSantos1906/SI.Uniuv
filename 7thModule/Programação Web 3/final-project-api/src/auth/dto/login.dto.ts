import { ApiProperty } from '@nestjs/swagger';
import { IsNotEmpty, IsString } from 'class-validator';

export class ReturnLoginDto {
  @ApiProperty()
  @IsString()
  @IsNotEmpty()
  access_token: string;
}

export class LoginDto {
  @ApiProperty()
  @IsString()
  @IsNotEmpty()
  email: string;
  @ApiProperty()
  @IsString()
  @IsNotEmpty()
  password: string;
}
