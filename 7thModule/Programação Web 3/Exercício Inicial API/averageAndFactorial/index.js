const express = require('express');
const app = express();
const port = 3000;

app.use(express.json());

app.get('/', ( request, response) =>{
    response.send('Invalid path')
})

app.post('/average', (req, res) => {
    const values = req.body.values;

    if (!Array.isArray(values) || values.length === 0) {
        return res.status(400).json({ error: 'Please provide an array of numbers.' });
    }

    const sum = values.reduce((acc, val) => acc + val, 0);
    const average = sum / values.length;

    res.json({ average: average });
});

const factorial = (n) => {
    if (n < 0) return undefined;
    if (n === 0) return 1;
    return n === 1 ? 1 : n * factorial(n - 1);
};

app.post('/factorial', (req, res) => {
    const number = req.body.number;

    if (typeof number !== 'number' || number < 0) {
        return res.status(400).json({ error: 'Please provide a non-negative integer.' });
    }

    const result = factorial(number);

    res.json({ factorial: result });
});

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
