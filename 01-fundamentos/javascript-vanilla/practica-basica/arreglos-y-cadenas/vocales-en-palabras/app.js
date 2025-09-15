// Cuantas vocales hay en total

let palabraUsusario = prompt(
  "Ingrese una palabra para saber cuántas vocales tiene"
);

const contarVocales = (palabra) => {
  const vocales = "aáeéiíoóuú";
  let cantidadVocales = 0;

  for (const letra of palabra) {
    if (vocales.includes(letra.toLowerCase())) {
      cantidadVocales++;
    }
  }
  return `La palabra ${palabraUsusario} tiene ${cantidadVocales} vocales`;
};

console.log(contarVocales(palabraUsusario));
