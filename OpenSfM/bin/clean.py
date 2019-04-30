import  numpy as np
from open3d import *
import sys
import os

path = sys.argv[1]
dr = os.path.join(os.path.abspath(os.path.dirname(path)),'cleaned.ply')
pcd = read_point_cloud(path)

cl,ind = statistical_outlier_removal(pcd,
            nb_neighbors=100, std_ratio=0.001)
#cl,ind = statistical_outlier_removal(cl,
#            nb_neighbors=30, std_ratio=0.05)

write_point_cloud(dr, cl)
