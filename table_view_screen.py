from PySide2.QtCore import QAbstractTableModel,Qt

class TableModel(QAbstractTableModel):

    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self._data[0])
    
    def headerData(self, section, orientation, role):
        if role==Qt.DisplayRole and orientation==Qt.Horizontal:
            if section==0:
                return "Malzeme"
            elif section == 1:
                return "Adet"
        return super().headerData(section, orientation, role)




class Products_TableModel(QAbstractTableModel):

    def __init__(self, data):
        super().__init__()
        self._data = data

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self._data[0])

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                value = self._data[index.row()][index.column()]
                return str(value)
            
    # def setData(self, index, value, role):
    #     if role == Qt.EditRole:
    #         data=list(self._data[index.row()])
    #         data[index.column()]=str(value)
    #         self._data[index.row()]=tuple(data)
    #         return True
    def headerData(self, section, orientation, role):
        if role==Qt.DisplayRole and orientation==Qt.Horizontal:
            if section==0:
                return "SERİ NUMARASI"
            elif section == 1:
                return "AD"
            elif section == 2:
                return "MODEL"
        return super().headerData(section, orientation, role)

    def flags(self, index):
        return Qt.ItemIsSelectable | Qt.ItemIsEnabled
    


class Products_Info_TableModel(QAbstractTableModel):

    def __init__(self, data):
        super().__init__()
        self._data = data

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        if len(self._data) > 0:
            return len(self._data[0])
        else:
            return 0

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole or role == Qt.EditRole:
                value = self._data[index.row()][index.column()]
                return str(value)
            
    def setData(self, index, value, role):
        if role == Qt.EditRole:
            data=list(self._data[index.row()])
            data[index.column()]=str(value)
            self._data[index.row()]=tuple(data)
            return True

    def flags(self, index):
        return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            if section == 0:
                return "HAT"
            elif section == 1:
                return "BAŞLANGIÇ"
            elif section == 2:
                return "BİTİŞ"
            elif section == 3:
                return "SÜRE"
            elif section == 4:
                return "NOT"
        return super().headerData(section, orientation, role)
    