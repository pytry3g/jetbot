import cv2


cascade_face = "./haarcascades/haarcascade_frontalface_alt.xml"
cascade = cv2.CascadeClassifier(cascade_face)

def detect(img):
    """Detect face to be given image.

    Argument:
        img (Image) : image

    Return:
        img (Image) : image
    """
    detected = cascade.detectMultiScale(img)
    for (x, y, w, h) in detected:
        # Write rectangle on the detected face.
        cv2.rectangle(img, (x, y), (x+w, y+h), pink)
    return img
