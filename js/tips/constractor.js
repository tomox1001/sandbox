/**
 * new無しでもhoge/fugaをグローバル化しない
 * @param a
 * @param b
 */
function Hoge(a, b) {
	if (!(this instanceof Hoge)) {
		return new Hoge(a, b);
	}
	this.hoge = a;
	this.fuge = b;
}
