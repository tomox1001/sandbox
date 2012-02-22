// method()メソッド
if (typeof Function.prototype.method !== "function") {
	Function.prototype.method = function(name, implementation){
		this.prototype[name] = implementation;
		return this;
	};
}

var Person = function (name) {
	this.name = name;
}.
	
	method('getName', function() {
		return this.name;
	}).
	method('setName', function(name) {
		this.name = name;
		return this;
	});
	
var a = new Person("tomox");
console.log(a.getName()); // tomox
console.log(a.setName('xomot').getName()); // xomot