import cv2
from PIL import Image

image_path = 'face.jpg'
cat_face_cascade = cv2.CascadeClassifier \
    ('haarcascade_frontalface_default.xml')
image = cv2.imread(image_path)
cat_face = cat_face_cascade.detectMultiScale(image)
print(cat_face)
cat = Image.open(image_path)
glasses = Image.open('facemask2.png')
mask = Image.open('mask.png')
cat = cat.convert("RGBA")
glasses = glasses.convert("RGBA")
for (x, y, w, h) in cat_face:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 1)
    glasses = glasses.resize((w+15, int(h / 2)))
    cat.paste(glasses, (x-15, int(y + h / 8)), glasses)
    mask = mask.resize((w + 25, int(h - 80)))
    cat.paste(mask, (x - 15, int(y + h - 200)), mask)
    cat.save("cat_with_glasses.png")
    cat_with_glasses = cv2.imread("cat_with_glasses.png")
    cv2.imshow("Cat_with_glasses", cat_with_glasses)
    cv2.waitKey()
cv2.imshow("Cat", image)
cv2.waitKey()
