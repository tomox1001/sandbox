var properties = [];
for (var p in obj) {
    if(obj.hasOwnProperty(p)) {
        properties.push(p);
    }
}

// ↑と同等の処理
var properties = Object.keys(obj);
