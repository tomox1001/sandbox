var Animal = function() {};
Animal.prototype = {
  sleep: function() { alert('zzz...'); }
};

var Human = function() {};
human.prototype = new animal();
human.prototype.workharder = function() {
  alert("i'm tired...");
  this.sleep();
};

var me = new Human();
me.workHarder();  // => I'm tired... => zzz...