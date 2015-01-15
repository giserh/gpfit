from numpy import size, inf, nan, ones, hstack, reshape, dot, tile
from lse_scaled import lse_scaled
from repcols import repcols

def softmax_affine(x, params, softness_param_is_alpha=False):
	'''
	params may come in as
	  1) a cell {ba, alpha}, or 
	  2) a vector (with alpha last)
	after reshaping (column-major), ba is dimx+1 by K
	first row is b
	rest is a


	if softness_param_is_alpha = false, then it's gamma (gamma = 1/alpha)
	'''
	
	ba = params[0:-1]
	softness = params[-1] #equivalent of end

	if softness_param_is_alpha:
		alpha = softness
	else:
		alpha = 1/softness

	#check sizes
	npt, dimx = x.shape
	K = size(ba)/(dimx+1)
	ba = ba.reshape(dimx+1, K, order='F')

	if alpha <= 0:
		y = inf*ones((npt,1))
		dydp = nan
		return y, dydp

    #augment data with column of ones
	X = hstack((ones((npt,1)), x))

	#compute affine functions
	z = dot(X,ba)

	y, dydz, dydsoftness = lse_scaled(z, alpha)

	if not softness_param_is_alpha:
		dydsoftness = - dydsoftness*(alpha**2)

	dydba = repcols(dydz, dimx+1) * tile(X, (1, K))

	dydsoftness.shape = (dydsoftness.size,1)
	dydp = hstack((dydba, dydsoftness))

	return y, dydp