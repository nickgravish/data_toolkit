
import numpy as np
from scipy import signal



def nan_helper(y):
    """Helper to handle indices and logical indices of NaNs.

    Input:
        - y, 1d numpy array with possible NaNs
    Output:
        - nans, logical indices of NaNs
        - index, a function, with signature indices= index(logical_indices),
          to convert logical indices of NaNs to 'equivalent' indices
    Example:
        >>> # linear interpolation of NaNs
        >>> nans, x= nan_helper(y)
        >>> y[nans]= np.interp(x(nans), x(~nans), y[~nans])
    """

    return np.isnan(y), lambda z: z.nonzero()[0]


def ReturnMedian(x, y, bins = 1):
    """Returns median along multiple measurements in y, binned along x

    Input:
        - x is n x 1 numpy array
        - y is n x m numpy array
    Output:
        - x along bins, median y values
    """

    x = x.flatten()
    y = y.flatten()

    x_minmax = [np.nanmin(x), np.nanmax(x)] # peak to peak gives range of x values

    # loop through all values
    x_out = np.arange(x_minmax[0], x_minmax[1], bins)
    y_out = np.zeros(x_out.shape)

    y_SD = np.zeros(x_out.shape)
    N    = np.zeros(x_out.shape)

    for kk in range(len(x_out)-1):
#         print kk
        # find all x,y pairs in bin width window
        mask = np.where((x >= x_out[kk]) & (x <= x_out[kk+1]))[0];

#       check if empty
        if mask.shape[0] > 0:
            y_out[kk] = np.nanmedian(y[mask[:]])
            N[kk] = mask.shape[0]
            y_SD[kk] = np.nanstd(y[mask[:]])

    return x_out, y_out, y_SD, N


def AverageAndLowPass(x,y, bins = 1):
    x_mn, y_mn = ReturnMedian(x,y, bins = bins)

    b, a = signal.butter(5, .2, btype = 'low')
    nans, x= nan_helper(y_mn) # find all nans
    y_mn[nans]= np.interp(x_mn[nans], x_mn[~nans], y_mn[~nans]) # interpolate through all nans
    y_filt = signal.filtfilt(b, a, y_mn)

    return x_mn,y_filt
