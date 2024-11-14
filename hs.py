import cv2
import easyocr

trigger_words = ['@Crypto_Sliv_Alliance','@Crypto_Sliv_','@Crypto_Sliv_All','Sliv_Alliance', 'Sliv' , 'Alliance','@Crypto','T.ME/CRYPTOSHAURMA','CRYPTOSHAURMA']

def censor_and_replace_text(image_path, trigger_words, replacement_text):
    # инициализация OCR с помощью доступных языковых моделей
    reader = easyocr.Reader(['en'])
    replacement_text = '@dragonroes'

    # чтение изображения с помощью OCR
    result = reader.readtext(image_path)

    # инициализация cv2
    image = cv2.imread(image_path)
    watermark = cv2.imread('watermark.jpg')
    
    # определение координат для прямоугольника
    rectangle_coords = None

    # получение размера и высоты альтернативного текста
    text_width, text_height = cv2.getTextSize(replacement_text, cv2.FONT_HERSHEY_SIMPLEX, 1, 2)

    # проход по результатам распознавания текста
    for detection in result:
        for word in trigger_words:
            if word in detection[1]:
                rectangle_coords = detection[0]
                print('нужный текст найден!')
                break
        if rectangle_coords is not None:
            break

    # рисование черного прямоугольника для закрытия текста и написание альтернативного текста на нем
    if rectangle_coords is not None:
        # увеличение длины прямоугольника
        cv2.rectangle(image, rectangle_coords[0], (rectangle_coords[2][0] + 90, rectangle_coords[2][1]), (0, 0, 0), -1)
        cv2.putText(image, replacement_text, (rectangle_coords[0][0] - 50, rectangle_coords[1][1] + text_height), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

    # сохранение изображения с изменениями
    cv2.imwrite('censored_12' + image_path, image)

# пример использования функции
censor_and_replace_text('fortest.jpg', trigger_words, '@dragonroes')