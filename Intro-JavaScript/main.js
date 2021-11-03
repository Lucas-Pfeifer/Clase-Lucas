// Single element
//console.log(document.getElementById("my-form"))
//console.log(document.querySelector("h1"))

// Multiple element
//console.log(document.querySelectorAll(".item"))
//console.log(document.getElementsByTagName("li"))


//const items = document.querySelectorAll(".item")
//items.forEach((item) => console.log(item));

//const ul = document.querySelector('.items');

//ul.remove();
//ul.lastElementChild.remove();
//ul.firstElementChild.remove();
//ul.firstElementChild.textContent = "Hello";
//ul.children[1].innerText = "Text";
//ul.lastElementChild.innerHTML = "<h1>Hello</h1>"


//const btn = document.querySelector('.btn');
//btn.style.background = "red";




/* const btn = document.querySelector('.btn');

btn.addEventListener('mouseover', (e) =>{
    e.preventDefault();
    document.querySelector('#my-form').style.background = 'green';
    //btn.style.background = "red";
}
);


btn.addEventListener('mouseout', (e) =>{
    e.preventDefault();
    document.querySelector('#my-form').style.background = "red";
}
); */



const myForm = document.querySelector('#my-form')
const nameInput = document.querySelector('#name')
const emailInput = document.querySelector('#email')
const msg = document.querySelector('.msg')
const userList = document.querySelector('#users')

myForm.addEventListener('submit', onSubmit);

function onSubmit(e) {
    e.preventDefault();

    if (nameInput.value === '' || emailInput.value === "") {
        msg.classList.add('error');
        msg.innerHTML = 'please enter all fields'

        setTimeout(() => msg.remove(), 3000)
    } else {
        const li = document.createElement('li');
        li.appendChild(document.createTextNode(`${nameInput.value} : ${emailInput.value}`));

        userList.appendChild(li)

        // Clear fields
        nameInput.value = '';
        nameInput.value = '';

    }
}






