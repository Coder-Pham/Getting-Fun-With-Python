'''Vid2Pi_Image
This is an improvement from Img2DOCX

Result's resolution = Source's resolution / 4 
'''

import os
import time

from mpmath import mp, pi
from PIL import Image, ImageDraw, ImageFont

from cv2 import (CAP_PROP_FPS, CAP_PROP_FRAME_COUNT, VideoCapture, VideoWriter,
                 imread, imwrite, destroyAllWindows)


def render_image(frame_no, number):
    count = time.time()

    source = Image.open(frame_no)
    source = source.rotate(0, expand=1)
    width, height = source.size

    # Create new
    result = Image.new('RGB', (width, height), color=(255, 255, 255))
    fnt = ImageFont.truetype('calibri.ttf', 7)

    # Resize
    width = int(width // 4)
    height = int(height // 4)
    source = source.resize((width, height))

    # Prepare for PI constant
    mp.dps = (height * width)
    pi = str(+mp.pi)

    # Process pixels
    draw = ImageDraw.Draw(result)
    for y in range(height):
        for x in range(width):
            r, g, b = source.getpixel((x, y))
            try:
                draw.text((x*4, y*4), pi[y*width + x],
                          font=fnt, fill=(r, g, b))
            except IndexError as error:
                # Debug only
                print('Length of PI: {}'.format(len(pi)))
                print('Error place: {}'.format(y*width + x))

    result.save(frame_no)
    print('Render frame {} in {:0.5f}s'.format(number, time.time() - count))


def main():
    # Get frame from video
    video = input('Video file: ')
    vidcap = VideoCapture(video)

    print('Total frame: {}'.format(vidcap.get(CAP_PROP_FRAME_COUNT)))
    print('Printing frames ...')

    success, image = vidcap.read()
    count = 1
    if success:
        if not os.path.isdir('Frame'):
            os.makedirs('Frame')
    else:
        print("Can't find video file")
        exit()

    while success:
        imwrite(os.path.join("Frame", "%d.jpg" % count),
                image)     # save frame as JPEG file
        success, image = vidcap.read()
        count += 1
    print("Done printing")

    # Render every frame
    frames = os.listdir("Frame")
    frames.sort(key=lambda name: int(name.split('.')[0]))
    for frame in frames:
        render_image(os.path.join("Frame", frame), frame.split('.')[0])

    # Write video
    structure = imread(os.path.join("Frame", frames[0]))
    height, width, layers = structure.shape
    vidwrite = VideoWriter(
        'result.AVI', -1, vidcap.get(CAP_PROP_FPS), (width, height))
    for frame in frames:
        img = imread(os.path.join("Frame", frame))
        vidwrite.write(img)

    cv2.destroyAllWindows()
    vidwrite.release()


if __name__ == '__main__':
    os.system('cls')
    count = time.time()
    main()
    print('Total time: {:0.5f}s\n'.format(time.time() - count))
    chose = input("Do you want to delete old frames[Y/N]: ")
    if (chose.upper() == "Y"):
        frames = os.listdir("Frame")
        for frame in frames:
            os.remove(os.path.join("Frame", frame))
    else:
        input('')
