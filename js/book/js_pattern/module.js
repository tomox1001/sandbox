function Gadget() {
	// private
	var name = "iPhone4S";
	// public
	this.getName = function () {
		return name;
	}
}

Gadget.prototype = (function(){
	// private
	var browser = "Mobile Webkit!";
	// public in prototype
	return {
		getBrowser : function() {
			return browser;
		}
	};
}());

var toy = new Gadget();

console.log(toy.getName());// special method
console.log(toy.getBrowser());// special method in prototype
