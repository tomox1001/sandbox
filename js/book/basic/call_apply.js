// thisの指すものを明示的にしていして関数を呼び出すには， Function#call や Function#apply を利用する
// Function#call と Function#apply の違いは，呼び出したい関数に渡す引数の指定の仕方だけ
sayName.call(smith);  // => Smith (thisがsmithを指す)
sayName.apply(john);  // => John  (thisがjohnを指す)