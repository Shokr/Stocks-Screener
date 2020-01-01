/**
 * Generate random chart data
 */
var chartData1 = [];
var chartData2 = [];
var chartData3 = [];
var chartData4 = [];

function generateChartData() {
    var firstDate = new Date();
    firstDate.setDate(firstDate.getDate() - 500);
    firstDate.setHours(0, 0, 0, 0);

    for (var i = 0; i < 500; i++) {
        var newDate = new Date(firstDate);
        newDate.setDate(newDate.getDate() + i);

        var a1 = Math.round(Math.random() * (40 + i)) + 100 + i;
        var b1 = Math.round(Math.random() * (1000 + i)) + 500 + i * 2;

        var a2 = Math.round(Math.random() * (100 + i)) + 200 + i;
        var b2 = Math.round(Math.random() * (1000 + i)) + 600 + i * 2;

        var a3 = Math.round(Math.random() * (100 + i)) + 200;
        var b3 = Math.round(Math.random() * (1000 + i)) + 600 + i * 2;

        var a4 = Math.round(Math.random() * (100 + i)) + 200 + i;
        var b4 = Math.round(Math.random() * (100 + i)) + 600 + i;

        chartData1.push({
            "date": newDate,
            "value": a1,
            "volume": b1
        });
        chartData2.push({
            "date": newDate,
            "value": a2,
            "volume": b2
        });
        chartData3.push({
            "date": newDate,
            "value": a3,
            "volume": b3
        });
        chartData4.push({
            "date": newDate,
            "value": a4,
            "volume": b4
        });
    }
}

generateChartData();

/**
 * Create the chart
 */
var chart = AmCharts.makeChart("chartdiv", {
    "type": "stock",
    "theme": "dark",
    "legend": {
        "color": "#fff",
    },

    // This will keep the selection at the end across data updates
    "glueToTheEnd": true,

    // Defining data sets
    "dataSets": [{
        "title": "BTC",
        "fieldMappings": [{
            "fromField": "value",
            "toField": "value"
        }, {
            "fromField": "volume",
            "toField": "volume"
        }],
        "dataProvider": chartData1,
        "categoryField": "date"
    }, {
        "title": "LTC",
        "fieldMappings": [{
            "fromField": "value",
            "toField": "value"
        }, {
            "fromField": "volume",
            "toField": "volume"
        }],
        "dataProvider": chartData2,
        "categoryField": "date"
    }, {
        "title": "XRP",
        "fieldMappings": [{
            "fromField": "value",
            "toField": "value"
        }, {
            "fromField": "volume",
            "toField": "volume"
        }],
        "dataProvider": chartData3,
        "categoryField": "date"
    }, {
        "title": "NEO",
        "fieldMappings": [{
            "fromField": "value",
            "toField": "value"
        }, {
            "fromField": "volume",
            "toField": "volume"
        }],
        "dataProvider": chartData4,
        "categoryField": "date"
    }],

    // Panels
    "panels": [{
        "showCategoryAxis": false,
        "title": "Value",
        "percentHeight": 60,
        "stockGraphs": [{
            "id": "g1",
            "valueField": "value",
            "comparable": true,
            "compareField": "value"
        }],
        "stockLegend": {
            "color": "#fff"
        }
    }, {
        "title": "Volume",
        "percentHeight": 40,
        "stockGraphs": [{
            "valueField": "volume",
            "type": "column",
            "showBalloon": false,
            "fillAlphas": 1
        }],
        "stockLegend": {
            "color": "#fff"
        }
    }],

    // Scrollbar settings
    "chartScrollbarSettings": {
        "graph": "g1",
        "usePeriod": "WW"
    },

    // Period Selector
    "periodSelector": {
        "position": "top",
        "periods": [{
            "period": "DD",
            "count": 10,
            "label": "10 days"
        }, {
            "period": "MM",
            "selected": true,
            "count": 1,
            "label": "1 month"
        }, {
            "period": "YYYY",
            "count": 1,
            "label": "1 year"
        }, {
            "period": "YTD",
            "label": "YTD"
        }, {
            "period": "MAX",
            "label": "MAX"
        }]
    },

    // Data Set Selector
    "dataSetSelector": {
        "position": "top"
    },

    // Event listeners
    "listeners": [{
        "event": "rendered",
        "method": function (event) {
            chart.mouseDown = false;
            chart.containerDiv.onmousedown = function () {
                chart.mouseDown = true;
            }
            chart.containerDiv.onmouseup = function () {
                chart.mouseDown = false;
            }
        }
    }]
});

/**
 * Set up interval to update the data periodically
 */
setInterval(function () {

    // if mouse is down, stop all updates
    if (chart.mouseDown)
        return;

    // normally you would load new datapoints here,
    // but we will just generate some random values
    // and remove the value from the beginning so that
    // we get nice sliding graph feeling

    // remove datapoint from the beginning
    // chartData1.shift();
    //chartData2.shift();
    //chartData3.shift();
    // chartData4.shift();

    // add new datapoint at the end
    var newDate = new Date(chartData1[chartData1.length - 1].date);
    newDate.setDate(newDate.getDate() + 1);

    var i = chartData1.length;

    var a1 = Math.round(Math.random() * (40 + i)) + 100 + i;
    var b1 = Math.round(Math.random() * (1000 + i)) + 500 + i * 2;

    var a2 = Math.round(Math.random() * (100 + i)) + 200 + i;
    var b2 = Math.round(Math.random() * (1000 + i)) + 600 + i * 2;

    var a3 = Math.round(Math.random() * (100 + i)) + 200;
    var b3 = Math.round(Math.random() * (1000 + i)) + 600 + i * 2;

    var a4 = Math.round(Math.random() * (100 + i)) + 200 + i;
    var b4 = Math.round(Math.random() * (100 + i)) + 600 + i;

    chart.dataSets[0].dataProvider.push({
        date: newDate,
        value: a1,
        volume: b1
    });
    chart.dataSets[1].dataProvider.push({
        date: newDate,
        value: a2,
        volume: b2
    });
    chart.dataSets[2].dataProvider.push({
        date: newDate,
        value: a3,
        volume: b3
    });
    chart.dataSets[3].dataProvider.push({
        date: newDate,
        value: a4,
        volume: b4
    });

    chart.validateData();
}, 1000);
