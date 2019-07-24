import perlin
import math
from PIL import Image
import numpy as np
import tqdm
import os

test_frame = False
num_frames = 100
ms_per_frame = 40
resolution = 600
v_length = 3.0
scale = 0.07
radius = 0.475
offset = 12
output_dir = "frames"


def field_vector_at(x, y, rot):
    radian = 2.0*math.pi*rot
    xv = perlin.noise(x*scale, y*scale, radius*math.cos(radian)+offset, radius*math.sin(radian))
    yv = perlin.noise(x*scale, y*scale + 128, radius*math.cos(radian)+offset, radius*math.sin(radian))
    return round(xv, 4), round(yv, 4)


if not os.path.isdir(output_dir):
    os.mkdir(output_dir)

frame_path_list = []


for frame in tqdm.tqdm(range(num_frames)):
    buffer = np.zeros(shape=[resolution, resolution, 3], dtype='uint8')
    # Draw operations go here

    lo_bound = int(1.0*resolution/8.0)
    hi_bound = int(7.0*resolution/8.0)
    rotation = frame/num_frames

    for i in tqdm.tqdm(range(lo_bound, hi_bound, 2)):
        for j in range(lo_bound, hi_bound, 2):
            #  Start tracing field vector path from this point
            x, y = i, j
            for v in range(200):
                xd, yd = field_vector_at(x, y, rotation)
                x += xd
                y += yd
                if x >= resolution or y >= resolution or x < 0 or y < 0:
                    continue
                ix, iy = int(x), int(y)
                if buffer[ix][iy][1] < 255:
                    buffer[ix][iy][1] += 3
                elif buffer[ix][iy][0] < 255:
                    buffer[ix][iy][0] += 2

    img = Image.fromarray(buffer)
    frame_path_list.append(output_dir+"\\f-{:0>8d}.png".format(frame))
    img.save(frame_path_list[-1])
    if test_frame:
        break
if not test_frame:
    # THIS DOES NOT WORK RIGHT NOW. The program will terminate with an error after the last frame is rendered.
    # For now, use ImageMagick with the following command:
    # convert f-*.png -delay 2 -loop 0 final.gif
    img = Image.new("RGB", resolution)
    first_frame = Image.open(output_dir+"f-00000000.png")
    img.paste(first_frame.copy())
    img.save("final.gif", format="GIF", append_images=frame_path_list[1:], duration=frame_duration, loop=0, optimize=True)
