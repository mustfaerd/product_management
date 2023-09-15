import sqlite3

class SignUpDB:
    def __init__(self) -> None:
        self.connect = sqlite3.connect(r"X:\ORTAK\urun_kontrol\databases\register.db")
        #self.connect = sqlite3.connect("register.db")
        self.cursor = self.connect.cursor()

    def create_table(self):
        """
        Tablo oluşturlur
        """
        self.cursor.execute("CREATE TABLE IF NOT EXISTS register (Username , Password , About, Security_Key )")
    
    
    def add_new_user(self, Username, Password, About, Security_Key):
        """
        kullanıcı kayıtları eklenir.
        """
        self.cursor.execute("INSERT INTO register VALUES(?,?,?,?)", (Username, Password, About,Security_Key))
        self.connect.commit()

    def check_username_exist(self, Username):
        """
        kullanıcı adı ve güvenlik kelimesi kontrol edilir.
        """
        if self.search_value(Username) is not None:
            return True
        else:
            return False

    def search_value(self, Username):
        """
        Değerler seçilir ve çekilir.
        """

        self.cursor.execute("Select Username TEXT From register where Username = ?",(Username,))
        data = self.cursor.fetchall()
        try:
            return data[0][0]
        except IndexError:
            return None 
        
    def get_Password(self, Password):
        """
        Şifrenin kontrol edilir.
        """
        self.cursor.execute("SELECT Password FROM users WHERE Password=?", (Password,))
        Password = self.cursor.fetchone()
        if Password:
            return Password[0]
        else:
            return None
    def search_user(self, Username):
        """
        Tablodaki verilerin kontrolü yapılır ve çekilme işlemleri yapılır.
        """
        self.cursor.execute("SELECT * FROM register WHERE Username=?", (Username,))
        user = self.cursor.fetchall()
        if user:
            return user
        else:
            return None
    

    def update_password(self, username, new_password):
        """
        Şifre güncelleme işlemleri yapılır.
        """
        self.cursor.execute("UPDATE register SET Password = ? WHERE Username = ?", (new_password, username))
        self.connect.commit()
   

