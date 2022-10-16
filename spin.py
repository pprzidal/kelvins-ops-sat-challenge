import os
from PIL import Image

def main():
    pwd = os.path.dirname(__file__)
    realdir = os.path.join(pwd, 'ops_sat_competiton_official_training')
    sheesh = os.listdir(realdir)
    for dir in sheesh:
        if os.path.isdir(os.path.join(realdir, dir)):
            sheesh2 = os.listdir(os.path.join(realdir, dir))
            print(sheesh2)
            for file in sheesh2:
                if file.endswith('.png'):
                    with Image.open(os.path.join(os.path.join(realdir, dir), file)) as pngfile:
                        for angle in [90, 180, 270]:
                            rotated_file = pngfile.rotate(angle)
                            rotated_file.save(os.path.join(os.path.join(realdir, dir), file.replace('.png', f'_{angle}.png')))

if __name__ == '__main__':
    main()