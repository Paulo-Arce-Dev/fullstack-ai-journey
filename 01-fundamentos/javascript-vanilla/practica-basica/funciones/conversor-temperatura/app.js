// Conversor de Temperatura

let opcionUsuario = prompt(
  "Ingrese lo que desea convertir. (escribe la palabra celsius o fahrenheit)"
).toLowerCase();

const celsiusAFahrenheint = () => {
  let gradosCelsius = parseFloat(
    prompt("Ingrese los gradus Celsius que desea convertir.")
  );
  let conversion = gradosCelsius * 1.8 + 32;
  return console.log(`Conversion: ${gradosCelsius} °C = ${conversion} °F`);
};

const farenheitACelsius = () => {
  let gradosFahrentheint = parseFloat(
    prompt("Ingrese los grados Fahrenheit que desea convertir.")
  );

  let conversion = (gradosFahrentheint - 32) * 0.55;
  return console.log(`Conversion: ${gradosFahrentheint} °F = ${conversion} °C`);
};

if (opcionUsuario == "celsius") {
  celsiusAFahrenheint();
} else if (opcionUsuario == "fahrenheit") {
  farenheitACelsius();
} else {
  alert(
    "Ingrese una opción correcta por favor. Verifique que la palabra escrita sea válida."
  );
}
