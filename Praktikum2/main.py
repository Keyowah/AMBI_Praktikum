from tkinter import filedialog as tkf
from tkinter import Tk
import numpy as np
from tempfile import TemporaryFile
np.set_printoptions(threshold=np.inf)

Tk().withdraw() # Wir wollen kein Tk-Fenster haben, sondern nur den filedialog für die Dateiauswahl im Explorer


def main(*args, **kwargs):
    """
    hi
    """    
    inppath = "C:/Users/Elias/Desktop/AMBI/AMBI_Praktikum/Praktikum2/aquifex-tRNA.fasta"
    prepro = [line.rstrip('\n') for line in open(inppath, 'r', encoding='utf-8')]
    seqlist = []
    for i in range(1, len(prepro), 3):
        seqlist.append(prepro[i]+prepro[i+1])
    #D1, D2 = build_matrices(seqlist)
    D1 = np.array([[ 0., 15., 15., 35., 41., 34., 34., 31., 27., 40., 29., 52., 32.,
        29., 22., 27., 47., 47., 42., 42., 40., 43., 41., 27., 22., 29.,
        29., 31., 24., 25., 23., 25., 46., 44., 38., 40., 41., 33., 27.,
        27., 23., 49., 20., 18.],
       [15.,  0.,  0., 34., 38., 32., 34., 27., 27., 45., 25., 45., 42.,
        44., 18., 24., 39., 39., 39., 34., 41., 40., 35., 28., 22., 35.,
        25., 29., 26., 21., 21., 18., 44., 39., 34., 40., 38., 26., 28.,
        21., 23., 43., 19., 16.],
       [15.,  0.,  0., 34., 38., 32., 34., 27., 27., 45., 25., 45., 42.,
        44., 18., 24., 39., 39., 39., 34., 41., 40., 35., 28., 22., 35.,
        25., 29., 26., 21., 21., 18., 44., 39., 34., 40., 38., 26., 28.,
        21., 23., 43., 19., 16.],
       [35., 34., 34.,  0., 20., 20., 20., 35., 33., 36., 30., 41., 34.,
        35., 32., 27., 27., 27., 38., 38., 40., 42., 39., 28., 31., 28.,
        33., 28., 36., 31., 31., 32., 43., 45., 43., 40., 45., 31., 39.,
        31., 24., 45., 34., 30.],
       [41., 38., 38., 20.,  0., 12., 16., 45., 33., 52., 40., 35., 44.,
        43., 41., 43., 28., 28., 40., 40., 41., 44., 42., 42., 38., 26.,
        41., 30., 39., 34., 45., 34., 42., 44., 45., 38., 46., 31., 48.,
        32., 40., 43., 40., 43.],
       [34., 32., 32., 20., 12.,  0., 12., 36., 34., 37., 37., 42., 27.,
        29., 34., 34., 24., 24., 41., 44., 39., 46., 46., 31., 29., 26.,
        32., 30., 33., 33., 37., 35., 47., 45., 41., 42., 45., 26., 33.,
        29., 31., 47., 34., 31.],
       [34., 34., 34., 20., 16., 12.,  0., 33., 37., 32., 38., 41., 31.,
        30., 29., 32., 24., 24., 43., 44., 44., 40., 43., 28., 26., 20.,
        28., 33., 32., 37., 40., 35., 43., 43., 40., 42., 40., 28., 37.,
        30., 29., 42., 33., 32.],
       [31., 27., 27., 35., 45., 36., 33.,  0., 35., 34., 27., 40., 33.,
        29., 25., 24., 53., 53., 40., 43., 37., 44., 44., 26., 28., 31.,
        19., 32., 30., 35., 35., 33., 48., 44., 37., 46., 37., 30., 29.,
        21., 23., 48., 30., 29.],
       [27., 27., 27., 33., 33., 34., 37., 35.,  0., 40., 32., 35., 26.,
        26., 29., 33., 36., 36., 44., 44., 44., 48., 45., 33., 32., 36.,
        40., 27., 37., 33., 32., 32., 47., 50., 37., 41., 40., 28., 37.,
        34., 33., 48., 29., 28.],
       [40., 45., 45., 36., 52., 37., 32., 34., 40.,  0., 39., 39., 34.,
        32., 35., 32., 52., 52., 42., 44., 41., 44., 44., 36., 40., 34.,
        32., 36., 32., 44., 37., 43., 45., 34., 33., 38., 35., 27., 39.,
        42., 29., 42., 37., 40.],
       [29., 25., 25., 30., 40., 37., 38., 27., 32., 39.,  0., 46., 31.,
        34., 21., 22., 46., 46., 42., 42., 40., 41., 42., 22., 25., 38.,
        25., 33., 31., 22., 25., 20., 49., 46., 44., 44., 45., 37., 38.,
        24., 21., 46., 27., 24.],
       [52., 45., 45., 41., 35., 42., 41., 40., 35., 39., 46.,  0., 43.,
        43., 43., 44., 45., 45., 44., 46., 44., 52., 46., 45., 41., 44.,
        43., 39., 44., 42., 51., 40., 52., 54., 42., 43., 47., 39., 45.,
        41., 47., 53., 43., 42.],
       [32., 42., 42., 34., 44., 27., 31., 33., 26., 34., 31., 43.,  0.,
         7., 21., 34., 44., 44., 38., 37., 43., 44., 38., 32., 31., 36.,
        36., 28., 33., 45., 29., 43., 47., 44., 40., 39., 43., 15., 30.,
        44., 35., 44., 31., 29.],
       [29., 44., 44., 35., 43., 29., 30., 29., 26., 32., 34., 43.,  7.,
         0., 19., 29., 46., 46., 37., 35., 39., 44., 36., 31., 31., 35.,
        33., 29., 36., 45., 29., 44., 46., 44., 35., 40., 39., 17., 32.,
        43., 36., 46., 31., 29.],
       [22., 18., 18., 32., 41., 34., 29., 25., 29., 35., 21., 43., 21.,
        19.,  0., 16., 43., 43., 38., 40., 42., 44., 41., 23., 15., 31.,
        23., 29., 29., 20., 23., 17., 47., 47., 40., 44., 40., 29., 25.,
        17., 25., 47., 20., 17.],
       [27., 24., 24., 27., 43., 34., 32., 24., 33., 32., 22., 44., 34.,
        29., 16.,  0., 46., 46., 38., 42., 39., 40., 42., 24., 19., 34.,
        24., 34., 30., 23., 21., 23., 47., 43., 38., 44., 39., 35., 31.,
        20., 21., 41., 28., 25.],
       [47., 39., 39., 27., 28., 24., 24., 53., 36., 52., 46., 45., 44.,
        46., 43., 46.,  0.,  0., 44., 46., 46., 44., 47., 39., 44., 23.,
        46., 37., 44., 39., 48., 37., 47., 48., 45., 36., 45., 37., 44.,
        40., 47., 46., 47., 43.],
       [47., 39., 39., 27., 28., 24., 24., 53., 36., 52., 46., 45., 44.,
        46., 43., 46.,  0.,  0., 44., 46., 46., 44., 47., 39., 44., 23.,
        46., 37., 44., 39., 48., 37., 47., 48., 45., 36., 45., 37., 44.,
        40., 47., 46., 47., 43.],
       [42., 39., 39., 38., 40., 41., 43., 40., 44., 42., 42., 44., 38.,
        37., 38., 38., 44., 44.,  0., 33., 15., 17., 33., 43., 36., 43.,
        41., 43., 38., 42., 40., 45., 52., 45., 54., 51., 45., 40., 39.,
        38., 40., 30., 43., 39.],
       [42., 34., 34., 38., 40., 44., 44., 43., 44., 44., 42., 46., 37.,
        35., 40., 42., 46., 46., 33.,  0., 34., 34.,  2., 44., 41., 41.,
        44., 41., 46., 37., 39., 42., 52., 45., 49., 46., 45., 38., 42.,
        39., 41., 45., 42., 39.],
       [40., 41., 41., 40., 41., 39., 44., 37., 44., 41., 40., 44., 43.,
        39., 42., 39., 46., 46., 15., 34.,  0., 30., 33., 43., 42., 42.,
        41., 44., 42., 44., 44., 44., 55., 55., 49., 51., 51., 41., 40.,
        36., 41., 41., 46., 41.],
       [43., 40., 40., 42., 44., 46., 40., 44., 48., 44., 41., 52., 44.,
        44., 44., 40., 44., 44., 17., 34., 30.,  0., 33., 42., 41., 43.,
        39., 47., 41., 42., 39., 45., 45., 42., 48., 48., 42., 44., 44.,
        42., 40., 27., 45., 42.],
       [41., 35., 35., 39., 42., 46., 43., 44., 45., 44., 42., 46., 38.,
        36., 41., 42., 47., 47., 33.,  2., 33., 33.,  0., 46., 42., 42.,
        45., 42., 47., 39., 40., 42., 52., 46., 49., 46., 46., 39., 42.,
        40., 42., 44., 43., 39.],
       [27., 28., 28., 28., 42., 31., 28., 26., 33., 36., 22., 45., 32.,
        31., 23., 24., 39., 39., 43., 44., 43., 42., 46.,  0., 19., 33.,
        20., 32., 31., 31., 33., 29., 46., 45., 42., 44., 44., 33., 31.,
        27., 23., 48., 25., 21.],
       [22., 22., 22., 31., 38., 29., 26., 28., 32., 40., 25., 41., 31.,
        31., 15., 19., 44., 44., 36., 41., 42., 41., 42., 19.,  0., 34.,
        24., 30., 21., 27., 28., 22., 47., 46., 43., 43., 39., 32., 25.,
        24., 25., 46., 22., 15.],
       [29., 35., 35., 28., 26., 26., 20., 31., 36., 34., 38., 44., 36.,
        35., 31., 34., 23., 23., 43., 41., 42., 43., 42., 33., 34.,  0.,
        26., 27., 37., 36., 39., 36., 46., 42., 44., 42., 43., 31., 38.,
        32., 29., 44., 34., 33.],
       [29., 25., 25., 33., 41., 32., 28., 19., 40., 32., 25., 43., 36.,
        33., 23., 24., 46., 46., 41., 44., 41., 39., 45., 20., 24., 26.,
         0., 33., 22., 28., 32., 27., 49., 47., 38., 39., 39., 32., 31.,
        24., 17., 46., 21., 23.],
       [31., 29., 29., 28., 30., 30., 33., 32., 27., 36., 33., 39., 28.,
        29., 29., 34., 37., 37., 43., 41., 44., 47., 42., 32., 30., 27.,
        33.,  0., 33., 30., 32., 30., 47., 49., 41., 39., 40., 25., 38.,
        32., 35., 47., 31., 27.],
       [24., 26., 26., 36., 39., 33., 32., 30., 37., 32., 31., 44., 33.,
        36., 29., 30., 44., 44., 38., 46., 42., 41., 47., 31., 21., 37.,
        22., 33.,  0., 30., 30., 28., 48., 45., 42., 43., 44., 34., 25.,
        33., 26., 49., 25., 25.],
       [25., 21., 21., 31., 34., 33., 37., 35., 33., 44., 22., 42., 45.,
        45., 20., 23., 39., 39., 42., 37., 44., 42., 39., 31., 27., 36.,
        28., 30., 30.,  0.,  5.,  9., 46., 44., 44., 41., 43., 28., 27.,
        24., 28., 41., 24., 22.],
       [23., 21., 21., 31., 45., 37., 40., 35., 32., 37., 25., 51., 29.,
        29., 23., 21., 48., 48., 40., 39., 44., 39., 40., 33., 28., 39.,
        32., 32., 30.,  5.,  0., 13., 47., 45., 44., 45., 43., 32., 28.,
        28., 28., 49., 25., 23.],
       [25., 18., 18., 32., 34., 35., 35., 33., 32., 43., 20., 40., 43.,
        44., 17., 23., 37., 37., 45., 42., 44., 45., 42., 29., 22., 36.,
        27., 30., 28.,  9., 13.,  0., 46., 46., 43., 44., 45., 30., 29.,
        23., 29., 42., 20., 19.],
       [46., 44., 44., 43., 42., 47., 43., 48., 47., 45., 49., 52., 47.,
        46., 47., 47., 47., 47., 52., 52., 55., 45., 52., 46., 47., 46.,
        49., 47., 48., 46., 47., 46.,  0., 48., 57., 52., 47., 41., 49.,
        40., 39., 40., 48., 47.],
       [44., 39., 39., 45., 44., 45., 43., 44., 50., 34., 46., 54., 44.,
        44., 47., 43., 48., 48., 45., 45., 55., 42., 46., 45., 46., 42.,
        47., 49., 45., 44., 45., 46., 48.,  0., 39., 43.,  8., 36., 49.,
        41., 44., 34., 47., 47.],
       [38., 34., 34., 43., 45., 41., 40., 37., 37., 33., 44., 42., 40.,
        35., 40., 38., 45., 45., 54., 49., 49., 48., 49., 42., 43., 44.,
        38., 41., 42., 44., 44., 43., 57., 39.,  0., 33., 36., 37., 45.,
        39., 41., 40., 42., 40.],
       [40., 40., 40., 40., 38., 42., 42., 46., 41., 38., 44., 43., 39.,
        40., 44., 44., 36., 36., 51., 46., 51., 48., 46., 44., 43., 42.,
        39., 39., 43., 41., 45., 44., 52., 43., 33.,  0., 41., 37., 48.,
        41., 39., 40., 43., 43.],
       [41., 38., 38., 45., 46., 45., 40., 37., 40., 35., 45., 47., 43.,
        39., 40., 39., 45., 45., 45., 45., 51., 42., 46., 44., 39., 43.,
        39., 40., 44., 43., 43., 45., 47.,  8., 36., 41.,  0., 37., 42.,
        40., 40., 34., 43., 42.],
       [33., 26., 26., 31., 31., 26., 28., 30., 28., 27., 37., 39., 15.,
        17., 29., 35., 37., 37., 40., 38., 41., 44., 39., 33., 32., 31.,
        32., 25., 34., 28., 32., 30., 41., 36., 37., 37., 37.,  0., 28.,
        25., 33., 40., 31., 30.],
       [27., 28., 28., 39., 48., 33., 37., 29., 37., 39., 38., 45., 30.,
        32., 25., 31., 44., 44., 39., 42., 40., 44., 42., 31., 25., 38.,
        31., 38., 25., 27., 28., 29., 49., 49., 45., 48., 42., 28.,  0.,
        22., 33., 49., 31., 23.],
       [27., 21., 21., 31., 32., 29., 30., 21., 34., 42., 24., 41., 44.,
        43., 17., 20., 40., 40., 38., 39., 36., 42., 40., 27., 24., 32.,
        24., 32., 33., 24., 28., 23., 40., 41., 39., 41., 40., 25., 22.,
         0., 19., 41., 26., 24.],
       [23., 23., 23., 24., 40., 31., 29., 23., 33., 29., 21., 47., 35.,
        36., 25., 21., 47., 47., 40., 41., 41., 40., 42., 23., 25., 29.,
        17., 35., 26., 28., 28., 29., 39., 44., 41., 39., 40., 33., 33.,
        19.,  0., 47., 26., 26.],
       [49., 43., 43., 45., 43., 47., 42., 48., 48., 42., 46., 53., 44.,
        46., 47., 41., 46., 46., 30., 45., 41., 27., 44., 48., 46., 44.,
        46., 47., 49., 41., 49., 42., 40., 34., 40., 40., 34., 40., 49.,
        41., 47.,  0., 49., 49.],
       [20., 19., 19., 34., 40., 34., 33., 30., 29., 37., 27., 43., 31.,
        31., 20., 28., 47., 47., 43., 42., 46., 45., 43., 25., 22., 34.,
        21., 31., 25., 24., 25., 20., 48., 47., 42., 43., 43., 31., 31.,
        26., 26., 49.,  0., 11.],
       [18., 16., 16., 30., 43., 31., 32., 29., 28., 40., 24., 42., 29.,
        29., 17., 25., 43., 43., 39., 39., 41., 42., 39., 21., 15., 33.,
        23., 27., 25., 22., 23., 19., 47., 47., 40., 43., 42., 30., 23.,
        24., 26., 49., 11.,  0.]])
    D2 = np.array([[ 0., 16., 16., 22., 26., 21., 20., 29., 18., 31., 22., 34., 21.,
        18., 20., 21., 28., 28., 37., 31., 34., 34., 31., 25., 21., 18.,
        23., 27., 23., 23., 23., 21., 41., 42., 40., 36., 38., 23., 26.,
        23., 22., 39., 16., 16.],
       [16.,  0.,  0., 23., 26., 24., 24., 26., 23., 33., 23., 32., 15.,
        15., 17., 21., 26., 26., 36., 31., 36., 34., 30., 25., 22., 24.,
        25., 26., 26., 21., 22., 18., 43., 38., 38., 40., 38., 16., 26.,
        21., 24., 37., 19., 16.],
       [16.,  0.,  0., 23., 26., 24., 24., 26., 23., 33., 23., 32., 15.,
        15., 17., 21., 26., 26., 36., 31., 36., 34., 30., 25., 22., 24.,
        25., 26., 26., 21., 22., 18., 43., 38., 38., 40., 38., 16., 26.,
        21., 24., 37., 19., 16.],
       [22., 23., 23.,  0., 20., 20., 20., 26., 25., 29., 19., 34., 24.,
        22., 20., 19., 28., 28., 31., 25., 33., 32., 25., 20., 26., 24.,
        24., 26., 28., 22., 21., 23., 45., 41., 45., 41., 42., 20., 32.,
        22., 14., 37., 26., 24.],
       [26., 26., 26., 20.,  0., 15., 18., 28., 27., 34., 24., 28., 25.,
        26., 23., 23., 27., 27., 36., 33., 36., 40., 34., 27., 20., 25.,
        23., 27., 22., 24., 29., 23., 47., 45., 47., 41., 47., 25., 30.,
        21., 22., 38., 21., 25.],
       [21., 24., 24., 20., 15.,  0., 12., 28., 27., 29., 29., 30., 20.,
        22., 19., 24., 26., 26., 36., 35., 38., 39., 36., 22., 18., 21.,
        22., 27., 24., 25., 29., 24., 48., 44., 44., 41., 43., 21., 24.,
        17., 22., 40., 24., 22.],
       [20., 24., 24., 20., 18., 12.,  0., 25., 28., 26., 26., 31., 24.,
        22., 17., 21., 26., 26., 36., 36., 42., 31., 36., 21., 16., 16.,
        17., 32., 23., 27., 30., 24., 44., 44., 43., 42., 40., 24., 28.,
        20., 19., 36., 22., 22.],
       [29., 26., 26., 26., 28., 28., 25.,  0., 30., 30., 27., 35., 27.,
        22., 24., 23., 34., 34., 33., 33., 35., 34., 34., 25., 26., 23.,
        17., 27., 29., 30., 28., 31., 49., 41., 39., 38., 40., 24., 29.,
        21., 22., 35., 29., 27.],
       [18., 23., 23., 25., 27., 27., 28., 30.,  0., 32., 26., 22., 22.,
        22., 20., 24., 31., 31., 38., 35., 39., 40., 35., 25., 20., 27.,
        29., 20., 26., 26., 27., 23., 42., 44., 38., 34., 39., 22., 28.,
        25., 27., 35., 20., 21.],
       [31., 33., 33., 29., 34., 29., 26., 30., 32.,  0., 35., 34., 33.,
        31., 30., 27., 35., 35., 31., 36., 36., 34., 36., 31., 33., 21.,
        26., 31., 28., 31., 35., 33., 41., 34., 39., 34., 33., 28., 33.,
        29., 25., 28., 30., 32.],
       [22., 23., 23., 19., 24., 29., 26., 27., 26., 35.,  0., 36., 23.,
        24., 21., 22., 27., 27., 37., 29., 36., 34., 28., 19., 22., 23.,
        22., 29., 27., 22., 25., 20., 45., 43., 42., 41., 42., 28., 33.,
        23., 19., 33., 27., 24.],
       [34., 32., 32., 34., 28., 30., 31., 35., 22., 34., 36.,  0., 32.,
        31., 28., 36., 35., 35., 38., 39., 38., 45., 38., 36., 27., 35.,
        35., 27., 33., 38., 38., 34., 52., 45., 45., 43., 45., 30., 32.,
        32., 37., 43., 28., 29.],
       [21., 15., 15., 24., 25., 20., 24., 27., 22., 33., 23., 32.,  0.,
         7.,  9., 23., 28., 28., 36., 32., 37., 39., 32., 26., 21., 25.,
        27., 25., 26., 19., 23., 20., 46., 42., 38., 43., 42., 18., 22.,
        22., 26., 38., 21., 20.],
       [18., 15., 15., 22., 26., 22., 22., 22., 22., 31., 24., 31.,  7.,
         0.,  7., 17., 25., 25., 33., 28., 34., 35., 28., 23., 21., 23.,
        23., 26., 29., 19., 21., 19., 45., 40., 37., 41., 40., 20., 23.,
        20., 25., 37., 20., 19.],
       [20., 17., 17., 20., 23., 19., 17., 24., 20., 30., 21., 28.,  9.,
         7.,  0., 16., 25., 25., 33., 28., 35., 34., 29., 21., 14., 21.,
        21., 23., 26., 19., 22., 18., 43., 42., 40., 41., 43., 17., 22.,
        19., 21., 36., 19., 15.],
       [21., 21., 21., 19., 23., 24., 21., 23., 24., 27., 22., 36., 23.,
        17., 16.,  0., 29., 29., 31., 28., 36., 30., 27., 20., 19., 22.,
        23., 28., 29., 24., 21., 22., 42., 39., 39., 36., 37., 25., 29.,
        20., 20., 32., 25., 22.],
       [28., 26., 26., 28., 27., 26., 26., 34., 31., 35., 27., 35., 28.,
        25., 25., 29.,  0.,  0., 43., 38., 41., 41., 38., 24., 26., 22.,
        26., 35., 29., 26., 28., 24., 48., 51., 44., 46., 49., 30., 24.,
        32., 30., 42., 30., 25.],
       [28., 26., 26., 28., 27., 26., 26., 34., 31., 35., 27., 35., 28.,
        25., 25., 29.,  0.,  0., 43., 38., 41., 41., 38., 24., 26., 22.,
        26., 35., 29., 26., 28., 24., 48., 51., 44., 46., 49., 30., 24.,
        32., 30., 42., 30., 25.],
       [37., 36., 36., 31., 36., 36., 36., 33., 38., 31., 37., 38., 36.,
        33., 33., 31., 43., 43.,  0., 12., 15., 17., 13., 33., 38., 30.,
        32., 33., 37., 39., 37., 41., 41., 32., 41., 39., 31., 32., 41.,
        31., 30., 29., 39., 36.],
       [31., 31., 31., 25., 33., 35., 36., 33., 35., 36., 29., 39., 32.,
        28., 28., 28., 38., 38., 12.,  0., 15., 18.,  2., 30., 35., 32.,
        30., 28., 35., 33., 30., 34., 36., 36., 39., 37., 37., 34., 38.,
        32., 29., 35., 34., 33.],
       [34., 36., 36., 33., 36., 38., 42., 35., 39., 36., 36., 38., 37.,
        34., 35., 36., 41., 41., 15., 15.,  0., 29., 13., 39., 37., 33.,
        35., 35., 36., 36., 35., 37., 43., 41., 38., 36., 39., 33., 35.,
        34., 37., 38., 37., 33.],
       [34., 34., 34., 32., 40., 39., 31., 34., 40., 34., 34., 45., 39.,
        35., 34., 30., 41., 41., 17., 18., 29.,  0., 17., 33., 37., 33.,
        30., 36., 37., 39., 34., 40., 34., 31., 31., 39., 28., 38., 45.,
        33., 26., 27., 36., 34.],
       [31., 30., 30., 25., 34., 36., 36., 34., 35., 36., 28., 38., 32.,
        28., 29., 27., 38., 38., 13.,  2., 13., 17.,  0., 31., 34., 33.,
        31., 29., 34., 33., 29., 33., 37., 36., 39., 37., 35., 33., 37.,
        30., 29., 33., 35., 32.],
       [25., 25., 25., 20., 27., 22., 21., 25., 25., 31., 19., 36., 26.,
        23., 21., 20., 24., 24., 33., 30., 39., 33., 31.,  0., 19., 20.,
        15., 29., 27., 28., 28., 25., 48., 43., 41., 40., 43., 27., 30.,
        23., 19., 37., 23., 21.],
       [21., 22., 22., 26., 20., 18., 16., 26., 20., 33., 22., 27., 21.,
        21., 14., 19., 26., 26., 38., 35., 37., 37., 34., 19.,  0., 23.,
        21., 25., 19., 26., 28., 21., 44., 45., 41., 39., 43., 22., 21.,
        19., 22., 37., 20., 15.],
       [18., 24., 24., 24., 25., 21., 16., 23., 27., 21., 23., 35., 25.,
        23., 21., 22., 22., 22., 30., 32., 33., 33., 33., 20., 23.,  0.,
        16., 25., 25., 25., 28., 24., 42., 41., 41., 39., 40., 20., 29.,
        20., 18., 33., 22., 20.],
       [23., 25., 25., 24., 23., 22., 17., 17., 29., 26., 22., 35., 27.,
        23., 21., 23., 26., 26., 32., 30., 35., 30., 31., 15., 21., 16.,
         0., 29., 22., 29., 30., 26., 47., 43., 41., 39., 43., 26., 30.,
        24., 15., 37., 18., 21.],
       [27., 26., 26., 26., 27., 27., 32., 27., 20., 31., 29., 27., 25.,
        26., 23., 28., 35., 35., 33., 28., 35., 36., 29., 29., 25., 25.,
        29.,  0., 26., 25., 25., 26., 43., 41., 39., 37., 41., 24., 33.,
        28., 30., 37., 25., 22.],
       [23., 26., 26., 28., 22., 24., 23., 29., 26., 28., 27., 33., 26.,
        29., 26., 29., 29., 29., 37., 35., 36., 37., 34., 27., 19., 25.,
        22., 26.,  0., 26., 28., 24., 45., 46., 44., 42., 44., 26., 23.,
        29., 24., 36., 22., 23.],
       [23., 21., 21., 22., 24., 25., 27., 30., 26., 31., 22., 38., 19.,
        19., 19., 24., 26., 26., 39., 33., 36., 39., 33., 28., 26., 25.,
        29., 25., 26.,  0.,  8.,  9., 44., 41., 40., 41., 44., 21., 25.,
        24., 26., 39., 24., 24.],
       [23., 22., 22., 21., 29., 29., 30., 28., 27., 35., 25., 38., 23.,
        21., 22., 21., 28., 28., 37., 30., 35., 34., 29., 28., 28., 28.,
        30., 25., 28.,  8.,  0., 16., 44., 40., 39., 40., 41., 25., 26.,
        28., 27., 38., 25., 23.],
       [21., 18., 18., 23., 23., 24., 24., 31., 23., 33., 20., 34., 20.,
        19., 18., 22., 24., 24., 41., 34., 37., 40., 33., 25., 21., 24.,
        26., 26., 24.,  9., 16.,  0., 46., 44., 43., 44., 43., 22., 25.,
        23., 26., 39., 21., 21.],
       [41., 43., 43., 45., 47., 48., 44., 49., 42., 41., 45., 52., 46.,
        45., 43., 42., 48., 48., 41., 36., 43., 34., 37., 48., 44., 42.,
        47., 43., 45., 44., 44., 46.,  0., 35., 39., 34., 34., 45., 48.,
        45., 40., 35., 47., 45.],
       [42., 38., 38., 41., 45., 44., 44., 41., 44., 34., 43., 45., 42.,
        40., 42., 39., 51., 51., 32., 36., 41., 31., 36., 43., 45., 41.,
        43., 41., 46., 41., 40., 44., 35.,  0., 30., 32., 11., 34., 44.,
        38., 39., 24., 44., 43.],
       [40., 38., 38., 45., 47., 44., 43., 39., 38., 39., 42., 45., 38.,
        37., 40., 39., 44., 44., 41., 39., 38., 31., 39., 41., 41., 41.,
        41., 39., 44., 40., 39., 43., 39., 30.,  0., 27., 23., 39., 42.,
        42., 41., 29., 43., 39.],
       [36., 40., 40., 41., 41., 41., 42., 38., 34., 34., 41., 43., 43.,
        41., 41., 36., 46., 46., 39., 37., 36., 39., 37., 40., 39., 39.,
        39., 37., 42., 41., 40., 44., 34., 32., 27.,  0., 26., 37., 42.,
        40., 37., 31., 39., 39.],
       [38., 38., 38., 42., 47., 43., 40., 40., 39., 33., 42., 45., 42.,
        40., 43., 37., 49., 49., 31., 37., 39., 28., 35., 43., 43., 40.,
        43., 41., 44., 44., 41., 43., 34., 11., 23., 26.,  0., 38., 44.,
        38., 39., 24., 43., 42.],
       [23., 16., 16., 20., 25., 21., 24., 24., 22., 28., 28., 30., 18.,
        20., 17., 25., 30., 30., 32., 34., 33., 38., 33., 27., 22., 20.,
        26., 24., 26., 21., 25., 22., 45., 34., 39., 37., 38.,  0., 23.,
        13., 25., 36., 23., 23.],
       [26., 26., 26., 32., 30., 24., 28., 29., 28., 33., 33., 32., 22.,
        23., 22., 29., 24., 24., 41., 38., 35., 45., 37., 30., 21., 29.,
        30., 33., 23., 25., 26., 25., 48., 44., 42., 42., 44., 23.,  0.,
        24., 32., 40., 29., 21.],
       [23., 21., 21., 22., 21., 17., 20., 21., 25., 29., 23., 32., 22.,
        20., 19., 20., 32., 32., 31., 32., 34., 33., 30., 23., 19., 20.,
        24., 28., 29., 24., 28., 23., 45., 38., 42., 40., 38., 13., 24.,
         0., 18., 33., 26., 22.],
       [22., 24., 24., 14., 22., 22., 19., 22., 27., 25., 19., 37., 26.,
        25., 21., 20., 30., 30., 30., 29., 37., 26., 29., 19., 22., 18.,
        15., 30., 24., 26., 27., 26., 40., 39., 41., 37., 39., 25., 32.,
        18.,  0., 34., 22., 25.],
       [39., 37., 37., 37., 38., 40., 36., 35., 35., 28., 33., 43., 38.,
        37., 36., 32., 42., 42., 29., 35., 38., 27., 33., 37., 37., 33.,
        37., 37., 36., 39., 38., 39., 35., 24., 29., 31., 24., 36., 40.,
        33., 34.,  0., 40., 39.],
       [16., 19., 19., 26., 21., 24., 22., 29., 20., 30., 27., 28., 21.,
        20., 19., 25., 30., 30., 39., 34., 37., 36., 35., 23., 20., 22.,
        18., 25., 22., 24., 25., 21., 47., 44., 43., 39., 43., 23., 29.,
        26., 22., 40.,  0., 11.],
       [16., 16., 16., 24., 25., 22., 22., 27., 21., 32., 24., 29., 20.,
        19., 15., 22., 25., 25., 36., 33., 33., 34., 32., 21., 15., 20.,
        21., 22., 23., 24., 23., 21., 45., 43., 39., 39., 42., 23., 21.,
        22., 25., 39., 11.,  0.]])
    print(D1, D2)
     

def build_matrices(seqlist):
    n = len(seqlist)
    D1 = np.zeros((n, n))
    D2 = np.zeros((n, n))
    for i in range(n):
        print(i)
        for j in range(n):
            D1[i][j] = hamming(seqlist[i], seqlist[j])
            D2[i][j] = levenshtein(seqlist[i], seqlist[j])
    return D1, D2


def hamming(seq1, seq2):
    n = len(seq1)
    m = len(seq2)
    dist = np.inf
    if n < m:
        y = seq1
        x = seq2
    else:
        x = seq1
        y = seq2
    for s in range(max(n,m)-min(n,m)+1):
        curdist = 0
        for i in range(min(n,m)):
            if x[i+s] != y[i]:
                curdist += 1
        if curdist < dist:
            dist = curdist
    return dist
            

def levenshtein(x,y):
    #Initialisierung
    len_x = len(x)
    len_y = len(y)
    matrix = np.zeros( (len_x+1, len_y+1) )

    #Trage Basisfaelle in die Matrix ein
    for i in range (1, len_x+1):
        matrix[i][0] = i

    for j in range (1, len_y+1):
        matrix[0][j] = j

    #Fuelle den Rest der Matrix aus, entweder wird eine Stelle ersetzt,
    #geloescht oder eingefuegt
    for i in range (1, len_x+1):
        for j in range (1, len_y+1):
            if x[i-1] == y[j-1]:
                matrix[i][j] = min(matrix[i-1][j-1], matrix[i-1][j-1]+1,
                               matrix[i][j-1]+1, matrix[i-1][j]+1)
            else:
                matrix[i][j] = min(matrix[i-1][j-1]+1,
                               matrix[i][j-1]+1, matrix[i-1][j]+1)

    #print("Matrix = ", matrix)

    return matrix[len_x][len_y]

if __name__ == "__main__":
    main()