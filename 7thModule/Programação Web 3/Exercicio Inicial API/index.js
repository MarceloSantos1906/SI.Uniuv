const express = require('express');
const app = express();
const port = 3000;

app.use(express.json());


//  GETS    //

//Hello World
app.get('/', ( request, response) =>{
    //username = require("os").userInfo().username;
    response.send("Hello World");
})

//  POSTS   //

//average
app.post('/average', (request, response) => {
    const values = request.body.values;
    if (!Array.isArray(values) || values.length === 0) {
        return response.status(400).json({ error: 'Please provide an array of numbers.' });
    }
    const sum = values.reduce((acc, val) => acc + val, 0);
    const average = sum / values.length;
    response.json({ average: average });
});

//Celsius to Fahrenheit conversion
app.post('/tempConvCF', (request, response) => {
    const tempC = request.body.tempC;
    if (typeof tempC !== 'number') {
        return response.status(400).json({ error: 'Please provide a number.' });
    }
    tempF = (tempC*1.8) + 32;
    response.json({ tempConvCF: tempF });
})
//Celsius to Kelvin conversion
app.post('/tempConvCK', (request, response) => {
    const tempC = request.body.tempC;
    if (typeof tempC !== 'number') {
        return response.status(400).json({ error: 'Please provide a number.' });
    }
    tempK = tempC+273.15;
    response.json({ tempConvCK: tempK });
})
//Celsius to Rankine conversion
app.post('/tempConvCR', (request, response) => {
    const tempC = request.body.tempC;
    if (typeof tempC !== 'number') {
        return response.status(400).json({ error: 'Please provide a number.' });
    }
    tempR = (tempC+273.15)*(9/5);
    response.json({ tempConvCR: tempR });
})

//Fahrenheit to Celsius conversion
app.post('/tempConvFC', (request, response) => {
    const tempF = request.body.tempF;
    if (typeof tempF !== 'number') {
        return response.status(400).json({ error: 'Please provide a number.' });
    }
    tempC = (tempF-32)/1.8;
    response.json({ tempConvFC: tempC });
})
//Fahrenheit to Kelvin conversion
app.post('/tempConvFK', (request, response) => {
    const tempF = request.body.tempF;
    if (typeof tempF !== 'number') {
        return response.status(400).json({ error: 'Please provide a number.' });
    }
    tempK = (tempF+459.67)*(5/9);
    response.json({ tempConvFK: tempK });
})
//Fahrenheit to Rankine conversion
app.post('/tempConvFR', (request, response) => {
    const tempF = request.body.tempF;
    if (typeof tempF !== 'number') {
        return response.status(400).json({ error: 'Please provide a number.' });
    }
    tempR = tempF+459.67;
    response.json({ tempConvFR: tempR });
})

//Kelvin to Celsius conversion
app.post('/tempConvKC', (request, response) => {
    const tempK = request.body.tempK;
    if (typeof tempK !== 'number') {
        return response.status(400).json({ error: 'Please provide a number.' });
    }
    tempC = tempK-273.15;
    response.json({ tempConvKC: tempC });
})
//Kelvin to Fahrenheit conversion
app.post('/tempConvKF', (request, response) => {
    const tempK = request.body.tempK;
    if (typeof tempK !== 'number') {
        return response.status(400).json({ error: 'Please provide a number.' });
    }
    tempF = (tempK*(9/5))-459.67;
    response.json({ tempConvKF: tempF });
})
//Kelvin to Rankine Conversion
app.post('/tempConvKR', (request, response) => {
    const tempK = request.body.tempK;
    if (typeof tempK !== 'number') {
        return response.status(400).json({ error: 'Please provide a number.' });
    }
    tempR = tempK*(9/5);
    response.json({ tempConvKR: tempR });
})

//Rankine to Celsius conversion
app.post('/tempConvRC', (request, response) => {
    const tempR = request.body.tempR;
    if (typeof tempR !== 'number') {
        return response.status(400).json({ error: 'Please provide a number.' });
    }
    tempC = (tempR*(5/9))-273.15;
    response.json({ tempConvRC: tempC });
})
//Rankine to Fahrenheit conversion
app.post('/tempConvRF', (request, response) => {
    const tempR = request.body.tempR;
    if (typeof tempR !== 'number') {
        return response.status(400).json({ error: 'Please provide a number.' });
    }
    tempF = tempR-459.67;
    response.json({ tempConvRF: tempF });
})
//Rankine to Kelvin Conversion
app.post('/tempConvRK', (request, response) => {
    const tempR = request.body.tempR;
    if (typeof tempR !== 'number') {
        return response.status(400).json({ error: 'Please provide a number.' });
    }
    tempK = tempR*(9/5);
    response.json({ tempConvRK: tempK });
})

//age
const calculateAge = (birthDate) => {
    const today = new Date();
    const birthDateParts = birthDate.split('/');
    const birthDay = parseInt(birthDateParts[0]);
    const birthMonth = parseInt(birthDateParts[1]) - 1;
    const birthYear = parseInt(birthDateParts[2]);
    const birth = new Date(birthYear, birthMonth, birthDay);
    let ageYears = today.getFullYear() - birth.getFullYear();
    let ageMonths = today.getMonth() - birth.getMonth();
    let ageDays = today.getDate() - birth.getDate();
    if (ageMonths < 0 || (ageMonths === 0 && ageDays < 0)) {
        ageYears--;
        ageMonths += 12;
    }
    if (ageDays < 0) {
        const previousMonth = new Date(today.getFullYear(), today.getMonth(), 0);
        ageDays += previousMonth.getDate();
        ageMonths--;
    }
    return { years: ageYears, months: ageMonths, days: ageDays };
};
app.post('/age', (request, response) => {
    const birthDate = request.body.birthDate;
    const datePattern = /^\d{2}\/\d{2}\/\d{4}$/;
    if (!datePattern.test(birthDate)) {
        return response.status(400).json({ error: 'Please provide a valid birth date in the format dd/mm/yyyy.' });
    }
    const age = calculateAge(birthDate);
    response.json({ age: age });
});

//even or oddfunction
app.post('/evenOrOdd', (request, response) => {
    const value = request.body.value;
    if (typeof value !== 'number') {
        return response.status(400).json({ error: 'Please provide a number.' });
    }
    if (value % 2 == 0) {
        response.json({ value: "even" });
    } else {
        response.json({ value: "odd" });
    }
})

//factorial
const factorial = (n) => {
    if (n < 0) return undefined;
    if (n === 0) return 1;
    return n === 1 ? 1 : n * factorial(n - 1);
};
app.post('/factorial', (request, response) => {
    const number = request.body.number;
    if (typeof number !== 'number' || number < 0) {
        return response.status(400).json({ error: 'Please provide a non-negative integer.' });
    }
    const result = factorial(number);
    response.json({ factorial: result });
});

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
