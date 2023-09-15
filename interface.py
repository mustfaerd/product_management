from ui_main import Ui_MainWindow
from PySide2.QtWidgets import QMainWindow, QInputDialog,QMessageBox, QLineEdit,QFileDialog
from PySide2.QtCore import QModelIndex, QPropertyAnimation, QRect
from PySide2.QtGui import QIntValidator
from database import ProductInformationDB
from table_view_screen import Products_TableModel, Products_Info_TableModel, TableModel
from operation_time_database import OperationInformationDB
from register_database import SignUpDB
from warehouse_database import WareHouseDB
from aircraft_supplies import AircraftSuppliesDB
import datetime
import multitasking


line_name = "HAT-"
blank = ""
model_type= {
                        "Boran1": "ROTAY WING",
                        "Boran2": "ROTAY WING",
                        "Aybars1":"VTOL",
                        "Aybars2":"VTOL"

                        }
ADMIN_CONTROL_TEXT = "Bms2023product!"

class Products(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui_main = Ui_MainWindow()
        self.ui_main.setupUi(self)
    #######################################################################################################################################################################################
    #---------------------------------------------------------------Common Functions - Ortak Fonksiyonlar---------------------------------------------------------------
    #######################################################################################################################################################################################
    def create_databases(self)->None:
        "Tüm veritabanlarını çağırır."
        self.product_information_db = ProductInformationDB()
        self.operation_information_db = OperationInformationDB()
        self.product_information_db.get_data_signal.connect(self.show_table)
        self.warehouse_db = WareHouseDB()
        self.signup_db = SignUpDB()
        self.aircraft_supplies_db = AircraftSuppliesDB()
        self.animation()

    def back_to_login_screen(self):
        """
        Uygulamayı kapatır.
        """
        self.ui_main.stackedWidget_1.setCurrentIndex(0)
        self.delete_label_closed()

    def open_main_screen(self):
        """
        Giriş ekranından ana ekrana geçer.
        """
        self.ui_main.stackedWidget_1.setCurrentIndex(2)
    def animation(self):
        """
        Giriş animasyonu
        """
        self.animation = QPropertyAnimation(self.ui_main.frame_2, b"geometry")
        self.animation.setDuration(1750)
        self.animation.setStartValue(QRect(0,10,1090,590))
        self.animation.setEndValue(QRect(545,295,0,0)) 
        self.animation.start() 

    def connect_buttons_to_events(self)->None:
        "Tüm butonları ilgili fonksiyonlara bağlar."
        self.ui_main.add_new_product_button.clicked.connect(self.register_product_information)
        self.ui_main.search_by_serial_no_button.clicked.connect(self.query_by_product_serial_number)
        self.ui_main.search_by_name_button.clicked.connect(self.check_products_by_name)
        self.ui_main.products_tableView.doubleClicked.connect(self.show_selected_product_info)
        self.ui_main.warehouse_add_button.clicked.connect(self.warehouse_add)
        self.ui_main.search_supplies_by_name_button.clicked.connect(self.show_warehouse_table)
        self.ui_main.warehouse_update_button.clicked.connect(self.update_warehouse)
        self.ui_main.delete_line_Button.clicked.connect(self.remove_line)
        self.ui_main.add_line_button.clicked.connect(self.create_line)
        self.ui_main.update_product_info_button.clicked.connect(self.save_table_to_database)
        # self.ui_main.excel_export_button.clicked.connect(self.export_the_tableview)
        self.ui_main.login_button.clicked.connect(self.login_screen)
        self.ui_main.back_button.clicked.connect(lambda:self.ui_main.stackedWidget_2.setCurrentIndex(1))
        self.ui_main.quit_button.clicked.connect(self.back_to_login_page)
        self.ui_main.password_lineEdit.returnPressed.connect(self.ui_main.login_button.click)
        self.ui_main.register_user_buton.clicked.connect(self.signup_information)
        self.ui_main.password_forgetten_button.clicked.connect(self.update_forgetten_password)    
        self.ui_main.register_button.clicked.connect(lambda:self.ui_main.stackedWidget_1.setCurrentIndex(1))
        self.ui_main.warehouse_delete_button.clicked.connect(self.warehouse_delete)   
        self.ui_main.back_main_menu_button.clicked.connect(lambda:self.ui_main.stackedWidget_1.setCurrentIndex(0))    
        self.ui_main.product_for_material_add_pushButton.clicked.connect(self.check_product_material) 
        self.ui_main.product_for_material_delete_pushButton.clicked.connect(self.delete_product_for_material_interface)
        self.ui_main.product_for_material_update_pushButton.clicked.connect(self.update_product_for_material_interface)
        self.ui_main.product_for_material_search_pushButton.clicked.connect(self.search_product_for_material)
        self.ui_main.back_storage_page_pushButton.clicked.connect(self.back_to_warehouse_pagge)
        self.ui_main.product_for_material_page_pushButton.clicked.connect(self.open_products_details)
        self.ui_main.product_for_material_amount_lineEdit.setValidator(QIntValidator(0,9999999,self))
        self.ui_main.wareouse_update_amount_line.setValidator(QIntValidator(0,9999999,self))
        self.ui_main.wareouse_amount_line.setValidator(QIntValidator(0,9999999,self))

    #######################################################################################################################################################################################
    #-----------------------------------------------The Start Codes of The Program  - Programın Başlangıç Kodları -------------------------------------------------------------------
    #######################################################################################################################################################################################
    def login_screen(self):
        """
        giriş yapmak için kullanılır kullanıcı kayıt olurken nerede çalıştığı bilgisini girer ve onu kontrol eder.
        """   
        if not self.ui_main.username_lineEdit.text() or not self.ui_main.password_lineEdit.text():
            QMessageBox.warning(self, "Hata", "Kullanıcı adı veya şifre boş bırakılamaz!")
        else:
            user = self.signup_db.search_user(self.ui_main.username_lineEdit.text())   
            if user is None:
                QMessageBox.warning(self, "Hata","Kullanıcı Adı Bulunamadı")
            elif  self.ui_main.password_lineEdit.text() == user[0][1]:
                if user[0][2] == 'Ekip Şefi':
                    self.enabled_true()
                elif user[0][2] == 'Teknik Servis' or user[0][2] == 'Yönetim':
                    self.enabled_false()  
                self.open_main_screen()
                self.delete_login_lineEdits()
            else:
                QMessageBox.warning(self, "Hata", "Şifre yada Kullanıcı Adı Hatalı!")



    def update_forgetten_password(self):
        """
        eğer şifre unutulursa anahtar kelime yardımıyla sıfırlama işlemi yapar.
        """
        user=self.signup_db.search_user(self.ui_main.username_lineEdit.text())
        if not user:
            QMessageBox.warning(None, "Sistem", "Kullanıcı adı bulunamadı")
            return
        security_key_input, ok = QInputDialog.getText(None, "Sistem", "Lütfen güvenlik anahtarını girin")
        if ok and security_key_input ==user[0][3]:
            new_password, ok = QInputDialog.getText(None, "Sistem", "Lütfen yeni şifrenizi girin")
            if ok and new_password:
                self.signup_db.update_password(self.ui_main.username_lineEdit.text(), new_password)
                QMessageBox.information(None, "Sistem", "Şifre başarıyla değiştirildi")
                self.back_to_login_screen()
        else:
            QMessageBox.critical(None, "Sistem", "Güvenlik anahtarı yanlış") 


    def signup_information(self):
        """
        Kaydetme işlevini yapar.
        """
        if not self.ui_main.register_username_lineEdit.text() or not self.ui_main.register_password_lineEdit.text() or not self.ui_main.security_key_lineEdit.text():
            QMessageBox.warning(None, "Sistem", "Lütfen kullanıcı adı, şifre ve güvenlik kelimesi giriniz!!!")
            return  
        if self.ui_main.register_about_comboBox.currentText() == 'Ekip Şefi':
            admin_password, ok = QInputDialog.getText(None, "Admin Şifresi", "Lütfen yönetici şifresini girin:", QLineEdit.Password)
            if not ok:
                return
            elif admin_password != ADMIN_CONTROL_TEXT:
                QMessageBox.warning(None, "Sistem", "Yanlış yönetici şifresi")
                return
        if self.ui_main.register_about_comboBox.currentText() == '---Lütfen çalıştığınız servisi seçiniz---':
            QMessageBox.warning(None, "Sistem", "Lütfen çalıştığınız servisi seçiniz")
            return
        if self.signup_db.check_username_exist(self.ui_main.register_username_lineEdit.text()) is False:
            self.signup_db.add_new_user(self.ui_main.register_username_lineEdit.text(),
                                        self.ui_main.register_password_lineEdit.text(),
                                        self.ui_main.register_about_comboBox.currentText(),
                                        self.ui_main.security_key_lineEdit.text())
            QMessageBox.information(None, "Sistem", "Kayıt Başarılı")
            self.back_to_login_screen()
            self.delete_signup_lineEdits()
        else:
            QMessageBox.critical(None, "Sistem", "Kullanıcı Adı Kullanılmaktadır")
    #######################################################################################################################################################################################                     
    #------------------------------------------------- Product Registration and Inquiry Procedure - Ürün Kayıt ve Sorgulama Prosedörü----------------------------------------------------                     
    #######################################################################################################################################################################################
    def register_product_information(self):      
        """
        Ürünlerin kayıt işlemi.
        """
        if self.product_information_db.check_product_id_exist(self.ui_main.new_serial_no_lineEdit.text()) is False:
            if self.automatic_product_reduction() is not True:
                return
            self.product_information_db.add_product_value(self.ui_main.new_serial_no_lineEdit.text(),
                                                    self.ui_main.new_product_model_comboBox.currentText(),
                                                    self.get_model_type(self.ui_main.new_product_model_comboBox.currentText()))
            
            QMessageBox.information(None, "Sistem", "Kayıt Başarılı")
        else:
            QMessageBox.critical(None, "Sistem", "Kayıt Başarısız Bu seri numarası kayıtlı")
    
    def show_products_by_name(self,model_name):
        """
        ComboBox'a göre aynı türden ürünleri tabloya yansıtır.
        """
        data=self.product_information_db.get_products_by_name(model_name)

    def show_table(self,data):
        data = Products_TableModel(data)
        self.ui_main.products_tableView.setModel(data)
        self.ui_main.products_tableView.horizontalHeader().setStretchLastSection(True)
    
    def query_by_product_serial_number(self):
        if self.product_information_db.check_product_id_exist(self.ui_main.search_serial_number_lineEdit.text()):
            self.show_product_by_id(self.ui_main.search_serial_number_lineEdit.text())
        else:
            QMessageBox.critical(None, "Sistem", "Ürün Kaydı Bulunamadı.")

    def show_product_by_id(self,id):
        """
        Ürünün seri numarasına göre tabloya yansıtır.
        """
        data=self.product_information_db.get_product_by_id(id)
        data = Products_TableModel(data)
        self.ui_main.products_tableView.setModel(data)
    
    #@multitasking.task
    def check_products_by_name(self):
        """
        Ürün sorgulama ekranı ve hata derlemesi.
        """
        if self.product_information_db.check_exist_product_name(self.ui_main.search_product_name_comboBox.currentText()) is True:
            #print("okey")
            self.show_products_by_name(self.ui_main.search_product_name_comboBox.currentText())
        else:
            QMessageBox.critical(None, "Sistem", "Ürün kaydı bulunamadı.")   

    def get_model_type(self,model):
        return model_type[model] 
    #######################################################################################################################################################################################
    # --------------------------------------------------------- Product Information Details - Ürünlerin Detaylı Bilgileri ------------------------------------------------------------------
    #######################################################################################################################################################################################
    def show_selected_product_info(self, index):
        """
        Seçilien ürünün detaylı bilgileri.
        """
        self.ui_main.stackedWidget_2.setCurrentWidget(self.ui_main.product_info_page)
        self.ui_main.serial_no_label.setText(self.ui_main.products_tableView.model().index(self.ui_main.products_tableView.currentIndex().row(),0).data())
        self.ui_main.name_label.setText(self.ui_main.products_tableView.model().index(self.ui_main.products_tableView.currentIndex().row(),1).data())
        self.ui_main.model_label.setText(self.ui_main.products_tableView.model().index(self.ui_main.products_tableView.currentIndex().row(),2).data())
        self.show_line_info(self.ui_main.products_tableView.model().index(self.ui_main.products_tableView.currentIndex().row(),0).data())

    def show_line_info(self,id):
        """
        Alınan ID de kayıtlı olan uçağı tabloya yansıtır.
        """
        self.table = self.operation_information_db.get_line_info(id)
        self.table = Products_Info_TableModel(self.table)
        self.ui_main.product_info_tableView.setModel(self.table)
        self.ui_main.product_info_tableView.horizontalHeader().setStretchLastSection(True)

    def remove_line(self):
        """
        Hattı siler ve hat numaralarını günceller.
        """
        
        self.operation_information_db.delete_row(self.ui_main.serial_no_label.text(), 
                            self.ui_main.product_info_tableView.model().index(self.ui_main.product_info_tableView.currentIndex().row(),0).data()) 
        self.show_line_info(self.ui_main.products_tableView.model().index(self.ui_main.products_tableView.currentIndex().row(),0).data())
        for i in range(self.ui_main.product_info_tableView.model().rowCount(QModelIndex)):
                self.operation_information_db.update_line_names(line_name+ str(i+1),
                                                self.ui_main.product_info_tableView.model().index(i,0).data(),
                                                self.ui_main.serial_no_label.text())
        self.show_line_info(self.ui_main.products_tableView.model().index(self.ui_main.products_tableView.currentIndex().row(),0).data())


    def create_line(self):
        """
        Yeni hat oluşturur.
        """
        self.operation_information_db.add_row(self.ui_main.serial_no_label.text(),
                                line_name + str(self.ui_main.product_info_tableView.model().rowCount(QModelIndex())+1),
                                blank,blank,blank,blank)
        self.show_line_info(self.ui_main.products_tableView.model().index(self.ui_main.products_tableView.currentIndex().row(),0).data())

    def save_table_to_database(self):
        """
        Ürün bilgilerini tablo üzerinde günceller ve veritabanına kaydeder.
        """
        for i in range(self.ui_main.product_info_tableView.model().rowCount(QModelIndex)):
            id=self.ui_main.serial_no_label.text()
            line=self.ui_main.product_info_tableView.model().index(i,0).data()
            starting_date=self.ui_main.product_info_tableView.model().index(i,1).data()
            end_date=self.ui_main.product_info_tableView.model().index(i,2).data()
            note=self.ui_main.product_info_tableView.model().index(i,4).data()

            if starting_date == blank and not end_date == blank:
                QMessageBox.critical(None, "Sistem", "Önce başlangıç tarihi girmelisiniz!")
            else :
                self.operation_information_db.update_line(starting_date,
                                        end_date,
                                        note,
                                        id,
                                        line)      
            if not starting_date == blank and not end_date == blank:
                try:
                    self.calculate_time(starting_date,end_date)
                    self.operation_information_db.update_time(str(self.time),
                                                            id,
                                                            line)
                    continue
                except ValueError:
                    QMessageBox.critical(None, "Hata", "GG/AA/YY formatında giriniz.")
                    continue
        self.show_line_info(self.ui_main.products_tableView.model().index(self.ui_main.products_tableView.currentIndex().row(),0).data())

    def calculate_time(self,start_date, end_date):
            """
            Hat sürelerini hesaplar.
            """
            start_date_value= datetime.datetime.strptime(str(start_date), "%d/%m/%Y")
            end_date_value= datetime.datetime.strptime(str(end_date), "%d/%m/%Y")
            self.time = (end_date_value) - (start_date_value)   
    #######################################################################################################################################################################################        
    #--------------------------------------------------------------------------------- WAREHOUSE - DEPO ---------------------------------------------------------------------------------
    #######################################################################################################################################################################################
    def show_warehouse(self,name):
        "Depoda aranan ürünü tabloda gösterir."
        data = self.warehouse_db.all_warehouse(name)
        data = TableModel(data)
        self.ui_main.warehouse_tableViw.setModel(data)
        self.ui_main.warehouse_tableViw.horizontalHeader().setStretchLastSection(True)
        
    def reflects_all_data_into_warehouse_table(self):
        data = self.warehouse_db.show_war()
        data = TableModel(data)
        self.ui_main.warehouse_tableViw.setModel(data)
        self.ui_main.warehouse_tableViw.horizontalHeader().setStretchLastSection(True)

    def warehouse_add(self):
        """
        Malzeme Deposuna Ürün Ekler.
        """
        if self.warehouse_db.check_warehouse(self.ui_main.warehouse_add_name_line.text()) is False and (self.ui_main.warehouse_add_name_line.text() != ""):
            if (self.ui_main.warehouse_add_name_line.text() != "") and (self.ui_main.wareouse_amount_line.text() != ""):
                self.warehouse_db.add_value(self.ui_main.warehouse_add_name_line.text(),
                                    self.ui_main.wareouse_amount_line.text())
                self.reflects_all_data_into_warehouse_table()
            else:
                QMessageBox.critical(None, "Sistem", "Boş Bırakılamaz")            
        else:
            QMessageBox.critical(None, "Sistem", "Sistemde mevcut ya da bu ürün eklenemez.")



    def show_warehouse_table(self):

        if len(self.ui_main.search_supplies_by_name_lineEdit.text()) > 0:
            if self.warehouse_db.check_warehouse(self.ui_main.search_supplies_by_name_lineEdit.text()) is True:
                self.show_warehouse(self.ui_main.search_supplies_by_name_lineEdit.text())
            else:
                QMessageBox.critical(None, "Sistem", "Ürün bulunamadı.")
        else:
            self.reflects_all_data_into_warehouse_table()

    def update_warehouse(self):
        """
        Malzeme Deposundaki Ürünleri Günceller.
        """
        if self.warehouse_db.check_storage_exist(self.ui_main.warehouse_update_name_line.text()) is True and(self.ui_main.warehouse_update_name_line.text() != ""):
            if(self.ui_main.warehouse_update_name_line.text() != "") and (self.ui_main.wareouse_update_amount_line.text() != ""):
                old_value = int(self.warehouse_db.all_tableview_warehouse(self.ui_main.warehouse_update_name_line.text()))
                new_value = int(self.ui_main.wareouse_update_amount_line.text())
                final_value = (old_value) + (new_value)
                self.warehouse_db.update_value(final_value,
                                        self.ui_main.warehouse_update_name_line.text())
                self.reflects_all_data_into_warehouse_table()
            else:
                QMessageBox.critical(None, "Sistem", "Boş Bırakılamaz.")                
        else:
            QMessageBox.critical(None, "Sistem", "Sistemde ürün yok ya da boş bırakılmaz.")
        
    def delete_label_closed(self):
        """
        Çıkış butonundan sonra line editleri temizler.
        """
        self.ui_main.search_serial_number_lineEdit.clear()
        self.ui_main.new_serial_no_lineEdit.clear()
        self.ui_main.warehouse_update_name_line.clear()
        self.ui_main.wareouse_update_amount_line.clear()
        self.ui_main.warehouse_add_name_line.clear()
        self.ui_main.wareouse_amount_line.clear()
        self.ui_main.search_supplies_by_name_lineEdit.clear()

    def warehouse_delete(self):
        if self.warehouse_db.check_storage_exist(self.ui_main.warehouse_delete_name_line.text()) is True:
            self.warehouse_db.warehouse_delete_material(self.ui_main.warehouse_delete_name_line.text())
            self.reflects_all_data_into_warehouse_table()
        else:
            QMessageBox.critical(None, "Sistem", "Böyle Bir Malzeme Zaten Yok!")

    def automatic_product_reduction(self):
        data = self.aircraft_supplies_db.pull_data(self.ui_main.new_product_model_comboBox.currentText())
        if len(self.warehouse_db.get_missing_material(data)) >0:
            QMessageBox.critical(None, "Sistem", f"Depoda aşağıdaki malzemeler eksik \n {self.warehouse_db.get_missing_material(data)} ")
            return False
        for material in data:
            self.warehouse_db.update_value(self.warehouse_db.get_storage_material_number(material[0])-int(material[1]),
                                           material[0])
        return True
    #######################################################################################################################################################################################
    #------------------------------------------------------------------------ Task Terminators ------------------------------------------------------------------------
    #######################################################################################################################################################################################
    def enabled_true(self):
        """
        Butonları aktif eder.
        """
        self.ui_main.update_product_info_button.setEnabled(True)
        self.ui_main.delete_line_Button.setEnabled(True)
        self.ui_main.add_line_button.setEnabled(True)
        self.ui_main.add_new_product_button.setEnabled(True)
        self.ui_main.warehouse_update_button.setEnabled(True)
        self.ui_main.warehouse_add_button.setEnabled(True)
        self.ui_main.warehouse_delete_button.setEnabled(True)

    def delete_login_lineEdits(self):
        """
        giriş ekranındaki lineEditleri giriş yaptıktan sonra siler.
        """
        self.ui_main.username_lineEdit.clear()
        self.ui_main.password_lineEdit.clear()

    def enabled_false(self):
        """
        Butonları pasif eder.    
        """
        self.ui_main.update_product_info_button.setEnabled(False)
        self.ui_main.delete_line_Button.setEnabled(False)
        self.ui_main.add_line_button.setEnabled(False)
        self.ui_main.add_new_product_button.setEnabled(False)
        self.ui_main.warehouse_update_button.setEnabled(False)
        self.ui_main.warehouse_add_button.setEnabled(False)
        self.ui_main.warehouse_delete_button.setEnabled(False)
    def back_to_login_page(self):
        """
        Ana sayfadan kullanıcı giriş ekranına geri döner.
        """
        self.ui_main.stackedWidget_1.setCurrentIndex(0)
        self.ui_main.username_lineEdit.setText("")
        self.ui_main.password_lineEdit.setText("")
        self.enabled_true()
        self.delete_label_closed()
            
    def delete_signup_lineEdits(self):
        self.ui_main.register_password_lineEdit.clear()
        self.ui_main.register_username_lineEdit.clear()
        self.ui_main.security_key_lineEdit.clear()

    def add_product_for_material(self):
        """
        Ürünü özgü parçaları eklemek için kullanılan fonksiyonlar.
        """
        if self.ui_main.product_for_material_name_lineEdit.text() != "" and self.ui_main.product_for_material_amount_lineEdit.text() != "":
            self.aircraft_supplies_db.add_storage_material_number(self.ui_main.product_for_material_comboBox.currentText(),
                                                            self.ui_main.product_for_material_name_lineEdit.text(),
                                                            self.ui_main.product_for_material_amount_lineEdit.text())
            self.show_product_for_material_interface()
        else:
            QMessageBox.critical(None, "Sistem" ,"Boş Bırakılamaz")


    def delete_product_for_material_interface(self):
        """
        Ürüne özgü parçaların silinmesi işlemi.
        """
        self.aircraft_supplies_db.delete_product_for_material(self.ui_main.product_for_material_comboBox.currentText(),
                                                           self.ui_main.product_for_material_name_lineEdit.text())
        self.show_product_for_material_interface()
    
    def update_product_for_material_interface(self):
        """
        Ürünü özgü parçaların güncellenmesi işlemi.
        """
        if self.ui_main.product_for_material_name_lineEdit.text() != "" and self.ui_main.product_for_material_amount_lineEdit.text():
            self.aircraft_supplies_db.update_product_for_material(self.ui_main.product_for_material_comboBox.currentText(),
                                                            self.ui_main.product_for_material_amount_lineEdit.text(),
                                                            self.ui_main.product_for_material_name_lineEdit.text()
                                                            )
            self.show_product_for_material_interface()
        else:
            QMessageBox.critical(None, "Sistem" ,"Boş Bırakılamaz")
        
    def show_product_for_material_interface(self):
        """
        Ürünü özgü kullanılan parçların tabloda gözükmesi.
        """
        data = self.aircraft_supplies_db.show_product_for_material(self.ui_main.product_for_material_comboBox.currentText())
        data = TableModel(data)
        self.ui_main.product_for_material_tableView.setModel(data)

    def show_products_in_table(self,model_name, name):
        data = self.aircraft_supplies_db.product_search(model_name, name)
        data = TableModel(data)
        self.ui_main.product_for_material_tableView.setModel(data)
        self.ui_main.product_for_material_tableView.horizontalHeader().setStretchLastSection(True)

    def search_product_for_material(self):
        if len(self.ui_main.product_for_material_name_lineEdit.text()) > 0:
        # self.aircraft_supplies_db.product_search()
            if self.aircraft_supplies_db.controller_product_exist(self.ui_main.product_for_material_comboBox.currentText(), self.ui_main.product_for_material_name_lineEdit.text()) is True:
                self.show_products_in_table(self.ui_main.product_for_material_comboBox.currentText(), self.ui_main.product_for_material_name_lineEdit.text())
            
            else:
                QMessageBox.critical(None, "Sistem", "Ürün Bulunamadı")
        else:
            QMessageBox.critical(None, "Sistem", "Aranan Ürün Bulunamadı")
            self.show_product_for_material_interface()



    def open_products_details(self):
        """
        Ürüne özgü parçaların güncellendiği ekrana geçiş yapar.
        """
        self.ui_main.stackedWidget_1.setCurrentIndex(3)

    def back_to_warehouse_pagge(self):
        """
        Depo ekranına dönüş fonksiyonu
        """
        self.ui_main.stackedWidget_1.setCurrentIndex(2)
        self.ui_main.tabWidget.setCurrentIndex(1)

            
    def check_product_material(self):
        if self.aircraft_supplies_db.controller_product_exist(self.ui_main.product_for_material_comboBox.currentText(), self.ui_main.product_for_material_name_lineEdit.text()) is False:
            
            self.add_product_for_material()
        else:
            QMessageBox.critical(None, "Sistem", "Bu Ürün Zaten Mevcut")