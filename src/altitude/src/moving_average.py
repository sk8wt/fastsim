# The MovingAverage implements the concept of window in a set of measurements.
# The window_size is the number of most recent measurements used in average.
# The measurements are continuously added using the method add.
# The get_average method must return the average of the last window_size measurements.
class MovingAverage():

    def __init__(self, window_size):
        self.window = []
        self.window_scale = window_size

    # add a new measurement
    def add(self, val):
        self.window.append(val)

    # return the average of the last window_size measurements added 
    # or the average of all measurements if less than window_size were provided
    def get_average(self):
        avg = 0.0
        if (len(self.window) == 0):
                return avg
        if self.window_scale > len(self.window):
                for item in self.window:
                        avg += item
                avg /= len(self.window)
        else:
                for i in range(len(self.window)-1, len(self.window) - self.window_scale, -1):
                        avg += self.window[i]
                avg /= self.window_scale
        return avg

