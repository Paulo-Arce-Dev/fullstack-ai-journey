// Cajero automático

let montoTotal = parseFloat(
  prompt("Ingrese el monto total de su dinero en su cuenta")
);
console.log(`Saldo total de la cuenta: ${montoTotal}`);

let montoDescontar = parseFloat(prompt("Ingrese cuanto quiere gastar"));
console.log(`Gasto del usuario a descontar: ${montoDescontar}`);

while (montoTotal >= montoDescontar) {
  montoTotal = montoTotal - montoDescontar;
  console.log(`Su saldo actual es: ${montoTotal}`);

  montoDescontar = parseFloat(prompt("Ingrese cuanto quiere gastar"));
  console.log(`Gasto del usuario: ${montoDescontar}`);
}
console.log("Saldo insuficiente.");
