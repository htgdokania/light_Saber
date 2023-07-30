import cv2
import numpy as np

def convert_image_to_2d_array(image_path, target_size):
    # Step 1: Load the image using OpenCV
    img = cv2.imread(image_path)

    # Step 2: Resize the image to the desired size
    img_resized = cv2.resize(img, target_size)
    # converting BGR to RGB
    img_resized = cv2.cvtColor(img_resized, cv2.COLOR_BGR2RGB)

    cv2.imshow("image",img_resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return img_resized
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Example usage:
    image_path = '/Users/harshdokania/Downloads/POVLightsaber-master/POVLightsaber/vadergray.png'
    target_size = (117, 144)  # Replace with your desired size (width, height)
    resulting_array = convert_image_to_2d_array(image_path, target_size)
    count =0

    print("{", end="")
    for k in range(len(resulting_array)):
        row=resulting_array[k]
        print("{",end="")
        for j in range(len(row)) :
            print("{",end="")
            ele=row[j]
            for i in range (len(ele)) :
                if(i<len(ele)-1):
                    print(ele[i],end=",")
                else:
                    print(ele[i], end="")
            if(j < len(row)-1):
                print("}",end=",")
            else:
                print("}", end="")
        if(k<len(resulting_array)-1):
            print("}",end=",\n")
        else:
            print("}", end="")
    print("}", end="")

