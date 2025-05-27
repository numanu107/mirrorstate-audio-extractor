from PIL import Image
import numpy as np

img = Image.open("Image Name").convert("RGB")
data = np.array(img)

cell_size = 388
start_x = 2 * cell_size
start_y = 2 * cell_size
block_size = 4 * cell_size

mp3_block = data[start_y:start_y + block_size, start_x:start_x + block_size, :]
mp3_bytes = mp3_block.flatten().tobytes()

with open("extracted.mp3", "wb") as f:
    f.write(mp3_bytes)
