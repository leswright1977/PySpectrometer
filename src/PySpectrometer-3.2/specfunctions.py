import numpy as np

def savitzky_golay(y, window_size, order, deriv=0, rate=1):
	#scipy
	#From: https://scipy.github.io/old-wiki/pages/Cookbook/SavitzkyGolay
	import numpy as np
	from math import factorial
	try:
		window_size = np.abs(np.int(window_size))
		order = np.abs(np.int(order))
	except ValueError:
		raise ValueError("window_size and order have to be of type int")
	if window_size % 2 != 1 or window_size < 1:
		raise TypeError("window_size size must be a positive odd number")
	if window_size < order + 2:
		raise TypeError("window_size is too small for the polynomials order")
	order_range = range(order+1)
	half_window = (window_size -1) // 2
	# precompute coefficients
	b = np.mat([[k**i for i in order_range] for k in range(-half_window, half_window+1)])
	m = np.linalg.pinv(b).A[deriv] * rate**deriv * factorial(deriv)
	# pad the signal at the extremes with
	# values taken from the signal itself
	firstvals = y[0] - np.abs( y[1:half_window+1][::-1] - y[0] )
	lastvals = y[-1] + np.abs(y[-half_window-1:-1][::-1] - y[-1])
	y = np.concatenate((firstvals, y, lastvals))
	return np.convolve( m[::-1], y, mode='valid')


def peakIndexes(y, thres=0.3, min_dist=1, thres_abs=False):
	#peakutils
	#from https://bitbucket.org/lucashnegri/peakutils/raw/f48d65a9b55f61fb65f368b75a2c53cbce132a0c/peakutils/peak.py
	if isinstance(y, np.ndarray) and np.issubdtype(y.dtype, np.unsignedinteger):
		raise ValueError("y must be signed")

	if not thres_abs:
		thres = thres * (np.max(y) - np.min(y)) + np.min(y)

	min_dist = int(min_dist)

	# compute first order difference
	dy = np.diff(y)

	# propagate left and right values successively to fill all plateau pixels (0-value)
	zeros, = np.where(dy == 0)

	# check if the signal is totally flat
	if len(zeros) == len(y) - 1:
		return np.array([])

	if len(zeros):
		# compute first order difference of zero indexes
		zeros_diff = np.diff(zeros)
		# check when zeros are not chained together
		zeros_diff_not_one, = np.add(np.where(zeros_diff != 1), 1)
		# make an array of the chained zero indexes
		zero_plateaus = np.split(zeros, zeros_diff_not_one)

		# fix if leftmost value in dy is zero
		if zero_plateaus[0][0] == 0:
			dy[zero_plateaus[0]] = dy[zero_plateaus[0][-1] + 1]
			zero_plateaus.pop(0)

		# fix if rightmost value of dy is zero
		if len(zero_plateaus) and zero_plateaus[-1][-1] == len(dy) - 1:
			dy[zero_plateaus[-1]] = dy[zero_plateaus[-1][0] - 1]
			zero_plateaus.pop(-1)

		# for each chain of zero indexes
		for plateau in zero_plateaus:
			median = np.median(plateau)
			# set leftmost values to leftmost non zero values
			dy[plateau[plateau < median]] = dy[plateau[0] - 1]
			# set rightmost and middle values to rightmost non zero values
			dy[plateau[plateau >= median]] = dy[plateau[-1] + 1]

	# find the peaks by using the first order difference
	peaks = np.where(
		(np.hstack([dy, 0.0]) < 0.0)
		& (np.hstack([0.0, dy]) > 0.0)
		& (np.greater(y, thres))
	)[0]

	# handle multiple peaks, respecting the minimum distance
	if peaks.size > 1 and min_dist > 1:
		highest = peaks[np.argsort(y[peaks])][::-1]
		rem = np.ones(y.size, dtype=bool)
		rem[peaks] = False

		for peak in highest:
			if not rem[peak]:
				sl = slice(max(0, peak - min_dist), peak + min_dist + 1)
				rem[sl] = True
				rem[peak] = False

		peaks = np.arange(y.size)[~rem]

	return peaks	

