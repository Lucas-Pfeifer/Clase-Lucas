/* let numeros = [1, "Test", "Hola"];

numeros.push("......");

numeros.unshift("Hola");

console.log(numeros);

console.log(numeros.indexOf("Hola"));


const person = {
  name: "Lucas",
  age: 12,
  hobbies: ["musica", "peliculas", "deportes"],
  addres: {
    street: "san juan de luz 4060",
    city: "Santiago",
  },
};

console.log(
  `Mi nombre es ${person.name} y vivo en ${person.addres.city}, me gustan las ${person.hobbies[1]}`
);

const {
  name,
  age,
  addres: { city },
} = person;

console.log(city);


const todos = [
  {
    id: 1,
    text: "Take the trash out",
    Completed: true,
  },
  {
    id: 2,
    text: "??",
    Completed: true,
  },
];
const todoJSON = JSON.stringify(todos);
console.log(todoJSON)
*/

const todos = [
  {
    id: 1,
    text: "Take the trash out",
    Completed: true,
  },
  {
    id: 2,
    text: "??",
    Completed: true,
  },
  {
    id: 3,
    text: "awd",
    Completed: true,
  },
  {
    id: 4,
    text: "dwa",
    Completed: true,
  },
  {
    id: 5,
    text: "Go to ",
    Completed: true,
  },
];

/* const TODOSJSON = JSON.parse(data.json);
console.log(todos[1]); */

/* let i = 0;
while (i < 10) {
  i++;
  console.log(i);
}
 */

/* for (let i = 0; i < todos.length; i++) {
  console.log(`Numero🤬: ${i}`);
}

for(let todo of todos) {
  console.log(todos.id)
} */

/* const todoText = todos.map(function (todo) {
  return todo.text;
});

console.log(todoText); */

// TodoText = TodoText2 
let TodoText2 = [];

for (let todo of todos) {
  TodoText2.push(todo.text)
}

console.log(TodoText2[4])
