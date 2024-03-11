## BlueJay-photoz
Photometric redshifts with EAZY for the Blue Jay catalog

# 1: NIRCam and HST only photometry
For photometry extraction details, ask Amir Khoram

File of catalog: 
'inputs/phot_cat.cat'

Contents of catalog:
	+-------------------+------------+---------------------------+
	|                   |            |                           |
	| Bands             |  Survey    |  Data FITS file           |
	|                   |            |                           |
	+===================+============+===========================+
	| NIRCAM            | Blue Jay   | 'data/Flux_Aperture_      |
	| F090W,F115W,F150W,|            | PSFMatched_AperCorr.fits' |
	| F200W F277W,F356W,|            |                           |
	| F410M,F444W       |            |                           |
	+-------------------+------------+---------------------------+
	| F606W,F814W       | CANDELS    | 'data/HST_Flux_           |
	| F125W,F160W       |            |  Aperture.fits'           |
	+-------------------+------------+---------------------------+
	| F140W             | 3D-HST     | same as above             |
	+-------------------+------------+---------------------------+

The catalog has a single line header with all column names as shown here: (ASCII file)

	# id RA DEC z_spec f_F090W e_F090W f_F115W e_F115W f_F150W e_F150W f_F200W e_F200W 
	f_F277W e_F277W f_F356W e_F356W f_F410M e_F410M f_F444W e_F444W f_F125W e_F125W f_F140W e_F140W 
	f_F160W e_F160W f_F606W e_F606W f_F814W e_F814W

All fluxes are in microJansky

Eazy parameters setting are default + modified parameters in Jupyter Notebook 'photoz_nircam.ipnb'

Templates used are in 'templates/' directory

======================== =================================================================================
Column Name               Column Content
======================== =================================================================================
1    #id				Unique identifier  
2    #RA				RA J2000 degrees 
3    #DEC				Dec J2000 degrees
4    #z_spec             spectroscopic redshift from 'data/redshifts_v0.1.txt' file (Prospector fits checked by eye)
...  #F_{str}            Normalized flux in filter 
...  #E_{str}            Normalized error in filter


# Outputs:
file names 'outputs/bluejay_photoz_hst.zphot*'
	-> .zout.fits = main output file, with all photometric redshifts + stellar pop. parameters
	-> .zphot.fits = output file with photometric redshifts
	-> .data.fits = all data
	-> .zeropoints = zeropoints correnction (not implemented)
	-> .translate = translation file for running EaZy

# Alternative outputs: with spectroscopic redshift prior enabled ('photometry_zspec.py')
file names = 'outputs/bluejay_photoz_zspec.zphot*'

#---------------------------------------------------------------------------------------------------

# 2: 3D-HST COSMOS photometric catalog + Blue Jay NIRCam
COSMOS 3D-HST release V4.1

File of catalog:
'inputs/phot_cat_norm_3dhst.cat'

Contents of catalog:
+-------------------+------------+---------------------------+
|                   |            |                           |
| Bands             |  Survey    |  Reference                |
|                   |            |                           |
+===================+============+===========================+
| NIRCAM            | Blue Jay   |                           |
| F090W,F115W,F150W,|            |                           |
| F200W F277W,F356W,|            |                           |
| F410M,F444W       |            |                           |
+-------------------+------------+---------------------------+
| u,g,r,i,z         | CFHTLS     | Erben et al. (2009)       |
|                   |            | Hildebrandt et al. (2009) |
+-------------------+------------+---------------------------+
| Bj, Vj, r+,i+,z+, |            |Taniguchi et al. (2007)    |
| 12 medium bands   |            |                           |
+-------------------+------------+---------------------------+
| F606W,F814W       | CANDELS    | Grogin et al. 2011,       |
|                   |            | Koekemoer et al. 2011     |
+-------------------+------------+---------------------------+
| J1,J2,J3          | NMBS       | Whitaker et al. (2011)    |
| H1,H2,K           |            |                           |
+-------------------+------------+---------------------------+
| J, H, Ks          | UltraVISTA | McCracken et al. (2012)   |
+-------------------+------------+---------------------------+
| Y, J, H, Ks       | WIRDS      | Bielby et al. (2012)      |
+-------------------+------------+---------------------------+
| F140W             | 3D-HST     | Brammer et al. 2012       |
+-------------------+------------+---------------------------+
| F125W,F160W       | CANDELS    | Grogin et al. 2011,       |
|                   |            | Koekemoer et al. 2011     |
+-------------------+------------+---------------------------+
| 3.6,4.5um         | SEDS       | Ashby et al. (2013)       |
+-------------------+------------+---------------------------+
| 5.8,8.0um         | EGS        | Bramby et al. (2008)      |
+-------------------+------------+---------------------------+

The catalog has a single line header with all column names as shown here: (ASCII file)

	# id RA DEC z_spec F_F090W E_F090W F_F115W E_F115W F_F150W E_F150W F_F200W E_F200W F_F277W E_F277W F_F356W E_F356W F_F410M E_F410M F_F444W E_F444W F_F160W F_IRAC2 W_IRAC1 E_IRAC1 F_IRAC1 W_UVISTA_KS E_UVISTA_KS F_UVISTA_KS W_KS E_KS F_KS W_K E_K E_IRAC2 F_K E_UVISTA_H F_UVISTA_H W_H E_H F_H W_H2 E_H2 F_H2 W_H1 E_H1 F_H1 W_F140W W_UVISTA_H E_F140W W_IRAC2 E_IRAC3 E_IA767 F_IA767 E_IA738 F_IA738 E_IA709 F_IA709 E_IA679 F_IA679 E_IA624 F_IA624 E_IA574 F_IA574 F_IRAC3 E_IA527 E_IA505 F_IA505 E_IA484 F_IA484 E_IA464 F_IA464 E_IA427 F_IA427 W_IRAC4 E_IRAC4 F_IRAC4 W_IRAC3 F_IA527 F_F140W W_UVISTA_J E_UVISTA_J W_I E_I F_I W_RP E_RP F_RP W_R E_R F_R W_F606W E_F606W F_F606W F_IP W_V F_V W_G E_G F_G W_B E_B F_B W_U E_U F_U W_F160W E_F160W E_V E_IP W_IP F_F814W F_UVISTA_J W_J E_J F_J W_J3 E_J3 F_J3 W_J2 E_J2 F_J2 W_J1 E_J1 F_J1 W_F125W E_F125W F_F125W W_UVISTA_Y E_UVISTA_Y F_UVISTA_Y W_ZP E_ZP F_ZP W_Z E_Z F_Z W_F814W E_F814W F_IA827 E_IA827

All fluxes are normalized to an AB zeropoint of 25, such that: magAB = 25.0-2.5*log10(flux)

======================== =================================================================================
Column Name               Column Content
======================== =================================================================================
1    #id				Unique identifier  
2    #RA				RA J2000 degrees 
3    #DEC				Dec J2000 degrees
4    #z_spec             spectroscopic redshift from 'data/redshifts_v0.1.txt' file (Prospector fits checked by eye)
...  #F_{str}            Normalize flux in filter 
...  #E_{str}            Normalized error in filter

Eazy parameters setting are default + modified parameters in Jupyter Notebook 'photoz_3dhst_nircam.ipynb'

Templates used are in 'templates/' directory

# Outputs:
file names 'outputs/bluejay_photoz_3dhst.zphot*'
	-> .zout.fits = main output file, with all photometric redshifts + stellar pop. parameters
	-> .zphot.fits = output file with photometric redshifts
	-> .data.fits = all data
	-> .zeropoints = zeropoints correnction (not implemented)
	-> .translate = translation file for running EaZy


