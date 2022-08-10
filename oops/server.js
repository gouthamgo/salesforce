//  class Literal 

//  defining an Object 

let person = {
    firstName : 'Brad',
    lastName : 'Roopt',

    // method
    getFunction: function(){
        return(`The name of the Person is 
        ${person.firstName} ${person.lastName}`)
    },
    // object within an object
    phoneNumber:{
        mobile: "12456",
        landline: '6745'
    }
}

console.log(person.getFunction());
console.log(person.phoneNumber.landline);