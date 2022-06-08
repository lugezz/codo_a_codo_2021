'use strict'

let numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

const body = document.body
const pre = document.getElementById("pre")

pre.textContent = numbers

//?
//? Arrays
//?

const push = document.getElementById("push")
const pop = document.getElementById("pop")
const unshift = document.getElementById("unshift")
const shift = document.getElementById("shift")

push.addEventListener("click", () => {
  numbers.push(numbers.slice(-1)[0] + 1)
  pre.textContent = numbers
})

pop.addEventListener("click", () => {
  numbers.pop()
  pre.textContent = numbers
})

shift.addEventListener("click", () => {
  numbers.shift()
  pre.textContent = numbers
})

unshift.addEventListener("click", () => {
  numbers.unshift(numbers[0] - 1)
  pre.textContent = numbers
})

const reverse = document.getElementById("reverse")
const sortaz = document.getElementById("sortaz")
const sort09 = document.getElementById("sort09")

body.addEventListener("click", e => {
  switch (e.target.id) {
    case "reverse":
      numbers.reverse()
      pre.textContent = numbers
      break
    case "sortaz":
      numbers.sort()
      pre.textContent = numbers
      break
    case "sort09":
      numbers.sort((a, b) => a - b)
      pre.textContent = numbers
      break
    default:
  }
})

//! __________________________________________________

const wrappers = document.querySelectorAll(".wrapper")
// wrappers.forEach(wrapper => wrapper.classList.add("hide"))

// let animals = ["🐶", "🐱", "🦖", "🦈", "🧟‍♀️"]
// pre.textContent = JSON.stringify(animals, null)

//? FOR EACH

const exampleForEach = () => {
  animals.forEach((animal, i) => {
    if (animal === "🐶") {
      console.log(animal, "es amigable 👌")
      return
    }
    if (animal === "🐱") {
      console.log(animal, "es amigable 👌")
      return
    }
    console.log(animal, "te atacará, corre 🏃")

    // if (animal === "🐶") console.log(animal, "es amigable 👌")
    // else if (animal === "🐱") console.log(animal, "es amigable 👌")
    // else console.log(animal, "te atacará, corre 🏃")

    // animal === "🐶"
    //   ? console.log(animal, "es amigable 👌")
    //   : animal === "🐱"
    //   ? console.log(animal, "es amigable 👌")
    //   : console.log(animal, "te atacará, corre 🏃")
  })
}
// exampleForEach()

//? EVERY
let key = "🐊"
const exampleEvery = () => animals.every(animal => animal !== key)

// console.log(`Libre de ${key}? ${exampleEvery() ? "Sí" : "No"}`)

//? SOME
key = "🧟‍♀️"
const exampleSome = () => animals.some(animal => animal === key)

// console.log(`Hay algún ${key}? ${exampleSome() ? "Sí" : "No"}`)

//? MAP
const exampleMap = () => animals.map(animal => animal + "❤️" + animal)

// console.log(exampleMap())

//? FILTER
key = "🦖"
const exampleFilter = () => {
  const arraySinDino = animals.filter(animal => animal !== key)
  return `Me gustan ellos ${arraySinDino} pero no el dinosaurio.`
}

// console.log(exampleFilter())

//? FIND & FIND_INDEX
const exampleFinds = () => {
  const indexOfShark = animals.findIndex(animal => animal === "🦈")
  console.log(`El índice en que se encuentra el 🦈 es: ${indexOfShark}`)

  const indexGreaterThan3 = animals.find((animal, i) => i >= 3)
  console.log(`El primer animal después del index 0 es: ${indexGreaterThan3}`)
}

// exampleFinds()

//? REDUCE
const exampleReduce = () => {
  // return [4, 6, 20, 6, 2, 49, 100].reduce((acu, cur) => acu + cur)
  // return [4, 6, 20, 100, 2, 49, 6].reduce((max, cur) => (cur > max ? cur : max))
}

// console.log(exampleReduce())

//! __________________________________________________

const capitalize = ([firstLetter, ...string]) =>
  firstLetter.toUpperCase() + string.join("")

// console.log(capitalize("hola alumnos."))
