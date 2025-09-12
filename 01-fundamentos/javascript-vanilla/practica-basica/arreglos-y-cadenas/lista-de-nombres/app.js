// Lista de nombres ordenados

// nombre ingresado por el usuario
let nombreUsuario = prompt(
  "Ingrese el nombre y apellido de la persona para agregar a la lista"
);
console.log(nombreUsuario);

// lista de nombres
const listaNombres = [];

// agregando el nombre del usuario a la lista
listaNombres.push(nombreUsuario);
console.log(listaNombres);

// lista en orden alfabético
listaNombres.sort();
console.log(listaNombres);
