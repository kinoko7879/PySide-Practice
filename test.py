from PySide2.QtGui import QImageReader
for image_fmt in QImageReader.supportedImageFormats():
    print(image_fmt.data().decode())
