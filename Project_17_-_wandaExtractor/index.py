from PIL import Image
from PIL.ExifTags import TAGS


#loading the image to be scrapped
image = Image.open("img.jpg")


#this line scraps the metadata from the image
exifdata = image.getexif()


#a loop to iterate through all the tags presents in the image metadata and log to display
for tagid in exifdata:
    #getting tag name 
    tagname = TAGS.get(tagid, tagid)

    #after getting tag ID, we get its respective value
    value = exifdata.get(tagid)

    #displaying the collected data
    print(f"{tagname:25}: {value}")