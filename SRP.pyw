import sys
import subprocess as sp

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QFontDatabase, QIcon, QPixmap
from PySide6.QtCore import Qt

from src.ui.design import Ui_MainWindow
from src.modules.file_descriptor import file_descriptor
from src.modules.sendMessage import sendMessage

cfg = file_descriptor("src/config/config.json", 'json', 'r')


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.setWindowFlag(Qt.WindowStaysOnTopHint, True)

        QFontDatabase.addApplicationFont('Fonts/Rubik-Regular.ttf')
        self.setWindowTitle('SRP ESO')
        self.setWindowIcon(QIcon('src/ui/img/SRP ESO.ico'))

        self.aotrun = False

        self.refresh()
        self.Focus()
        self.AOTrun()

        # Main tab
        self.ui.pb_strength.clicked.connect(lambda: sendMessage('dice', '\\\Cила:', f'/dice {self.ui.le_strength.text()}d6', self.skillcount, self.skillsLine))
        self.ui.pb_agility.clicked.connect(lambda: sendMessage('dice', '\\\Ловкость:', f'/dice {self.ui.le_agility.text()}d6', self.skillcount, self.skillsLine))
        self.ui.pb_intellegence.clicked.connect(lambda: sendMessage('dice', '\\\Интеллект:', f'/dice {self.ui.le_intellegence.text()}d6', self.skillcount, self.skillsLine))
        self.ui.pb_charisma.clicked.connect(lambda: sendMessage('dice', '\\\Харизма:', f'/dice {self.ui.le_charisma.text()}d6', self.skillcount, self.skillsLine))
        self.ui.pb_luck.clicked.connect(lambda: sendMessage('dice', '\\\Удача:', f'/dice {self.ui.le_luck.text()}d6', self.skillcount, self.skillsLine))

        self.ui.pb_ll.clicked.connect(lambda: sendMessage('sendMessage', '/ll'))
        self.ui.pb_try.clicked.connect(lambda: sendMessage('sendMessage', '/try  '))

        self.ui.pb_infoSkills.clicked.connect(lambda: sendMessage('sendMessage', f'\\\{self.skillsLine}'))
        self.ui.pb_recInfo.clicked.connect(lambda: sendMessage('sendMessage', f'/iam {self.skillsLine} {self.ui.te_info.toPlainText()}'))

        self.ui.pb_AOTon.clicked.connect(lambda: self.Focus())
        self.ui.pb_AOTauto.clicked.connect(lambda: self.AOTswitch())

        # Config tab
        self.ui.pb_select.clicked.connect(lambda: self.actions('select'))
        self.ui.pb_create.clicked.connect(lambda: self.actions('create'))
        self.ui.pb_delete.clicked.connect(lambda: self.actions('del'))
        self.ui.pb_save.clicked.connect(lambda: self.save())

        # About tab
        self.ui.lb_logo.setPixmap(QPixmap('src/ui/img/SRP ESO.ico'))
        self.ui.lb_logo.setScaledContents(True)

        about = file_descriptor('README.txt', 'txt', 'r')
        self.ui.te_about.setText(about)

    def AOTrun(self):
        if cfg['settings']['aotautorun']:
            self.setWindowFlag(Qt.WindowStaysOnTopHint, True)
            self.ui.pb_AOTauto.setText('Always On Top: True')
            self.show()

    def AOTswitch(self):
        if cfg['settings']['aotautorun']:
            self.setWindowFlag(Qt.WindowStaysOnTopHint, False)
            self.ui.pb_AOTauto.setText('Always On Top: False')
            cfg['settings']['aotautorun'] = False
        else:
            self.setWindowFlag(Qt.WindowStaysOnTopHint, True)
            self.ui.pb_AOTauto.setText('Always On Top: True')
            cfg['settings']['aotautorun'] = True
        self.show()
        file_descriptor("src/config/config.json", 'json', 'w', cfg)

    def Focus(self):
            self.aot = sp.Popen('src/ui/Focus/Focus.exe', shell=False)

    def actions(self, type):
        ch_cfg = file_descriptor("src/config/characters_config.json", 'json', 'r')

        if type == 'select':
            print(self.ui.cb_character.currentText())
            ch_cfg['characterlast'] = self.ui.cb_character.currentText()

        if type == 'create':
            if self.ui.le_newCh.text() != "":
                ch_cfg['characterslist'].append(self.ui.le_newCh.text())
                ch_cfg['characterlast'] = self.ui.le_newCh.text()
                ch_cfg['characters'][self.ui.le_newCh.text()] = {"name": "SampleName", "info": "SampleInfo", "skills": {"strength": "0", "agility": "0", "intellegence": "0", "charisma": "0", "luck": "0"}}
                self.ui.le_newCh.setText('')

        elif type == 'del':
            ch_cfg['characters'].pop(self.ui.cb_character.currentText())
            ch_cfg['characterslist'].remove(self.ui.cb_character.currentText())
            ch_cfg['characterlast'] = ch_cfg['characterslist'][-1]

        file_descriptor("src/config/characters_config.json", 'json', 'w', ch_cfg)
        self.refresh()

    def save(self) -> None:
        ch_cfg = file_descriptor("src/config/characters_config.json", 'json', 'r')

        ch_cfg['characters'][ch_cfg['characterlast']]['name'] = self.ui.le_name.text()
        ch_cfg['characters'][ch_cfg['characterlast']]['info'] = self.ui.te_info.toPlainText()

        ch_cfg['characters'][ch_cfg['characterlast']]['skills']['strength'] = self.ui.le_strength.text()
        ch_cfg['characters'][ch_cfg['characterlast']]['skills']['agility'] = self.ui.le_agility.text()
        ch_cfg['characters'][ch_cfg['characterlast']]['skills']['intellegence'] = self.ui.le_intellegence.text()
        ch_cfg['characters'][ch_cfg['characterlast']]['skills']['charisma'] = self.ui.le_charisma.text()
        ch_cfg['characters'][ch_cfg['characterlast']]['skills']['luck'] = self.ui.le_luck.text()

        file_descriptor("src/config/characters_config.json", 'json', 'w', ch_cfg)
        self.refresh()

    def refresh(self) -> None:
        ch_cfg = file_descriptor("src/config/characters_config.json", 'json', 'r')

        self.aotautorun = cfg['settings']['aotautorun']

        self.ui.cb_character.clear()
        self.ui.cb_character.addItems(ch_cfg['characterslist'])
        self.ui.cb_character.setCurrentText(ch_cfg['characterlast'])

        self.ui.le_name.setText(ch_cfg['characters'][ch_cfg['characterlast']]['name'])
        self.ui.te_info.setText(ch_cfg['characters'][ch_cfg['characterlast']]['info'])

        self.ui.le_strength.setText(ch_cfg['characters'][ch_cfg['characterlast']]['skills']['strength'])
        self.ui.le_agility.setText(ch_cfg['characters'][ch_cfg['characterlast']]['skills']['agility'])
        self.ui.le_intellegence.setText(ch_cfg['characters'][ch_cfg['characterlast']]['skills']['intellegence'])
        self.ui.le_charisma.setText(ch_cfg['characters'][ch_cfg['characterlast']]['skills']['charisma'])
        self.ui.le_luck.setText(ch_cfg['characters'][ch_cfg['characterlast']]['skills']['luck'])

        self.ui.lb_nameM.setText('Name: ' + self.ui.le_name.text())
        self.skillsLine = '|Сил ' + self.ui.le_strength.text() + ' Лов '+ self.ui.le_agility.text() + ' Инт ' + self.ui.le_intellegence.text() + ' Хар ' +self.ui.le_charisma.text() + ' Удч ' + self.ui.le_luck.text()+'|'
        self.ui.lb_skillsM.setText('Skills: ' + self.skillsLine)

        self.skillcount = int(self.ui.le_strength.text()) + int(self.ui.le_agility.text()) + int(self.ui.le_intellegence.text()) + int(self.ui.le_charisma.text()) + int(self.ui.le_luck.text())
        if self.skillcount > 25:
            self.ui.lb_skillsWarnM.setText(f'Ваши показатели слишком высоки!\n(сумма скилов больше 25 на {self.skillcount-25}!!!)')
            self.ui.lb_skillsWarnM.setStyleSheet("QLabel { color: rgb(255, 0, 0); }")
        elif self.skillcount < 25:
            self.ui.lb_skillsWarnM.setText(f'Вы использовали не все очки навыков!\n(Осталось {25-self.skillcount})')
            self.ui.lb_skillsWarnM.setStyleSheet("QLabel { color: rgb(0, 255, 0); }")
        else:
            self.ui.lb_skillsWarnM.setText('')


if __name__ == "__main__":
        app = QApplication(sys.argv)

        window = MainWindow()
        window.show()

        sys.exit(app.exec())
