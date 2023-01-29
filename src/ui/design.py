# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QTabWidget, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(308, 463)
        MainWindow.setStyleSheet(u"\n"
"QWidget {\n"
"    color: white;\n"
"    background-color: #121212;\n"
"    font-family: Rubik;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QTextEdit, QLineEdit, QComboBox, QPushButton {\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"    selection-background-color: #bbbbbb;\n"
"}\n"
"\n"
"QTabWidget::pane { /* The tab widget frame */\n"
"    border-top: 2px solid #C2C7CB;\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    left: 5px; /* move to the right by 5px */\n"
"}\n"
"\n"
"/* Style the tab using the tab sub-control. Note that\n"
"    it reads QTabBar _not_ QTabWidget */\n"
"QTabBar::tab {\n"
"	color: black;\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3)"
                        ";\n"
"    border: transparent;\n"
"    border-bottom-color: #C2C7CB; /* same as the pane color */\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    min-width: 8ex;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"    background: #888;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    border-color: #888;\n"
"    border-bottom-color: rgb(255, 255, 255); /* same as pane color */\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    margin-top: 2px; /* make non-selected tabs look smaller */\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.tab_1.setStyleSheet(u"")
        self.gridLayout_9 = QGridLayout(self.tab_1)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.verticalSpacer_6 = QSpacerItem(0, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_9.addItem(self.verticalSpacer_6, 8, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lb_nameM = QLabel(self.tab_1)
        self.lb_nameM.setObjectName(u"lb_nameM")

        self.verticalLayout_2.addWidget(self.lb_nameM)

        self.lb_skillsM = QLabel(self.tab_1)
        self.lb_skillsM.setObjectName(u"lb_skillsM")

        self.verticalLayout_2.addWidget(self.lb_skillsM)

        self.lb_skillsWarnM = QLabel(self.tab_1)
        self.lb_skillsWarnM.setObjectName(u"lb_skillsWarnM")

        self.verticalLayout_2.addWidget(self.lb_skillsWarnM)


        self.gridLayout_9.addLayout(self.verticalLayout_2, 0, 0, 1, 2)

        self.verticalSpacer_7 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_9.addItem(self.verticalSpacer_7, 2, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(0, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_9.addItem(self.verticalSpacer_4, 5, 0, 1, 1)

        self.verticalSpacer_15 = QSpacerItem(0, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_15, 10, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_2, 7, 1, 1, 1)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.pb_infoSkills = QPushButton(self.tab_1)
        self.pb_infoSkills.setObjectName(u"pb_infoSkills")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_infoSkills.sizePolicy().hasHeightForWidth())
        self.pb_infoSkills.setSizePolicy(sizePolicy)

        self.gridLayout_6.addWidget(self.pb_infoSkills, 0, 1, 1, 1)

        self.lbl_8 = QLabel(self.tab_1)
        self.lbl_8.setObjectName(u"lbl_8")
        sizePolicy.setHeightForWidth(self.lbl_8.sizePolicy().hasHeightForWidth())
        self.lbl_8.setSizePolicy(sizePolicy)

        self.gridLayout_6.addWidget(self.lbl_8, 0, 0, 1, 1)

        self.pb_recInfo = QPushButton(self.tab_1)
        self.pb_recInfo.setObjectName(u"pb_recInfo")
        sizePolicy.setHeightForWidth(self.pb_recInfo.sizePolicy().hasHeightForWidth())
        self.pb_recInfo.setSizePolicy(sizePolicy)

        self.gridLayout_6.addWidget(self.pb_recInfo, 2, 1, 1, 1)

        self.lbl_0 = QLabel(self.tab_1)
        self.lbl_0.setObjectName(u"lbl_0")
        sizePolicy.setHeightForWidth(self.lbl_0.sizePolicy().hasHeightForWidth())
        self.lbl_0.setSizePolicy(sizePolicy)

        self.gridLayout_6.addWidget(self.lbl_0, 2, 0, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_7, 2, 2, 1, 1)


        self.gridLayout_9.addLayout(self.gridLayout_6, 9, 0, 1, 1)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.pb_try = QPushButton(self.tab_1)
        self.pb_try.setObjectName(u"pb_try")
        sizePolicy.setHeightForWidth(self.pb_try.sizePolicy().hasHeightForWidth())
        self.pb_try.setSizePolicy(sizePolicy)

        self.gridLayout_7.addWidget(self.pb_try, 1, 1, 1, 1)

        self.pb_ll = QPushButton(self.tab_1)
        self.pb_ll.setObjectName(u"pb_ll")
        sizePolicy.setHeightForWidth(self.pb_ll.sizePolicy().hasHeightForWidth())
        self.pb_ll.setSizePolicy(sizePolicy)

        self.gridLayout_7.addWidget(self.pb_ll, 0, 1, 1, 1)

        self.lbl_shift = QLabel(self.tab_1)
        self.lbl_shift.setObjectName(u"lbl_shift")
        sizePolicy.setHeightForWidth(self.lbl_shift.sizePolicy().hasHeightForWidth())
        self.lbl_shift.setSizePolicy(sizePolicy)

        self.gridLayout_7.addWidget(self.lbl_shift, 1, 0, 1, 1)

        self.lbl_tab = QLabel(self.tab_1)
        self.lbl_tab.setObjectName(u"lbl_tab")
        sizePolicy.setHeightForWidth(self.lbl_tab.sizePolicy().hasHeightForWidth())
        self.lbl_tab.setSizePolicy(sizePolicy)

        self.gridLayout_7.addWidget(self.lbl_tab, 0, 0, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_6, 1, 2, 1, 1)


        self.gridLayout_9.addLayout(self.gridLayout_7, 7, 0, 1, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.lbl_2 = QLabel(self.tab_1)
        self.lbl_2.setObjectName(u"lbl_2")
        sizePolicy.setHeightForWidth(self.lbl_2.sizePolicy().hasHeightForWidth())
        self.lbl_2.setSizePolicy(sizePolicy)

        self.gridLayout_4.addWidget(self.lbl_2, 1, 0, 1, 1)

        self.lbl_4 = QLabel(self.tab_1)
        self.lbl_4.setObjectName(u"lbl_4")
        sizePolicy.setHeightForWidth(self.lbl_4.sizePolicy().hasHeightForWidth())
        self.lbl_4.setSizePolicy(sizePolicy)

        self.gridLayout_4.addWidget(self.lbl_4, 3, 0, 1, 1)

        self.pb_intellegence = QPushButton(self.tab_1)
        self.pb_intellegence.setObjectName(u"pb_intellegence")
        sizePolicy.setHeightForWidth(self.pb_intellegence.sizePolicy().hasHeightForWidth())
        self.pb_intellegence.setSizePolicy(sizePolicy)

        self.gridLayout_4.addWidget(self.pb_intellegence, 2, 1, 1, 1)

        self.lbl_5 = QLabel(self.tab_1)
        self.lbl_5.setObjectName(u"lbl_5")
        sizePolicy.setHeightForWidth(self.lbl_5.sizePolicy().hasHeightForWidth())
        self.lbl_5.setSizePolicy(sizePolicy)

        self.gridLayout_4.addWidget(self.lbl_5, 4, 0, 1, 1)

        self.pb_luck = QPushButton(self.tab_1)
        self.pb_luck.setObjectName(u"pb_luck")
        sizePolicy.setHeightForWidth(self.pb_luck.sizePolicy().hasHeightForWidth())
        self.pb_luck.setSizePolicy(sizePolicy)

        self.gridLayout_4.addWidget(self.pb_luck, 4, 1, 1, 1)

        self.pb_agility = QPushButton(self.tab_1)
        self.pb_agility.setObjectName(u"pb_agility")
        sizePolicy.setHeightForWidth(self.pb_agility.sizePolicy().hasHeightForWidth())
        self.pb_agility.setSizePolicy(sizePolicy)

        self.gridLayout_4.addWidget(self.pb_agility, 1, 1, 1, 1)

        self.pb_charisma = QPushButton(self.tab_1)
        self.pb_charisma.setObjectName(u"pb_charisma")
        sizePolicy.setHeightForWidth(self.pb_charisma.sizePolicy().hasHeightForWidth())
        self.pb_charisma.setSizePolicy(sizePolicy)

        self.gridLayout_4.addWidget(self.pb_charisma, 3, 1, 1, 1)

        self.pb_strength = QPushButton(self.tab_1)
        self.pb_strength.setObjectName(u"pb_strength")
        self.pb_strength.setEnabled(True)
        sizePolicy.setHeightForWidth(self.pb_strength.sizePolicy().hasHeightForWidth())
        self.pb_strength.setSizePolicy(sizePolicy)

        self.gridLayout_4.addWidget(self.pb_strength, 0, 1, 1, 1)

        self.lbl_3 = QLabel(self.tab_1)
        self.lbl_3.setObjectName(u"lbl_3")
        sizePolicy.setHeightForWidth(self.lbl_3.sizePolicy().hasHeightForWidth())
        self.lbl_3.setSizePolicy(sizePolicy)

        self.gridLayout_4.addWidget(self.lbl_3, 2, 0, 1, 1)

        self.lbl_1 = QLabel(self.tab_1)
        self.lbl_1.setObjectName(u"lbl_1")
        sizePolicy.setHeightForWidth(self.lbl_1.sizePolicy().hasHeightForWidth())
        self.lbl_1.setSizePolicy(sizePolicy)

        self.gridLayout_4.addWidget(self.lbl_1, 0, 0, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_5, 2, 2, 1, 1)


        self.gridLayout_9.addLayout(self.gridLayout_4, 4, 0, 1, 1)

        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_2 = QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.le_name = QLineEdit(self.tab_2)
        self.le_name.setObjectName(u"le_name")

        self.gridLayout_3.addWidget(self.le_name, 0, 1, 1, 1)

        self.lbl_info = QLabel(self.tab_2)
        self.lbl_info.setObjectName(u"lbl_info")

        self.gridLayout_3.addWidget(self.lbl_info, 2, 0, 1, 1, Qt.AlignHCenter)

        self.lbl_name = QLabel(self.tab_2)
        self.lbl_name.setObjectName(u"lbl_name")

        self.gridLayout_3.addWidget(self.lbl_name, 0, 0, 1, 1, Qt.AlignHCenter)

        self.verticalSpacer = QSpacerItem(10, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.te_info = QTextEdit(self.tab_2)
        self.te_info.setObjectName(u"te_info")

        self.gridLayout_3.addWidget(self.te_info, 3, 0, 1, 2)


        self.gridLayout_2.addLayout(self.gridLayout_3, 0, 0, 1, 4)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.cb_character = QComboBox(self.tab_2)
        self.cb_character.addItem("")
        self.cb_character.addItem("")
        self.cb_character.setObjectName(u"cb_character")

        self.verticalLayout_3.addWidget(self.cb_character)

        self.pb_select = QPushButton(self.tab_2)
        self.pb_select.setObjectName(u"pb_select")

        self.verticalLayout_3.addWidget(self.pb_select)

        self.le_newCh = QLineEdit(self.tab_2)
        self.le_newCh.setObjectName(u"le_newCh")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.le_newCh.sizePolicy().hasHeightForWidth())
        self.le_newCh.setSizePolicy(sizePolicy1)
        self.le_newCh.setSizeIncrement(QSize(0, 2))

        self.verticalLayout_3.addWidget(self.le_newCh)

        self.pb_create = QPushButton(self.tab_2)
        self.pb_create.setObjectName(u"pb_create")

        self.verticalLayout_3.addWidget(self.pb_create)

        self.pb_delete = QPushButton(self.tab_2)
        self.pb_delete.setObjectName(u"pb_delete")

        self.verticalLayout_3.addWidget(self.pb_delete)

        self.pb_save = QPushButton(self.tab_2)
        self.pb_save.setObjectName(u"pb_save")

        self.verticalLayout_3.addWidget(self.pb_save)


        self.gridLayout_2.addLayout(self.verticalLayout_3, 2, 3, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 1, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.lbl_intellegence = QLabel(self.tab_2)
        self.lbl_intellegence.setObjectName(u"lbl_intellegence")

        self.gridLayout.addWidget(self.lbl_intellegence, 3, 0, 1, 1, Qt.AlignHCenter)

        self.lbl_agility = QLabel(self.tab_2)
        self.lbl_agility.setObjectName(u"lbl_agility")

        self.gridLayout.addWidget(self.lbl_agility, 2, 0, 1, 1, Qt.AlignHCenter)

        self.lbl_strength = QLabel(self.tab_2)
        self.lbl_strength.setObjectName(u"lbl_strength")

        self.gridLayout.addWidget(self.lbl_strength, 1, 0, 1, 1, Qt.AlignHCenter)

        self.lbl_charisma = QLabel(self.tab_2)
        self.lbl_charisma.setObjectName(u"lbl_charisma")

        self.gridLayout.addWidget(self.lbl_charisma, 4, 0, 1, 1, Qt.AlignHCenter)

        self.lbl_luck = QLabel(self.tab_2)
        self.lbl_luck.setObjectName(u"lbl_luck")

        self.gridLayout.addWidget(self.lbl_luck, 5, 0, 1, 1, Qt.AlignHCenter)

        self.le_strength = QLineEdit(self.tab_2)
        self.le_strength.setObjectName(u"le_strength")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.le_strength.sizePolicy().hasHeightForWidth())
        self.le_strength.setSizePolicy(sizePolicy2)
        self.le_strength.setMaximumSize(QSize(20, 100))

        self.gridLayout.addWidget(self.le_strength, 1, 1, 1, 1)

        self.lbl_skills = QLabel(self.tab_2)
        self.lbl_skills.setObjectName(u"lbl_skills")

        self.gridLayout.addWidget(self.lbl_skills, 0, 0, 1, 1, Qt.AlignHCenter)

        self.le_agility = QLineEdit(self.tab_2)
        self.le_agility.setObjectName(u"le_agility")
        sizePolicy2.setHeightForWidth(self.le_agility.sizePolicy().hasHeightForWidth())
        self.le_agility.setSizePolicy(sizePolicy2)
        self.le_agility.setMaximumSize(QSize(20, 100))

        self.gridLayout.addWidget(self.le_agility, 2, 1, 1, 1)

        self.le_intellegence = QLineEdit(self.tab_2)
        self.le_intellegence.setObjectName(u"le_intellegence")
        sizePolicy2.setHeightForWidth(self.le_intellegence.sizePolicy().hasHeightForWidth())
        self.le_intellegence.setSizePolicy(sizePolicy2)
        self.le_intellegence.setMaximumSize(QSize(20, 100))

        self.gridLayout.addWidget(self.le_intellegence, 3, 1, 1, 1)

        self.le_charisma = QLineEdit(self.tab_2)
        self.le_charisma.setObjectName(u"le_charisma")
        sizePolicy2.setHeightForWidth(self.le_charisma.sizePolicy().hasHeightForWidth())
        self.le_charisma.setSizePolicy(sizePolicy2)
        self.le_charisma.setMaximumSize(QSize(20, 100))

        self.gridLayout.addWidget(self.le_charisma, 4, 1, 1, 1)

        self.le_luck = QLineEdit(self.tab_2)
        self.le_luck.setObjectName(u"le_luck")
        sizePolicy2.setHeightForWidth(self.le_luck.sizePolicy().hasHeightForWidth())
        self.le_luck.setSizePolicy(sizePolicy2)
        self.le_luck.setMaximumSize(QSize(20, 100))

        self.gridLayout.addWidget(self.le_luck, 5, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 2, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 2, 2, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_8 = QGridLayout(self.tab_3)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_8.addItem(self.verticalSpacer_3, 1, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lb_logo = QLabel(self.tab_3)
        self.lb_logo.setObjectName(u"lb_logo")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lb_logo.sizePolicy().hasHeightForWidth())
        self.lb_logo.setSizePolicy(sizePolicy3)
        self.lb_logo.setMinimumSize(QSize(100, 100))
        self.lb_logo.setMaximumSize(QSize(100, 100))
        self.lb_logo.setScaledContents(True)

        self.horizontalLayout.addWidget(self.lb_logo)

        self.lb_about = QLabel(self.tab_3)
        self.lb_about.setObjectName(u"lb_about")

        self.horizontalLayout.addWidget(self.lb_about, 0, Qt.AlignLeft|Qt.AlignBottom)


        self.gridLayout_8.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.te_about = QTextEdit(self.tab_3)
        self.te_about.setObjectName(u"te_about")

        self.gridLayout_8.addWidget(self.te_about, 2, 0, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lb_nameM.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.lb_skillsM.setText(QCoreApplication.translate("MainWindow", u"Skills:", None))
        self.lb_skillsWarnM.setText(QCoreApplication.translate("MainWindow", u"SkillsWarn", None))
        self.pb_infoSkills.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u044a\u044f\u0432\u0438\u0442\u044c \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044e \u043e \u0441\u043a\u0438\u043b\u043b\u0430\u0445 \u0432 \u0447\u0430\u0442", None))
#if QT_CONFIG(shortcut)
        self.pb_infoSkills.setShortcut(QCoreApplication.translate("MainWindow", u"9", None))
#endif // QT_CONFIG(shortcut)
        self.lbl_8.setText(QCoreApplication.translate("MainWindow", u"9)", None))
        self.pb_recInfo.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u0441\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044e \u043e \u043f\u0435\u0440\u0441\u043e\u043d\u0430\u0436\u0435", None))
#if QT_CONFIG(shortcut)
        self.pb_recInfo.setShortcut(QCoreApplication.translate("MainWindow", u"0", None))
#endif // QT_CONFIG(shortcut)
        self.lbl_0.setText(QCoreApplication.translate("MainWindow", u"0)", None))
        self.pb_try.setText(QCoreApplication.translate("MainWindow", u"/try", None))
#if QT_CONFIG(shortcut)
        self.pb_try.setShortcut(QCoreApplication.translate("MainWindow", u"Shift+T", None))
#endif // QT_CONFIG(shortcut)
        self.pb_ll.setText(QCoreApplication.translate("MainWindow", u"/ll", None))
#if QT_CONFIG(shortcut)
        self.pb_ll.setShortcut(QCoreApplication.translate("MainWindow", u"Tab", None))
#endif // QT_CONFIG(shortcut)
        self.lbl_shift.setText(QCoreApplication.translate("MainWindow", u"Shift+T)", None))
        self.lbl_tab.setText(QCoreApplication.translate("MainWindow", u"Tab)", None))
        self.lbl_2.setText(QCoreApplication.translate("MainWindow", u"2)", None))
        self.lbl_4.setText(QCoreApplication.translate("MainWindow", u"4)", None))
        self.pb_intellegence.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c \u0418\u043d\u0442\u0435\u043b\u043b\u0435\u043a\u0442", None))
#if QT_CONFIG(shortcut)
        self.pb_intellegence.setShortcut(QCoreApplication.translate("MainWindow", u"3", None))
#endif // QT_CONFIG(shortcut)
        self.lbl_5.setText(QCoreApplication.translate("MainWindow", u"5)", None))
        self.pb_luck.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0441\u043f\u044b\u0442\u0430\u0442\u044c \u0423\u0434\u0430\u0447\u0443", None))
#if QT_CONFIG(shortcut)
        self.pb_luck.setShortcut(QCoreApplication.translate("MainWindow", u"5", None))
#endif // QT_CONFIG(shortcut)
        self.pb_agility.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0435\u043c\u0435\u043d\u0438\u0442\u044c \u041b\u043e\u0432\u043a\u043e\u0441\u0442\u044c", None))
#if QT_CONFIG(shortcut)
        self.pb_agility.setShortcut(QCoreApplication.translate("MainWindow", u"2", None))
#endif // QT_CONFIG(shortcut)
        self.pb_charisma.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c \u0425\u0430\u0440\u0438\u0437\u043c\u0443", None))
#if QT_CONFIG(shortcut)
        self.pb_charisma.setShortcut(QCoreApplication.translate("MainWindow", u"4", None))
#endif // QT_CONFIG(shortcut)
        self.pb_strength.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u043c\u0435\u043d\u0438\u0442\u044c \u0421\u0438\u043b\u0443", None))
#if QT_CONFIG(shortcut)
        self.pb_strength.setShortcut(QCoreApplication.translate("MainWindow", u"1", None))
#endif // QT_CONFIG(shortcut)
        self.lbl_3.setText(QCoreApplication.translate("MainWindow", u"3)", None))
        self.lbl_1.setText(QCoreApplication.translate("MainWindow", u"1)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("MainWindow", u"Main", None))
        self.le_name.setText("")
        self.lbl_info.setText(QCoreApplication.translate("MainWindow", u"Info", None))
        self.lbl_name.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.cb_character.setItemText(0, QCoreApplication.translate("MainWindow", u"New Item2", None))
        self.cb_character.setItemText(1, QCoreApplication.translate("MainWindow", u"New Item", None))

        self.cb_character.setCurrentText(QCoreApplication.translate("MainWindow", u"New Item2", None))
        self.pb_select.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.pb_create.setText(QCoreApplication.translate("MainWindow", u"Create", None))
        self.pb_delete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.pb_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.lbl_intellegence.setText(QCoreApplication.translate("MainWindow", u"Intellegence", None))
        self.lbl_agility.setText(QCoreApplication.translate("MainWindow", u"Agility", None))
        self.lbl_strength.setText(QCoreApplication.translate("MainWindow", u"Strength", None))
        self.lbl_charisma.setText(QCoreApplication.translate("MainWindow", u"Charisma", None))
        self.lbl_luck.setText(QCoreApplication.translate("MainWindow", u"Luck", None))
        self.lbl_skills.setText(QCoreApplication.translate("MainWindow", u"Skills", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Config", None))
        self.lb_logo.setText("")
        self.lb_about.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e\u0440 \u0441\u043a\u0440\u0438\u043f\u0442\u0430 @LolerFox\n"
"(aka. [\u0422\u0443\u043b\u044c\u043f\u0430]\u0428\u0442\u0438\u0440\u043b\u0438\u0446)\n"
"\u00a9SRP ESO v2.0\n"
"\u0421\u043a\u0440\u0438\u043f\u0442 \u0440\u0430\u0441\u043f\u0440\u043e\u0441\u0442\u0440\u0430\u043d\u044f\u0435\u0442\u0441\u044f\n"
"\u043f\u043e \u043b\u0438\u0446\u0435\u043d\u0437\u0438\u0438 \u043e\u0442\u043a\u0440\u044b\u0442\u043e\u0433\u043e \u041f\u041e\n"
"GNU General Public License", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"About", None))
    # retranslateUi
