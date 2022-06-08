// Ejemplo No Async
function logUsersfromAPI() {
    let cont = 1;

    setInterval(() => {
        document.getElementsByTagName('p')[0].textContent = cont
        cont++
    }, 100);

    const boton = document.getElementsByTagName("input")[0]

    boton.addEventListener("click", () => {
        const isAsync = false
        const request = new XMLHttpRequest() // Como se hacía antes
        request.open("get", "https://jsonplaceholder.typicode.com/users", isAsync)
            // Antes no existía el último argumento si es asíncrono. Ahora se solucionaría con un true, sin embargo igual
            //quedó viejo

        request.onload = function(e) {
            const res = e.target.response
            const users = JSON.parse(res)
            console.log(users)
        }

        request.send()
    })

}

//logUsersfromAPI()

// Ejemplo Async
// Pido todos los usuarios del servidor

function getLastPostFromUserWithId(id) {
    fetch('https://jsonplaceholder.typicode.com/users')
        .then(res => res.json())
        .then(users => {
            console.log("Linea 39. Users", users)
            const [user] = users.filter(user => user.id === id)
            return user
        })
        .then(user => {
            console.log("Linea 44. User", user)
            const { id: userID, name: userName } = user
            // Es lo mismo que hacer lo siguiente:
            // const userID = user.id
            // const userName = user.name

            // Pido todos los posteos al servidor
            fetch('https://jsonplaceholder.typicode.com/posts')
                .then(unparsedResponse => unparsedResponse.json())
                .then(posts => {
                    const userPosts = posts.filter(post => post.userId == userID)
                    console.log("Linea 51. Posts", userPosts)
                    return userPosts
                })
                .then(posts => {
                    const lastPost = posts.sort((a, b) => b.Id - a.Id)[0]
                        // si pongo la a primero lo hace en forma descendiente. Así toma el primero
                    return lastPost.title
                })
                .then(lastPostTitle => {
                    console.log("Línea 59. Último Post", {
                        name: userName,
                        title: lastPostTitle
                    })
                })
                .catch(err => console.log(err))
                .finally(() => console.log('Tenemos todo lo necesario'))
        })
        .catch(err => console.log(err))
        .finally(() => console.log('Fin del ejemplo?'))
        // Ver que sale antes que termine el fetch interno
}

getLastPostFromUserWithId(5)

// Para que sea menos quilombo está el async await

// Ejemplo Heladería
let stocks = {
    fruits: ["strawberry", "grapes", "banana", "apple"],
    liquid: ["water", "ice"],
    holder: ["cone", "cup", "stick"],
    toppings: ["chocolate", "peanuts"],
};

/* let order = (idFruit, call_prod) => {

    setTimeout(() => {
        console.log(`${stocks.fruits[idFruit]} was selected`);
        call_prod();
    }, 2000);
};

let production = () => {

    setTimeout(() => {
        console.log('Production has started');

        setTimeout(() => {
            console.log('The fruit has been chopped');

            setTimeout(() => {
                console.log(`${stocks.liquid[0]} and ${stocks.liquid[1]} were added`);

                setTimeout(() => {
                    console.log('The machine has started');

                    setTimeout(() => {
                        console.log(`Icecream was placed on ${stocks.holder[0]}`);

                        setTimeout(() => {
                            console.log(`${stocks.toppings[0]} was selected`);

                            setTimeout(() => {
                                console.log('Icecream was served')
                            }, 2000)
                        }, 3000);
                    }, 2000);
                }, 1000);
            }, 1000);
        }, 2000);
    }, 0);
};

order(0, production); */

// Así se hacía cuando no existían las promesas

// Ahora con las promesas
let isShopOpen = true;

let order = (time, work) => {

    return new Promise((res, rej) => {
        if (isShopOpen) {
            setTimeout(() => {
                res(work())
            }, time)

        } else {
            rej(console.log('Our shop is closed'))
        }
    });
};

order(2000, () => console.log(`${stocks.fruits[1]} was selected`))
    .then(() => order(0, () => console.log('Production has started')))
    .then(() => order(2000, () => console.log('The fruit has been chopped')))
    .then(() => order(1000, () => console.log(`${stocks.liquid[0]} and ${stocks.liquid[1]} were added`)))
    .then(() => order(1000, () => console.log('The machine has started')))
    .then(() => order(2000, () => console.log(`Icecream was placed on ${stocks.holder[0]}`)))
    .then(() => order(3000, () => console.log(`${stocks.toppings[0]} was selected`)))
    .then(() => order(2000, () => console.log('Icecream was served')))
    .catch(() => console.log('Customer left'))
    .finally(() => console.log('Day ended, shop is close')); // Aunque esté resolved o rejected