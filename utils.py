import numpy as np
import pandas as pd
from dotmap import DotMap
import yaml



def get_config_from_yaml(yml_file):
    """
    Get the config from a yml file
    :param yml_file:
    :return: config(namespace) or config(dictionary)
    """
    # parse the configurations from the config json file provided
    with open(yml_file, "r") as config_file:
        config_dict = yaml.load(config_file, Loader=yaml.FullLoader)

    # convert the dictionary to a namespace using bunch lib
    config = DotMap(config_dict)

    return config, config_dict



