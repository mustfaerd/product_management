import sqlite3
import multitasking

class OperationInformationDB:
    def __init__(self) -> None:
        self.connect = sqlite3.connect(r"X:\ORTAK\urun_kontrol\databases\time.db")
        #self.connect = sqlite3.connect("time.db")
        self.cursor = self.connect.cursor()
    
    def create_table(self):
        """
        Hat kayıt tablosu.
        """
        self.cursor.execute("Create table if not exists time_db ( ID, HAT, BAŞLAMA, BİTİŞ , SÜRE, NOTE)")
    
    def add_row(self,id, line, starting_date, end_date, time, note):
        """
        Veritabanına yeni hat alanı ekler.
        """
        self.cursor.execute("INSERT INTO time_db VALUES(?,?,?,?,?,?)",(id,line, starting_date, end_date, time,note))
        self.connect.commit()

    def update_line(self, starting_date, end_date, note, id, line):
        """
        Hat bilgilerini günceller.
        """
        self.cursor.execute("UPDATE time_db SET BAŞLAMA=?,BİTİŞ=?, NOTE=? WHERE ID= ? and HAT=?",(starting_date, end_date,note,id,line))
        self.connect.commit()
    
    def update_time(self,time,id,line):
        """
        Hesaplanan zamanı database ekler.
        """
        self.cursor.execute("UPDATE time_db SET SÜRE=? where ID=? and HAT=?",(time,id,line))
        self.connect.commit()
    
    def delete_row(self,id,line):
        """
        Seçilen hattı siler.
        """
        self.cursor.execute("DELETE From time_db where ID= ? and HAT= ?",(id,line))
        self.connect.commit()
    
    def update_line_names(self,new_line,line,id):
        """
        Hat isimlerini günceller.
        """
        self.cursor.execute("UPDATE time_db SET HAT=? where HAT=? and ID=?",(new_line,line, id))
        self.connect.commit()
    
    def get_line_info(self,id):
        """s
        Seri numarasına göre ürünün hat bilgilerini çeker.
        """
        data = self.send_request("Select HAT, BAŞLAMA, BİTİŞ, SÜRE, NOTE From time_db where ID= ?",(id,),data_request=True)
        try:
            return data
        except IndexError:
            return None
    
    @multitasking.task
    def send_request(self,request:str,parameters:tuple,data_request:bool=False):
        self.cursor.execute(request,parameters)
        if data_request:
            return self.cursor.fetchall()


# ben   = OperationInformationDB()
# ben.create_table()