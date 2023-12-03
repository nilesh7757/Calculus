import cv2 as cv
import numpy as np

# cv.imshow('gr',gray)

def res(frame,scale=0.60):
    width = int(frame.shape[1]*scale)
    length =int(frame.shape[0]*scale)
    dimension = (width,length)
    return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)
img = cv.imread('Image/D.jpeg')
resize = res(img)   
cv.imshow('color',resize)
gray = cv.cvtColor(resize,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)
blur = cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
cv.imshow('blur',blur)
canny = cv.Canny(blur,100,80)
cv.imshow('canny',canny)
cv.waitKey(0)
