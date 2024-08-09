const { response } = require('express');
const productsService = require('./productsService');
const productsController = require('express').Router();

const sendResponse = async (response, id, message) => {
    try {
        return response.status(id).send(message);
    } catch(e) {
        console.log(e);
        return false
    }
}
const sendError = async (response, errorId, message) => {
    try {
        response.status(errorId).send(`
            <html>
                <body>
                    <img src="${message}" style = "height:100%; margin:auto; display:block"/>
                </body>
            </html>
        `);
    } catch (e) {
        console.error(e);
        return false;
    }
};
productsController.get('/', async(request, response = '') => {
    products = await productsService.getAll();
    return response.json(products);
});

productsController.get('/:id', async(request, response = '') => {
    try {
        product = await productsService.get(request.params.id)
        if(!product) {
            return sendError(response, 404, 'https://http.cat/404');
        }
        return response.json(product);
    } catch(e) {
        return sendError(response, 500, 'https://http.cat/500');
    }
});

productsController.post('/', async(request, response) => {
    let {name, price} = request.body;
    product = await productsService.post(name, price);
    if(!product) {
        return sendError(response, 401, 'https://http.cat/401');
    }
    return response.json(product);
});

productsController.patch('/:id', async(request, response = '') => {
    let { name, price } = request.body;
    let { id } = request.params;
    product = await productsService.patch(id, name, price);
    if(!product) {
        return sendError(response, 401, 'https://http.cat/401');
    }
    return response.json(product);
});

productsController.delete('/:id', async(request, response = '') => {
    const { id } = request.params;
    if (await productsService.remove(id)) {
        return sendResponse(response, 204, 'https://http.cat/204');
    } else if (!product) {
        return sendError(response, 404, 'https://http.cat/404');
    }
    return response.json(product);
});

module.exports = productsController;