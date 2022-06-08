function crearContador() {
  let contadorPrivado = 0

  return function incrementar() {
    contadorPrivado = contadorPrivado + 1
    return contadorPrivado
  }
}

// const contador = crearContador()
// console.log(contador())
// console.log(contador())
// console.log(contador())

// console.log(contador)

const miContador = (function () {
  let _contador = 0

  function incrementar() {
    return ++_contador
  }

  function decrementar() {
    return --_contador
  }

  function valor() {
    return _contador
  }

  return {
    incrementar,
    decrementar,
    valor
  }
})()

miContador.decrementar()
miContador.decrementar()
miContador.decrementar()
miContador.decrementar()
miContador.decrementar()

// console.log(miContador.incrementar())
console.log(miContador.decrementar())
