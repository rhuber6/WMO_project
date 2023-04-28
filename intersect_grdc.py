import geopandas as gpd
import pandas as pd

grdc_gauges = gpd.read_file("/Users/rachel1/Downloads/bootstrap_gauges.gpkg")
print("gauges read in")

basins = gpd.read_file("/Users/rachel1/Downloads/hydrobasins_level2.geojson")
print("basins read in")
intersections = gpd.sjoin(grdc_gauges, basins, predicate='intersects')
print("did intersection")
intersections.to_csv("grdc_points_assigned.csv")