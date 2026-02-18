import imageio.v3 as iio

#list that contain images
filenames = [
    "pic1.jpg",
    "pic2.jpg"
]

#will be used to store the actual image from these files
images = [
    
]

#The .imread() method loads an image based on the file path. 
# So now, our images variable has all the images!
for filename in filenames:
    images.append(iio.imread(filename))
    
    
#lastlpy use the imwrite to create the gif
#This takes in four arguments:
"""
'team.gif': This is the name you want to give to your new GIF file.
images: The list containing the image data.
duration = 500: How long each picture should show in the GIF, in milliseconds.
loop = 0: How many times the GIF should repeat (0 means it keeps looping forever).
"""

iio.imwrite("gen&ian.gif", images, duration = 5, loop = 0)