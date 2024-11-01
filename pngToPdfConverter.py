import aspose.words as aw
import os

for file in os.listdir("outputFiles"):
    os.remove("outputFiles/" + file)

destination = input("Enter desired destination: ")
keepOgFiles = input("Keep original files? (y/n): ")

if keepOgFiles.lower() == "y":
    keepOgFiles = True
else:
    keepOgFiles = False

if destination == "downloads":
    destination = "C:/Users/jackz/Downloads/"

if os.listdir(destination):
    pass

for file in os.listdir("filesToConvert"):
    doc = aw.Document()
    builder = aw.DocumentBuilder(doc)
    builder.insert_image("filesToConvert/" + file)
    filenameWithoutExtension = file.replace(".png", "")
    doc.save(destination + "/" + filenameWithoutExtension + "_converted.pdf")
    if not keepOgFiles:    
        os.remove("filesToConvert/" + file)