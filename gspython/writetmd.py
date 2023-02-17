import os
import numpy as np
import struct
import argparse
import cv2
import readtmd


def writetmd(fpath, heightMap, mmpp):

    pdir = os.path.dirname(os.path.abspath(fpath))
    if not os.path.exists(pdir) or not fpath.lower().endswith('.tmd'):
        return None

    cols = heightMap.shape[1]
    rows = heightMap.shape[0]

    with open(fpath, "wb") as fd:
        fd.write('Binary TrueMap Data File v2.0'.encode())
        fd.write('\r'.encode())
        fd.write('\n'.encode())
        fd.write(bytearray([0]))
        fd.write(bytearray([0]))

        # image size
        fd.write(struct.pack('i', cols))
        fd.write(struct.pack('i', rows))

        # length and width of axes
        fd.write(struct.pack('f', mmpp*cols))
        fd.write(struct.pack('f', mmpp*rows))

        # offset
        fd.write(struct.pack('f', mmpp * 0.0))
        fd.write(struct.pack('f', mmpp * 0.0))

        # Write matrix
        for y in range(rows):
            rdata = heightMap[y,:]
            fd.write(struct.pack('f'*len(rdata), *rdata))

    return True

#
#
#
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('inputfile', action='store', help='Input a yaml file')
    arguments = parser.parse_args()
    
    hm, hdata = readtmd.readtmd(arguments.inputfile)

    writetmd('test.tmd', hm, hdata.mmpp)
   
  
