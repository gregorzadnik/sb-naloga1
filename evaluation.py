import os
from glob import glob
from LBP import return_histogram


path = ".\\awe"
image_paths = [y for x in  os.walk(path) for y in glob(os.path.join(x[0], '*.png'))]
classes = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[], 10:[] }
for ix, image_path in enumerate(image_paths):
    histogram = return_histogram(image_path)
    index = int(image_path[-6:-4])
    classes[index].append(histogram)
    print(ix)

for key, value in classes.items():
    print(f"{key}: {len(value)}")
