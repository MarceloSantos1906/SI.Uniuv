const container = document.getElementById("container-notas");
const template = document.getElementById("notas-template");

const adicionarNota = () => {
  const el = template.content.cloneNode(true);
  let id = (document.getElementsByClassName('nota').length + 1);
  let notaId = "nota_" + id;
  label = el.querySelectorAll("label")[0];
  label.innerText  += ` ${id}`;
  label.htmlFor = notaId;
  
  input = el.querySelectorAll("input")[0];
  input.id = notaId;
  input.addEventListener('keypress', onlyNumbers);
  input.addEventListener('change', (el) => {
    if (Number(el.target.value)>10 || Number(el.target.value)<0){
        console.error('Nota está inválida');
        el.target.classList.add('is-invalid');
        el.target.focus();
    }else{
        el.target.classList.remove('is-invalid')
        el.target.classList.add('is-valid');
    }
  });

  container.appendChild(el);
}
function onlyNumbers(event) {
  if (!['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', ','].includes(event.key)){
    event.preventDefault();
  }
}

window.addEventListener("load", () => {
  adicionarNota();
});

document.getElementById('adicionar').addEventListener('click', adicionarNota);

document.getElementById('calcular').addEventListener('click', () => {
  const notas = document.getElementsByClassName('nota');
  let soma = 0;
  for (nota of notas) {
    soma += Number(nota.value);
  }
  
  let resultado = (soma / notas.length).toFixed(2);

  const exibeResultado = (res) => {
    let divResultado = document.getElementById('resultado');
    if (divResultado === null) {
        let newDiv = document.createElement('div');
        newDiv.className = 'resultado';
        newDiv.id = 'resultado';
        container.appendChild(newDiv);
        divResultado = document.getElementById('resultado');
    }
    
    divResultado.innerText = `Resultado ${res}`;
  }

  exibeResultado(resultado);

});
