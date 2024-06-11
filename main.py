import matplotlib.colors

from camera import CameraModel
import argparse
from utils import get_config_from_yaml
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


def generate_data(focal_length_min, focal_length_max, focal_length_binsize, start_distance, end_distance,
                  distance_binsize, pixel_size, x_resolution, y_resolution):

    focal_length_n_divisions = int((focal_length_max - focal_length_min) // focal_length_binsize)

    focal_lengths = np.linspace(start=focal_length_min, stop=focal_length_max, num=focal_length_n_divisions)

    dfs = {}

    df = None

    for focal_length in focal_lengths:

        print(focal_length, "focal_length")
        camera = CameraModel(f=focal_length, pixel_size=pixel_size, x_resolution=x_resolution,
                             y_resolution=y_resolution)

        distance_n_divisions = int((end_distance - start_distance) // distance_binsize)

        distances = np.linspace(start=start_distance, stop=end_distance, num=distance_n_divisions)

        lengths_rounded = []
        ppms = []
        ppms_rounded = []
        valid_distances = []
        for distance in distances:
            ppm = camera.get_pixels_for_meter_at_z(z=distance)
            print(ppm)
            if ppm > 0.5:
                nearest_pixel = np.ceil(ppm)
                length_rounded = nearest_pixel / ppm
                lengths_rounded.append(length_rounded)
                ppms.append(ppm)
                ppms_rounded.append(nearest_pixel)
                valid_distances.append(distance)

        focal_length_entries = [round(focal_length*1e3,1) for _ in range(len(ppms))]
        if df is None:
            ppm_col = {"z(m)": valid_distances, f"Rounded Lengths (m)": lengths_rounded,
                       f"PPM": ppms, f"PPM_rounded": ppms_rounded, f"f": focal_length_entries}
            df = pd.DataFrame(ppm_col)
        else:
            # df[f"Rounded Lengths (m)"] = pd.Series(lengths_rounded,
            #                                        index=distances)
            #
            # df[f"PPM"] = pd.Series(ppms, index=distances)
            #
            # df[f"PPM_rounded"] = pd.Series(ppms_rounded, index=distances)
            # df[f"f"] = pd.Series(focal_length_entries, index=distances)

            ppm_col = {"z(m)": valid_distances, f"Rounded Lengths (m)": lengths_rounded,
                       f"PPM": ppms, f"PPM_rounded": ppms_rounded, f"f": focal_length_entries}
            df2 = pd.DataFrame(ppm_col)
            df = pd.concat([df, df2])

        dfs[focal_length] = df
        print(df["Rounded Lengths (m)"])

    print(df.head())
    sns.relplot(
        data=df, kind="scatter",
        x="z(m)", y="Rounded Lengths (m)", hue="f", palette="Set1"
    )

    plt.show()

    return df


if __name__ == "__main__":
    config, _ = get_config_from_yaml("config/config.yaml")

    print(config)

    generate_data(focal_length_min=config.focal_length_min, focal_length_max=config.focal_length_max,
                  focal_length_binsize=config.focal_length_binsize, start_distance=config.distance_start,
                  end_distance=config.distance_end,
                  distance_binsize=config.distance_binsize, pixel_size=config.pixel_size,
                  x_resolution=config.resolution[0], y_resolution=config.resolution[1])
