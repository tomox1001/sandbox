function loop(fn, times, delay) {
	if (!times || times < 0) {
		throw new Error('invalid parameter times', times);
	}
	if (!delay || delay < 0) {
		throw new Error('invalid parameter delay', delay);
	}
	function _loop(n) {
		if (n === times) {
			return;
		}
		fn(n);
		setTimeout(function() {
			_loop(n + 1);
		}, delay);
	}
	_loop(0);
}

/**
 * 10ms間隔で50回実行する
 */
loop(function(i) {
	console.log(i);
}, 50, 10);
