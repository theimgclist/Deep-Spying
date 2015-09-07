__author__ = 'Tony Beltramelli www.tonybeltramelli.com - 04/09/2015'

from Sensor import *


class Gyroscope(Sensor):
    def __init__(self, path, view):
        Sensor.__init__(self, base_path=path, file_path="{}gyroscope.csv".format(path), view=view)

        self.sampling_rate = 62500
        self.median_filter_window_size = 9
        self.filter_type = "lowpass"
        self.process_variance_q = 1e-05
        self.measurement_variance_estimate = 1e-02

        Sensor.process(self, merge_axis=False)

