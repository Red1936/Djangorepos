// script.js
document.addEventListener("DOMContentLoaded", function () {
    // Obtén el elemento DOM del contenedor
    var chart = document.getElementById('chart');

    // Inicializa un gráfico de ECharts en el contenedor
    var miGrafico = echarts.init(chart);

    // Datos de ejemplo para los días de la semana y sus valores
    var x_data = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'];
    var y_data = [10, 20, 15, 30, 25, 10, 5];

    // Configura el gráfico ECharts
    var option = {
        xAxis: {
            type: 'category',
            data: x_data,
        },
        yAxis: {
            type: 'value',
        },
        series: [{
            data: y_data,
            type: 'bar',
        }]
    };

    // Establece la configuración en el gráfico
    miGrafico.setOption(option);
});

