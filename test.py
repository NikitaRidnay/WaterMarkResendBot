import pytesseract
import cv2

# Read the image
img = cv2.imread('test.jpeg') 

# Check if the image is read correctly
if img is None:
    print('Could not read the image')
    exit()

# Convert the image to RGB format
img_2RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Configuration for Tesseract
config = ("--psm 6 --oem 3 -c tessedit_char_whitelist=@#-_ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")

# Get the data from the image
text = pytesseract.image_to_data(img_2RGB, config=config)

# Extract the text
text_data = ''
for i, el in enumerate(text.splitlines()):
    if i != 0:        
        el = el.split()
        try:
            # Get the text
            x, y, w, h = int(el[6]), int(el[7]), int(el[8]), int(el[9])
            text_ = pytesseract.image_to_string(img_2RGB[y:y+h, x:x+w], config=config)
            text_data += text_ + '\n'
        except:
            pass

print("Extracted Text:")
print(text_data)

# Check if the text "@Crypto_Sliv_Alliance" is present
if "Alliance" in text_data:
    print("Text found")
    
    # Find the coordinates of the text
    for i, el in enumerate(text.splitlines()):
        if i != 0:        
            el = el.split()
            try:
                # Get the text
                x, y, w, h = int(el[6]), int(el[7]), int(el[8]), int(el[9])
                text_ = pytesseract.image_to_string(img_2RGB[y:y+h, x:x+w], config=config)
                
                if text_ == "Alliance":
                    # Draw the red rectangle
                    cv2.rectangle(img, (x, y), (w + x, h + y), (0, 0, 255), 2)
                    cv2.imwrite('edited.jpeg', img)

                    break
                
            except:
                pass
    
else:
    print("Text not found")

# Save the edited image