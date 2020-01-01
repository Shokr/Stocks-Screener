
$(function () {
    "use strict";

    //Overlay Graph Line 
    var ctx = document.getElementById("overlay-graph-line");
    ctx.height = 100;
    var myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: ["2010", "2011", "2012", "2013", "2014", "2015", "2016"],
            type: 'line',

            datasets: [{
                label: "My First dataset",
                data: [28, 35, 36, 48, 46, 42, 60],
                backgroundColor: "rgba(255,117,136,0.12)",
                borderColor: "#FF4961",
                borderWidth: 3,
                strokeColor: "#FF4961",
                capBezierPoints: !0,
                pointColor: "#fff",
                pointBorderColor: "#fff",
                pointBackgroundColor: "#FF4961",
                pointBorderWidth: 3,
                pointRadius: 5,
                pointHoverBackgroundColor: "#FFF",
                pointHoverBorderColor: "#FF4961",
                pointHoverRadius: 7
            }]
        },
        options: {
            responsive: true,
            tooltips: {
                enabled: false,
            },
            legend: {
                display: false,
                labels: {
                    usePointStyle: false,

                },


            },
            scales: {
                xAxes: [{
                    display: false,
                    gridLines: {
                        display: false,
                        drawBorder: false
                    },
                    scaleLabel: {
                        display: false,
                        labelString: 'Month'
                    }
                }],
                yAxes: [{
                    display: false,
                    gridLines: {
                        display: false,
                        drawBorder: false
                    },
                    scaleLabel: {
                        display: true,
                        labelString: 'Value'
                    }
                }]
            },
            title: {
                display: false,
            }
        }
    });

});
