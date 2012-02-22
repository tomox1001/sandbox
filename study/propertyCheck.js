// プロパティが存在するかどうかチェックするのに↓の
// 二通りの書き方ができます。

var obj = {
    a : 'a'
};

console.log('a' in obj);
console.log(obj.hasOwnProperty('a'));

// ↓

true
true

// この場合、in演算子の方が早いらしいので通常オススメです。
// ただし、

console.log('toString' in obj);
console.log(obj.hasOwnProperty('toString'));

// ↓

true
false

// のようにin演算子だと、プロトタイプチェーンを辿った
// プロパティもアリと判定されてしまうので、注意が必要です。
