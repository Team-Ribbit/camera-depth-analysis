from camera import CameraModel
import argparse
from utils import get_config_from_yaml
import numpy as np
import pandas as pd


def generate_data(focal_length_min, focal_length_max, focal_length_binsize , end_distance,distance_binsize):


    focal_length_n_divisions = int((focal_length_max - focal_length_min) // focal_length_binsize)

    
    focal_lengths = np.linspace(start=focal_length_min, stop=focal_length_max, num=focal_length_n_divisions)

    df = None

    # print(focal_length_min, focal_length_max)
    
    # print(focal_lengths)
    
    for focal_length in focal_lengths:
        print(focal_length, "focal_length")
        ppms = []
        camera = CameraModel(f=focal_length)

        distance_n_divisions = int(end_distance // distance_binsize)


        distances = np.linspace(start=1, stop=end_distance, num=distance_n_divisions)

        for distance in distances:
            print(distance)
            ppm = camera.get_ppm(z=distance)
            print("ppm",ppm)
            ppms.append(ppm)

        print(f"{focal_length}", ppms)
        ppm_col = {focal_length: ppms}
        if df is None:
            df = pd.DataFrame(ppm_col)
            df.index = distances
        else:
            df[focal_length] = pd.Series(ppms, index=distances)

    
    print(df)
    return df


    

    

if __name__ == "__main__":
    config, _ = get_config_from_yaml("config/config.yaml")


    print(config)


    generate_data(focal_length_min=config.focal_length_min, focal_length_max=config.focal_length_max, focal_length_binsize=config.focal_length_binsize, end_distance=config.distance, distance_binsize=config.distance_binsize)


