import cv2
import face_recognition
import pickle
import os

folderPath = 'Images'

if not os.path.exists(folderPath):
    print(f"Folder '{folderPath}' does not exist.")
    exit(1)

pathList = os.listdir(folderPath)
imgList = []
studentIds = []

print("Loading Images...")

for path in pathList:
    if path.endswith(('.png', '.jpg', '.jpeg')):
        imgPath = os.path.join(folderPath, path)
        img = cv2.imread(imgPath)

        if img is not None:
            imgList.append(img)
            studentIds.append(os.path.splitext(path)[0].strip())
        else:
            print(f"Failed to load: {path}")

print("Student IDs found:", studentIds)
print(f"Image shape: {img.shape}, dtype: {img.dtype}")

def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        if img is None:
            print("Image is None, skipping.")
            continue

        if img.shape[2] == 4:
            img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

        # Convert kareg BGR se RGB
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Ensure dtype is uint8 (error aaskta he )
        if img_rgb.dtype != 'uint8':
            img_rgb = img_rgb.astype('uint8')

        # dekhega shape he  (H, W, 3)
        if len(img_rgb.shape) != 3 or img_rgb.shape[2] != 3:
            print(f"Skipping image due to unsupported shape: {img_rgb.shape}")
            continue

        # b/w chack
        if len(img_rgb.shape) == 2:
            print("Image is grayscale, converting to RGB.")
            img_rgb = cv2.cvtColor(img_rgb, cv2.COLOR_GRAY2RGB)

        encodes = face_recognition.face_encodings(img_rgb)

        if encodes:
            encodeList.append(encodes[0])
        else:
            print("No face found in one image. Skipping.")
    return encodeList



print("Encoding Started...")
encodeListKnown = findEncodings(imgList)
encodeListKnownWithIds = [encodeListKnown, studentIds]
print("Encoding Complete")

try:
    with open("EncodeFile.p", 'wb') as file:
        pickle.dump(encodeListKnownWithIds, file)
    print("EncodeFile.p saved successfully.")
except Exception as e:
    print(f"Error saving EncodeFile.p: {e}")

