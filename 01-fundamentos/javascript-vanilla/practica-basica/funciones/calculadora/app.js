// Calculadora simple

// sumar
const sumar = () => {
  let num1 = parseFloat(prompt("Ingrese su primer número"));
  let num2 = parseFloat(prompt("Ingrese su segundo número para sumar"));

  let resultado = num1 + num2;
  return console.log(`El resultado de su suma es: ${resultado}`);
};

// resta
const resta = () => {
  let num1 = parseFloat(prompt("Ingrese su primer número"));
  let num2 = parseFloat(prompt("Ingrese su segundo número para restar"));

  let resultado = num1 - num2;
  return console.log(`El resultado de su resta es: ${resultado}`);
};

// multiplicar
const multiplicar = () => {
  let num1 = parseFloat(prompt("Ingrese su primer número"));
  let num2 = parseFloat(prompt("Ingrese su segundo número para multiplicar"));

  let resultado = num1 * num2;
  return console.log(`El resultado de su multiplicación es: ${resultado}`);
};

// division
const division = () => {
  let num1 = parseFloat(prompt("Ingrese su primer número"));
  let num2 = parseFloat(prompt("Ingrese su segundo número para dividir"));
  let resultado = num1 / num2;
  return console.log(`El resultado de su división es: ${resultado}`);
};

function calculadora() {
  console.log("######################################");
  console.log("######### Calculadora Básica #########");
  console.log("######################################");
  console.log("Selecciona una opción válida por favor!");
  let opcionUsuario = parseInt(
    prompt("Ingresa el número que corresponde a la operación")
  );
  console.log("1. Sumar");
  console.log("2. Restar");
  console.log("3. Multiplicar");
  console.log("4. División");
  console.log("0. Salir");

  if (opcionUsuario <= 4) {
    if (opcionUsuario === 1) return sumar();
    if (opcionUsuario === 2) return resta();
    if (opcionUsuario === 3) return multiplicar();
    if (opcionUsuario === 4) return division();
  } else {
    console.log("Seleccione una opción válida por favor.");
  }
}

calculadora();
