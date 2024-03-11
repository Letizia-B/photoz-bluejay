#   photometric redshift of Blue Jay catalog from NIRCam data
#	 now using zspec from prospector!!
import numpy as np
import eazy
import warnings

#---------------------------------------------------------
#   CONSTRUCT THE PARAMETERS DICTIONARY
params = {}

params['CATALOG_FILE'] = 'phot_cat4.cat' 
params['MAIN_OUTPUT_FILE'] = 'bluejay_photz_zspec'

# Galactic extinction
#params['MW_EBV'] = 0.0195 #median extinction in the COSMOS field
params['CAT_HAS_EXTCORR'] = False

params['Z_STEP'] = 0.01
params['Z_MIN'] = 1.01
params['Z_MAX'] = 7.

#template file (following Weaver2024) 
params['TEMPLATES_FILE'] = 'templates/sfhz/corr_sfhz_13.param'

# following Weaver 2024 apply 5% error!!
params['SYS_ERR'] = 0.05

params['FIX_ZSPEC'] = True
params['PRIOR_ABZP'] = 23.9

params['REST_FILTERS'] = [153,154,155,161,162,163]

translate_file = 'zphot.translate'

#   INITIALIZE PHOTOZ OBJECT
self = eazy.photoz.PhotoZ(param_file=None, translate_file=translate_file, zeropoint_file=None,
                          params=params, load_prior=False, load_products=False,n_proc=4)

'''#   ITERATIVE ZEROPOINT ESTIMATION
NITER = 3
NBIN = np.minimum(self.NOBJ // 5, 10)

self.param.params['VERBOSITY'] = 1.
for iter in range(NITER):
    print('Iteration: ', iter)

    sn = self.fnu / self.efnu
    clip = (sn > 1).sum(axis=1) > 3  # Generally make this higher to ensure reasonable fits
    self.iterate_zp_templates(idx=self.idx[clip], update_templates=False,
                              update_zeropoints=True, iter=iter, n_proc=4,
                              save_templates=False, error_residuals=False,
                              NBIN=NBIN, get_spatial_offset=False)

# Turn off error corrections derived above
self.set_sys_err(positive=True)'''

# fit_parallel renamed to fit_catalog 14 May 2021
self.fit_catalog(self.idx, n_proc=4)

# Derived parameters (z params, RF colors, masses, SFR, etc.)
warnings.simplefilter('ignore', category=RuntimeWarning)
zout, hdu = self.standard_output(simple=False,
                                 rf_pad_width=0.5, rf_max_err=2,
                                 prior=False, beta_prior=True,
                                 UBVJ=[153,154,155,161,162,163],
						   absmag_filters=[],
                                 extra_rf_filters=[])



