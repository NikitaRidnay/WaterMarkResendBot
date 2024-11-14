import cv2
import numpy as np
import easyocr

# Чтение изображения с помощью cv2
image = cv2.imread('test.jpeg')

# Инициализация OCR с помощью доступных языковых моделей
reader = easyocr.Reader(['en'])

# Чтение изображения с помощью OCR
result = reader.readtext('test.jpeg')

# Определение координат для прямоугольника
rectangle_coords = None

# Заданный альтернативный текст для прямоугольника
alternative_text = "@yourchannel"

# Получение размера и высоты альтернативного текста
text_width, text_height = cv2.getTextSize(alternative_text, cv2.FONT_HERSHEY_SIMPLEX, 1, 2)

# Проход по результатам распознавания текста
for detection in result:
    if 'Crypto_Sliv_Alliance' in detection[1]:
        rectangle_coords = detection[0]
        break

# Рисование блюра с текстом вместо прямоугольника
if rectangle_coords is not None:
    x1, y1, x2, y2 = rectangle_coords[0][0], rectangle_coords[0][1], rectangle_coords[2][0], rectangle_coords[2][1]
    # Добавление прямоугольного маски на изображение
    mask = np.zeros((y2 - y1, x2 - x1, 3), np.uint8)
    mask[:] = (255, 255, 255)
    image_with_mask = cv2.addWeighted(image, 1, mask, 1, 0)

    # Рисование блюра
    blur = cv2.blur(image_with_mask, (100, 100))
    cv2.addWeighted(blur, 1, image, 1, 0)

    # Добавление текста поверх блюра
    cv2.putText(image, alternative_text, (x1, y1 + text_height), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

# Сохранение изображения с изменениями
cv2.imwrite('bluredhhjjo.jpeg', image)
