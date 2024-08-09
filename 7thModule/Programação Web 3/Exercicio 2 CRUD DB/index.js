const express = require('express');
const productsController = require('./productsController');

const listenPort = 3000;
const app = express();
app.use(express.json());

app.get('/', (request, response) => {
    response.send('Hello World!');
});

app.use('/products', productsController);

app.listen(listenPort, () => {
    console.log("listening on http://localhost:" + listenPort);
});
