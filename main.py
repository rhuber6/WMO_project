import geopandas as gpd
import pandas as pd
from zipfile import ZipFile
import glob
import os

# with ZipFile("/Users/rachel1/Downloads/basins_skipped.zip", 'r') as zObject:
# Extracting all the members of the zip
# into a specific location.
# zObject.extractall(
# path="/Users/rachel1/Downloads/ALL_BASINS")
# path to csv files
dir = "/Users/rachel1/Downloads/basins_grdc/basins/"

# path to basins

dir_gpkg = "/Users/rachel1/Downloads/tdxhydro_basins_20s_europe/*.gpkg"

# buffer_distance = 0.04

for file in glob.glob(dir_gpkg):
    num = file[-18:-8]
    print(num)
    points_dir = dir + num + ".csv"
    points = pd.read_csv(points_dir)
    gdf = gpd.GeoDataFrame(points, geometry=gpd.points_from_xy(points['lon_gauge'], points['lat_gauge']))
    gdf = gdf.drop('index_right', axis=1)
    print("finished reading in gpkg")
    # Buffer the point geometries
    # gdf.geometry = gdf.geometry.buffer(buffer_distance)

    gdf = gdf.set_crs('EPSG:4326')
    gdf.reset_index(drop=True, inplace=True)
    # print("buffered")
    geopackage = gpd.read_file(file)
    print("finished reading file")

    geopackage = gpd.sjoin(gdf, geopackage, predicate='intersects')
    # this is the name of the csv that will be produced - idk what directory you will want it save to
    geopackage.to_csv(f"{num}_with_stream_grdc.csv")
    print("made_csv")
