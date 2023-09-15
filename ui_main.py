# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainTVIQNB.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import images_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1124, 690)
        MainWindow.setMinimumSize(QSize(1100, 690))
        MainWindow.setMaximumSize(QSize(1124, 694))
        MainWindow.setStyleSheet(u"QLabel{\n"
"background-color: rgb(255,255,255);\n"
"font-family: \"Calibri\";\n"
"font-weight:bold;\n"
"font-size:23px;\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton{\n"
"color: rgb(0,,0,0);\n"
"background-color: rgb(255,255,255);\n"
"font-family: \"Calibri\";\n"
"font-weight:bold;\n"
"font-size:23px;\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"QLineEdit{\n"
"color: rgb(0,,0,0);\n"
"background-color: rgb(255,255,255);\n"
"font-family: \"Calibri\";\n"
"font-weight:bold;\n"
"font-size:23px;\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"QComboBox{\n"
"color: rgb(0,,0,0);\n"
"background-color: rgb(255,255,255);\n"
"font-family: \"Calibri\";\n"
"font-weight:bold;\n"
"font-size:23px;\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"QTableView{\n"
"background-image: url(:/images/Images/table_background.png);\n"
"color: rgb(0,,0,0);\n"
"background-color: rgb(255,255,255);\n"
"font-family: \"Calibri\";\n"
"font-weight:bold;\n"
"font-size:23px;\n"
"border-radius: 12px;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.formLayout = QFormLayout(self.centralwidget)
        self.formLayout.setObjectName(u"formLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(1100, 635))
        self.frame.setStyleSheet(u"QFrame{\n"
"	background-image: url(:/images/Images/page_background.jpeg);\n"
"}")
        self.frame.setFrameShape(QFrame.Panel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.stackedWidget_1 = QStackedWidget(self.frame)
        self.stackedWidget_1.setObjectName(u"stackedWidget_1")
        self.stackedWidget_1.setMaximumSize(QSize(1076, 611))
        self.stackedWidget_1.setLayoutDirection(Qt.LeftToRight)
        self.stackedWidget_1.setAutoFillBackground(False)
        self.stackedWidget_1.setStyleSheet(u"")
        self.login_page = QWidget()
        self.login_page.setObjectName(u"login_page")
        self.login_page.setStyleSheet(u"")
        self.register_button = QPushButton(self.login_page)
        self.register_button.setObjectName(u"register_button")
        self.register_button.setGeometry(QRect(560, 370, 291, 31))
        self.register_button.setStyleSheet(u"color: rgb(0,,0,0);\n"
"background-color: rgb(255,255,255);\n"
"font-size:20px;\n"
"font-weight:bold;\n"
"border-radius: 12px;\n"
"font-family: \"Calibri\";\n"
"font-weight:bold;\n"
"font-size:23px;")
        self.password_forgetten_button = QPushButton(self.login_page)
        self.password_forgetten_button.setObjectName(u"password_forgetten_button")
        self.password_forgetten_button.setGeometry(QRect(300, 410, 521, 31))
        self.password_forgetten_button.setStyleSheet(u"color: rgb(0,,0,0);\n"
"background-color: rgb(255,255,255);\n"
"font-size:20px;\n"
"font-weight:bold;\n"
"border-radius: 12px;\n"
"font-family: \"Calibri\";\n"
"font-weight:bold;\n"
"font-size:23px;")
        self.login_button = QPushButton(self.login_page)
        self.login_button.setObjectName(u"login_button")
        self.login_button.setGeometry(QRect(260, 370, 281, 31))
        self.login_button.setStyleSheet(u"color: rgb(0,,0,0);\n"
"background-color: rgb(255,255,255);\n"
"font-size:20px;\n"
"font-weight:bold;\n"
"border-radius: 12px;\n"
"font-family: \"Calibri\";\n"
"font-weight:bold;\n"
"font-size:23px;")
        self.label_10 = QLabel(self.login_page)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(490, 110, 141, 141))
        self.label_10.setStyleSheet(u"background-image: url(:/images/Images/bms_145x145.jpg);\n"
"\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 70px;")
        self.username_lineEdit = QLineEdit(self.login_page)
        self.username_lineEdit.setObjectName(u"username_lineEdit")
        self.username_lineEdit.setGeometry(QRect(200, 280, 711, 31))
        self.username_lineEdit.setStyleSheet(u"color: rgb(0,,0,0);\n"
"background-color: rgb(255,255,255);\n"
"font-family: \"Calibri\";\n"
"font-weight:bold;\n"
"font-size:23px;\n"
"border-radius: 12px;\n"
"")
        self.password_lineEdit = QLineEdit(self.login_page)
        self.password_lineEdit.setObjectName(u"password_lineEdit")
        self.password_lineEdit.setGeometry(QRect(240, 329, 631, 31))
        self.password_lineEdit.setStyleSheet(u"color: rgb(0,,0,0);\n"
"background-color: rgb(255,255,255);\n"
"font-family: \"Calibri\";\n"
"font-weight:bold;\n"
"font-size:23px;\n"
"border-radius: 12px;")
        self.password_lineEdit.setEchoMode(QLineEdit.Password)
        self.frame_2 = QFrame(self.login_page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, -10, 1101, 621))
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"")
        self.label_4.setPixmap(QPixmap(u"Images/icon-removebg-preview.png"))
        self.label_4.setScaledContents(True)

        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)

        self.stackedWidget_1.addWidget(self.login_page)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.register_about_comboBox = QComboBox(self.page)
        self.register_about_comboBox.addItem("")
        self.register_about_comboBox.addItem("")
        self.register_about_comboBox.addItem("")
        self.register_about_comboBox.addItem("")
        self.register_about_comboBox.setObjectName(u"register_about_comboBox")
        self.register_about_comboBox.setGeometry(QRect(180, 250, 711, 31))
        font = QFont()
        font.setFamily(u"Calibri")
        font.setBold(True)
        font.setWeight(75)
        self.register_about_comboBox.setFont(font)
        self.register_about_comboBox.setStyleSheet(u"")
        self.register_user_buton = QPushButton(self.page)
        self.register_user_buton.setObjectName(u"register_user_buton")
        self.register_user_buton.setGeometry(QRect(400, 410, 281, 31))
        self.register_user_buton.setStyleSheet(u"")
        self.register_username_lineEdit = QLineEdit(self.page)
        self.register_username_lineEdit.setObjectName(u"register_username_lineEdit")
        self.register_username_lineEdit.setGeometry(QRect(220, 289, 631, 31))
        self.register_username_lineEdit.setFont(font)
        self.register_username_lineEdit.setStyleSheet(u"")
        self.register_username_lineEdit.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.register_username_lineEdit.setClearButtonEnabled(True)
        self.security_key_lineEdit = QLineEdit(self.page)
        self.security_key_lineEdit.setObjectName(u"security_key_lineEdit")
        self.security_key_lineEdit.setGeometry(QRect(340, 370, 391, 31))
        self.security_key_lineEdit.setFont(font)
        self.security_key_lineEdit.setStyleSheet(u"")
        self.security_key_lineEdit.setClearButtonEnabled(True)
        self.register_password_lineEdit = QLineEdit(self.page)
        self.register_password_lineEdit.setObjectName(u"register_password_lineEdit")
        self.register_password_lineEdit.setGeometry(QRect(280, 330, 521, 31))
        self.register_password_lineEdit.setFont(font)
        self.register_password_lineEdit.setStyleSheet(u"")
        self.register_password_lineEdit.setClearButtonEnabled(True)
        self.label_12 = QLabel(self.page)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(470, 50, 141, 141))
        self.label_12.setStyleSheet(u"background-image: url(:/images/Images/bms_145x145.jpg);\n"
"\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 70px;")
        self.back_main_menu_button = QPushButton(self.page)
        self.back_main_menu_button.setObjectName(u"back_main_menu_button")
        self.back_main_menu_button.setGeometry(QRect(490, 450, 111, 31))
        self.back_main_menu_button.setStyleSheet(u"")
        self.stackedWidget_1.addWidget(self.page)
        self.main_screen_page = QWidget()
        self.main_screen_page.setObjectName(u"main_screen_page")
        self.main_screen_page.setStyleSheet(u"")
        self.gridLayout_3 = QGridLayout(self.main_screen_page)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tabWidget = QTabWidget(self.main_screen_page)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(1054, 589))
        self.tabWidget.setStyleSheet(u"")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tab.setStyleSheet(u"")
        self.gridLayout_4 = QGridLayout(self.tab)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.stackedWidget_2 = QStackedWidget(self.tab)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setMinimumSize(QSize(1026, 538))
        self.stackedWidget_2.setMaximumSize(QSize(1026, 16777215))
        self.stackedWidget_2.setStyleSheet(u"")
        self.product_info_page = QWidget()
        self.product_info_page.setObjectName(u"product_info_page")
        self.product_info_page.setMinimumSize(QSize(1026, 538))
        self.product_info_page.setStyleSheet(u"")
        self.model_label = QLabel(self.product_info_page)
        self.model_label.setObjectName(u"model_label")
        self.model_label.setGeometry(QRect(720, 10, 281, 31))
        self.model_label.setStyleSheet(u"background-image: url(:/images/Images/table_background.png);")
        self.delete_line_Button = QPushButton(self.product_info_page)
        self.delete_line_Button.setObjectName(u"delete_line_Button")
        self.delete_line_Button.setGeometry(QRect(200, 490, 171, 28))
        self.delete_line_Button.setStyleSheet(u"")
        self.serial_no_label = QLabel(self.product_info_page)
        self.serial_no_label.setObjectName(u"serial_no_label")
        self.serial_no_label.setGeometry(QRect(20, 10, 281, 31))
        self.serial_no_label.setStyleSheet(u"background-image: url(:/images/Images/table_background.png);")
        self.back_button = QPushButton(self.product_info_page)
        self.back_button.setObjectName(u"back_button")
        self.back_button.setGeometry(QRect(650, 490, 171, 28))
        self.back_button.setStyleSheet(u"")
        self.add_line_button = QPushButton(self.product_info_page)
        self.add_line_button.setObjectName(u"add_line_button")
        self.add_line_button.setGeometry(QRect(20, 490, 171, 28))
        self.add_line_button.setStyleSheet(u"")
        self.excel_export_button = QPushButton(self.product_info_page)
        self.excel_export_button.setObjectName(u"excel_export_button")
        self.excel_export_button.setGeometry(QRect(830, 490, 171, 28))
        self.excel_export_button.setStyleSheet(u"")
        self.name_label = QLabel(self.product_info_page)
        self.name_label.setObjectName(u"name_label")
        self.name_label.setGeometry(QRect(380, 10, 281, 31))
        self.name_label.setFont(font)
        self.name_label.setStyleSheet(u"background-image: url(:/images/Images/table_background.png);")
        self.update_product_info_button = QPushButton(self.product_info_page)
        self.update_product_info_button.setObjectName(u"update_product_info_button")
        self.update_product_info_button.setGeometry(QRect(380, 490, 261, 28))
        self.update_product_info_button.setStyleSheet(u"")
        self.product_info_tableView = QTableView(self.product_info_page)
        self.product_info_tableView.setObjectName(u"product_info_tableView")
        self.product_info_tableView.setGeometry(QRect(20, 50, 981, 431))
        self.product_info_tableView.setMaximumSize(QSize(981, 16777215))
        self.product_info_tableView.setStyleSheet(u"color: rgb(0,,0,0);\n"
"background-image: url(:/images/Images/table_background.png);\n"
"background-color: rgb(255,255,255);\n"
"font-family: \"Calibri\";\n"
"font-weight:bold;\n"
"font-size:23px;\n"
"border-radius: 12px;")
        self.product_info_tableView.setEditTriggers(QAbstractItemView.AllEditTriggers)
        self.product_info_tableView.setDragEnabled(False)
        self.stackedWidget_2.addWidget(self.product_info_page)
        self.products_page = QWidget()
        self.products_page.setObjectName(u"products_page")
        self.products_page.setStyleSheet(u"")
        self.products_tableView = QTableView(self.products_page)
        self.products_tableView.setObjectName(u"products_tableView")
        self.products_tableView.setGeometry(QRect(10, 30, 741, 411))
        self.products_tableView.setStyleSheet(u"color: rgb(0,,0,0);\n"
"background-image: url(:/images/Images/table_background.png);\n"
"background-color: rgb(255,255,255);\n"
"font-family: \"Calibri\";\n"
"font-weight:bold;\n"
"font-size:23px;\n"
"border-radius: 12px;")
        self.products_tableView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.products_tableView.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.products_tableView.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.products_tableView.setWordWrap(False)
        self.search_product_name_comboBox = QComboBox(self.products_page)
        self.search_product_name_comboBox.addItem("")
        self.search_product_name_comboBox.addItem("")
        self.search_product_name_comboBox.addItem("")
        self.search_product_name_comboBox.addItem("")
        self.search_product_name_comboBox.setObjectName(u"search_product_name_comboBox")
        self.search_product_name_comboBox.setGeometry(QRect(10, 450, 691, 41))
        self.search_product_name_comboBox.setStyleSheet(u"")
        self.search_by_name_button = QPushButton(self.products_page)
        self.search_by_name_button.setObjectName(u"search_by_name_button")
        self.search_by_name_button.setGeometry(QRect(710, 450, 41, 41))
        self.search_by_name_button.setStyleSheet(u"")
        self.search_serial_number_lineEdit = QLineEdit(self.products_page)
        self.search_serial_number_lineEdit.setObjectName(u"search_serial_number_lineEdit")
        self.search_serial_number_lineEdit.setGeometry(QRect(10, 500, 551, 41))
        self.search_serial_number_lineEdit.setStyleSheet(u"")
        self.search_serial_number_lineEdit.setClearButtonEnabled(True)
        self.search_by_serial_no_button = QPushButton(self.products_page)
        self.search_by_serial_no_button.setObjectName(u"search_by_serial_no_button")
        self.search_by_serial_no_button.setGeometry(QRect(570, 500, 181, 41))
        self.search_by_serial_no_button.setStyleSheet(u"")
        self.new_serial_no_lineEdit = QLineEdit(self.products_page)
        self.new_serial_no_lineEdit.setObjectName(u"new_serial_no_lineEdit")
        self.new_serial_no_lineEdit.setGeometry(QRect(770, 30, 251, 51))
        self.new_serial_no_lineEdit.setStyleSheet(u"")
        self.new_serial_no_lineEdit.setClearButtonEnabled(True)
        self.new_product_model_comboBox = QComboBox(self.products_page)
        self.new_product_model_comboBox.addItem("")
        self.new_product_model_comboBox.addItem("")
        self.new_product_model_comboBox.addItem("")
        self.new_product_model_comboBox.addItem("")
        self.new_product_model_comboBox.setObjectName(u"new_product_model_comboBox")
        self.new_product_model_comboBox.setGeometry(QRect(770, 90, 251, 41))
        self.new_product_model_comboBox.setStyleSheet(u"")
        self.add_new_product_button = QPushButton(self.products_page)
        self.add_new_product_button.setObjectName(u"add_new_product_button")
        self.add_new_product_button.setGeometry(QRect(770, 140, 91, 41))
        self.add_new_product_button.setStyleSheet(u"")
        self.quit_button = QPushButton(self.products_page)
        self.quit_button.setObjectName(u"quit_button")
        self.quit_button.setGeometry(QRect(930, 140, 91, 41))
        self.quit_button.setStyleSheet(u"")
        self.label_14 = QLabel(self.products_page)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(830, 270, 141, 141))
        self.label_14.setStyleSheet(u"background-image: url(:/images/Images/bms_145x145.jpg);\n"
"\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 70px;\n"
"")
        self.stackedWidget_2.addWidget(self.products_page)

        self.gridLayout_4.addWidget(self.stackedWidget_2, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.storage_page = QWidget()
        self.storage_page.setObjectName(u"storage_page")
        self.storage_page.setStyleSheet(u"")
        self.warehouse_add_name_line = QLineEdit(self.storage_page)
        self.warehouse_add_name_line.setObjectName(u"warehouse_add_name_line")
        self.warehouse_add_name_line.setGeometry(QRect(210, 250, 131, 31))
        self.warehouse_add_name_line.setStyleSheet(u"")
        self.warehouse_add_name_line.setClearButtonEnabled(True)
        self.wareouse_amount_line = QLineEdit(self.storage_page)
        self.wareouse_amount_line.setObjectName(u"wareouse_amount_line")
        self.wareouse_amount_line.setGeometry(QRect(350, 250, 111, 31))
        self.wareouse_amount_line.setStyleSheet(u"")
        self.wareouse_amount_line.setClearButtonEnabled(True)
        self.warehouse_add_button = QPushButton(self.storage_page)
        self.warehouse_add_button.setObjectName(u"warehouse_add_button")
        self.warehouse_add_button.setGeometry(QRect(10, 290, 451, 31))
        self.warehouse_add_button.setStyleSheet(u"")
        self.wareouse_update_amount_line = QLineEdit(self.storage_page)
        self.wareouse_update_amount_line.setObjectName(u"wareouse_update_amount_line")
        self.wareouse_update_amount_line.setGeometry(QRect(350, 20, 121, 31))
        self.wareouse_update_amount_line.setStyleSheet(u"")
        self.wareouse_update_amount_line.setClearButtonEnabled(True)
        self.warehouse_update_button = QPushButton(self.storage_page)
        self.warehouse_update_button.setObjectName(u"warehouse_update_button")
        self.warehouse_update_button.setGeometry(QRect(10, 60, 461, 31))
        self.warehouse_update_button.setStyleSheet(u"")
        self.warehouse_update_name_line = QLineEdit(self.storage_page)
        self.warehouse_update_name_line.setObjectName(u"warehouse_update_name_line")
        self.warehouse_update_name_line.setGeometry(QRect(210, 20, 131, 31))
        self.warehouse_update_name_line.setFont(font)
        self.warehouse_update_name_line.setStyleSheet(u"")
        self.warehouse_update_name_line.setClearButtonEnabled(True)
        self.warehouse_tableViw = QTableView(self.storage_page)
        self.warehouse_tableViw.setObjectName(u"warehouse_tableViw")
        self.warehouse_tableViw.setGeometry(QRect(580, 10, 461, 471))
        self.warehouse_tableViw.setStyleSheet(u"background-image: url(:/images/Images/table_background.png);\n"
"color: rgb(0,,0,0);\n"
"background-color: rgb(255,255,255);\n"
"font-family: \"Calibri\";\n"
"font-weight:bold;\n"
"font-size:23px;\n"
"border-radius: 12px;")
        self.search_supplies_by_name_lineEdit = QLineEdit(self.storage_page)
        self.search_supplies_by_name_lineEdit.setObjectName(u"search_supplies_by_name_lineEdit")
        self.search_supplies_by_name_lineEdit.setGeometry(QRect(580, 490, 351, 31))
        self.search_supplies_by_name_lineEdit.setStyleSheet(u"")
        self.search_supplies_by_name_lineEdit.setClearButtonEnabled(True)
        self.search_supplies_by_name_button = QPushButton(self.storage_page)
        self.search_supplies_by_name_button.setObjectName(u"search_supplies_by_name_button")
        self.search_supplies_by_name_button.setGeometry(QRect(940, 490, 111, 31))
        self.search_supplies_by_name_button.setStyleSheet(u"")
        self.warehouse_delete_button = QPushButton(self.storage_page)
        self.warehouse_delete_button.setObjectName(u"warehouse_delete_button")
        self.warehouse_delete_button.setGeometry(QRect(10, 500, 451, 31))
        self.warehouse_delete_button.setStyleSheet(u"")
        self.warehouse_delete_name_line = QLineEdit(self.storage_page)
        self.warehouse_delete_name_line.setObjectName(u"warehouse_delete_name_line")
        self.warehouse_delete_name_line.setGeometry(QRect(240, 460, 221, 31))
        self.warehouse_delete_name_line.setStyleSheet(u"")
        self.warehouse_delete_name_line.setClearButtonEnabled(True)
        self.label = QLabel(self.storage_page)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 191, 31))
        self.label.setStyleSheet(u"background:transparent;\n"
"color: rgb(255, 255, 255);")
        self.label_2 = QLabel(self.storage_page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 250, 191, 31))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"background:transparent;\n"
"color: rgb(255, 255, 255);")
        self.label_3 = QLabel(self.storage_page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 460, 221, 31))
        self.label_3.setStyleSheet(u"background:transparent;\n"
"color: rgb(255, 255, 255);")
        self.product_for_material_page_pushButton = QPushButton(self.storage_page)
        self.product_for_material_page_pushButton.setObjectName(u"product_for_material_page_pushButton")
        self.product_for_material_page_pushButton.setGeometry(QRect(580, 530, 241, 31))
        self.product_for_material_page_pushButton.setStyleSheet(u"")
        self.product_for_material_page_pushButton_exel = QPushButton(self.storage_page)
        self.product_for_material_page_pushButton_exel.setObjectName(u"product_for_material_page_pushButton_exel")
        self.product_for_material_page_pushButton_exel.setGeometry(QRect(840, 530, 211, 31))
        self.product_for_material_page_pushButton_exel.setStyleSheet(u"")
        self.tabWidget.addTab(self.storage_page, "")
        self.warehouse_add_name_line.raise_()
        self.wareouse_amount_line.raise_()
        self.warehouse_add_button.raise_()
        self.wareouse_update_amount_line.raise_()
        self.warehouse_update_button.raise_()
        self.warehouse_update_name_line.raise_()
        self.warehouse_tableViw.raise_()
        self.search_supplies_by_name_lineEdit.raise_()
        self.search_supplies_by_name_button.raise_()
        self.warehouse_delete_button.raise_()
        self.warehouse_delete_name_line.raise_()
        self.label.raise_()
        self.label_3.raise_()
        self.product_for_material_page_pushButton.raise_()
        self.product_for_material_page_pushButton_exel.raise_()
        self.label_2.raise_()

        self.gridLayout_3.addWidget(self.tabWidget, 1, 0, 1, 1)

        self.stackedWidget_1.addWidget(self.main_screen_page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.product_for_material_update_pushButton = QPushButton(self.page_2)
        self.product_for_material_update_pushButton.setObjectName(u"product_for_material_update_pushButton")
        self.product_for_material_update_pushButton.setGeometry(QRect(320, 270, 121, 31))
        self.product_for_material_update_pushButton.setStyleSheet(u"")
        self.product_for_material_comboBox = QComboBox(self.page_2)
        self.product_for_material_comboBox.addItem("")
        self.product_for_material_comboBox.addItem("")
        self.product_for_material_comboBox.addItem("")
        self.product_for_material_comboBox.addItem("")
        self.product_for_material_comboBox.setObjectName(u"product_for_material_comboBox")
        self.product_for_material_comboBox.setGeometry(QRect(30, 90, 561, 31))
        self.product_for_material_comboBox.setStyleSheet(u"")
        self.product_for_material_tableView = QTableView(self.page_2)
        self.product_for_material_tableView.setObjectName(u"product_for_material_tableView")
        self.product_for_material_tableView.setGeometry(QRect(610, 40, 461, 541))
        self.product_for_material_tableView.setStyleSheet(u"color: rgb(0,,0,0);\n"
"background-image: url(:/images/Images/table_background.png);\n"
"background-color: rgb(255,255,255);\n"
"font-family: \"Calibri\";\n"
"font-weight:bold;\n"
"font-size:23px;\n"
"border-radius: 12px;")
        self.product_for_material_name_lineEdit = QLineEdit(self.page_2)
        self.product_for_material_name_lineEdit.setObjectName(u"product_for_material_name_lineEdit")
        self.product_for_material_name_lineEdit.setGeometry(QRect(80, 140, 471, 31))
        self.product_for_material_name_lineEdit.setStyleSheet(u"")
        self.product_for_material_name_lineEdit.setClearButtonEnabled(True)
        self.product_for_material_amount_lineEdit = QLineEdit(self.page_2)
        self.product_for_material_amount_lineEdit.setObjectName(u"product_for_material_amount_lineEdit")
        self.product_for_material_amount_lineEdit.setGeometry(QRect(130, 190, 381, 31))
        self.product_for_material_amount_lineEdit.setStyleSheet(u"")
        self.product_for_material_amount_lineEdit.setClearButtonEnabled(True)
        self.product_for_material_add_pushButton = QPushButton(self.page_2)
        self.product_for_material_add_pushButton.setObjectName(u"product_for_material_add_pushButton")
        self.product_for_material_add_pushButton.setGeometry(QRect(170, 270, 121, 31))
        self.product_for_material_add_pushButton.setStyleSheet(u"")
        self.product_for_material_delete_pushButton = QPushButton(self.page_2)
        self.product_for_material_delete_pushButton.setObjectName(u"product_for_material_delete_pushButton")
        self.product_for_material_delete_pushButton.setGeometry(QRect(470, 240, 121, 31))
        self.product_for_material_delete_pushButton.setStyleSheet(u"")
        self.product_for_material_search_pushButton = QPushButton(self.page_2)
        self.product_for_material_search_pushButton.setObjectName(u"product_for_material_search_pushButton")
        self.product_for_material_search_pushButton.setGeometry(QRect(30, 250, 121, 31))
        self.product_for_material_search_pushButton.setStyleSheet(u"")
        self.label_13 = QLabel(self.page_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(230, 320, 141, 141))
        self.label_13.setStyleSheet(u"background-image: url(:/images/Images/bms_145x145.jpg);\n"
"\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 70px;")
        self.back_storage_page_pushButton = QPushButton(self.page_2)
        self.back_storage_page_pushButton.setObjectName(u"back_storage_page_pushButton")
        self.back_storage_page_pushButton.setGeometry(QRect(250, 490, 101, 31))
        self.back_storage_page_pushButton.setStyleSheet(u"")
        self.stackedWidget_1.addWidget(self.page_2)
        self.product_for_material_update_pushButton.raise_()
        self.product_for_material_comboBox.raise_()
        self.product_for_material_name_lineEdit.raise_()
        self.product_for_material_amount_lineEdit.raise_()
        self.product_for_material_add_pushButton.raise_()
        self.product_for_material_delete_pushButton.raise_()
        self.product_for_material_search_pushButton.raise_()
        self.label_13.raise_()
        self.back_storage_page_pushButton.raise_()
        self.product_for_material_tableView.raise_()

        self.gridLayout.addWidget(self.stackedWidget_1, 1, 0, 1, 1)


        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1124, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.username_lineEdit, self.password_lineEdit)
        QWidget.setTabOrder(self.password_lineEdit, self.login_button)
        QWidget.setTabOrder(self.login_button, self.register_button)
        QWidget.setTabOrder(self.register_button, self.password_forgetten_button)
        QWidget.setTabOrder(self.password_forgetten_button, self.search_product_name_comboBox)
        QWidget.setTabOrder(self.search_product_name_comboBox, self.search_by_name_button)
        QWidget.setTabOrder(self.search_by_name_button, self.search_serial_number_lineEdit)
        QWidget.setTabOrder(self.search_serial_number_lineEdit, self.search_by_serial_no_button)
        QWidget.setTabOrder(self.search_by_serial_no_button, self.new_serial_no_lineEdit)
        QWidget.setTabOrder(self.new_serial_no_lineEdit, self.new_product_model_comboBox)
        QWidget.setTabOrder(self.new_product_model_comboBox, self.add_new_product_button)
        QWidget.setTabOrder(self.add_new_product_button, self.quit_button)
        QWidget.setTabOrder(self.quit_button, self.products_tableView)
        QWidget.setTabOrder(self.products_tableView, self.add_line_button)
        QWidget.setTabOrder(self.add_line_button, self.delete_line_Button)
        QWidget.setTabOrder(self.delete_line_Button, self.update_product_info_button)
        QWidget.setTabOrder(self.update_product_info_button, self.back_button)
        QWidget.setTabOrder(self.back_button, self.excel_export_button)
        QWidget.setTabOrder(self.excel_export_button, self.product_info_tableView)
        QWidget.setTabOrder(self.product_info_tableView, self.tabWidget)
        QWidget.setTabOrder(self.tabWidget, self.warehouse_update_name_line)
        QWidget.setTabOrder(self.warehouse_update_name_line, self.wareouse_update_amount_line)
        QWidget.setTabOrder(self.wareouse_update_amount_line, self.warehouse_update_button)
        QWidget.setTabOrder(self.warehouse_update_button, self.warehouse_add_name_line)
        QWidget.setTabOrder(self.warehouse_add_name_line, self.wareouse_amount_line)
        QWidget.setTabOrder(self.wareouse_amount_line, self.warehouse_add_button)
        QWidget.setTabOrder(self.warehouse_add_button, self.warehouse_delete_name_line)
        QWidget.setTabOrder(self.warehouse_delete_name_line, self.warehouse_delete_button)
        QWidget.setTabOrder(self.warehouse_delete_button, self.search_supplies_by_name_lineEdit)
        QWidget.setTabOrder(self.search_supplies_by_name_lineEdit, self.search_supplies_by_name_button)
        QWidget.setTabOrder(self.search_supplies_by_name_button, self.warehouse_tableViw)
        QWidget.setTabOrder(self.warehouse_tableViw, self.register_about_comboBox)
        QWidget.setTabOrder(self.register_about_comboBox, self.register_username_lineEdit)
        QWidget.setTabOrder(self.register_username_lineEdit, self.register_password_lineEdit)
        QWidget.setTabOrder(self.register_password_lineEdit, self.security_key_lineEdit)
        QWidget.setTabOrder(self.security_key_lineEdit, self.register_user_buton)

        self.retranslateUi(MainWindow)

        self.stackedWidget_1.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.register_button.setText(QCoreApplication.translate("MainWindow", u"Kaydol", None))
        self.password_forgetten_button.setText(QCoreApplication.translate("MainWindow", u"\u015eifremi Unuttum", None))
        self.login_button.setText(QCoreApplication.translate("MainWindow", u"Giri\u015f ", None))
        self.label_10.setText("")
        self.username_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Kullan\u0131c\u0131 ad\u0131...", None))
        self.password_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u015eifre...", None))
        self.label_4.setText("")
        self.register_about_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"---L\u00fctfen \u00c7al\u0131\u015ft\u0131\u011f\u0131n\u0131z Birimi Se\u00e7iniz---", None))
        self.register_about_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Ekip \u015eefi", None))
        self.register_about_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Y\u00f6netim", None))
        self.register_about_comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Teknik Servis", None))

        self.register_user_buton.setText(QCoreApplication.translate("MainWindow", u"Kaydol", None))
        self.register_username_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Kullan\u0131c\u0131 Ad\u0131...", None))
        self.security_key_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"G\u00fcvenlik Anahtar\u0131...", None))
        self.register_password_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u015eifre...", None))
        self.label_12.setText("")
        self.back_main_menu_button.setText(QCoreApplication.translate("MainWindow", u"Geri", None))
        self.model_label.setText("")
        self.delete_line_Button.setText(QCoreApplication.translate("MainWindow", u"HAT S\u0130L", None))
        self.serial_no_label.setText("")
        self.back_button.setText(QCoreApplication.translate("MainWindow", u"GER\u0130", None))
        self.add_line_button.setText(QCoreApplication.translate("MainWindow", u"HAT EKLE", None))
        self.excel_export_button.setText(QCoreApplication.translate("MainWindow", u"EXCEL", None))
        self.name_label.setText("")
        self.update_product_info_button.setText(QCoreApplication.translate("MainWindow", u"G\u00dcNCELLE", None))
        self.search_product_name_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Boran1", None))
        self.search_product_name_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Boran2", None))
        self.search_product_name_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Aybars1", None))
        self.search_product_name_comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Aybars2", None))

        self.search_by_name_button.setText(QCoreApplication.translate("MainWindow", u"?", None))
        self.search_serial_number_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Seri Numara...", None))
        self.search_by_serial_no_button.setText(QCoreApplication.translate("MainWindow", u"Ara", None))
        self.new_serial_no_lineEdit.setText("")
        self.new_serial_no_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Seri Numaras\u0131", None))
        self.new_product_model_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Boran1", None))
        self.new_product_model_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Boran2", None))
        self.new_product_model_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Aybars1", None))
        self.new_product_model_comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Aybars2", None))

        self.new_product_model_comboBox.setPlaceholderText("")
        self.add_new_product_button.setText(QCoreApplication.translate("MainWindow", u"Kaydet", None))
        self.quit_button.setText(QCoreApplication.translate("MainWindow", u"\u00c7\u0131k\u0131\u015f", None))
        self.label_14.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"URUN", None))
        self.warehouse_add_name_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Malzeme ", None))
        self.wareouse_amount_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Miktar", None))
        self.warehouse_add_button.setText(QCoreApplication.translate("MainWindow", u"Ekle", None))
        self.wareouse_update_amount_line.setText("")
        self.wareouse_update_amount_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Miktar", None))
        self.warehouse_update_button.setText(QCoreApplication.translate("MainWindow", u"G\u00fcncelle", None))
        self.warehouse_update_name_line.setText("")
        self.warehouse_update_name_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Malzeme ", None))
        self.search_supplies_by_name_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Malzeme ismi...", None))
        self.search_supplies_by_name_button.setText(QCoreApplication.translate("MainWindow", u"Ara", None))
        self.warehouse_delete_button.setText(QCoreApplication.translate("MainWindow", u"Sil", None))
        self.warehouse_delete_name_line.setText("")
        self.warehouse_delete_name_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Malzeme ", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u00dcr\u00fcn G\u00fcncelleme", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Yeni \u00dcr\u00fcn ", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u" \u00dcr\u00fcn Silme", None))
        self.product_for_material_page_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u00dcr\u00fcn D\u00fczenle", None))
        self.product_for_material_page_pushButton_exel.setText(QCoreApplication.translate("MainWindow", u"Excel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.storage_page), QCoreApplication.translate("MainWindow", u"DEPO", None))
        self.product_for_material_update_pushButton.setText(QCoreApplication.translate("MainWindow", u"G\u00fcncelle", None))
        self.product_for_material_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Boran1", None))
        self.product_for_material_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Boran2", None))
        self.product_for_material_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Aybars1", None))
        self.product_for_material_comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Aybars2", None))

        self.product_for_material_name_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Malzeme ismi...", None))
        self.product_for_material_amount_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Malzeme miktar\u0131...", None))
        self.product_for_material_add_pushButton.setText(QCoreApplication.translate("MainWindow", u"Ekle", None))
        self.product_for_material_delete_pushButton.setText(QCoreApplication.translate("MainWindow", u"Sil", None))
        self.product_for_material_search_pushButton.setText(QCoreApplication.translate("MainWindow", u"Ara", None))
        self.label_13.setText("")
        self.back_storage_page_pushButton.setText(QCoreApplication.translate("MainWindow", u"Geri", None))
    # retranslateUi

