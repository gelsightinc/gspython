import os
import sys
sys.path.append('C:\\Users\\zhaoc\\source\\repos\\gspython')
from gspython import *
import matplotlib.pyplot as plt


def main():

    # Load a previously saved scan
    scanpath = 'C:\\Users\\Public\\Documents\\GelSight\\Scans\\Magnet_line_test_scans\\G500-001'
    sdata = readscan(scanpath)

    # Display the scan data
    print(sdata)

    # Display the scan images
    for im in sdata.images:
        image = plt.imread(im)
        plt.figure()
        plt.imshow(image)

    plt.show()

    ## load tmd file
    # basename = os.path.basename(scanpath)
    # basename += '.tmd'
    # fpath = os.path.join(scanpath, basename)
    # stmd = readtmd(fpath)
    # plt.figure()
    # plt.imshow(stmd[0])
    # plt.show()

if __name__ == "__main__":
    main()