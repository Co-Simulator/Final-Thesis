import os
import warnings
import pandas as pd
import pandapower as pp


for file_name in os.listdir("G:\Project\Power_Grid\Case Files\MatPower files"):
    if file_name.endswith(".mat"):
        MAT_File = file_name
MAT_name = os.path.splitext(MAT_File)[0]
input_directory = os.path.dirname(os.path.realpath('__file__'))
net = pp.converter.from_mpc(os.path.join(input_directory, './' + MAT_File), casename_mpc_file = MAT_name)
warnings.filterwarnings('ignore')






