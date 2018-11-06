import cv2
import numpy as np

def isInThePicture(img,x,y):
    [size_x,size_y] = img.shape
    return ((x >= 0 ) and (x <= size_x) and (y >= 0 ) and (y <= size_y))

def isIn (arr, x,y):
    [[a,b]] = np.isin([[x,y]],arr)
    return a and b

def findAllNeaghbor(img, x, y):
    count = 0
    [size_x,size_y] = img.shape
    checked_queue = []
    one_queue = []
    one_queue.append([x,y])
    pixel_size=1
    row = len(one_queue)
    cv2.namedWindow('image',cv2.WINDOW_NORMAL)
    cv2.resizeWindow('image', 960,540)
    img[x,y] = 200
    while(count != row): 
        [x,y] = one_queue[count]
        img[x,y] = 200
        for i in [-pixel_size, pixel_size]:
            for j in [-pixel_size,pixel_size]:

                if (isInThePicture(img,x,y+j))  and (([x,y+j] in one_queue) ==False) and (img[x,y+j] == 0):
                    one_queue.append([x,y+j])
                if (isInThePicture(img,x+i,y))  and (([x+i,y] in one_queue) ==False) and (img[x+i,y] == 0):
                    one_queue.append([x+i,y])

        count = count +1
        row = len(one_queue)
        cv2.imshow("image", img)
        cv2.waitKey(1)
    cv2.destroyAllWindows
    return count
        
#img = cv2.imread("./1_cluster.png",0)
#img = cv2.imread('./multi_clusters.png',0)
#img = cv2.imread("./1_cluster2.png",0)
img = cv2.imread('./multi2.png',0)
clusterNumber = 0
area = 0
[x,y] = img.shape
for i in range(x):
    for j in range(y):
        if img[i,j] == 0:
            area = area + findAllNeaghbor(img,i,j)
            clusterNumber = clusterNumber +1

print("The area of the cluster is: ", area)
print('The number of cluster is: ', clusterNumber)

