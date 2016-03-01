from utils import *
import re

inputDir = "in/"
outputDir = "out/"
format = "ICON" # SCREENSHOT or ICON for now

files = list_of_files(inputDir)

for f in files:
    imageFile = inputDir + f

    fileregex = re.compile('(.*)\.(png|jpg)$', re.IGNORECASE)

    if fileregex.findall(f):

        name = fileregex.findall(f)[0][0]
        ext = fileregex.findall(f)[0][1]

        print "resizing: " + f

        if format == "SCREENSHOT":
            ## Create screenshots for iPhone 3.5
            i = resize_to_width(imageFile, 640, 960)
            save_to_file(i, outputDir + "/" + name + "-iphone-3.5." + ext)

            ## Create screenshots for iPhone 4.0
            i = resize_to_width(imageFile, 640, 1136)
            save_to_file(i, outputDir + "/" + name + "-iphone-4.0." + ext)

            ## Create screenshots for iPhone 4.7
            i = resize_to_width(imageFile, 750, 1334)
            save_to_file(i, outputDir + "/" + name + "-iphone-4.7." + ext)

            ## Create screenshots for iPhone 5.5
            i = resize_to_width(imageFile, 1242, 2208)
            save_to_file(i, outputDir + "/" + name + "-iphone-5.5." + ext)

        if format == "ICON":
            i = resize_to_width(imageFile, 120, 120)
            save_to_file(i, outputDir + "/" + name + "-60@2x." + ext)

            i = resize_to_width(imageFile, 180, 180)
            save_to_file(i, outputDir + "/" + name + "-60@3x." + ext)

            i = resize_to_width(imageFile, 76, 76)
            save_to_file(i, outputDir + "/" + name + "-76." + ext)

            i = resize_to_width(imageFile, 152, 152)
            save_to_file(i, outputDir + "/" + name + "-76@2x." + ext)

            i = resize_to_width(imageFile, 29, 29)
            save_to_file(i, outputDir + "/" + name + "-Small-29." + ext)

            i = resize_to_width(imageFile, 58, 58)
            save_to_file(i, outputDir + "/" + name + "-Small-29@2x-1." + ext)

            i = resize_to_width(imageFile, 58, 58)
            save_to_file(i, outputDir + "/" + name + "-Small-29@2x." + ext)

            i = resize_to_width(imageFile, 87, 87)
            save_to_file(i, outputDir + "/" + name + "-Small-29@3x." + ext)

            i = resize_to_width(imageFile, 40, 40)
            save_to_file(i, outputDir + "/" + name + "-Small-40." + ext)

            i = resize_to_width(imageFile, 80, 80)
            save_to_file(i, outputDir + "/" + name + "-Small-40@2x-1." + ext)

            i = resize_to_width(imageFile, 80, 80)
            save_to_file(i, outputDir + "/" + name + "-Small-40@2x." + ext)

            i = resize_to_width(imageFile, 120, 120)
            save_to_file(i, outputDir + "/" + name + "-Small-40@3x." + ext)

print "done"
