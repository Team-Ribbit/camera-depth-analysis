import numpy as np

class CameraModel():
    def __init__(self, f):
        self.f = f
        self._DATUM = 1 # 1m


    def get_ppm(self, z):
        """
        calculate how man pixels would 1 meter be given z distance
        :param z:
        :return:
        """
        if z < self._minimum_distance_to_meter():
            pixels =  np.NaN
        else:
            pixels = self.f * (self._DATUM / z)
        
        return pixels

    def _minimum_distance_to_meter(self):
        """
        Calculate the minimum distance to see 1 meter based on the current field of view
        :return:
        """
        pass

        return 0






