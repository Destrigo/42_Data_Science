import cv2
import numpy as np


def ft_invert(array) -> np.array:
    """
    inverts like a photo negative
    """
    data = np.array(array)
    data = 255 - data
    cv2.imshow("invert", data)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return data


def ft_red(array) -> np.array:
    """Keep only the red channel."""
    red = np.array(array)
    red[:, :, 1] = 0  # remove green
    red[:, :, 0] = 0  # remove blue
    cv2.imshow("red", red)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return red


def ft_green(array) -> np.array:
    """Keep only the green channel."""
    green = np.array(array)
    green[:, :, 0] = 0  # remove blue
    green[:, :, 2] = 0  # remove red
    cv2.imshow("gren", green)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return green


def ft_blue(array) -> np.array:
    """Keep only the blue channel."""
    blue = np.array(array)
    blue[:, :, 1] = 0  # remove green
    blue[:, :, 2] = 0  # remove red
    cv2.imshow("blue", blue)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return blue


def ft_grey(array) -> np.array:
    """Convert to grayscale (average of RGB channels)."""
    grey = (
        0.2989 * array[:, :, 2] +  # Red channel
        0.5870 * array[:, :, 1] +  # Green channel
        0.1140 * array[:, :, 0]    # Blue channel
    )
    grey = grey.astype(np.uint8)
    cv2.imshow("grey", grey)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return np.stack((grey, grey, grey), axis=2)
