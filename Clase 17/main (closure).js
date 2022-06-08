function crearContador() {
    let conta = 0;

    return function incrementar() {
        conta = conta + 1;
        return conta;
    }
}

/* const contador = crearContador();

console.log(contador());
console.log(contador());
console.log(contador());
console.log(contador()); */

const miContador = (function() {
    let conta = 0;

    function incrementar() {
        return conta++;
    }

    function decrementar() {
        return --conta;
    }

    function valor() {
        return conta;
    }

    return {
        incrementar;
        decrementar;
        valor;
    }

})()

miContador.decrementar();
miContador.decrementar();
miContador.decrementar();
miContador.decrementar();