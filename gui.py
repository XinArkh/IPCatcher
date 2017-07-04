import sys
from PyQt5 import QtWidgets, QtCore
from ip_practice import ip_get, data_pretreatment, data_get, translation

class GUI(QtWidgets.QWidget):
    def __init__(self):
        super(GUI, self).__init__()
        self.setWindowTitle("IP定位器")
        self.setGeometry(300, 300, 350, 170)
        self.button = QtWidgets.QPushButton("开始", self)
        self.button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button.move(20, 20)
        self.button.clicked.connect(self.show_data)
        self.setFocus()

        self.label_1 = QtWidgets.QLineEdit(self)
        self.label_1.move(160, 22)
        self.label_2 = QtWidgets.QLineEdit(self)
        self.label_2.move(160, 52)
        self.label_3 = QtWidgets.QLineEdit(self)
        self.label_3.move(160, 82)
        self.label_4 = QtWidgets.QLineEdit(self)
        self.label_4.move(160, 112)

    def show_data(self):
        text, ok = QtWidgets.QInputDialog.getText(self, "请确认", "请输入“我要上车”：")
        if ok:
            if text == "我要上车":
                self.show_data_2()
            else:
                self.label_1.setText("这趟车不发了")
                self.label_2.setText("这趟车不发了")
                self.label_3.setText("这趟车不发了")
                self.label_4.setText("这趟车不发了")


    def show_data_2(self):
        text, ok = QtWidgets.QInputDialog.getText(self, "请确认", "请输入“我已刷卡”：")
        if ok:
            if text == "我已刷卡":
                ip = ip_get.getip()
                responseJson = data_pretreatment.pretreatment(ip)
                country = data_get.getcountry(responseJson)
                country_CH = translation.translate(country)
                country_code = data_get.getcountry_code(responseJson)
                latitude = data_get.getlatitude(responseJson)
                longitude = data_get.getlongitude(responseJson)
                self.label_1.setText("IP：" + ip)
                self.label_2.setText("国家：" + country_CH + "(" + country_code + ")")
                self.label_3.setText("纬度：" + str(latitude))
                self.label_4.setText("经度：" + str(longitude))
            else:
                self.label_1.setText("这趟车不发了")
                self.label_2.setText("这趟车不发了")
                self.label_3.setText("这趟车不发了")
                self.label_4.setText("这趟车不发了")

app = QtWidgets.QApplication(sys.argv)
input_dialog = GUI()
input_dialog.show()
sys.exit(app.exec_())