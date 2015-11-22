function addPersonMethods(obj)
{
//var obj ={'name':1};

 obj.greet = function greet(str)
            {
              console.log(str + ", my name is "+ obj.name);
            //  system.log(str + "my name is"+this.name);
            };

 obj.compareAge= function compareAge(str)
            {
    if(obj.age === str.age)
      {
        console.log("My name is "+ obj.name + " and I'm equally young as "+ str.name );
      }

      if(obj.age > str.age)
      {
        console.log("My name is "+ obj.name + " and I'm older than " + str.name);
      }

      if(obj.age < str.age)
      {
        console.log("My name is "+ obj.name + " and I'm younger than " + str.name);
      }
  };

obj.namesake=  function namesake(str)
      {
        if(obj.name === str.name)
        {
        console.log("We have the same name, "+ str.name + " and I!");
        }
        else {
            console.log("We have different names, "+ str.name + " and I.");
          }
        };

return obj;
}
