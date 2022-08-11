// Encapsulation

class person{
    constructor(name,id){
        this.name = name;
        this.id = id;
    }
    add_Address(add){
        this.add = add;
    }
    getDetails(){
        console.log(`Name is the ${this.name}, Address is the : ${this.add}`)
    }
}

let person1 = new person('Sonam','12');
person1.add_Address('Delhi');
person1.getDetails();