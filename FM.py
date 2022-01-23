import cv2
import cvzone
import mediapipe as mp
from cvzone.FaceMeshModule import FaceMeshDetector

cap = cv2.VideoCapture(0)
detector = FaceMeshDetector(maxFaces=1)
while True:
    success, img = cap.read()
    img, faces = detector.findFaceMesh(img, draw=False)

    if faces:
        face = faces[0]
        pointLeft = face[145]
        pointRight = face[374]
        #The below codes of line i.e line 18 to locate the left eye,line 20 to locate the right eye and
        # line 22 is to draw line between two eyes.
        #cv2.circle(img, pointLeft, 5, (255, 0, 255),cv2.FILLED)
        #cv2.circle(img, pointRight, 5, (255, 0, 255), cv2.FILLED)
        #cv2.line(img, pointLeft, pointRight, (0, 255, 0), 3)
        #Finding the distance between the two eyes
        w, _ = detector.findDistance(pointLeft, pointRight)
        W = 6.3
        #finding the focal length
        #d = 50
        #f = (w*d)/W
        #print(f)

        #Finding the distance
        f = 840
        distance = (W*f)/w
        print(distance)
        #displaying the distance that are measured on the top of the face
        cvzone.putTextRect(img, f"Distance: {int(distance)}cm", (face[10][0]-100, face[10][1]-50), scale=2)


    #Displaying the livewebcam
    cv2.imshow("kk", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
