// Tabla de multiplicar

let numTablaMultiplicar = parseInt(
  prompt("Ingresa el número del 1 al 10 que desea saber su tabla")
);

for (let i = 0; i <= 10; i++) {
  let multiplicacion = numTablaMultiplicar * i;
  console.log(`${numTablaMultiplicar} X ${i} = ${multiplicacion}`);
}
