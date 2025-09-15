// Cuantas vocales hay en total

let palabraUsusario = prompt(
  "Ingrese una palabra para saber cuántas vocales tiene"
);

// funcion para contar las vocales
const contarVocales = (palabra) => {
  const vocales = "aáeéiíoóuú";
  let cantidadVocales = 0;

  // recorrer cada letra de la palabra
  for (const letra of palabra) {
    // buscamos coincidencia de vocales y la palabra
    if (vocales.includes(letra.toLowerCase())) {
      cantidadVocales++;
    }
  }
  return `La palabra ${palabraUsusario} tiene ${cantidadVocales} vocales`;
};

// mostrando resultado en consola
console.log(contarVocales(palabraUsusario));
