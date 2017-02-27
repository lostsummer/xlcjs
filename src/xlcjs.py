from __future__ import division
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ui_dlg import Ui_Dialog
from scipy.optimize import fsolve, root
from ui_logindlg import Ui_LoginDialog
from math import sqrt, sin, cos, acos, pi

try:
    _fromUtf8 = QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class myLoginDialog(QDialog, Ui_LoginDialog):
	def __init__(self, mainWidget, parent=None):
		super(myLoginDialog, self).__init__(parent)
		self.setupUi(self)
		self.mainWidget = mainWidget

	@pyqtSlot()
	def on_pushButton_clicked(self):
		self.hide()
		self.mainWidget.show()


class myDlg(QDialog, Ui_Dialog):

	def __init__(self, parent=None):
		super(myDlg, self).__init__(parent)
		self.setupUi(self)
		self.connect(self, SIGNAL(_fromUtf8("currentChanged(int)")), self.on_tabWidget_currentChanged)
		self.sjll_input = []
		self.sjll_output = []
		self.cdbh=[]
		self.cs_input = {}
		self.cs_output = {}
		

        
	@pyqtSlot()
	def on_pushButton_2_clicked(self):
		self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)

	@pyqtSlot()
	def on_pushButton_3_clicked(self):
		self.tableWidget.setRowCount(self.tableWidget.rowCount() - 1)

	@pyqtSlot()
	def on_pushButton_clicked(self):
		self.tableWidget_2.setRowCount(self.tableWidget.rowCount())
		self.getSjllInput()
		self.caculateSjll()
		self.setSjllOutput()

	@pyqtSlot()
	def on_pushButton_4_clicked(self):
		self.tableWidget_3.setRowCount(self.tableWidget_3.rowCount() + 1)

	@pyqtSlot()
	def on_pushButton_5_clicked(self):
		self.tableWidget_3.setRowCount(self.tableWidget_3.rowCount() - 1)

	@pyqtSlot()
	def on_pushButton_6_clicked(self):
		self.getCdbhInput()
		self.caculateCdbh()
		self.setCdbhOutput()

	@pyqtSlot()
	def on_pushButton_13_clicked(self):
		self.getCSInput()
		self.caculateCS()
		self.setCSOutput()

	@pyqtSlot()
	def on_pushButton_14_clicked(self):
		self.getCSInput()
		self.caculateCS_Y()
		self.setCS_YOutput()

	@pyqtSlot()
	def on_pushButton_7_clicked(self):
		D6 = self.DoubleSpinBox1_3.value()
		D7 = self.DoubleSpinBox2_3.value()
		D8 = self.DoubleSpinBox3_3.value()
		D9 = self.DoubleSpinBox4_3.value()
		D10 = self.DoubleSpinBox5_3.value()
		D11 = self.DoubleSpinBox6_3.value()
		D12 = self.DoubleSpinBox7_3.value()
		D13 = self.DoubleSpinBox8_3.value()
		I6 = self.DoubleSpinBox9_3.value()
		I7 = self.DoubleSpinBox10_3.value()
		I8 = self.DoubleSpinBox11_3.value()
		I9 = self.DoubleSpinBox12_3.value()
		I10 = self.DoubleSpinBox13_3.value()

		try:
			D15 = D9-D10
			D16 = D11-D12
			D17 = D9-D11
			D18 = D6/I9
			D19 = I10+D15+I8*D13**2/2/I6+(D10-D12)
			D20 = D19/3*(1-2*cos(pi/3+acos(1-27/8*2*I8*D18**2/I7**2/I6/D19**3)/3))
			D21 = sqrt(D18**2/(I6*D20**3))
			D22 = D20/2*(sqrt(1+8*I8*D21**2)-1)*(D7/D8)**0.25
			D23 = (I10+D16)/D22+I8*D18**2/2/I6/D22*(1/I7**2/D16**2-1/D22**2)
		except ZeroDivisionError:
			D15 = D16 = D17 = D18 = D19 = D20 = D21 = D22 = D23 = 0

		self.DoubleSpinBox1_4.setValue(D15)
		self.DoubleSpinBox2_4.setValue(D16)
		self.DoubleSpinBox3_4.setValue(D17)
		self.DoubleSpinBox4_4.setValue(D18)
		self.DoubleSpinBox5_4.setValue(D19)
		self.DoubleSpinBox6_4.setValue(D20)
		self.DoubleSpinBox7_4.setValue(D21)
		self.DoubleSpinBox8_4.setValue(D22)
		self.DoubleSpinBox9_4.setValue(D23)


	@pyqtSlot()
	def on_pushButton_9_clicked(self):
		D6 = self.DoubleSpinBox1_8.value()
		D7 = self.DoubleSpinBox2_8.value()
		D8 = self.DoubleSpinBox3_8.value()
		D9 = self.DoubleSpinBox4_8.value()
		D10 = self.DoubleSpinBox5_8.value()
		D11 = self.DoubleSpinBox6_8.value()
		D12 = self.DoubleSpinBox7_8.value()
		D13 = self.DoubleSpinBox8_8.value()
		I6 = self.DoubleSpinBox9_8.value()
		I7 = self.DoubleSpinBox10_8.value()
		I8 = self.DoubleSpinBox11_8.value()
		I9 = self.DoubleSpinBox12_8.value()
		I10 = self.DoubleSpinBox13_8.value()

		try:
			D15 = D9-D10
			D16 = D11-D12
			D17 = D9-D11
			D18 = D6/I9
			D19 = I10+D15+I8*D13**2/2/I6+(D10-D12)
			D20 = D19/3*(1-2*cos(pi/3+acos(1-27/8*2*I8*D18**2/I7**2/I6/D19**3)/3))
			D21 = sqrt(D18**2/(I6*D20**3))
			D22 = D20/2*(sqrt(1+8*I8*D21**2)-1)*(D7/D8)**0.25
			D23 = (I10+D16)/D22+I8*D18**2/2/I6/D22*(1/I7**2/D16**2-1/D22**2)
		except ZeroDivisionError:
			D15 = D16 = D17 = D18 = D19 = D20 = D21 = D22 = D23 = 0

		self.DoubleSpinBox1_7.setValue(D15)
		self.DoubleSpinBox2_7.setValue(D16)
		self.DoubleSpinBox3_7.setValue(D17)
		self.DoubleSpinBox4_7.setValue(D18)
		self.DoubleSpinBox5_7.setValue(D19)
		self.DoubleSpinBox6_7.setValue(D20)
		self.DoubleSpinBox7_7.setValue(D21)
		self.DoubleSpinBox8_7.setValue(D22)
		self.DoubleSpinBox9_7.setValue(D23)

	@pyqtSlot()
	def on_pushButton_10_clicked(self):
		D3 = self.DoubleSpinBox1_9.value()
		D4 = self.DoubleSpinBox2_9.value()
		D5 = self.DoubleSpinBox3_9.value()
		I3 = self.DoubleSpinBox4_9.value()
		I4 = self.DoubleSpinBox5_9.value()

		D8 = D5 * D3
		D11 = 6.9*(I4-I3)
		D12 = D8+D4*D11

		self.DoubleSpinBox1_10.setValue(D8)
		self.DoubleSpinBox2_10.setValue(D11)
		self.DoubleSpinBox3_10.setValue(D12)
	
	def on_tabWidget_currentChanged(self):
		self.DoubleSpinBox2_3.setValue(self.DoubleSpinBox2.value())
		self.DoubleSpinBox3_3.setValue(self.DoubleSpinBox3.value())
		self.DoubleSpinBox5_3.setValue(self.DoubleSpinBox5.value())
		self.DoubleSpinBox7_3.setValue(self.DoubleSpinBox7.value())
		self.DoubleSpinBox8_3.setValue(self.DoubleSpinBox7_2.value())
		self.DoubleSpinBox9_3.setValue(self.DoubleSpinBox10.value())
		self.DoubleSpinBox10_3.setValue(self.DoubleSpinBox11.value())
		self.DoubleSpinBox11_3.setValue(self.DoubleSpinBox12.value())
		self.DoubleSpinBox12_3.setValue(self.DoubleSpinBox8.value())
		self.DoubleSpinBox13_3.setValue(self.DoubleSpinBox14.value())

		self.DoubleSpinBox2_8.setValue(self.DoubleSpinBox2.value())
		self.DoubleSpinBox3_8.setValue(self.DoubleSpinBox3.value())
		self.DoubleSpinBox5_8.setValue(self.DoubleSpinBox5.value())
		self.DoubleSpinBox7_8.setValue(self.DoubleSpinBox7.value())
		self.DoubleSpinBox8_8.setValue(self.DoubleSpinBox7_2.value())
		self.DoubleSpinBox9_8.setValue(self.DoubleSpinBox10.value())
		self.DoubleSpinBox10_8.setValue(self.DoubleSpinBox11.value())
		self.DoubleSpinBox11_8.setValue(self.DoubleSpinBox12.value())
		self.DoubleSpinBox12_8.setValue(self.DoubleSpinBox8.value())
		self.DoubleSpinBox13_8.setValue(self.DoubleSpinBox14.value())

		__D36 = self.DoubleSpinBox14.value()
		__D9 = self.DoubleSpinBox5.value()
		__D11 = self.DoubleSpinBox7.value()
		__D20 = self.DoubleSpinBox6_4.value()
		__D22 = self.DoubleSpinBox8_4.value()

		D3 = __D36 + __D9 - __D11
		I3 = __D20
		I4 = __D22

		self.DoubleSpinBox1_9.setValue(D3)
		self.DoubleSpinBox4_9.setValue(I3)
		self.DoubleSpinBox5_9.setValue(I4)

	def caculateSjll(self):
		rowCount = len(self.sjll_input)
		self.sjll_output = []
		for i in range(rowCount):
			self.sjll_output.append({})
			if self.sjll_input[i] == None:
				self.sjll_output[i] = None
			else:
				getEqResult(self.sjll_input[i], self.sjll_output[i])
				

	def getSjllInput(self):
		rowCount = self.tableWidget.rowCount()
		self.sjll_input = []
		for i in range(rowCount):
			self.sjll_input.append({})
			for j in range(ord('L') - ord('A') + 1):
				k = chr(ord('A') + j)
				try:
					self.sjll_input[i][k] = float(self.tableWidget.item(i, j).text())
				except (ValueError, AttributeError):
					self.sjll_input[i] = None
					break


	def setSjllOutput(self):
		rowCount = len(self.sjll_output)
		for i in range(rowCount):
			if self.sjll_output[i] == None:
				continue
			for j in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
				item = QTableWidgetItem(format(self.sjll_output[i][j], '.3f'))
				n = ord(j) - ord('A')
				self.tableWidget_2.setItem(i, n, item)


	def getCdbhInput(self):
		rowCount = self.tableWidget_3.rowCount()
		self.cdbh = []
		for i in range(rowCount):
			self.cdbh.append({})
			for j in ['A', 'B', 'C']:
				n = ord(j) - ord('A')
				try:
					self.cdbh[i][j] = float(self.tableWidget_3.item(i, n).text())
				except (ValueError, AttributeError):
					self.cdbh[i] = None
					break

	def setCdbhOutput(self):
		rowCount = len(self.cdbh)
		for i in range(rowCount):
			if self.cdbh[i] == None:
				continue
			item = QTableWidgetItem(format(self.cdbh[i]['D'], '.1f'))
			self.tableWidget_3.setItem(i, 3, item)

	def caculateCdbh(self):
		rowCount = len(self.cdbh)
		for i in range(rowCount):
			if self.cdbh[i] == None:
				continue
			self.cdbh[i]['D'] = self.cdbh[i]['A'] * (self.cdbh[i]['B'] - self.cdbh[i]['C'])

	def getCSInput(self):
		input = {}
		input['D5'] = self.DoubleSpinBox1.value()
		input['D6'] = self.DoubleSpinBox2.value()
		input['D7'] = self.DoubleSpinBox3.value()
		input['D8'] = self.DoubleSpinBox4.value()
		input['D9'] = self.DoubleSpinBox5.value()
		input['D10'] = self.DoubleSpinBox6.value()
		input['D11'] = self.DoubleSpinBox7.value()
		input['I5'] = self.DoubleSpinBox8.value()
		input['I6'] = self.DoubleSpinBox9.value()
		input['I7'] = self.DoubleSpinBox10.value()
		input['I8'] = self.DoubleSpinBox11.value()
		input['I9'] = self.DoubleSpinBox12.value()
		input['I10'] = self.DoubleSpinBox13.value()
		input['D22'] = self.DoubleSpinBox1_2.value()
		input['D23'] = self.DoubleSpinBox2_2.value()
		input['D24'] = self.DoubleSpinBox3_2.value()
		input['D25'] = self.DoubleSpinBox4_2.value()
		input['D26'] = self.DoubleSpinBox6_2.value()
		input['D27'] = self.DoubleSpinBox7_2.value()
		input['D28'] = self.DoubleSpinBox8_2.value()
		input['D29'] = self.DoubleSpinBox9_2.value()
		input['D30'] = self.DoubleSpinBox10_2.value()
		input['D31'] = self.DoubleSpinBox11_2.value()
		input['D32'] = self.DoubleSpinBox12_2.value()
		input['D33'] = self.DoubleSpinBox13_2.value()
		input['D36'] = self.DoubleSpinBox14.value()

		self.cs_input = input

	def setCSOutput(self):
		output = self.cs_output
		self.DoubleSpinBox1_2.setValue(output['D22'])
		self.DoubleSpinBox2_2.setValue(output['D23'])
		self.DoubleSpinBox3_2.setValue(output['D24'])
		self.DoubleSpinBox4_2.setValue(output['D25'])
		self.DoubleSpinBox6_2.setValue(output['D26'])
		self.DoubleSpinBox7_2.setValue(output['D27'])
		self.DoubleSpinBox8_2.setValue(output['D28'])
		self.DoubleSpinBox9_2.setValue(output['D29'])
		self.DoubleSpinBox10_2.setValue(output['D30'])
		self.DoubleSpinBox11_2.setValue(output['D31'])
		self.DoubleSpinBox12_2.setValue(output['D32'])
		self.DoubleSpinBox13_2.setValue(output['D33'])
		self.DoubleSpinBox5_2.setValue(output['G23'])
		#self.DoubleSpinBox14.setValue(output['D33'])

	def caculateCS(self):
		input = self.cs_input
		D5 = input['D5']
		D6 = input['D6']
		D7 = input['D7']
		D8 = input['D8']
		D9 = input['D9']
		D10 = input['D10']
		D11 = input['D11']
		I5 = input['I5']
		I6 = input['I6']
		I7 = input['I7']
		I8 = input['I8']
		I9 = input['I9']
		I10 = input['I10']
		
		D22 = D5 / I5
		D24 = D8 - D9
		G23 = (I9*D22**2/I7)**(1/3)
		G25 = (I9*(D5/D7)**2/I7)**(1/3)
		D25 = max(D10-D11, G25)
		D26 = D8-D10
		D27 = D5/I6/D24

		print("D22:{0} D24:{1} G23:{2} G25:{3} D25:{4} D26:{5} D27:{6}".format(D22, D24, G23, G25, D25, D26, D27))
		#D28 = (D22**2/(I7*D23**3)) ** (1/2)
		#D29 = (D23**3+I9*D22**2/(2*I7*I8**2))/D23**2
		#D30 = D23/2*((1+8*I9*D28**2)-1)**(1/2)*(D6/D7)**2.5
		#D31 = I9*(D5/D7)**2/(2*I7*I8**2*D25**2)-I9*(D5/D7)**2/(2*I7*D30**2)
		#D32 = D29-D24-I9*D27**2/2/I7-(D9-D11)
		#D33 = I10*D30-D25-D31
		#D32 - D33 == 0

		def func(v):
			_D23, _D28, _D29, _D30, _D31, _D32, _D33 = v.tolist()
			return [
					sqrt(D22**2/(I7*_D23**3)) - _D28,
					(_D23**3+I9*D22**2/(2*I7*I8**2))/_D23**2 - _D29,
					_D23/2 * (sqrt(1+8*I9*_D28**2)-1) * (D6/D7)**0.25 - _D30,
					I9*(D5/D7)**2 / (2*I7 * I8**2 * D25**2) - I9*(D5/D7)**2/(2*I7*_D30**2) - _D31,
					_D29-D24-I9*D27**2/2/I7-(D9-D11) - _D32,
					I10*_D30-D25-_D31 - _D33,
					_D32 + 0.000 - _D33
					]
		
		D23 = self.DoubleSpinBox2_2.value()
		if D23 == 0:
			D23 = 0.5

		D28 = (D22**2/(I7*D23**3)) ** 0.5
		D29 = (D23**3+I9*D22**2/(2*I7*I8**2))/D23**2
		D30 = D23/2 * ((1+8*I9*D28**2)**0.5-1)* (D6/D7)**0.25
		D31 = I9*(D5/D7)**2 / (2*I7 * I8**2 * D25**2) - I9*(D5/D7)**2/(2*I7*D30**2)
		D32 = D29-D24-I9*D27**2/2/I7-(D9-D11)
		D33 = I10*D30-D25-D31
		D33 = D32

		r = fsolve(func, [D23, D28, D29, D30, D31, D32, D33])
		#r = fsolve(func, [D23, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1])
		D23 = r[0]
		D28 = r[1]
		D29 = r[2]
		D30 = r[3]
		D31 = r[4]
		D32 = r[5]
		D33 = r[6]
		#r = root(func, [D23, D28, D29, D30, D31, D32, D33], method='lm')
		#D23 = r._D23
		#D28 = r._D28
		#D29 = r._D29
		#D30 = r._D30
		#D31 = r._D31
		#D32 = r._D32
		#D33 = r._D33
		#print(r.x)

		self.cs_output["D22"] = D22
		self.cs_output["D23"] = D23
		self.cs_output["D24"] = D24
		self.cs_output["D25"] = D25
		self.cs_output["D26"] = D26
		self.cs_output["D27"] = D27
		self.cs_output["D28"] = D28
		self.cs_output["D29"] = D29
		self.cs_output["D30"] = D30
		self.cs_output["D31"] = D31
		self.cs_output["D32"] = D32
		self.cs_output["D33"] = D33
		self.cs_output["G23"] = G23
		

	def caculateCS_Y(self):
		input = self.cs_input
		D5 = input['D5']
		D6 = input['D6']
		D7 = input['D7']
		D8 = input['D8']
		D9 = input['D9']
		D10 = input['D10']
		D11 = input['D11']
		I5 = input['I5']
		I6 = input['I6']
		I7 = input['I7']
		I8 = input['I8']
		I9 = input['I9']
		I10 = input['I10']
		D22 = input['D22']
		D23 = input['D23']
		D24 = input['D24']
		D25 = input['D25']
		D26 = input['D26']
		D27 = input['D27']
		D28 = input['D28']
		D29 = input['D29']
		D30 = input['D30']
		D31 = input['D31']
		D32 = input['D32']
		D33 = input['D33']
		D36 = input['D36']

		D39 = D36+D24+I9*D27**2/2/I7+(D9-D11)
		D40 = D39/3*(1-2*cos(pi/3+acos(1-27/8*2*I9*D22**2/I8**2/I7/D39**3)/3))
		D41 = sqrt(D22**2/(I7*D40**3))
		D42 = D40/2*(sqrt(1+8*I9*D41**2)-1)*(D6/D7)**0.25
		D43 = (D36+D25)/D42+I9*D22**2/2/I7/D42*(1/I8**2/D25**2-1/D42**2)
		D44 = 0.49*(0.1*D41*D41-D41+5)

		self.cs_output['D39'] = D39
		self.cs_output['D40'] = D40
		self.cs_output['D41'] = D41
		self.cs_output['D42'] = D42
		self.cs_output['D43'] = D43
		self.cs_output['D44'] = D44

	def setCS_YOutput(self):
		self.DoubleSpinBox15.setValue(self.cs_output['D39'])
		self.DoubleSpinBox16.setValue(self.cs_output['D40'])
		self.DoubleSpinBox17.setValue(self.cs_output['D41'])
		self.DoubleSpinBox18.setValue(self.cs_output['D42'])
		self.DoubleSpinBox19.setValue(self.cs_output['D43'])
		self.DoubleSpinBox20.setValue(self.cs_output['D44'])



def getEqResult(input, output):
	a_ = input['A']
	b_ = input['B']
	c_ = input['C']
	d_ = input['D']
	e_ = input['E']
	f_ = input['F']
	g_ = input['G']
	h_ = input['H']
	i_ = input['I']
	j_ = input['J']
	k_ = input['K']
	l_ = input['L']
	b = c_ / b_
	a = b / a_

	def func(v):
		c, d, e, f, g, h = v.tolist()
		return [
				c/2*((1+8*d_*b**2/e_/c**3)**0.5-1)*(g_/h_)**0.25-d,
				d_*b**2/2/e_/f_**2/i_**2-d_*b**2/2/e_/d**2-e,
				c+d_*b**2/2/e_/c**2/f_**2-f,
				f-a_-d_*a**2/2/e_-(k_-l_)-g,
				j_*d-i_-e-h,
				h-g
				]

	r = fsolve(func, [0.1,0.1,0.1,0.1,0.1,0.1])
	output['A'] = a
	output['B'] = b
	output['C'] = r[0]
	output['D'] = r[1]
	output['E'] = r[2]
	output['F'] = r[3]
	output['G'] = r[4]
	output['H'] = r[5]



if __name__ == "__main__":
	import sys
 	app = QApplication(sys.argv)
 	dlg = myDlg()
 	loginDlg = myLoginDialog(dlg)
	loginDlg.show()
	sys.exit(app.exec_())