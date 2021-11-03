/* const todos = [
  {
    id: 1,
    text: "Take the trash out",
    Completed: true,
  },
  {
    id: 2,
    text: "??",
    Completed: false,
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

 let numeros = [1, 'Test', 'Hola'];

numeros.push('......');

numeros.unshift('Hola');

console.log(numeros);

console.log(numeros.indexOf('Hola'));

const person = {
  name: 'Lucas',
  age: 12,
  hobbies: ['musica', 'peliculas', 'deportes'],
  addres: {
    street: 'san juan de luz 4060',
    city: 'Santiago',
  },
};

console.log(
  `Mi nombre es ${person.name} y vivo en ${person.addres.city}, me gustan las ${person.hobbies[1]}`
); 

 let i = 0;
while (i < 10) {
  i++;
  console.log(i);
}
 

 for (let i = 0; i < todos.length; i++) {
  console.log(`Numero🤬: ${i}`);
}

for(let todo of todos) {
  console.log(todos.id)
} 

 const todoText = todos.map(function (todo) {
  return todo.text;
});

console.log(todoText); 

// TodoText = TodoText2
 let TodoText2 = [];

for (let todo of todos) {
  TodoText2.push(todo.text);
}

console.log(TodoText2[4]);

// forEach
const todoCompleted = todos.filter(function (todo) {
  return todo.Completed === true;
});

console.log(todoCompleted);

// if 😈
let var1 = 1;
let var2 = 10;

if (var1 === 1 || var2 === 10) {
  console.log(`var1 es igual a ${var1} o var2 es igual a ${var2}`);
}
if (var1 === 1 && var2 === 10) {
  console.log(`var1 es igual a ${var1} y var2 es igual a ${var2}`);
}

const x = 11;
const color = x > 10 ? 'red' : 'blue'; 

 function addNums(num1 = 1, num2 = 1) {
  return num1 + num2;
}
addNums(1, 10); */

//funcion constructora de objetos
/* function Person(firstName, lastName, birthday) {
  this.firstName = firstName;
  this.lastName = lastName;
  this.birthday = new Date(birthday);
  this.getBirthYear = function () {
    return this.birthday.getFullYear();
  };
  this.getFullName = function () {
    return `${this.firstName} ${this.lastName}`;
  };
}

function Medico(firstName, lastName, birthday, area = "") {
  Person.call(this, firstName, lastName, birthday);
  this.area = area;
} 
*/

//class person

class Person {
  constructor(firstName, lastName, birthday) {
    this.firstName = firstName;
    this.lastName = lastName;
    this.birthday = new Date(birthday);
  }
  getBirthYear() {
    return this.birthday.getFullYear();
  };
  getFullName() {
    return `${this.firstName} ${this.lastName}`;
  };

}

let human1 = new Person("Lucas", "Pfeifer", "12-15-2008");
//let medico1 = new Medico("Juan", "...", "12-15-2008", "Hola");
console.log(human1);

//repaso funcion flecha
/* const numero01 = 10
const numero02 = 20
const numero = (n01, n02) => n01 + n02;
const resultado = numero(numero01, numero02);
console.log(resultado) */


//console.log(numero(10))
