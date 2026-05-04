import cv2
import numpy as np
from load_image import ft_load


def ft_transpose3d(image: list) -> list:
    """
    Transpose a 3D list (swap height and width axes).
    """
    h, w, c = len(image), len(image[0]), len(image[0][0])
    return [[[image[y][x][ch] for ch in range(c)] for y in range(h)]
            for x in range(w)]


def main():
    """
    Make a program which must load the image "animal.jpeg",
    cut a square part from it
    and transpose it to produce the image below.
    It should display it, print the new shape
    and the data of the image after the transpose.
    """
    print(ft_load("animal.jpeg"))
    image = cv2.imread("animal.jpeg")
    if image is None:
        raise AssertionError("Wrong image path")
    image = image[:400, :400, :]
    data = np.array(ft_transpose3d(image))
    print(f"New shape after Transpose: {data.shape}")
    print(data)
    cv2.imshow("ex04", data)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
