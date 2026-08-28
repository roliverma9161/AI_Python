import cv2
# read image
img = cv2.imread('C:\\Users\\roliv\\OneDrive\\Desktop\\AI_Python\\data science', 1)
# height, width, number of channels in image

#dimension = img.shape
height = img.shape[0]
width = img.shape[1]
channels = img.shape[2]
size1 = img.size
print('Image Dimension : ',dimension)
print('Image Height: ',height)
print('Image Width: ',width)
print('Number of Channels : ',channels)
print('Image Size :', size1)
