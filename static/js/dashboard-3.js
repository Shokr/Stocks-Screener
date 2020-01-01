
$(function () {
    "use strict";

  
    var aaa = getRandomData('April 01 2017', 60);

    // Candlestick
    var ctx = document.getElementById("candlestick");
    ctx.height = 100;
    new Chart(ctx, {
        type: 'candlestick',
        data: {
            datasets: [{
                label: "Crypto Market",
                data: aaa,
                fractionalDigitsCount: 2,
            }]
        },
        options: {
            responsive: true,
            tooltips: {
                position: 'nearest',
                mode: 'index',
            },
        },
    });

});
