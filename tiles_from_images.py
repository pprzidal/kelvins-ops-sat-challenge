import os, random, uuid

from PIL import Image

images_dir = "/home/phillip/PycharmProjects/the_opssat_case_starter_kit/images"
OUTDIR = "/home/phillip/PycharmProjects/the_opssat_case_starter_kit/to_classify"

def main(seed=42):
    random.seed(seed)
    target_width, target_height = 200, 200
    pics = os.listdir(images_dir)
    for pic in pics:
        with Image.open(os.path.join(images_dir, pic)) as pngfile:
            width, height = pngfile.size
            for i in range(100):
                w, h = random.uniform(0, 1), random.uniform(0, 1)
                prob_w, prob_h = min(w * width, width - 200), min(h * height, height - 200)
                img = pngfile.crop((prob_w, prob_h, prob_w + target_width, prob_h + target_height))
                img.save(os.path.join(OUTDIR, uuid.uuid4().__str__() + '.png'))
    print(pics)
    """
    with Image.open(os.path.join(os.path.join(realdir, dir), file)) as pngfile:
        for angle in [90, 180, 270]:
            rotated_file = pngfile.rotate(angle)
            rotated_file.save(os.path.join(os.path.join(realdir, dir), file.replace('.png', f'_{angle}.png')))
    """

if __name__ == '__main__':
    main()