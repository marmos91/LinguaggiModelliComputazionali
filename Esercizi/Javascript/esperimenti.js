// Type augmenting
var Point = function(x, y)
{
   this.x = x;
   this.y = y;
}

Point.prototype.toString = function()
{
   console.log("X: ", this.x," Y: ", this.y);
};

var p1 = new Point(3, 4);
var p2 = new Point(5, 7);

p1.toString();
p2.toString();

Point.prototype.toString = function()
{
   console.log("Modificato X: ", this.x, "Modificato Y: ", this.y);
};

Point.prototype.new_value = function()
{
   console.log("New value requested");  
};

var p3 = new Point(1, 1);
p3.toString();

// Extending Number prototype with some magic powder
Number.prototype.times = function(f) 
{
   for(i=0; i<this.valueOf(); i++)
      if(typeof f === "function")
         f();
}

(3).times(function()
{
   console.log("Bella uoma!");
});


// Private members and getter/setter methods 
var Point = function(x, y)
{
   var private_x = x;
   var private_y = y;
   this.x = function() { return private_x};
   this.y = function() { return private_y};
   this.setX = function(new_value) {this.x = function() {return new_value;}};
   this.setY = function(new_value) {this.y = function() {return new_value}};
}

/////////////////////////////////////////////////////
var semiPoint = function(private_x)
{
   this.x = function(){return private_x};
};

var Point = function(private_x, private_y)
{   
   semiPoint.call(this, private_x);
   this.y = function(){return private_private_y};
};

Point.prototype.setX = function(x)
{
   this.x = function(){ return x };
}
/////////////////////////////////////////////////////

var baseClass = function(secret, x, y)
{
   secret = secret || {};
   secret.pippo = function() {return x};
   return {
      publicValue: y
   };
};

var extensionClass = function(x, y)
{
   secret = {pippo: "a"}, self = baseClass(secret, x, y);
   console.log("public value",self.publicValue);
   console.log("private value")
   console.log(secret);
   return self;
};
/////////////////////////////////////////////////////