import view, model, sys, traceback
from PyQt6.QtWidgets import QApplication


class Controller:
    """
    Klasse die sich um die Kommunikation zwischen dem Model und der View kümmert
    """

    def __init__(self, to_classify_dir: str = "/home/phillip/PycharmProjects/the_opssat_case_starter_kit/to_classify"):
        self.view = view.View(self)
        self.model = model.Model(to_classify_dir)
        self.view.setNextImage(self.model.next())
        """
        self.pb_agricultural.clicked.connect(c.agr)
        self.pb_cloud.clicked.connect(c.clo)
        self.pb_mountain.clicked.connect(c.mou)
        self.pb_natural.clicked.connect(c.nat)
        self.pb_none.clicked.connect(c.non)
        self.pb_river.clicked.connect(c.riv)
        self.pb_sea_ice.clicked.connect(c.sea)
        self.pb_snow.clicked.connect(c.sno)
        self.pb_water.clicked.connect(c.wat)
        """

    def wat(self):
        self.model.put_current_into('Water')
        self.view.setNextImage(self.model.next())

    def sno(self):
        self.model.put_current_into('Snow')
        self.view.setNextImage(self.model.next())

    def sea(self):
        self.model.put_current_into('Sea_ice')
        self.view.setNextImage(self.model.next())

    def riv(self):
        self.model.put_current_into('River')
        self.view.setNextImage(self.model.next())

    def non(self):
        self.view.setNextImage(self.model.next())

    def nat(self):
        self.model.put_current_into('Natural')
        self.view.setNextImage(self.model.next())

    def mou(self):
        try:
            print('here')
            self.model.put_current_into('Mountain')
            self.view.setNextImage(self.model.next())
            print('there')
        except Exception as e:
            traceback.print_exc(e)

    def clo(self):
        self.model.put_current_into('Cloud')
        self.view.setNextImage(self.model.next())

    def agr(self):
        self.model.put_current_into('Agricultural')
        self.view.setNextImage(self.model.next())

if __name__ == '__main__':
    try:
        to_classify_dir = sys.argv[1]
        # pass
    except Exception: # weil value error mit dem parsen vom port und dem Fall das der user nur "python main.py" macht
        print('Usage works like this: python controller.py <to_classify_dir>\n')
        sys.exit(1)
    app = QApplication([])
    c = Controller()
    c.view.show()
    sys.exit(app.exec())
