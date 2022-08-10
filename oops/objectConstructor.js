//  Using an Object Constructor

function person(firstName, lastName){
    this.firstName = firstName;
    this.lastName = lastName
}

//  creating new instances for the person object 

let person1 = new person('Ram', 'sita');
let person2 = new person('brad','pitt');

console.log(person1.firstName);
console.log(`${person2.firstName} ${person1.lastName}`)