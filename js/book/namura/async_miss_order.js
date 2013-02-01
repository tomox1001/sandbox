var fs = require('fs');

try {
	fs.readFile('dummy_file.txt', function(err, data) {
		console.log(data);
	});
} catch (e) {
	console.log('this never called');
}
