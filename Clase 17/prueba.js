function saludar() {
    let respuesta = prompt('Hola Artime, ¿Cómo fue tu día?')

    if (respuesta == 'Bien') {
        alert('Me alegro');
    } else {
        alert('Qué embole');
    }
}

const multipli = (x, y) => x * y;

console.log(multipli(10, 30));

function prueba(cb) {
    let a = 'Luis'
    cb(a);
    return a;
}

function decirNombre(nombre) {
    console.log(nombre);
}

let tempo = prueba(decirNombre);

const botoncillo = document.getElementById("pruebaArt");

/* botoncillo.onclick = () => {
    alert('Hola ' + tempo)
} */

/* botoncillo.addEventListener('click', saludar);

function saludar() {
    alert('Estoy saludando a ' + tempo)
} */

/* botoncillo.addEventListener('click', () => alert('Estoy saludando a ' + tempo)); */

botoncillo.addEventListener('click', (e) => { console.log(e.target) });