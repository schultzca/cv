import cv2
from threading import Thread


class WebcamVideoStream:

    def __init__(self, src=0):
        # initialize video stream and capture first frame
        self.stream = cv2.VideoCapture(src)
        (self.grabbed, self.frame) = self.stream.read()

        # initialize variable that indicates if thread should be stopped
        self.stopped = False


    def start(self):
        # set thread stop indicator to false
        self.stopped = False

        # start thread to read frames from video stream
        Thread(target=self.update, args=()).start()
        return self

    def update(self):
        # keep looping infinitely until thread is stopped
        while True:

            # if thread indicator variable is set stop the thread
            if self.stopped:

                # release the video stream
                self.stream.release()

                return

            # otherwise, read the next frame from the stream
            (self.grabbed, self.frame) = self.stream.read()

    def read(self):
        # return the most recently read frame
        return self.frame

    def stop(self):
        # indicate the thread should be stopped
        self.stopped = True