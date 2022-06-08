const nuevoLink = document.createElement('a')
nuevoLink.setAttribute('href', '#')
nuevoLink.className = "btn"
    // nuevoLink.classList.add('link', 'btn', 'active')
    // nuevoLink.className = 'link active'
nuevoLink.textContent = "Soy un link"
document.body.appendChild(nuevoLink)

if (localStorage.getItem('credentials') === null) {
    const newForm = document.createElement('form')

    newForm.innerHTML = `
    <form action="">
    <input type="text" name="user" id="user">
    <input type="password" name="password" id="password">
    <input type="submit" name="submit" id='submit'>
    </form>
    `
    document.body.appendChild(newForm);

    const btnSubmit = document.querySelector('#submit');
    const txtUser = document.querySelector('#user');
    const txtPass = document.querySelector('#password');

    btnSubmit.addEventListener('click', (e) => {
        e.preventDefault();

        //document.querySelector('a').classList.toggle('active')

        const userLoggedIn = {
            username: txtUser.value,
            password: txtPass.value
        };

        localStorage.setItem('credentials', JSON.stringify(userLoggedIn));
        window.location.reload();
    })

} else {
    const userCredentials = JSON.parse(localStorage.getItem('credentials'));

    console.log(userCredentials);
    const newParagraph = document.createElement('p');
    const btnLogout = document.createElement('input');
    btnLogout.setAttribute('type', 'button');
    btnLogout.setAttribute('value', 'Cerrar sesión');

    btnLogout.addEventListener('click', (e) => {
        localStorage.removeItem('credentials');
        window.location.href = "./index.html"
    })

    newParagraph.textContent = `Hola ${userCredentials.username}, su contraseña es ${userCredentials.password}`;

    document.body.appendChild(newParagraph);
    document.body.appendChild(btnLogout);
}