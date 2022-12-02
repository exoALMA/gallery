import casa_cube as casa
import matplotlib.pyplot as plt
import numpy as np
import pymcfost as mcfost

vsys=0.
dir='~/Observations/exoALMA/final/'
distance= [71.5,  # V4046 Sgr
           157.2, # LkCa15
           144.,  # DM Tau
           180.7, # SY Cha
           308.6, # HD34282
           155.9, # MWC758
           140.,  # J1604
           147.1,  # J1852
           151.0,  # J1842
           135.,  # HD135344B
           97.9,  # PDS66
           149.4  # CQ Tau
]

# disc size in arcsec, used to rescale images to different sizes
limits=[
       6.,
       6.,
       6.,
       6.,
       6.,
       6.,
       6.,
       6.,
       6.,
       6.,
       6.,
       6.,
]

label=['V4046 Sgr',
       'LkCa 15',
       'DM Tau',
       'SY Cha',
       'AA Tau',
       'HD 34282',
       'MWC 758',
       'J1604',
       'J1852',
       'J1842',
       'HD 135344B',
       'PDS 66',
       'CQ Tau',
]

CO12=[
       'V4046_Sgr/V4046_Sgr_12CO_robust0.5_width0.100kms_threshold2.0sigma_taper0.1arcsec.clean.image.fits',
       'LkCa_15/LkCa_15_12CO_robust1.0_width0.100kms_threshold2.0sigma_taper0.15arcsec.clean.image.fits',
       #'DMTau/DM_Tau_12CO_robust0.5_width0.100kms_threshold2.0sigma_taper0.1arcsec.clean.pbcor.fits',
       #'../DMTau/DM_Tau_12CO_robust0.5_width0.1kms_threshold4.0sigma.clean.image.fits',
       '../DM_Tau/DM_Tau_12CO_robust0.5_width0.1kms_threshold4.0sigma.clean.JvMcorr.fits',
       '../SYCha/SY_Cha_12CO_robust0.5_width0.1kms_threshold4.0sigma.clean.image_denoise.fits',
#       '../SYCha/SY_Cha_12CO_robust0.5_width0.1kms_threshold4.0sigma.clean.JvMcorr.fits',
       'AA_Tau/AA_Tau_12CO_robust0.5_width0.100kms_threshold2.0sigma_taper0.1arcsec.clean.image.fits',
       '../HD34282/HD_34282_12CO_robust0.5_width0.1kms_threshold4.0sigma.clean.image.fits',
       'MWC_758/MWC_758_12CO_robust0.5_width0.100kms_threshold2.0sigma_taper0.1arcsec.clean.image.fits',
       'J1604-2130/RXJ1604.3-2130_12CO_robust0.0_width0.100kms_threshold3.0sigma_taper0.1arcsec.clean.image.fits',
       'J1852-3700/RXJ1852.3-3700_12CO_robust0.5_width0.100kms_threshold2.0sigma_taper0.1arcsec.clean.image.fits',
       'J1842-3532/RXJ1842.9-3532_12CO_robust0.0_width0.100kms_threshold2.0sigma_taper0.1arcsec.clean.image.fits',
       'HD_13534/HD_135344B_12CO_robust0.0_width0.100kms_threshold2.0sigma_taper0.1arcsec.clean.image.fits',
       'PDS_66/PDS_66_12CO_robust0.5_width0.100kms_threshold2.0sigma.clean.image.fits',
       '../CQTau/CQ_Tau_12CO_robust0.5_width0.1kms_threshold4.0sigma.clean.JvMcorr.image.fits',
       ]

CO13=[
'V4046_Sgr/V4046_Sgr_13CO_robust0.0_width0.100kms_threshold2.0sigma_taper0.1arcsec.clean.image.fits',
'LkCa_15/LkCa_15_13CO_robust0.0_width0.100kms_threshold2.0sigma_taper0.1arcsec.clean.image.fits',
'DM_Tau/DM_Tau_13CO_robust0.5_width0.100kms_threshold2.0sigma.clean.image.fits',
'../SYCha/SY_Cha_13CO_robust0.5_width0.1kms_threshold4.0sigma.clean.image.fits',
'blank',
'../HD34282/HD_34282_13CO_robust0.5_width0.1kms_threshold4.0sigma.clean.image.fits',
'MWC_758/MWC_758_13CO_robust0.5_width0.100kms_threshold2.0sigma.clean.image.fits',
'J1604-2130/RXJ1604.3-2130_13CO_robust0.5_width0.100kms_threshold3.0sigma.clean.image.fits',
'J1852-3700/RXJ1852.3-3700_13CO_robust0.5_width0.100kms_threshold2.0sigma.clean.image.fits',
'J1842-3532/RXJ1842.9-3532_13CO_robust0.5_width0.100kms_threshold2.0sigma.clean.image.fits',
'HD_13534/HD_135344B_13CO_robust0.0_width0.100kms_threshold2.0sigma_taper0.1arcsec.clean.image.fits',
'PDS_66/PDS_66_13CO_robust0.5_width0.028kms_threshold2.0sigma_taper0.15arcsec.clean.image.fits',
'../CQTau/CQ_Tau_13CO_robust0.5_width0.1kms_threshold4.0sigma.clean.JvMcorr.image.fits',
       ]

CS=[
'V4046_Sgr/V4046_Sgr_CS_robust0.5_width0.200kms_threshold2.0sigma_taper0.15arcsec.clean.image.fits',
'LkCa_15/LkCa_15_CS_robust1.0_width0.200kms_threshold2.0sigma_taper0.15arcsec.clean.image.fits',
'DM_Tau/DM_Tau_CS_robust0.5_width0.200kms_threshold2.0sigma_taper0.15arcsec.clean.image.fits',
'../SYCha/SY_Cha_CS_robust0.5_width0.1kms_threshold4.0sigma.clean.image.fits',
'blank',
'../HD34282/HD_34282_CS_robust0.5_width0.1kms_threshold4.0sigma.clean.image.fits',
'MWC_758/MWC_758_CS_robust1.0_width0.200kms_threshold2.0sigma_taper0.15arcsec.clean.image.fits',
'J1604-2130/RXJ1604.3-2130_CS_robust0.5_width0.200kms_threshold3.0sigma_taper0.15arcsec.clean.image.fits',
'J1852-3700/RXJ1852.3-3700_CS_robust0.5_width0.200kms_threshold2.0sigma_taper0.15arcsec.clean.image.fits',
'J1842-3532/RXJ1842.9-3532_CS_robust1.0_width0.200kms_threshold2.0sigma_taper0.15arcsec.clean.image.fits',
'HD_13534/HD_135344B_CS_robust0.5_width0.200kms_threshold2.0sigma_taper0.15arcsec.clean.image.fits',
'blank',
'../CQTau/CQ_Tau_CS_robust0.5_width0.1kms_threshold4.0sigma.clean.JvMcorr.image.fits',
]

scatt=[
'../SPHERE/V4046_Sgr_SPHERE_2016-03-14_H.fits',
'../SPHERE/LkCa_15_SPHERE_2015-12-19_J.fits',
'../SPHERE/DM_Tau_SPHERE_2018-10-02_H.fits',
'../SPHERE/SY_Cha_SPHERE_2021-01-02_K.fits',
'blank',
'../SPHERE/HD_34282_SPHERE_2015-12-19_J.fits',
'../SPHERE/MWC_758_2019-11-18_Q_phi_star_pol_subtr.fits',
'../SPHERE/RX_J1604.3-2130A_SPHERE_2017-09-17_J.fits',
'../SPHERE/2MASS_J18521730-3700119_SPHERE_2017-05-16_H.fits',
'../SPHERE/RXJ1842_SPHERE_2021-05-16_H.fits',
'../SPHERE/HD135344B_SPHERE_2016-06-30_J.fits',
'../SPHERE/PDS_66_SPHERE_2016-03-16_H.fits',
'../SPHERE/CQTau_SPHERE_2017-10-06_J.fits',
#'../SPHERE/HD143006_SPHERE_2016-07-01_J.fits',
#'../SPHERE/RXJ1615-3255_SPHERE_2016-03-15_H.fits',
#'../SPHERE/V_DM_Tau_2020-12-19_Q_phi_star_pol_subtr.fits',
]

cont=[
'V4046_Sgr/V4046_Sgr_ACASBLB_contap1.image.fits',
'LkCa_15/LkCa_15_ACASBLB_contap1.image.fits',
'DM_Tau/DM_Tau_ACASBLB_contap0.image.fits',
'SY_Cha/SY_Cha_SBLB_contap1.image.fits',
'AA_Tau/AA_Tau_ACASBLB_contap1.image.fits',
'HD_34282/HD_34282_ACASBLB_contap1.image.fits',
'MWC_758/MWC_758_LB_contp3.image.fits',
'J1604-2130/J1604_scaled_ACASBLB_contap1.image.fits',
'J1852-3700/J1852-3700_SBLB_contap1.image.fits',
'J1842-3532/RXJ1842-3532_SBLB_contap1.image.fits',
'HD_13534/HD_135344B_SBLB_contap1.image.fits',
'PDS_66/PDS_66_SBLB_iteration2_contap1.image.fits',
'CQ_Tau/CQ_Tau_scaled_SBLB_contap1.image.fits'
#'J1615-3255/J1615_ACASBLB_contap1.image.fits',
]

plot_type='all'

nx = 4
ny = 3

if (plot_type=='all'):
   files = CO12
   ny = len(files)
   nx = 5 # 12CO, 13CO, CS, continuum, scattered light
elif (plot_type=='scatt'):
   files = scatt
elif (plot_type=='cont'):
   files = cont
elif (plot_type=='CS'):
   files = CS
elif (plot_type=='CO13'):
   files = CO13
else:
   files = CO12

fig, axes = plt.subplots(nrows=ny, ncols=nx, figsize=(4*nx,4*ny), sharex='all', sharey='all')
plt.subplots_adjust(wspace=0.01, hspace=0.01)

print("plotting gallery of ",plot_type)

if (plot_type != 'line'):
   plt.style.use('dark_background')

for i,file in enumerate(files):
    no_ylabel = True
    no_xlabel = True
    cb = False
    print("opening ",file)

    lim = 6. #*150./distance[i]
    limits = [lim,-lim,-lim,lim]

    ax = axes.ravel()[i]

    if (plot_type == 'line'):
       ax.annotate(label[i],xy=[-12.,22.],ha='left',size=12)
    elif (plot_type == 'all'):
       ax.get_xaxis().set_visible(False)
       ax.get_yaxis().set_visible(False)
       axes[i,0].annotate(label[i],xy=[5.5,5.],ha='left',size=12)
       axes[i,0].annotate('12CO',xy=[-5.5,5.],ha='right',size=12)
       axes[i,1].annotate('13CO',xy=[-5.5,5.],ha='right',size=12)
       axes[i,2].annotate('CS',xy=[-5.5,5.],ha='right',size=12)
       axes[i,3].annotate('Continuum',xy=[-5.5,5.],ha='right',size=12)
       axes[i,4].annotate('Qphi',xy=[-5.5,5.],ha='right',size=12)
    else:
       ax.get_xaxis().set_visible(False)
       ax.get_yaxis().set_visible(False)
       ax.annotate(label[i],xy=[5.5,5.],ha='left',size=12)

    if (file=='blank'):
       img = np.zeros((256,256))
       ax.imshow(img,cmap='inferno',vmin=0.,vmax=10.,extent=limits)

    elif (plot_type=='scatt'):
       CO = casa.Cube(dir+file,pixelscale=0.01225)
       CO.image = np.abs(np.nan_to_num(CO.image))
       fmax=np.max(CO.image)
       fmin=fmax/10000.
       CO.plot(iv=1,ax=ax,limits=limits,colorbar=cb,fmin=fmin,fmax=fmax,  # iv=1 for Qphi
               no_ylabel=no_ylabel,no_xlabel=no_xlabel,no_vlabel=True,no_clabel=True,color_scale='log') #,fmin=vsys-4.,fmax=vsys+4.)

    elif (plot_type=='line'):
       CO = casa.Cube(dir+file)
       lp = np.nansum(CO.image, axis=(1,2)) / CO._beam_area_pix()
       ax.plot(CO.velocity,lp)

       if (CO13[i] != 'blank'):
          cube2 = casa.Cube(dir+CO13[i])
          lp = np.nansum(cube2.image, axis=(1,2)) / cube2._beam_area_pix()
          ax.plot(cube2.velocity,lp,label='13CO')

       if (CS[i] != 'blank'):
          cube3 = casa.Cube(dir+CS[i])
          lp = np.nansum(cube3.image, axis=(1,2)) / cube3._beam_area_pix()
          ax.plot(cube3.velocity,lp,label='CS0')

       if (i==nx*ny-1):
          ax.legend()
       #CO.plot_line() #,fmin=vsys-4.,fmax=vsys+4.)
    elif (plot_type=='cont'):
       CO = casa.Cube(dir+file)
       #CO.image = np.nan_to_num(CO.image)
       CO.plot(ax=ax,limits=limits,Tb=True,colorbar=cb,fmin=2.,
               no_ylabel=no_ylabel,no_xlabel=no_xlabel,no_vlabel=True,no_clabel=True,) #,fmin=vsys-4.,fmax=vsys+4.)

    elif (plot_type=='all'):
       CO = casa.Cube(dir+file)
       CO.plot(ax=axes[i,0],moment=8,limits=limits,Tb=True,colorbar=cb,fmin=2.,
               no_ylabel=no_ylabel,no_xlabel=no_xlabel,no_vlabel=True,no_clabel=True,) #,fmin=vsys-4.,fmax=vsys+4.)

       if (CO13[i] != 'blank'):
          CO13i = casa.Cube(dir+CO13[i])
          CO13i.plot(ax=axes[i,1],moment=8,limits=limits,Tb=True,colorbar=cb,fmin=2.,
               no_ylabel=no_ylabel,no_xlabel=no_xlabel,no_vlabel=True,no_clabel=True,) #,fmin=vsys-4.,fmax=vsys+4.)

       if (CS[i] != 'blank'):
          CSi = casa.Cube(dir+CS[i])
          CSi.plot(ax=axes[i,2],moment=8,limits=limits,Tb=True,colorbar=cb,fmin=2.,
               no_ylabel=no_ylabel,no_xlabel=no_xlabel,no_vlabel=True,no_clabel=True,) #,fmin=vsys-4.,fmax=vsys+4.)

       if (cont[i] != 'blank'):
          conti = casa.Cube(dir+cont[i])
          conti.plot(ax=axes[i,3],limits=limits,Tb=True,colorbar=cb,fmin=2.,
               no_ylabel=no_ylabel,no_xlabel=no_xlabel,no_vlabel=True,no_clabel=True,) #,fmin=vsys-4.,fmax=vsys+4.)

       if (scatt[i] != 'blank'):
          scatti = casa.Cube(dir+scatt[i],pixelscale=0.01225)
          scatti.image = np.abs(np.nan_to_num(scatti.image))
          fmax=np.max(scatti.image)
          fmin=fmax/10000.
          scatti.plot(iv=1,ax=axes[i,4],limits=limits,colorbar=cb,fmin=fmin,fmax=fmax,  # iv=1 for Qphi
               no_ylabel=no_ylabel,no_xlabel=no_xlabel,no_vlabel=True,no_clabel=True,color_scale='log') #,fmin=vsys-4.,fmax=vsys+4.)
    else:
       CO = casa.Cube(dir+file)
       CO.plot(ax=ax,moment=8,limits=limits,Tb=True,colorbar=cb,fmin=0.,
               no_ylabel=no_ylabel,no_xlabel=no_xlabel,no_vlabel=True,no_clabel=True,) #,fmin=vsys-4.,fmax=vsys+4.)

plt.savefig('gallery-'+plot_type+'.pdf',bbox_inches='tight')
plt.savefig('gallery-'+plot_type+'.png',dpi=800,bbox_inches='tight')

#plt.show()
