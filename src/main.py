import json
import sys

from PyQt5.QtCore import QLocale, Qt, QCoreApplication
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QComboBox, QVBoxLayout, QFormLayout, QWidget

QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
QCoreApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)  # HighDPI support

QApplication.setFont(QFont('Arial', 12))


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__initVal()
        self.__initUi()

    def __initVal(self):
        self.__language_dict = {
            "en_US": "English",
            "es_ES": "Spanish",
            "zh_CN": "Chinese",
            "ru_RU": "Russian",
            "ko_KR": "Korean",
            "fr_FR": "French",
            "de_DE": "German",
            "it_IT": "Italian",
            "hi_IN": "Hindi",
            "ar_AE": "Arabic"
        }

    def __initUi(self):
        self.setWindowTitle('Translation Example')
        self.__langLbl = QLabel('Language')
        self.__langCmbBox = QComboBox()
        self.__langCmbBox.addItems(self.__language_dict.keys())

        lay = QFormLayout()
        lay.addRow(self.__langLbl, self.__langCmbBox)
        lay.setContentsMargins(0, 0, 0, 0)

        langWidget = QWidget()
        langWidget.setLayout(lay)

        self.__sampleLbl = QLabel('Hello World!')
        self.__sampleLbl.setFont(QFont('Arial', 24))

        lay = QVBoxLayout()
        lay.addWidget(langWidget)
        lay.addWidget(self.__sampleLbl)
        lay.setAlignment(Qt.AlignTop)

        mainWidget = QWidget()
        mainWidget.setLayout(lay)

        self.setCentralWidget(mainWidget)

        self.__langCmbBox.currentTextChanged.connect(self.__langChanged)

    def __langChanged(self, lang=None):
        translations = {}
        with open('translations.json', 'r', encoding='utf-8') as file:
            translations = json.load(file)

        language = lang
        if not lang:
            language = QLocale.system().name()
            if language not in translations:
                language = 'en_US'  # Default language


        translation = translations[language]
        print(translation)
        self.__sampleLbl.setText(translation['Hello World!'])
        self.setWindowTitle(translation['Translation Example'])
        self.__langLbl.setText(translation['Language'])


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
