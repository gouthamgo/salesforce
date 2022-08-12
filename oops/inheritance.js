//  Inheritance

class person{
    constructor(name){
        this.name = name;
    }

    //  method to return the string 
    toString(){
        return(`Name of the person${this.name}`)
    }
}

class student extends person{
    constructor(name,id){
        super(name);
        this.id = id;
    }
    toString(){
        return(`${super.toString()}, student id i s ${this.id}`)
    }
}

let student1 = new student('Rocky', '23');
console.log(student1.toString());