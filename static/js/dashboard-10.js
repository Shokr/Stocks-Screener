
$(function () {
  "use strict";

  //Earning Graph Bottom
  var ctx = document.getElementById("canvas4");
  ctx.height = 100;
  var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
      datasets: [{
        label: 'A',
        type: 'line',
        backgroundColor: "#f00",
        borderColor: "#f00",
        fill: false,
        lineTension: 0,
        borderDash: [8, 4],
        data: []
      }, {
        label: 'B',
        backgroundColor: "#4c84ff",
        borderColor: "#4c84ff",
        fill: false,
        cubicInterpolationMode: 'monotone',
        data: []
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: true,
      legend: {
        display: false
      },
      title: {
        display: false,
        text: ''
      },
      scales: {
        xAxes: [{
          type: 'realtime',
          display: false,
          barPercentage: 0.5,
          categoryPercentage: 0.5
        }],
        yAxes: [{
          type: 'linear',
          display: false,
          scaleLabel: {
            display: true,
            labelString: 'value'
          },
          ticks: {
            beginAtZero: true
          }
        }]
      },
      tooltips: {
        mode: 'nearest',
        intersect: false
      },
      hover: {
        mode: 'nearest',
        intersect: false
      },
      plugins: {
        streaming: {
          duration: 20000,
          refresh: 1000,
          delay: 1000,
          frameRate: 5,

          onRefresh: function (chart) {
            chart.data.datasets.forEach(function (dataset) {
              dataset.data.push({
                x: moment(),
                y: Math.random() * 100
              });
            });
          }
        }
      }
    }
  });

});
