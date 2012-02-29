/**
 * Created by JetBrains WebStorm.
 * User: kawano_tomonori
 * Date: 11/08/02
 * Time: 19:12
 * To change this template use File | Settings | File Templates.
 */

// 即時関数
(function() {
    window.log = function() {
        console.log.apply(console, arguments);
    }

//    log('hoge');

    //
    var mouseX = 0;
    var mouseY = 0;
    document.addEventListener("mousemove", function(e){
        mouseX = e.clientX + document.body.scrollLeft;
        mouseY = e.clientY + document.body.scrollTop;

        log(mouseX);
        log(mouseY);
    }, false);

    var icon = document.createElement("img");
    icon.src = "http://a1.twimg.com/profile_images/1284991379/images_reasonably_small.jpg";
    icon.style.position = "absolute";

//    debugger;
    
    window.addEventListener('load', function(e) {
        init();
    }, false);

    function init() {
        document.body.appendChild(icon);

        // 描画
        function Sprite(img) {
            var _x = 0;
            var _y = 0;

            return {
                set x(value){
                   _x = value;
                    img.style.left = value + 'px';
                },
                get x() {
                    return _x;
                },
                
                set y(value){
                   _y = value;
                    img.style.top = value + 'px';
                },
                get y() {
                    return _y;
                },
                vx: 0,
                vy: 0
            };
        };

        var sp = new Sprite(icon);
        var FPS = 60;
        var spring = 0.2;
        var friction = 0.85;
        
        var intevalID = setInterval(function() {
            sp.vx += (mouseX - sp.x) + spring;
            sp.vx *= friction;
            sp.x += sp.vx;

            sp.vy += (mouseY - sp.y) + spring;
            sp.vy *= friction;
            sp.y += sp.vy;

        }, 1000 / FPS);

    };
})();
