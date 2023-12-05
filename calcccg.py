import matplotlib.pyplot as plt
import numpy as np

def calcccg(s1,s2,Nlag,dt):
    #calculates a cross-correlation function for the two spike trains s1, and
    #s2 (which are vectors of 0s and 1s). Nlag is the number of time bins to
    #the left and right of 0 to include. dt is the time binning of the spike 
    #trains (in seconds). Output is a 2*Nlag+1 vector in units of Hz.
    Ns = len(s1)
    T = dt * Ns
    correl = np.correlate(s1,s2,mode='full')

    return correl[(Ns-Nlag-1):(Ns+Nlag)]/T
