// sumar
const sumar = () => {
  let num1 = parseFloat(prompt("Ingrese su primer número"));
  let num2 = parseFloat(prompt("Ingrese su segundo número para sumar"));

  let resultado = num1 + num2;
  return console.log(`El resultado de su suma es: ${resultado}`);
};

export default sumar;
