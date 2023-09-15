import sqlite3
import sys

class WareHouseDB:
	def __init__(self) -> None:
		self.connect = sqlite3.connect(r"X:\ORTAK\urun_kontrol\databases\warehouse_database.db")
		#self.connect = sqlite3.connect("warehouse_database.db")
		self.cursor = self.connect.cursor()

	def table_creat(self):
		self.cursor.execute("Create table if not exists warehouse_database (NAME TEXT, AMOUNT TEXT)")

	def add_value(self,  name, model):
		self.cursor.execute("INSERT INTO warehouse_database Values(?,?)", (name, model))
		self.connect.commit()
	
	def update_value(self, amount, name):
		self.cursor.execute("Update warehouse_database set AMOUNT = ? where NAME = ?", (amount, name))
		self.connect.commit()

	# def deneme(self):
	#     self.cursor.execute("Select * From warehouse_database")
	#     data = self.cursor.fetchall()
	#     try:
	#         print(data[0][1])
	#         return data[0][1]
	#     except IndexError:
	#         return None


	def all_warehouse(self,name):
		self.cursor.execute("Select NAME, AMOUNT From warehouse_database where NAME = ?",(name,))
		data = self.cursor.fetchall()
		try:
			return data
		except IndexError:
			return None
		
	def all_tableview_warehouse(self,name):
		self.cursor.execute("Select NAME, AMOUNT From warehouse_database where NAME = ?",(name,))
		data = self.cursor.fetchall()
		try:
			return data[0][1]
		except IndexError:
			return None
		
	def show_war(self):
		self.cursor.execute("Select NAME, AMOUNT From warehouse_database")
		data = self.cursor.fetchall()
		try:
			return data
		except IndexError:
			return None
		
	def show_warehouse_id(self,name):
		self.cursor.execute("Select NAME, AMOUNT From warehouse_database where NAME = ?",(name,))
		data = self.cursor.fetchall()
		try:
			return data
		except IndexError:
			return None

	def check_warehouse(self,name):
		if self.show_warehouse_id(name):
			return True
		else:
			return False
		
	def get_storage_material_number(self,name):
		self.cursor.execute("Select AMOUNT From warehouse_database where NAME = ?",(name,))
		product = self.cursor.fetchall()
		try:
			return int(product[0][0])
		except IndexError:
			return 0
		
	def warehouse_delete_material(self,name):
		self.cursor.execute("DELETE From warehouse_database where NAME = ?",(name,))
		self.connect.commit()
  
	def search_material(self, name):

		self.cursor.execute("Select NAME From warehouse_database where NAME = ?",(name,))
		data = self.cursor.fetchall()
		try:
			return data[0][0]
		except IndexError:
			return None

	def check_storage_exist(self,name):
		if self.search_material(name) is not None:
			return True
		else:
			return False  
	
	def get_missing_material(self,requirements:list)->list:
		missing_materials = []
		for material in requirements:
			if self.check_storage_exist(material[0]) is False:
				missing_materials.append(material[0])
		return missing_materials

