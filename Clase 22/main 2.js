/* // Lee el usuario 1 de la API
fetch('https://jsonplaceholder.typicode.com/users/1')
    .then(response => response.json())
    .then(data => console.log(data))

// Trata de tratar el objeto del usuario 11 que no existe
fetch('https://jsonplaceholder.typicode.com/users/11')
    .then(response => console.log(response))
    // Se observa que el ok es false, es conveniente ver esto antes que el status 404

// El catch no identifica error cuando el usuario no existe, sí lo haría si esta mal el link
fetch('https://jsonplaceholder.typicode.com/users/11')
    .then(response => response.json())
    .then(user => console.log(user))
    .catch(error => console.log("Error: ", error))
    .finally(() => console.log('Terminó la petición')) // debe estar como callback, sino se ejecuta primero */

/* const data = fetch('./data.json')
    .then(response => response.json())
    .then(parseResponse => console.log(parseResponse));

console.log(data); // Esta linea se ejecuta sin esperar */

// Para eso tengo que hacer esto:
/* let data = {}

fetch('./data.json')
    .then(response => response.json())
    .then(parseResponse => {
        data = parseResponse
        console.log(data.users[2].fullname)
    }) */


const miFetch = new Promise((resolve, reject) => {
    setTimeout(() => {
        resolve(fetch("./data.json"))
    }, 2000)
})

miFetch
    .then(res => res.text())
    .then(data => console.log(data))
    .catch(err => console.log(err))
    .finally(() => console.log('Terminó el proceso'))