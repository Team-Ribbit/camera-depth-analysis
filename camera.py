import numpy as np


class CameraModel():
    def __init__(self, f, pixel_size, x_resolution, y_resolution):
        self.f = f
        self._DATUM = 1  # 1m
        self.pixel_size = pixel_size  # how long each pixel is in meters
        self.ppm = 1 / pixel_size

    def get_pixels_for_meter_at_z(self, z):
        """
        calculate how man pixels would 1 meter be given z distance
        :param z:
        :return:
        """
        if z < self._minimum_distance_to_meter():
            pixels = np.NaN
        else:
            pixels = self.f * (self._DATUM / z) * self.ppm

        return pixels

    def _minimum_distance_to_meter(self):
        """
        Calculate the minimum distance to see 1 meter based on the current field of view
        :return:
        """
        pass

        return 0


"""
at a given distance, what is the error at different zooms

x - distance (z)
y - error of z (m)
- PPM integer error
- The actual error on the bboxes for each distance (for now, keep it at 60% at all distances, but it should be a vector that becomes configurat)
- worst case scenario assumption 


for each error, you get pixe error, you multiply by ppm, and result is three different meter errors

Each different instances of the line would be different focal lengths
3 different plots

"""
