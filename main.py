import sys
import numpy as np
from collections import defaultdict
from database import Database
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
# get UI windows
from MainWindowPop import Ui_MainWindow as UI_MainWindow
from MainWindowMel import Ui_MainWindow as MelWindow
from AddWindow import Ui_MainWindow as AddWindow
from RemoveWindow import Ui_MainWindow as RemoveWindow
from BoxplotWindow import BoxplotWindow


class MainWindow(QMainWindow, UI_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.database = Database()
        self.database.load(False)
        self.mel_window = None
        self.add_window = None
        self.remove_window = None
        
        self.load_pop_table(self.database.get_all_samples())
        self.tableWidget.setSortingEnabled(True)
        
        self.melButton.clicked.connect(self.melanoma_window)
        self.actionAdd_Sample.triggered.connect(self.add_sample)
        self.actionRemove_Sample.triggered.connect(self.remove_sample)
        
        
        
    def add_row(self, row, sample, total, population, count, percentage):
        # to display and sort as actual numeric
        total_item = QTableWidgetItem()
        count_item = QTableWidgetItem()
        percent_item = QTableWidgetItem()
        total_item.setData(Qt.DisplayRole, total)
        count_item.setData(Qt.DisplayRole, count)
        percent_item.setData(Qt.DisplayRole, percentage)
        
        self.tableWidget.setItem(row, 0, QTableWidgetItem(str(sample)))
        self.tableWidget.setItem(row, 1, total_item)
        self.tableWidget.setItem(row, 2, QTableWidgetItem(str(population)))
        self.tableWidget.setItem(row, 3, count_item)
        self.tableWidget.setItem(row, 4, percent_item)

            
    def load_pop_table(self, samples):
        self.tableWidget.clearContents()
        # set rows to samples * 5 for each population
        self.tableWidget.setRowCount(len(samples)*5)
        count = 0
        for row in samples:
            # do percentage calculations
            bCount = row[11]
            cd8Count = row[12]
            cd4Count = row[13]
            nkCount = row[14]
            monoCount = row[15]
            total = bCount + cd8Count + cd4Count + nkCount + monoCount
            
            self.add_row(count    , row[8], total, 'b_cell', bCount, bCount/total)
            self.add_row(count + 1, row[8], total, 'cd8_t_cell', cd8Count, cd8Count/total)
            self.add_row(count + 2, row[8], total, 'cd4_t_cell', cd4Count, cd4Count/total)
            self.add_row(count + 3, row[8], total, 'nk_cell', nkCount, nkCount/total)
            self.add_row(count + 4, row[8], total, 'monocyte', monoCount, monoCount/total)
            count += 5
            
            
    def melanoma_window(self):
        if self.mel_window is None:
            self.mel_window = MelWindow(self.database)
        self.mel_window.show()
    
    def add_sample(self):
        if self.add_window is None:
            self.add_window = AddWindow(self.database)
        self.add_window.show()
        self.add_window.destroyed.connect(self.add_closed)
        
    def add_closed(self):
        self.load_pop_table(self.database.get_all_mel_samples())
        
    def remove_sample(self):
        if self.remove_window is None:
            self.remove_window = RemoveWindow(self.database)
        self.remove_window.show()
        self.remove_window.destroyed.connect(self.remove_closed)
    
    def remove_closed(self):
        self.load_pop_table(self.database.get_all_mel_samples())
            

class MelWindow(QMainWindow, MelWindow):
    def __init__(self, database):
        super().__init__()
        self.setupUi(self)
        self.database = database
        self.boxplot_window = None
        self.baseline_only = False
        self.plotButton.clicked.connect(self.show_boxplots)
        self.baselineCheckBox.clicked.connect(self.baseline_clicked)
        
        
        
        self.load_pop_table(self.database.get_all_mel_samples())
        self.set_significant_populations()
        
        
    def add_row(self, row, sample, response, total, population, count, percentage):
        # to display and sort as actual numeric
        total_item = QTableWidgetItem()
        count_item = QTableWidgetItem()
        percent_item = QTableWidgetItem()
        total_item.setData(Qt.DisplayRole, total)
        count_item.setData(Qt.DisplayRole, count)
        percent_item.setData(Qt.DisplayRole, percentage)
        
        self.tableWidget.setItem(row, 0, QTableWidgetItem(sample))
        self.tableWidget.setItem(row, 1, QTableWidgetItem(response))
        self.tableWidget.setItem(row, 2, total_item)
        self.tableWidget.setItem(row, 3, QTableWidgetItem(population))
        self.tableWidget.setItem(row, 4, count_item)
        self.tableWidget.setItem(row, 5, percent_item)
    
    
    def load_pop_table(self, samples):
        self.tableWidget.clearContents()
        # set rows to samples * 5 for each population
        self.tableWidget.setRowCount(len(samples)*5)
        count = 0
        for row in samples:
            # baseline filtering
            if self.baseline_only:
                if row[10] != 0:
                    continue
            
            # do percentage calculations
            bCount = row[11]
            cd8Count = row[12]
            cd4Count = row[13]
            nkCount = row[14]
            monoCount = row[15]
            total = bCount + cd8Count + cd4Count + nkCount + monoCount
            
            self.add_row(count    , row[8], row[7], total, 'b_cell', bCount, bCount/total)
            self.add_row(count + 1, row[8], row[7], total, 'cd8_t_cell', cd8Count, cd8Count/total)
            self.add_row(count + 2, row[8], row[7], total, 'cd4_t_cell', cd4Count, cd4Count/total)
            self.add_row(count + 3, row[8], row[7], total, 'nk_cell', nkCount, nkCount/total)
            self.add_row(count + 4, row[8], row[7], total, 'monocyte', monoCount, monoCount/total)
            count += 5
            
            
    def baseline_clicked(self):
        self.baseline_only = not self.baseline_only
        samples = self.database.get_all_mel_samples()
        
        if self.baseline_only:
            # gather additional info
            projects = defaultdict(int)
            subjects = {} # subject: (sex, response)
            for sample in samples:
                projects[sample[1]] += 1
                subjects[sample[2]] = (sample[5], sample[7])
                
            male = 0
            female = 0
            responders = 0
            nonresponders = 0
            for subject in subjects.values():
                if subject[0] == "M":
                    male += 1
                else:
                    female += 1
                
                if subject[1] == "y":
                    responders += 1
                else:
                    nonresponders += 1
                            
            # assemble display string
            details = ""
            for project, count in projects.items():
                details += f"{project}: {count} samples | "
            
            details += f"{male} men, {female} women | "
            details += f"{responders} responders, {nonresponders} non-responders"
            self.detailsLabel.setText(details)
            
        else:
            self.detailsLabel.setText("")
        
        self.load_pop_table(samples)
        
        
        
    def show_boxplots(self):
        ydataset, ndataset = self.get_responder_data()
        if self.boxplot_window is None:
            self.boxplot_window = BoxplotWindow(ydataset, ndataset)
        self.boxplot_window.show()
        
    def set_significant_populations(self):
        ydataset, ndataset = self.get_responder_data()
        sig_string = ""
        for population, ydata in ydataset.items():
            ndata = ndataset[population]
            
            # sort to get min and max
            ydata.sort()
            ndata.sort()
            
            ymedian = np.median(ydata)
            nmedian = np.median(ndata)
            
            # considering significant as the median falling outside the range of the other
            if (ymedian < ndata[0] or ymedian > ndata[-1]) and \
               (nmedian < ydata[0] or nmedian > ydata[-1]):
                sig_string += f"{population}, "
        
        self.significantLabel.setText(sig_string[:-2])
        
        
    def get_responder_data(self):
        # get melanoma data
        bCounts = self.database.get_mel_population_counts('b_cell')
        cd8Counts = self.database.get_mel_population_counts('cd8_t_cell')
        cd4Counts = self.database.get_mel_population_counts('cd4_t_cell')
        nkCounts = self.database.get_mel_population_counts('nk_cell')
        monoCounts = self.database.get_mel_population_counts('monocyte')
        # separate into responder and non responding
        ybCounts = [count[0] for count in bCounts if count[1] == 'y']
        ycd8Counts = [count[0] for count in cd8Counts if count[1] == 'y']
        ycd4Counts = [count[0] for count in cd4Counts if count[1] == 'y']
        ynkCounts = [count[0] for count in nkCounts if count[1] == 'y']
        ymonoCounts = [count[0] for count in monoCounts if count[1] == 'y']
        nbCounts = [count[0] for count in bCounts if count[1] == 'n']
        ncd8Counts = [count[0] for count in cd8Counts if count[1] == 'n']
        ncd4Counts = [count[0] for count in cd4Counts if count[1] == 'n']
        nnkCounts = [count[0] for count in nkCounts if count[1] == 'n']
        nmonoCounts = [count[0] for count in monoCounts if count[1] == 'n']
        # create dicts with each population as key
        ydataset = {'b_cell':ybCounts, 'cd8_t_cell':ycd8Counts, 'cd4_t_cell':ycd4Counts, 'nk_cell':ynkCounts, 'monocyte':ymonoCounts}
        ndataset = {'b_cell':nbCounts, 'cd8_t_cell':ncd8Counts, 'cd4_t_cell':ncd4Counts, 'nk_cell':nnkCounts, 'monocyte':nmonoCounts}
        return (ydataset, ndataset)
        

class AddWindow(QMainWindow, AddWindow):
    def __init__(self, database):
        super().__init__()
        self.setupUi(self)
        self.database = database
        
        self.addButton.clicked.connect(self.add_clicked)
        
    def add_clicked(self):
        # get values
        project = self.projectLineEdit.text()
        subject = self.subjectLineEdit.text()
        condition = self.conditionLineEdit.text()
        age = self.ageLineEdit.text()
        sex = self.sexLineEdit.text()
        treatment = self.treatmentLineEdit.text()
        response = self.responseLineEdit.text()
        sample = self.sampleLineEdit.text()
        sample_type = self.sampleTypeLineEdit.text()
        tft = self.tftLineEdit.text()
        b_cell = self.bLineEdit.text()
        cd8_cell = self.cd8LineEdit.text()
        cd4_cell = self.cd4LineEdit.text()
        nk_cell = self.nkLineEdit.text()
        monocyte = self.monoLineEdit.text()
        
        self.database.add_sample((project, subject, condition, age, sex, treatment, response, sample, sample_type, tft, b_cell, cd8_cell, cd4_cell, nk_cell, monocyte))
        
        # clear values
        self.projectLineEdit.setText("")
        self.subjectLineEdit.setText("")
        self.conditionLineEdit.setText("")
        self.ageLineEdit.setText("")
        self.sexLineEdit.setText("")
        self.treatmentLineEdit.setText("")
        self.responseLineEdit.setText("")
        self.sampleLineEdit.setText("")
        self.sampleTypeLineEdit.setText("")
        self.tftLineEdit.setText("")
        self.bLineEdit.setText("")
        self.cd8LineEdit.setText("")
        self.cd4LineEdit.setText("")
        self.nkLineEdit.setText("")
        self.monoLineEdit.setText("")
        
        
class RemoveWindow(QMainWindow, RemoveWindow):
    def __init__(self, database):
        super().__init__()
        self.setupUi(self)
        self.database = database
        
        self.removeButton.clicked.connect(self.remove_clicked)
        
    def remove_clicked(self):
        sample = self.sampleLineEdit.text()
        self.database.delete_sample(sample)
        self.sampleLineEdit.setText("")
        
        

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()