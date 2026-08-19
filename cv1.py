#importing the opencv module 
import cv2 
# using imread('path') and 0 denotes read as grayscale image and 1 for rgb Image 
img = cv2.imread("C:\\Users\\roliv\\Downloads\\WhatsApp Image 2024-08-05 at 7.15.14 PM (1).jpeg") 
#This is using for display the image 
cv2.imshow("image",img) 
cv2.waitKey(0) # This is necessary to be required so that the image doesn't close immediately. 
#It will run continuously until the key press. 
cv2.destroyAllWindows()