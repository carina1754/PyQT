from pyupbit import WebSocketManager
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Worker(QThread):
    recv = pyqtSignal(dict)

    def run(self):
        # create websocket for Bithumb
        wm = WebSocketManager("ticker", ["KRW-QTUM"])
        while True:
            data = wm.get()
            print(data)
            self.recv.emit(data)


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        label = QLabel("QTUM", self)
        label.move(20, 20)
        
        label = QLabel("이율", self)
        label.move(20, 40)
        
        self.price = QLabel("", self)
        self.price.move(80, 25)
        self.price.resize(100, 20)

        self.price2 = QLabel("", self)
        self.price2.move(80, 45)
        self.price2.resize(100, 20)
        
        self.th = Worker()
        self.th.recv.connect(self.receive_msg)
        self.th.start()
    
    @pyqtSlot(dict)
    def receive_msg(self, data):
        print(data)
        close_price = data.get("trade_price")
        inner_price = round(close_price/5770*100-100,3)
        self.price.setText(str(close_price))
        self.price2.setText(str(inner_price))


if __name__ == '__main__':
   app = QApplication(sys.argv)
   mywindow = MyWindow()
   mywindow.show()
   app.exec_()