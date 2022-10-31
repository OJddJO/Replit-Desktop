from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon
from pypresence import Presence
from time import time

clientId = "1028218378357329990"
try:
    RPC = Presence(clientId)
    RPC.connect()
    print("Discord RPC is ready !")
except:
    print("Discord not found.")

RPC.update(
    large_image="logo",
    large_text="Replit Desktop",
    start=time(),
)

class WebEnginePage(QWebEnginePage):
    def __init__(self, *args, **kwargs):
        QWebEnginePage.__init__(self, *args, **kwargs)

app = QApplication([])

view = QWebEngineView()
page = WebEnginePage()
view.setPage(page)
view.load(QUrl("https://replit.com/~"))

view.setWindowTitle("Replit Desktop")
view.setWindowIcon(QIcon('logo.png'))
view.showMaximized()

app.exec_()

try:
    RPC.close()
except:
    pass
