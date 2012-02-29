// クラス (のようなもの) の定義

/**
 * コンストラクタとなる関数
 * @param name
 * @param age
 */
var Man = function(name, age) {
  // プロパティの初期化
  this.name = name;
  this.age = age;
};

// メソッド・プロパティの定義
Man.prototype = {
  sayName: function() { alert("My name is " + this.name + "."); }
}

// インスタンスの作成
var bob = new Man('Bob', 35);
bob.sayName();  // => My name is Bob.