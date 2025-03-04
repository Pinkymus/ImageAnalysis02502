import cv2
import numpy as np
from skimage.util import img_as_float
from skimage.filters import threshold_otsu

def show_in_moved_window(win_name, img, x, y):
    """
    Show an image in a window, where the position of the window can be given
    """
    cv2.namedWindow(win_name)
    cv2.moveWindow(win_name, x, y)
    cv2.imshow(win_name, img)

def capture_from_camera_and_show_images():
    print("Starting image capture")

    print("Opening connection to camera")
    url = 0
    use_droid_cam = True
    if use_droid_cam:
        url = "http://10.209.125.207:4747/video"
    cap = cv2.VideoCapture(url)
    # cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()

    print("Starting camera loop")
    # Get first image
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame")
        exit()

    stop = False

    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame_float = img_as_float(frame_gray)
    thres = threshold_otsu(frame_float)

    while not stop:
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame. Exiting ...")
            break

        # Transform image to gray scale and then to float, so we can do some processing
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame_float = img_as_float(frame_gray)


        thres = 0.05 * threshold_otsu(frame_float) + 0.95 * thres

        threshholding = np.vectorize(lambda x: 0.0 if x < thres else 1.0)

        thres_img = threshholding(frame_float)

        # Display the resulting frame
        show_in_moved_window("Input", frame, 0, 10)
        show_in_moved_window("Difference image", thres_img, 1200, 10)

        if cv2.waitKey(1) == ord("q"):
            stop = True

    print("Stopping image loop")
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    capture_from_camera_and_show_images()
