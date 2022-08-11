// Onject create method 

//  create a simple object with properties 

const coder = {
    isStudying: false,
    printIntro: function(){
        console.log(`my name is ${this.name}, Am I studying? ${this.isStudying}`)
    }
}

// Object create method

const me = Object.create(coder);

//  name is the property set on 'me' , but not on the coder

me.name = 'Rakul';

// Inherited properties can be overwritten

me.isStudying = true;

me.printIntro();


