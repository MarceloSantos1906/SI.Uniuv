import fastify from 'fastify';
import { registerBook } from './routes/register/registerBook';
import { serializerCompiler, validatorCompiler } from 'fastify-type-provider-zod';

const app = fastify();
const port = 3000;

app.setValidatorCompiler(validatorCompiler);
app.setSerializerCompiler(serializerCompiler);

app.register(registerBook);

app.get('/', async () => {
    return 'Hello World';
});

app.listen({ port: port })
    .then(() => {
        console.log('server running at http://localhost:' + port);
    })
    .catch(err => {
        console.error(err);
        process.exit(1);
    });
