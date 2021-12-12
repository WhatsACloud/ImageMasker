import PIL.Image
import io

def getJpegSize(fileName): #where f is a file opened with the function open()
    with open(fileName, "rb") as f:
        content = f.read()
        return content.index(bytes.fromhex('FFD9'))+2 #extra 2 to account for ffD9, which is 2 bytes long

def coverData(fileName, data):
    print("covering data")
    with open(fileName, "ab") as f:
        f.write(data)
        f.close()

def extractData(fileName):
    print("extracting data...")
    with open(fileName, "rb") as f:
        f.seek(getJpegSize(fileName))
        return f.read()

def readImg(image):
    img = PIL.Image.open(image)
    byteArr = io.BytesIO()
    img.save(byteArr, format="PNG")
    return byteArr.getvalue()

def createImageFromData(data):
    newImg = PIL.Image.open(io.BytesIO(data))
    newImg.save("newImage.png")

def removeData(fileName):
    with open(fileName, "ab") as f:
        f.truncate(getJpegSize(fileName))

if __name__ == '__main__':
    image = "fieldImage.jpeg"
    image2 = "balloonsImage.png"
    #coverData(image, b"test")
    #extractData(image)
    """img = readImg(image2)
    coverData(image, img)
    createImageFromData(extractData(image))"""
    removeData(image)
    print(extractData(image))