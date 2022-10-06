import os, requests, sys, threading
import time


def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

DATA_FOLDER_NAME = 'ops_sat_competiton_official'

def main():
    stop = False
    # pwd = project working directory
    pwd = os.path.dirname(__file__)
    print(f"Assuming {pwd} as Project directory")
    data_path = os.path.join(pwd, DATA_FOLDER_NAME)
    try:
        os.mkdir(data_path)
    except FileExistsError:
        print("seems like the directory already exists")
        # TODO make eingabe ob ordner löschen und von neu beginnen?
    print(f"Created data path{os.linesep}Downloading zip file ", end="")
    def loop():
        while not stop:
            print('.', end='')
            time.sleep(0.1)
    def download():
        r = requests.get('https://zenodo.org/record/6524750/files/ops_sat.zip?download=1')
        with open(f'{DATA_FOLDER_NAME}/downloadedZip.zip', 'wb') as f:
            f.write(r.content)
    th = threading.Thread(target=loop)
    th2 = threading.Thread(target=download)
    th.start()
    th2.start()
    # To save to a relative path.
    th2.join()
    stop = True
    th.join()
    os.system({
        'linux': f"unzip {data_path}/downloadedZip.zip -d {data_path}",
        'windows': f"Expand-Archive -Path {data_path}/downloadedZip.zip -DestinationPath {data_path}"
    }[sys.platform.lower()])


if __name__ == '__main__':
    main()