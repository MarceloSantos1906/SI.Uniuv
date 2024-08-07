const resultDisplay = document.querySelector('.result');
const spinBtn = document.querySelector('.spin-btn');
const betAmountInput = document.getElementById('bet-amount');
const walletDisplay = document.getElementById('wallet');

const redNumbers = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36];
const blackNumbers = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35];

let chips = 100; // Starting amount of chips
let intervalo = 10;
let numero_anterior = 0;

updateWalletDisplay();

function startRoulette(intervalo) {
    let randomNumber = generateRandomNumber();
    const betAmount = parseFloat(betAmountInput.value);
    if (betAmount > chips) {
        alert('Saldo insuficiente!');
        return;
    }

    if (numero_anterior === randomNumber){
        startRoulette(intervalo);
    }
    numero_anterior = randomNumber;
    updateResultDisplay(randomNumber);

    if (intervalo < 200){
        setTimeout(startRoulette, intervalo, intervalo + 2);
    } else {
        let payout = evaluateBet(randomNumber, betAmount);
        console.log(payout);
        chips += payout;
        updateWalletDisplay();
        updateResultDisplay(randomNumber);
        spinBtn.disabled = false;
        document.getElementById('idk').innerText = (
            `Você apostou ${betAmount} fichas. ${payout >= 0 ? 'Você ganhou ' + payout + ' fichas!' : 'Você perdeu ' + (-payout) + ' fichas.'}`);
    }
}


function updateResultDisplay(number) {
    resultDisplay.textContent = number;

    // Verificar cor do número
    if (redNumbers.includes(number)) {
        resultDisplay.style.color = 'red';
    } else if (blackNumbers.includes(number)) {
        resultDisplay.style.color = 'black';
    } else {
        resultDisplay.style.color = 'green'; // Zero é verde
    }
}

function generateRandomNumber() {
    return Math.floor(Math.random() * 37); // Gera números entre 0 e 36
}

function evaluateBet(winningNumber, betAmount) {
    const selectedBet = getSelectedBet();
    return payoutBet(selectedBet, winningNumber, betAmount);
}

function getSelectedBet() {
    const betType = document.querySelector('input[name="bet"]:checked').value;
    switch (betType) {
        case 'number':
            return {
                type: 'number',
                number: parseInt(document.getElementById('number-input').value)
            };
        case 'dozen':
            return {
                type: 'dozen',
                dozen: document.getElementById('dozen-select').value
            };
        case 'range':
            return {
                type: 'range',
                range: document.getElementById('range-select').value
            };
        case 'color':
            return {
                type: 'color',
                color: document.getElementById('color-select').value
            };
        case 'evenOdd':
            return {
                type: 'evenOdd',
                choice: document.getElementById('evenOdd-select').value
            };
        case 'column':
            return {
                type: 'column',
                column: document.getElementById('column-select').value
            };
    }
}

function payoutBet(selectedBet, winningNumber, betAmount) {
    let payout = 0;
    switch (selectedBet.type) {
        case 'number':
            if (winningNumber === selectedBet.number) {
                payout = betAmount * 35;
            } else {
                payout = (betAmount * 35) * -1;
            }
            break;
        case 'color':
            if ((selectedBet.color === 'red' && redNumbers.includes(winningNumber)) ||
                (selectedBet.color === 'black' && blackNumbers.includes(winningNumber))) {
                payout = betAmount; // Pagamento igual à aposta
            } else {
                payout = (betAmount) * -1;
            }
            break;
        case 'evenOdd':
            if ((selectedBet.choice === 'even' && winningNumber % 2 === 0) ||
                (selectedBet.choice === 'odd' && winningNumber % 2 !== 0)) {
                payout = betAmount; // Pagamento igual à aposta
            } else {
                payout = (betAmount) * -1;
            }
            break;
        case 'range':
            if ((selectedBet.range === 'low' && winningNumber >= 1 && winningNumber <= 18) ||
                (selectedBet.range === 'high' && winningNumber >= 19 && winningNumber <= 36)) {
                payout = betAmount; // Pagamento igual à aposta
            } else {
                payout = (betAmount) * -1;
            }
            break;
        case 'dozen':
            if ((selectedBet.dozen === 'first' && winningNumber >= 1 && winningNumber <= 12) ||
                (selectedBet.dozen === 'second' && winningNumber >= 13 && winningNumber <= 24) ||
                (selectedBet.dozen === 'third' && winningNumber >= 25 && winningNumber <= 36)) {
                payout = betAmount * 2; // Pagamento igual a 2 vezes a aposta
            } else {
                payout = (betAmount * 2) * -1;
            }
            break;
        case 'column':
            if ((selectedBet.column === 'first' && (winningNumber - 1) % 3 === 0) ||
                (selectedBet.column === 'second' && winningNumber % 3 === 0) ||
                (selectedBet.column === 'third' && (winningNumber + 1) % 3 === 0)) {
                payout = betAmount * 2; // Pagamento igual a 2 vezes a aposta
            } else {
                payout = (betAmount * 2) * -1;
            }
            break;
    }
    return payout; // Retornar lucro ou prejuízo (aposta deduzida)
}


function updateWalletDisplay() {
    walletDisplay.textContent = `Saldo: ${chips} fichas`;
}

spinBtn.addEventListener('click', () => {
    spinBtn.disabled = true; // Desabilitar botão enquanto a roleta estiver girando
    startRoulette(intervalo);
});
