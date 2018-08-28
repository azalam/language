import os
import shutil

sounds = ['a', 'b', 'c', 'd', 'e', 'ey', 'f', 'g', 'h', 'i', 'iy', 'j', 'k', 'l', 'm', 'n', 'o', 'ow', 'p', 'q', 'r', 's', 't', 'u', 'uw', 'v', 'w', 'x', 'y', 'z']


def make_dirs():
    for s in sounds:
        os.makedirs(s)
        if s in ['ey', 'iy', 'ow', 'uw']:
            continue
        if s not in ['e', 'i', 'o', 'u']:
            os.makedirs(2 * s)


def remove_dirs():
    a = input('Are you sure?: (Y/n) ')
    if a in ['y', 'Y', 'yes', 'Yes']:
        for s in os.listdir():
            if os.path.isdir(s):
                shutil.rmtree(s)
    else:
        return


if __name__ == '__main__':
    pass
    # make_dirs()
    # remove_dirs()
