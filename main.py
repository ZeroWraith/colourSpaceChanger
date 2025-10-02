import cv2 as cv
import numpy as np

def togrey(img):
    cv.imshow("Orignal Image",img)
    img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    cv.imshow("Greyscale",img) 
    cv.waitKey(0)
    cv.destroyAllWindows()

def tohsv(img):
    cv.imshow("Orignal Image",img)
    img = cv.cvtColor(img,cv.COLOR_BGR2HSV)
    cv.imshow("HSV",img) 
    cv.waitKey(0)
    cv.destroyAllWindows()

def tolab(img):
    cv.imshow("Orignal Image",img)
    img = cv.cvtColor(img,cv.COLOR_BGR2Lab)
    cv.imshow("LAB",img) 
    cv.waitKey(0)
    cv.destroyAllWindows()
    
def torgb(img):
    cv.imshow("Orignal Image",img)
    img = cv.cvtColor(img,cv.COLOR_BGR2RGB)
    cv.imshow("RGB",img) 
    cv.waitKey(0)
    cv.destroyAllWindows()



src=input("ENter the path to the image: ")
img = cv.imread(src)


while True:
    print ("Choose an opetion --")
    print("1. Greyscale ")
    print("2. HSV")
    print("3. CIELAB")
    print("4. RGB")
    print("5. Quit")
    choice = int(input("Enter your Choice: "))
    
    match choice:
        case 1:
            togrey(img)         
            
        case 2:
            tohsv(img) 
        case 3:
            tolab(img)
        case 4:
            torgb(img)
        case 5:
            break
            cv.destroyAllWindows()