from PIL import Image
import os, sys
import glob
from tqdm import tqdm

root_dir = "prepareData/"
sucess = 0
corrupt = 0

for filename in tqdm(glob.iglob(root_dir + '**/*.jpg', recursive=True)):
    try:
        im = Image.open(filename)
        imResize = im.resize((256, 256), Image.ANTIALIAS)
        imResize.save(filename , 'JPEG', quality=90)
        sucess += 1
        
    except (IOError, SyntaxError) as e:
        os.remove(filename)
        corrupt += 1
        
print("sucessful: " + str(sucess))
print("coruppted: " + str(corrupt))
    