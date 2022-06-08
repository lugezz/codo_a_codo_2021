const usuarios = [
    { nombre: 'Pedro', apellido: 'Pérez' },
    { nombre: 'Lucas', apellido: 'Gómez' },
    { nombre: 'Gastón', apellido: 'Pérez' },
]

for (let i = 0; i < usuarios.length; i++) {
    console.log(usuarios[i].nombre);
}

// ---------------

for (const usuario in usuarios) {
    console.log(usuarios[usuario].nombre)
};

for (const usuario of usuarios) {
    console.log(usuario.nombre);
}

// ---------------

for (let usuario in usuarios) {
    console.log(`Nombre de usuarios.${usuario} = ${usuarios[usuario].nombre} y Apellido de usuarios.${usuario} = ${usuarios[usuario].apellido} `);
}

let frutas = ["Manzana", "Plátano", "Naranja"];

for (i = 0; i < 3; i++) {
    console.log(frutas[i]);
}