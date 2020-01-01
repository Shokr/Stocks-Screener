
let draw = Chart.controllers.line.prototype.draw;
Chart.controllers.line = Chart.controllers.line.extend({
    draw: function () {
        draw.apply(this, arguments);
        let nk = this.chart.chart.ctx;
        let _stroke = nk.stroke;
        nk.stroke = function () {
            nk.save();
            nk.shadowColor = '#ccc';
            nk.shadowBlur = 10;
            nk.shadowOffsetX = 0;
            nk.shadowOffsetY = 4;
            _stroke.apply(this, arguments)
            nk.restore();
        }
    }
});
// Line Shadow Background
(nk = document.getElementById("lineShadow-bg")).height = 100;
myChart = new Chart(nk, {
    type: 'line',
    data: {
        labels: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun", "Mon"],
        datasets: [{
            data: [100, 70, 150, 120, 300, 250, 400, 300],
            backgroundColor: "rgba(0, 123, 255, 0.1)",
            borderWidth: 4,
            borderColor: "rgba(0, 123, 255, 0.9)",
            pointBackgroundColor: "#FFF",
            pointBorderColor: "rgba(0, 123, 255, 0.9)",
            pointHoverBackgroundColor: "#FFF",
            pointHoverBorderColor: "rgba(0, 123, 255, 0.9)",
            pointRadius: 0,
            pointHoverRadius: 6,
            fill: !0
        },
        {
            data: [20, 70, 300, 120, 180, 220, 450, 250],
            borderWidth: 4,
            backgroundColor: "rgba(247,147,26,0.1)",
            borderColor: "rgba(247,147,26,0.9)",
            pointBackgroundColor: "#FFF",
            pointBorderColor: "rgba(247,147,26,0.9)",
            pointHoverBackgroundColor: "#FFF",
            pointHoverBorderColor: "rgba(247,147,26,0.9)",
            pointRadius: 0,
            pointHoverRadius: 6,
            fill: !0
        }
        ]
    },
    options: {
        responsive: !0,
        legend: {
            display: !1
        },
        scales: {
            xAxes: [{
                display: !1,
                gridLines: {
                    display: !1
                }
            }],
            yAxes: [{
                display: !1,
                ticks: {
                    padding: 10,
                    stepSize: 100,
                    max: 600,
                    min: 0
                },
                gridLines: {
                    display: !0,
                    drawBorder: !1,
                    lineWidth: 1,
                    zeroLineColor: "#e5e5e5"
                }
            }]
        }
    },
});



