function Hoge(a, b) {
	console.log(a);
	console.log(b);
	console.log(this);
	console.log(this.hoge);
}

var target = {hoge:"HOGE"};

// thisと引数の束縛
var bound = Hoge.bind(target, "1", "2");
bound();
