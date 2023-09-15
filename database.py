import sqlite3
import multitasking
from PySide2.QtCore import QObject,Signal

class ProductInformationDB(QObject):
    get_data_signal = Signal(list)
    def __init__(self) -> None:
        super().__init__()
        # self.connect = sqlite3.connect(r"X:\ORTAK\urun_kontrol\databases\product_management.db")
        # #self.connect = sqlite3.connect("product_management.db")
        # self.cursor = self.connect.cursor()
        pass

    def table_create(self):
        """
        Ürün bilgi tablosunu oluşturur.
        """
        self.cursor.execute("Create table if not exists product_database (ID, MODEL, TYPE)")

    def add_product_value(self, id,model ,type):
        """
        Tabloya yeni veri ekler.
        """
        self.cursor.execute("INSERT INTO product_database Values(?,?,?)", (id, model, type))
        self.connect.commit()

    def update_product_type(self,model_type):
        self.cursor.execute("UPDATE product_database SET TYPE=? WHERE MODEL=?", (model_type))
        self.connect.commit()


    def search_product_value(self, id):
        """
        ID numarasından ürün arar.
        """
        self.cursor.execute("Select ID From product_database where ID = ?",(id,))
        data = self.cursor.fetchall()
        try:
            return data[0][0]
        except IndexError:
            return None
    
    def check_product_id_exist(self,id):
        """
        Gelen parametrenin kaydını kontrol eder.
        """
        if self.search_product_value(id) is not None:
            return True
        else:
            return False  

    def get_product_by_id(self,id):
        """
        Ürün ID numarasına tablodaki verileri çeker.
        """
        self.cursor.execute("Select ID, MODEL, TYPE From product_database where  ID = ?",(id,))
        data = self.cursor.fetchall()
        try:
            return data
        except IndexError:
            return None
    
    
    def get_products_by_name(self,model):
        """
        Ürün ismine göre ürünün detaylarını çeker.
        """
        #self.cursor.execute("Select ID, MODEL, TYPE From product_database where  MODEL = ?",(model,))
        data = self.send_request("Select ID, MODEL, TYPE From product_database where  MODEL = ?",(model,),data_request=True)
        
        try:
            return data
        except IndexError:
            return None
        
    def check_exist_product_name(self,name):
        """
        Gelen parametrenin kaydını kontrol eder.
        """
        if self.get_products_by_name(name):
            return True
        else:
            return False
    
    @multitasking.task
    def send_request(self,request:str,parameters:tuple,data_request:bool=False):
        with SQLite(r"X:\ORTAK\urun_kontrol\databases\product_management.db") as cur:
            #print(cur.execute(request,parameters).fetchall())
            data = cur.execute(request,parameters).fetchall()
            self.get_data_signal.emit(data)
            return data

class SQLite():
    def __init__(self, file='sqlite.db'):
        self.file=file
    def __enter__(self):
        self.conn = sqlite3.connect(self.file)
        return self.conn.cursor()
    def __exit__(self, type, value, traceback):
        self.conn.commit()
        self.conn.close()

