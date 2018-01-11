"""Take pictures using Webcam and write them to disk"""

import cv2
import queue

from image_writer import ImageWriter
from webcam import WebcamVideoStream


def main():

    # Create file queue
    file_queue = queue.Queue()

    # Initialize video stream
    vs = WebcamVideoStream(src=0).start()

    # Initialize image writer
    ir = ImageWriter(queue=file_queue).start()

    name = input("Please enter name of individual: ")

    while True:

        # Read most recent video frame
        frame = vs.read()

        # Copy frame to display and annotate
        frame_copy = frame.copy()

        # Overlay name to frame
        cv2.putText(frame_copy, name, (25, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2, cv2.LINE_AA)

        # Display current frame
        cv2.imshow("Video", frame_copy)

        # Send frame to image writer thread
        key = cv2.waitKey(1) & 0xFF

        # Enter new name
        if key == ord("n"):
            name = input("Please enter name of individual: ")

        # Capture picture and write to disk
        if key == ord("p"):
            file_queue.put((name, frame))

        # Quit application
        if key == ord("q"):
            cv2.destroyAllWindows()
            break

    # Stop the image writing thread
    ir.stop()

    # Stop the video stream thread
    vs.stop()


if __name__ == "__main__":
    main()