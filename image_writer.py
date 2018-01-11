import cv2
import queue
from threading import Thread
import uuid

class ImageWriter:
    """Write images to disk using a separate thread."""

    def __init__(self, queue: queue.Queue):

        # Initialize file queue
        self.file_queue = queue

        # Initialize thread stop indicator
        self.stopped = False

    def start(self):
        Thread(target=self.write, args=()).start()
        return self

    def write(self):
        # Infinitely loop unitl thread is stopped
        while True:

            # Stop thread if stop indicator has been triggered
            if self.stopped:
                return

            try:

                # Get next element in queue
                (name, image) = self.file_queue.get()

                # Generate output filename
                filename = "{}_{}.jpg".format(name.replace(" ", "_"), uuid.uuid4())

                # Write image to disk
                cv2.imwrite(filename, image)

            except queue.Empty:
                pass

    def stop(self):
        self.stopped = True