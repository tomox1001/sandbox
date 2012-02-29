myname = "global";

// アンチパターン
(function func(){
	alert(myname); // undefined
	var myname = "local";
	alert(myname); // local
}());
