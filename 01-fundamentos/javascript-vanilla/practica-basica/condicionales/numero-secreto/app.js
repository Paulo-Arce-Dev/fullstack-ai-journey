// Juego del número secreto entre 1 y 10

// obtener numero entre 1 y 10 aleatoriamente
numeroSecreto = parseInt(Math.random() * 10) + 1;

// obtener numero del usuario
opcionUsuario = parseInt(prompt("Adivina el número secreto"));

if (numeroSecreto === opcionUsuario) {
  alert(`Felicitaciones adivinaste el número secreto. Era ${numeroSecreto}`);
} else {
  alert(`Lo siento el número secreto era: ${numeroSecreto}`);
}
