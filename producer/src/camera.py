import cv2


class MP4File():
    def __init__(self) -> None:
        self.capture = None
        self.name = 'stream'
        self._file_path = 'rtsp://stream-simulator:8554/media'
        self._start_frame = 0


    @property
    def url(self):
        return self._file_path


    def setup(self):
        self.set_capture()
        self.set_start_frame()


    def set_capture(self):
        self.capture = cv2.VideoCapture(self.url)


    def set_start_frame(self):
        self.capture.set(cv2.CAP_PROP_POS_FRAMES, self._start_frame)


    def get_timestamp(self):
        return self.capture.get(cv2.CAP_PROP_POS_MSEC) / 1000.0


    def read(self):
        return self.capture.read()


    def stop(self) -> None:
        self.capture.release()
