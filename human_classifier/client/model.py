import os
import socket
import threading


class Model:
    """
    Kümmert sich um die Verbindung zum GameServer und gibt diesem die Eingabe des Benutzers
    und schickt diesem Meldungen des Servers.
    """

    def __init__(self, to_classify_dir: str = "/home/phillip/PycharmProjects/the_opssat_case_starter_kit/to_classify", dst_dir: str = "/home/phillip/PycharmProjects/the_opssat_case_starter_kit/ops_sat_competiton_official_training"):
        self.pointer = -1
        self.files = os.listdir(to_classify_dir)
        self.to_classify_dir = to_classify_dir
        self.dst_dir = dst_dir

    def next(self):
        if self.pointer == len(self.files):
            return None
        self.pointer += 1
        return os.path.join(self.to_classify_dir, self.files[self.pointer])

    def put_current_into(self, where: str):
        os.replace(os.path.join(self.to_classify_dir, self.files[self.pointer]), os.path.join(self.dst_dir, where) + '/' + self.files[self.pointer])
