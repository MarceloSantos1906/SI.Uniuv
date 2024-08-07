const express = require('express');
const cors = require('cors');

const listenPort = 3001;
const app = express();
app.use(cors({
    origin: '*'
}), express.json());


app.get('/', (request, response) => {
    response.send('Mensagem enviada!');
});

app.post('/soma', (request, response) => {
    let {n1, n2} = request.body;
	let total = Number(n1) + Number(n2);
	
	return response.json(total)
});

app.post('/imc', (request, response) => {
    let {altura, peso} = request.body;

    altura = Number(altura);
    peso = Number(peso);

    if (!altura || !peso) return response.status(401).send('Altura e peso são obrigatórios e devem ser numéricos ')

    let imc = peso / ( altura * altura );
    imc = imc.toFixed(2);
    
    let retorno = { imc: imc, resultado: ''};
    if (imc<17) {
        retorno.resultado = 'Muito abaixo do peso';
    }else if(imc<18.5){
        retorno.resultado = 'Abaixo do peso';
    }else if(imc<25){
        retorno.resultado = 'Peso normal';
    }else if(imc<30){
        retorno.resultado = 'Acima do peso';
    }else if(imc<35){
        retorno.resultado = 'Obesidade grau I';
    }else if(imc<40){
        retorno.resultado = 'Obesidade grau II';
    }else{
        retorno.resultado = 'Obesidade grau III';
    }

    return response.json(retorno);

})

app.listen(listenPort, () => { 
    console.log('listening on http://localhost:' + listenPort); 
});
