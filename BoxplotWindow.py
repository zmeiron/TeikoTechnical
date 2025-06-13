import numpy as np
from PySide6.QtWidgets import QMainWindow
from PySide6.QtCharts import QChart, QChartView, QBoxPlotSeries, QBoxSet

class BoxplotWindow(QMainWindow):
    def __init__(self, y_dataset, n_dataset):
        super().__init__()

        y_series = QBoxPlotSeries()
        y_series.setName("Responders")
    
        n_series = QBoxPlotSeries()
        n_series.setName("Non-Responders")
        
        # create boxplot
        for population, data in y_dataset.items():
            y_box = QBoxSet(population)
            self._setup_box(y_box, data)
            y_series.append(y_box)
        
        for population, data in n_dataset.items():
            n_box = QBoxSet(population)
            self._setup_box(n_box, data)
            n_series.append(n_box)
            
        
        # create chart to display boxplot
        chart = QChart()
        chart.addSeries(y_series)
        chart.addSeries(n_series)
        chart.setTitle("Comparing responsive samples with cell population relative frequencies")
        chart.createDefaultAxes()

        chart_view = QChartView(chart)
        self.setCentralWidget(chart_view)
        self.resize(800, 600)
        self.setWindowTitle("Population Boxplots")
        
    
    def _setup_box(self, box, data):
        data.sort()
        median = np.median(data)
        upper_quartile = np.percentile(data, 75)
        lower_quartile = np.percentile(data, 25)

        box.setValue(0, data[0])  # min
        box.setValue(1, lower_quartile)  # Q1
        box.setValue(2, median)  # med
        box.setValue(3, upper_quartile)  # Q3
        box.setValue(4, data[-1])  # max
