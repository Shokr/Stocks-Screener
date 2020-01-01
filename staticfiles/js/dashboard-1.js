$(function () {
    "use strict";


    $(".peity-btc")
        .peity("line", {
            width: '100%',
            height: '100'
        });

    $(".peity-ltc")
        .peity("line", {
            width: '100%',
            height: '100'
        });
    $(".peity-neo")
        .peity("line", {
            width: '100%',
            height: '100'
        });
    $(".peity-dash")
        .peity("line", {
            width: '100%',
            height: '100'
        });
    $(".peity-eth")
        .peity("line", {
            width: '100%',
            height: '100'
        });
    $(".peity-xrp")
        .peity("line", {
            width: '100%',
            height: '100'
        });


    /////////////////
    // BTC Live
    /////////////////
    var updatingBtc = $(".btc-live-price")
        .peity("line", {
            width: "100%",
            height: '150'
        })

    setInterval(function () {
        var random = Math.round(Math.random() * 20)
        var values = updatingBtc.text()
            .split(",")
        values.shift()
        values.push(random)

        updatingBtc
            .text(values.join(","))
            .change()
    }, 2000);



    //////////////////
    // NEO Live
    ///////////////

    var updatingNeo = $(".neo-live-price")
        .peity("line", {
            width: "100%",
            height: '150'
        })

    setInterval(function () {
        var random = Math.round(Math.random() * 20)
        var values = updatingNeo.text()
            .split(",")
        values.shift()
        values.push(random)

        updatingNeo
            .text(values.join(","))
            .change()
    }, 2000);

    /////////////////
    // XRP Live
    ////////////////
    var updatingXrp = $(".xrp-live-price")
        .peity("line", {
            width: "100%",
            height: '150'
        })

    setInterval(function () {
        var random = Math.round(Math.random() * 20)
        var values = updatingXrp.text()
            .split(",")
        values.shift()
        values.push(random)

        updatingXrp
            .text(values.join(","))
            .change()
    }, 2000);
 
})
