function loop(fn, times, unit) {
        unit = unit || 10;
        function _loop(n) {
                for (var i = n; i < n + unit && i < times; i++) {
                        fn(i);
                        if (i === times - 1) {
                                return;
                        }
                }
                process.nextTick(function() {
                        _loop(n + unit);
                });
        }
        _loop(0);
}

/**
 * 10回ごとにnextTickを挟む
 */
loop(function(i) {
    console.log(i);
}, 100);