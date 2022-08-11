// abstraction

function person(fname,lname){
    let firstName = fname;
    let lastName = lname;

    let getDetails_noaccess = function(){
        return(`First name is ${firstName} 
        Last Name is : ${lastName}`)
    }

    this.getDetails_access = function(){
        return(`First Name is ${firstName}
        and the last name is ${lastName}`)
    }
}

let person1 = new person('Rodi', 'last');
console.log(person1.firstName),
console.log(person1.getDetails_noaccess);
console.log(person1.getDetails_access);