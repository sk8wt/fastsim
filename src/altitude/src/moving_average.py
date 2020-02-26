# The MovingAverage implements the concept of window in a set of measurements.
# The window_size is the number of most recent measurements used in average.
# The measurements are continuously added using the method add.
# The get_average method must return the average of the last window_size measurements.
class MovingAverage():

    def __init__(self, window_size):
        #TODO 
        pass

    # add a new measurement
    def add(self, val):
        #TODO
        pass
     
    # return the average of the last window_size measurements added 
    # or the average of all measurements if less than window_size were provided
    def get_average(self):
        #TODO
        pass
