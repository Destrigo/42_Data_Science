import cv2
import numpy as np
from load_image import ft_load


def main():
    """
    Create a program that should load the image "animal.jpeg",
    print some information
    about it and display it after "zooming".
    • The size in pixel on both X and Y axis
    • The number of channel
    • The pixel content of the image.
    • Display the scale on the x and y axis on the image
    If anything went wrong, the program must not stop abruptly
    and handle any error with a clear message.
    """
    print(ft_load("animal.jpeg"))
    image = cv2.imread("animal.jpeg")
    if image is None:
        raise AssertionError("Wrong image path")
    image = image[:400, :400, :]
    data = np.array(image)
    print(f"New shape after slicing: {data.shape}")
    print(data)
    cv2.imshow("ex03", data)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
