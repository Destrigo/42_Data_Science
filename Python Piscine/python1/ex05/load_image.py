import cv2
import numpy as np


def ft_load(path: str) -> np.array:
    """
    You need to write a function that loads an image, prints its format,
    and its pixels content in RGB format.
    You have to handle, at least, JPG and JPEG format.
    You need to handle any error with a clear error message
    """
    image = cv2.imread(path)
    if image is None:
        raise AssertionError("Wrong image path")
    data = np.array(image)
    cv2.imshow("ex02", image)
    print(f"The shape of image is: {data.shape}")
    print(data)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return data
