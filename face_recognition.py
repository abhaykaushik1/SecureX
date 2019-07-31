import cv2
import pickle
import time
from datetime import datetime, timedelta
import LockFinal
import new_email
import SecurityGUI

SEEN_FACE = False


def run_face_recognition():
    global SEEN_FACE
    face_cascade = cv2.CascadeClassifier(
        'cascades/data/haarcascade_frontalface_alt2.xml')
    # eye_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_eye.xml')

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("trainer.yml")

    with open("labels.pickle", "rb") as f:
        og_labels = pickle.load(f)
        labels = {v:k for k,v in og_labels.items()}

    cap = cv2.VideoCapture(0)

    while not SEEN_FACE:
        # Capture Frame by frame
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5,
                                              minNeighbors=5)
        for (x, y, w, h) in faces:
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]

            # recognize this
            id_, conf = recognizer.predict(roi_gray)
            if 45 <= conf <= 85:
                print(id_)
                print(labels[id_])
                font = cv2.FONT_HERSHEY_SIMPLEX
                name = labels[id_]
                color = (255, 255, 255)
                stroke = 2
                cv2.putText(frame, name, (x,y), font, 1, color, stroke,
                            cv2.CV_8S)
                if name == "abhay-kaushik":
                    SEEN_FACE = True
                    continue
            img_itm = "10.jpeg"
            cv2.imwrite(img_itm, roi_color)

            color = (255, 0, 0)
            stroke = 2
            end_cord_x = x+w
            end_cord_y = y+h
            cv2.rectangle(frame, (x,y), (end_cord_x,end_cord_y), color, stroke)

        # Display the resulting frame
        cv2.imshow('frame', frame)
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break

        time.sleep(5)
        # When everything is done, release the capture.
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    path = LockFinal.get_file()
    if not path.endswith(".acs"):
        path = LockFinal.encrypt(path)
    #SecurityGUI.display()
    run_face_recognition()
    if SEEN_FACE:
        file_path = LockFinal.decrypt(path)
        new_email.send_email('Login Detected', 'Abhay Kaushik')
