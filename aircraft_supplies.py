import sqlite3


class AircraftSuppliesDB:
    def __init__(self) -> None:
        self.connect = sqlite3.connect(r"X:\ORTAK\urun_kontrol\databases\aircraft_supplies.db")
        #self.connect = sqlite3.connect("aircraft_supplies.db")
        self.cursor = self.connect.cursor()

    def creat_table(self):
        self.cursor.execute("Create table if not exists Boran1 (MATERIAL TEXT, AMOUNT INT)")
        self.cursor.execute("Create table if not exists Boran2 (MATERIAL TEXT, AMOUNT INT)")
        self.cursor.execute("Create table if not exists Aybars1 (MATERIAL TEXT, AMOUNT INT)")
        self.cursor.execute("Create table if not exists Aybars2 (MATERIAL TEXT, AMOUNT INT)")

    def pull_data(self, model_name):
        self.cursor.execute(f"Select * From {model_name}")
        data = self.cursor.fetchall()
        return data
    
    def add_storage_material_number(self, modelname,number, name):
        self.cursor.execute(f"INSERT INTO {modelname} Values(?,?)", (number, name))
        self.connect.commit()

    def delete_product_for_material(self,modelname,name):
        self.cursor.execute(f"DELETE From {modelname} where MATERIAL = ?",(name,))
        self.connect.commit()

    def update_product_for_material(self,modelname,number,name):
        self.cursor.execute(f"Update {modelname} set AMOUNT = ? where MATERIAL = ?", (number, name))
        self.connect.commit()

    # def show_product_for_material(self,modelname,name)
    def product_search(self,modelname,name):
        self.cursor.execute(f"Select * From {modelname} where MATERIAL = ?",(name,))
        data = self.cursor.fetchall()
        try:
            return data
        except IndexError:
            return None

    def show_product_for_material(self,modelname):
        self.cursor.execute(f"Select MATERIAL, AMOUNT From {modelname}")
        data = self.cursor.fetchall()
        try:
            return data
        except IndexError:
            return None
        
    def check_product_exist(self, modelname,name):
        self.cursor.execute(f"Select MATERIAL From {modelname} where MATERIAL =  ?",(name,))
        data = self.cursor.fetchall()
        try:
            return data
        except IndexError:
            return None

    def controller_product_exist(self,modelname, name):
        if self.check_product_exist(modelname, name):
            return True
        else:
            return False
