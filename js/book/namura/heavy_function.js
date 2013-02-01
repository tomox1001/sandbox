function isPrime (num) {
	if (num < 2) return false;
	else if (num == 2) return true;
	if (num % 2 ==0) return false;
	for (var i = 3;  i*i <= num; i+=2) {
		if (num % i === 0) return false;
	};
	return true;
}

function heavy (start, end) {
	var prime = 0;
	for (var i = start; i < end; i++) {
		if (isPrime(i)) {
			prime++;
		}
	}
	console.log("found", prime, "primes between", start, "and", end);
	return prime;
}

var sum = 0;
for (var i = 0; i < 5; i++) {
	sum += heavy(i*1000000, (i+1)*1000000);
}
console.log('total',sum,'primes');

var count = 0;
var id = setInterval(function() {
	console.log('interval executed', count++);
	if(count == 5) {
		clearInterval(id)
	}
}, 100);
