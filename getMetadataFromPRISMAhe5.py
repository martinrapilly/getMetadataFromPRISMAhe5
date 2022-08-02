#Name: getMetadataFromPRISMAhe5.py
#Description: reads he5 PRISMA files content to access any metadata information.
#Note: HDFview (free software available on the web) is a good start to see the structure (groups and datasets) and values of your PRISMA he5 metadata. This script allows your to extract those data and use it for an analysis
#Note: a detailed explanation of all metadata values is available here: http://prisma.asi.it/missionselect/docs/PRISMA%20Product%20Specifications_Is2_3.pdf
#Author: martin rapilly, mrapilly60@uasd.edu.do/martin.rapilly@get.omp.eu
#Universidad Autónoma de Santo Domingo (Dominican Republic)/ Université Toulouse III Paul Sabatier, laboratoire GET (France)

#import libraries
import h5py
import numpy as np
import matplotlib.pyplot as plt
import xarray as xr
import pandas as pd
from itertools import chain
import gdal, osr

#enter your filepath here
filename=r"C:\...\foo.he5"

#open he5 file
f = h5py.File(filename,'r')
print ("f.name",f.name)


#he5 files are made of groups and datasets
#Some metada are located in the root group (referenced just as "/"). Use the attrs object to access those metada
#To see what is inside the root group attributes, use this:
for x in f.attrs:
    print (x)
#To get values from one attribute, for instance the central wavelength of all Visible and Near-Infrared (VNIR) and Short-wave Infrared (SWIR) bands, use this:
List_Cw_Vnir = f.attrs['List_Cw_Vnir']
List_Cw_Swir = f.attrs['List_Cw_Swir']
print ("List_Cw_Vnir",List_Cw_Vnir)
print ("List_Cw_Swir",List_Cw_Swir)


#to get a list of groups and datasets available (other than the root group), use this:
def print_name(name, obj):
    if isinstance(obj, h5py.Dataset):
        print ('Dataset:', name)
    elif isinstance(obj, h5py.Group):
        print ('Group:', name)
with h5py.File(filename, 'r')  as f: # file will be closed when we exit from WITH scope
    f.visititems(print_name)


    #to read data values, use this:
    
    #read SWIR and VNIR cube contents.
    #Note: HCO stands for Hyperspectral cube whereas PCO stands for Panchromatic cube 
    SWIRcube = f['HDFEOS/SWATHS/PRS_L2D_HCO/Data Fields/SWIR_Cube'][()]#[()] is to get the value. Can be replaced with .value
    VNIRcube = f['HDFEOS/SWATHS/PRS_L2D_HCO/Data Fields/VNIR_Cube'][()]
    #print the shapes of both cubes:
    print ("SWIRcube.shape",SWIRcube.shape)#prints number of rows, bands and columns
    print ("VNIRcube.shape",VNIRcube.shape)#prints number of rows, bands and columns
    #get values from a cube:
    print ("VNIRcube[500][30][600]",VNIRcube[500][30][600])#get value from pixel with row no.500, column no.600 and band 30
    
    #read latitude and longitude contents
    lat = f['HDFEOS/SWATHS/PRS_L2D_HCO/Geolocation Fields/Latitude'][()]
    lon = f['HDFEOS/SWATHS/PRS_L2D_HCO/Geolocation Fields/Longitude'][()]
    #print the shapes of latitude and longitude arrays
    print ("lat.shape",lat.shape)
    print ("lon.shape",lon.shape)

   
       

    
   


        
        
