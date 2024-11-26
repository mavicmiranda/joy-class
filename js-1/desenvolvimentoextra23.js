let numerosDaSorte = [7, 3, 28, 27, 13, 14];

numerosDaSorte.forEach(numero => {
    if (numero % 2 === 0 && numero < 50) {
        console.log(`${numero} é par e menor que 50`);
    } else if (numero < 50) {
        console.log(`${numero} é menor que 50`);
    } else {
        console.log(`${numero} é maior que 50`);
    }
});
