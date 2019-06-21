# -*- coding: utf-8 -*-<
# ============= main.py ===============<

import sys
import os
import Qt
from main_ui import Ui_MainWindow


class ImageViewer(Qt.QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        try:
            super(ImageViewer, self).__init__(parent)
            # Get a reference to the window
            self.ui = Ui_MainWindow()

            # Init the window
            self.ui.setupUi(self)
            # Set the handler for
            btn_load_image = self.ui.pushButtonViewStart
            btn_load_image.clicked.connect(self.btn_load_image)

        except Exception as exc:
            print(exc)
            # self.console.log_err(exc)
            raise RuntimeError("ImageViewer.__init__")

    def btn_load_image(self):
        try:
            print("btn_load_image start")
            # Ask the user to select an image
            input_img_path = Qt.QtWidgets.QFileDialog.getOpenFileName()[0]
            print(input_img_path)

        except Exception as exc:
            print(exc)

            raise RuntimeError("btn_load_image")


def main(argv):
    try:
        # Create the application
        app = Qt.QtWidgets.QApplication(argv)
        window = ImageViewer()
        window.show()
        sys.exit(app.exec_())
    except Exception as exc:
        print(str(exc))
        raise RuntimeError("main")


if __name__ == "__main__":
    try:

        # Call the main function
        main(sys.argv)

    except Exception as exc:
        print(str(exc))
