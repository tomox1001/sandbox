/**
 * 配列の生成方法
 */
function create() {
	var ary1 = [1, 2, 3];          // => [1, 2, 3]
	var ary2 = new Array(3);       // => [undefined, undefined, undefined]
	var ary3 = new Array(3, 4, 5); // => [3, 4, 5]
};

/**
 * 配列の参照と代入
 */
function read() {
	var ary = [1, 2, 3];
	ary[2];               // => 3   (配列のインデックスは0オリジン)
	ary[0] = 3;           // => ary == [3, 2, 3]
};

/**
 * 配列の操作
 */
function use() {
	// 宣言
	var ary = [1, 2, 3];

	// 先頭を取り出す
	var a = ary.shift(); // => a == 1, ary == [2, 3]

	// 先頭に追加
	ary.unshift(5);      // => ary == [5, 2, 3]

	// 末尾を取り出す
	var b = ary.pop();   // => b == 3, ary == [5, 2]

	// 末尾に追加
	ary.push(9);         // => ary == [5, 2, 9]

	// 部分コピーを得る
	var c = ary.slice(1, 2);
	// => c == [2], ary == [5, 2, 9]
	// 一部を置き換える
	var d= ary.splice(1, 2, "a", "b", "c");
	// => d == [2, 9], ary == [5, "a", "b", "c"]
};


/**
 * 連想配列
 */
(function associativeArray() {
	// オブジェクトの定義。JSON はこの表記法を基にしている
	var a = {a: 123, b: 456};
	a['a'];                // => 123 (連想配列風アクセス)
	a.b;                   // => 456 (プロパティ風アクセス)
	a['c'] = 789;          // 要素の追加
	a.d = 123;
});
