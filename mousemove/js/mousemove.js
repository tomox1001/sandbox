// 変数宣言
var spd = 0.85;
var mouseX = 0;
var mouseY = 0;
var moveX = 0;
var moveY = 0;
var eX = 0;
var eY = 0;
var pageX = 0;
var pageY = 0;

// mousemoveイベント登録
document.addEventListener('mousemove', onMouseMove, false);

// インターバル設定
setInterval(imgMove, 30);

function onMouseMove(e) {
    pageX = e.pageX;
    pageY = e.pageY;
}

function imgMove() {
    moveX += (pageX - eX);
    moveY += (pageY - eY);
    moveX *= spd;
    moveY *= spd;

    eX += moveX;
    eY += moveY;
    img1.style.left = eX + "px";
    img1.style.top = eY + "px";
}
