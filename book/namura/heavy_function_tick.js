function isPrime (num) {
	if (num < 2) return false;
	else if (num == 2) return true;
	if (num % 2 ==0) return false;
	for (var i = 3;  i*i <= num; i+=2) {
		if (num % i === 0) return false;
	};
	return true;
}

var total = 0;

function heavy (start, end) {
	var prime = 0;
	for (var i = start; i < end; i++) {
		if (isPrime(i)) {
			prime++;
		}
	}
	if (end < 50000000) {
		console.log("found", prime, "primes between", start, "and", end);
		process.nextTick(function() {
			total += heavy(end, end+1000000);
		});
	} else {
		console.log('total', total, 'primes');
	}

	return prime;
}

heavy(0, 1000000);

var count = 0;
var id = setInterval(function() {
	console.log('interval executed', count++);
	if(count == 5) {
		clearInterval(id)
	}
}, 100);
