const connection = require('./db-mysql');

const getAll = async() => {
    let db = await connection();
    let [ rows ] = await db.query('SELECT * FROM products');
    return rows;
}

const get = async(id) => {
    let db = await connection();
    let [ products ] = await db.query(`SELECT * FROM products WHERE id = ${id}`);
    return(products[0] ?? null);
}

const post = async(name, price) => {
    price = parseFloat(price);
    if (name == '' || price == '' || price < 0) {
        return false;
    }

    const product = {
        name,
        price
    }

    try {
        let db = await connection();

        dbResponse = await db.query("INSERT INTO products (name, price) VALUES (?, ?)", [ product.name, product.price ]);

        if (dbResponse[0].affectedRows == 1) {
            product.id = dbResponse[0].insertId;
            console.log("C");
        }
    } catch (e) {
        console.log(e);
        return false;
    }

    return product;
}

const patch = async (id, name, price) => {
    price = parseFloat(price);
    if (name == '' || price == '' || price < 0) {
        return false;
    }

    try {
        let db = await connection();

        let product = await find(id);
        if (!product) {
            return false;
        }

        product.name = name;
        product.price = price;

        dbResponse = await db.query('UPDATE products SET ? WHERE id = ?', [ product, product.id ]);

        if (dbResponse[0].affectedRows == 1) {
            return product;
        }
    } catch(e) {
        console.log(e);
        return false;
    }
}

const remove = async(id) => {
    try {
        let db = await connection();

        let product = await find(id);
        if (!product) {
            return false;
        }

        dbResponse = await db.query('DELETE FROM products WHERE id = ?', [ id ]);

        return (dbResponse[0].affectedRows);
    } catch(e) {
        return false;
    }
}

module.exports = {
    getAll,
    get,
    post,
    patch,
    remove
}