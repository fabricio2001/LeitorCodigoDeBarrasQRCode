import cv2
from pyzbar import pyzbar

if (False):

    cap = cv2.VideoCapture(0)

    while True:

        ret, img = cap.read()

        barcodes = pyzbar.decode(img)
        code = len(barcodes)

        if (code != 0):
            for barcode in barcodes:
                (x, y, w, h) = barcode.rect
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
                barcodeData = barcode.data.decode("utf-8")
                barcodeType = barcode.type
                text = "{} ({})".format(barcodeData, barcodeType)
                cv2.putText(img, text, (x, y - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
                print("Type: {}".format(barcodeType))
                print("Data: {}".format(barcodeData))

        cv2.imshow("img", img)
        if cv2.waitKey(1) == 27:
            break

else:
    path = "barcode.png"
    img = cv2.imread(path)

    barcodes = pyzbar.decode(img)
    code = len(barcodes)

    if (code != 0):
        for barcode in barcodes:
            (x, y, w, h) = barcode.rect
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
            barcodeData = barcode.data.decode("utf-8")
            barcodeType = barcode.type
            text = "{} ({})".format(barcodeData, barcodeType)
            cv2.putText(img, text, (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
            print("Type: {}".format(barcodeType))
            print("Data: {}".format(barcodeData))

    cv2.imshow("Image", img)
    cv2.waitKey(0)


cv2.destroyAllWindows()
