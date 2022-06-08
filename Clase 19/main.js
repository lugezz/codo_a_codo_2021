let nombrez = "Artime";
let author = 'Mozart'

console.log(...nombrez);
console.log(nombrez.substring(1, 4));

console.log(`My favorite poem is ${nombrez} by ${author}.`);

//! Elementos del DOM
const addPhone = document.querySelector("#addPhone")
const addEmail = document.querySelector("#addEmail")
    // const inputGroup = document.querySelector(".input-group-phone")

//! Handlers
const handleClick = function(event, type, name, value) {
    const newInputGroup = document.createElement("div")
    newInputGroup.className = "input-group"

    newInputGroup.innerHTML = `
    <label for="${name}">${value}</label>
    <input type="${type}" name="${name}" id="${name}" />
  `

    const parentElement = event.target.parentElement
    const button = event.target

    // inputGroup.insertBefore(newInputGroup, addPhone)
    parentElement.insertBefore(newInputGroup, button)
}

//! Event listeners
// addPhone.addEventListener("click", function (e) {
//   handleClick(e, "tel", "phone", "Teléfono")
// })
// addEmail.addEventListener("click", function (e) {
//   handleClick(e, "email", "email", "Email")
// })

document.body.addEventListener("click", e => {
    const targets = ["addEmail", "addPhone"]

    // if (!(e.target.id === "addEmail") && !(e.target.id === "addPhone")) return
    if (!targets.includes(e.target.id)) return


    e.target.id === "addPhone" ?
        handleClick(e, "tel", "phone", "Teléfono") :
        handleClick(e, "email", "email", "Email")
})

//! Submit
/* const form = document.querySelector("form"); */


const handleSubmit = (e) => {
    e.preventDefault()

    let formContacto = document.forms['contacto'];
    let formData = new FormData(formContacto)

    const configur = {
        method: 'POST',
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: new URLSearchParams(formData).toString()
    }

    fetch('/', configur).then(() => console.log('El formulario se envió correctamente'))
        .catch((error) => alert(error))
}

document.querySelector("form").addEventListener("submit", handleSubmit);

// form.addEventListener("submit", e => {
//     e.preventDefault();

//     console.log("Submit en formulario");

//     /* const nombre = document.querySelector("#name").value; */

//     if (nombre.length === 0) {
//         alert('El campo nombre está vacío');
//         return;
//     }

//     const telefono = document.querySelector("#phone").value;
//     const regex = /^[0-9]+$/g;
//     if (!regex.test(telefono)) {
//         alert('El campo teléfono contiene caracteres inválidos');
//         return;
//     }


//     console.log('El formulario se envió correctamente')
// })