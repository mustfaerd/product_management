from ui_main import Ui_MainWindow
from PySide2.QtWidgets import QApplication, QLineEdit
from interface import Products
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_screen = Products()
    main_screen.connect_buttons_to_events()
    main_screen.create_databases()
    main_screen.show()
    sys.exit(app.exec_())