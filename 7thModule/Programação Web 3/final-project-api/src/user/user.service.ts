import * as bcrypt from 'bcrypt';
import { JwtService } from '@nestjs/jwt';

@Injectable()
export class UserService {
  constructor(private jwtService: JwtService) {}

  async register(userData: RegisterUserDto): Promise<User> {
    const hashedPassword = await bcrypt.hash(userData.password, 10);
  }

  async validateUser(email: string, pass: string): Promise<any> {
    const user = await this.findOneByEmail(email); 
    const isPasswordValid = await bcrypt.compare(pass, user.password);
    if (user && isPasswordValid) {
      return user;
    }
    return null;
  }

  async login(user: any) {
    const payload = { username: user.email, sub: user.id };
    return {
      access_token: this.jwtService.sign(payload),
    };
  }
}
