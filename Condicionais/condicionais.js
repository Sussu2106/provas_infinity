let nome = prompt("Digite seu nome:");
let altura = Number(prompt("Digite sua altura em centímetros:")) / 100;
let peso = Number(prompt("Digite seu peso em kg:"));
let imc = peso / (altura ** 2);

let classificacao =
  imc < 16 ? "Baixo peso muito grave" :
  imc < 17 ? "Baixo peso grave" :
  imc < 18.5 ? "Baixo peso" :
  imc < 25 ? "Peso normal" :
  imc < 30 ? "Sobrepeso" :
  imc < 35 ? "Obesidade grau I" :
  imc < 40 ? "Obesidade grau II" :
  "Obesidade grau III";

console.log("Nome:", nome);
console.log("IMC:", imc.toFixed(2));
console.log("Classificação:", classificacao);
