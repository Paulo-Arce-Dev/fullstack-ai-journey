// Juego número par o impar
numeroUsuario = parseInt(prompt("Ingrese un numero mayor a cero por favor!"));

if (numeroUsuario > 0) {
  if (numeroUsuario % 2 === 0) {
    alert(`El número ${numeroUsuario} es: Par`);
  } else {
    alert(`El número ${numeroUsuario} es: Impar`);
  }
} else {
  alert("Ingrese un núemero mayor a cero por favor");
}
