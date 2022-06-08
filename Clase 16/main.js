var result = '';
var i = 0;
do {
    i += 1;
    result += i + ' ';
}
while (i > 0 && i < 5);
// Despite i == 0 this will still loop as it starts off without the test

console.log(result);

//--------------------------------------------

"use strict"

// const nombre = "José"
// const apellido = "Lopez"
// let edad = 32
// let msg = ""
// const anioNacimiento = 1989

// if (anioNacimiento > 2000) {
//   msg = "Tiene menos de 21 años"
// } else {
//   msg = "Es mayor de 21 años"
// }

// console.log(msg)

const txtTareas = document.getElementById("txtTareas")
const btnOk = document.querySelector("#btnOk")
const divContainerTareas = document.querySelector("#containerTareas")

function agregarInputs() {
    const nro = txtTareas.value
    for (let i = 0; i < nro; i++) {
        const nuevoInput = document.createElement('input')
        nuevoInput.setAttribute('type', 'text')
            //  nuevoInput.setAttribute('style', 'display: block; margin-bottom: 1rem;')
            //  nuevoInput.style.display = "block"
            //  nuevoInput.style.marginBottom = "1rem"
            //? Pendiente agregar un CSS con la clase .miInput y demás 
        nuevoInput.classList.add('miInput')
        divContainerTareas.appendChild(nuevoInput)
    }
}

btnOk.addEventListener("click", agregarInputs)