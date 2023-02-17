import os
import gspython
import matplotlib.pyplot as plt

def main():

    # Load a previously saved scan
    scanpath = os.path.dirname("./testdata/Dime/")
    sdata = gspython.readscan(scanpath)

    # Display the scan data
    print(sdata)

    # Display the scan images
    for im in sdata.images:
        image = plt.imread(im)
        plt.figure()
        plt.imshow(image)

    plt.show()

if __name__ == "__main__":
    main()