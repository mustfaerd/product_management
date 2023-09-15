from fixed_products import FixedProductsDB
from warehouse_database import WareHouseDB

class AllAircraft:

    def __init__(self):
        self.fixed = FixedProductsDB()
        self.warehouse = WareHouseDB()

    # def boranOne(self):W
    #     data = ["kamera", "kep", "kanat"]

    #     # for i in data:
    #     #     a = self.fixed.search_value_boran2(i)
    #     #     print(a)
    #     z = 0
    #     while z == len(data):
    #         for i in data:
    #             b = self.fixed.search_value_boran2(i)
    #             print(b)
    #         z += 1
    def update_material_number(self):
        if self.ui_main.new_product_name_comboBox.currentText() == "Boran 1":
            for material in self.boran_1:
                self.storage.update_storage_number(int(self.storage.get_storage_material_number(material))-int(self.boran_1[material]),material)
                print(self.boran_1[material])
        else:
            print("sdafssafasf")
        



ben = AllAircraft()
ben.boranOne()