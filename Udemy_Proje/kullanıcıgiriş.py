import sys
import sqlite3
from PyQt5 import QtWidgets

class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.baglanti_olustur()
        self.init_ui()

    def baglanti_olustur(self):
        baglanti = sqlite3.connect("database.db")
        self.cursor = baglanti.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS üyeler (kullanıcı_adı TEXT, parola TEXT)")
        baglanti.commit()

    def init_ui(self):
        self.kullanici_adi = QtWidgets.QLineEdit()
        self.parola = QtWidgets.QLineEdit()
        self.parola.setEchoMode(QtWidgets.QLineEdit.Password)
        self.giris = QtWidgets.QPushButton("Giriş Yap")
        self.kayit = QtWidgets.QPushButton("Kaydol")
        self.yazi_alani = QtWidgets.QLabel("")

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.kullanici_adi)
        v_box.addWidget(self.parola)
        v_box.addWidget(self.yazi_alani)
        v_box.addStretch()
        v_box.addWidget(self.giris)
        v_box.addWidget(self.kayit)

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)

        self.setWindowTitle("Kullanıcı Girişi")
        self.giris.clicked.connect(self.login)
        self.kayit.clicked.connect(self.sign_up)
        self.show()

    def login(self):
        adi = self.kullanici_adi.text()
        par = self.parola.text()
        self.cursor.execute("SELECT * FROM üyeler WHERE kullanıcı_adı = ? AND parola = ?", (adi, par))
        data = self.cursor.fetchall()

        if len(data) == 0:
            self.yazi_alani.setText("Böyle bir kullanıcı yok. Lütfen tekrar deneyin.")
        else:
            self.yazi_alani.setText("Hoşgeldiniz, " + adi)

    def sign_up(self):
        adi = self.kullanici_adi.text()
        par = self.parola.text()

        if adi and par:  # Check if username and password are not empty
            self.cursor.execute("SELECT * FROM üyeler WHERE kullanıcı_adı = ?", (adi,))
            data = self.cursor.fetchall()

            if len(data) == 0:
                self.cursor.execute("INSERT INTO üyeler (kullanıcı_adı, parola) VALUES (?, ?)", (adi, par))
                self.yazi_alani.setText("Kayıt işlemi başarılı. Hoşgeldiniz, " + adi)
                self.kullanici_adi.clear()
                self.parola.clear()
            else:
                self.yazi_alani.setText("Bu kullanıcı adı zaten kullanılıyor.")
        else:
            self.yazi_alani.setText("Kullanıcı adı ve parola boş bırakılamaz.")

app = QtWidgets.QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())
