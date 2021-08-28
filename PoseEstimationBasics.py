import cv2 as cv
import mediapipe as mp
import time

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()

cap =  cv.VideoCapture(0)
pTime=0
while True:
    success,img = cap.read()
    #resizeimg = cv.resize(img, (700,600), interpolation = cv.INTER_LINEAR)
    #resizeRGB = cv.cvtColor(resizeimg,cv.COLOR_BGR2RGB)
    #results = pose.process(resizeRGB)
    imgRGB = cv.cvtColor(img,cv.COLOR_BGR2RGB)
    results = pose.process(imgRGB)

    print(results.pose_landmarks)
    if results.pose_landmarks:
        #mpDraw.draw_landmarks(resizeimg,results.pose_landmarks,mpPose.POSE_CONNECTIONS)
        mpDraw.draw_landmarks(img,results.pose_landmarks,mpPose.POSE_CONNECTIONS)
        for id,lm in enumerate(results.pose_landmarks.landmark):
            #h, w , c = resizeimg.shape
            h, w , c = img.shape
            print(id,lm)
            cx,cy = int(lm.x*w),int(lm.y*h)



    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    #cv.putText(resizeimg,str(int(fps)),(70,50),cv.FONT_HERSHEY_PLAIN,3,(255,0,0),3)
    cv.putText(img,str(int(fps)),(70,50),cv.FONT_HERSHEY_PLAIN,3,(255,0,0),3)

    
    #cv.imshow("Video",resizeimg)
    cv.imshow("Video",img)


    cv.waitKey(1)


