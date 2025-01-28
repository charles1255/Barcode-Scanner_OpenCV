import cv2
from pyzbar import pyzbar

def decode_barcode(frame):
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        x, y, w, h = barcode.rect
        # Draw rectangle around the barcode
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        barcode_data = barcode.data.decode('utf-8')
        barcode_type = barcode.type
        # Display the barcode data and type
        text = f'{barcode_data} ({barcode_type})'
        cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    return frame


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    
    frame = decode_barcode(frame)

    
    cv2.imshow('Barcode/QR Code Scanner', frame)

    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
