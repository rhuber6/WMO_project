import geopandas as gpd
import pandas as pd

grdc_points = gpd.read_file("/Users/rachel1/Downloads/bootstrap_gauges.gpkg")
print("gauges read in")
grdc_points_europe = grdc_points[grdc_points['model_id'].str.startswith('12')]
for_intersection = grdc_points_europe.to_crs("EPSG:3857")
for_intersection.drop(['me_sim', 'mae_sim',
       'rmse_sim', 'r2_sim', 'mape_sim', 'nse_sim', 'kge_sim', 'me_corr',
       'mae_corr', 'rmse_corr', 'r2_corr', 'mape_corr', 'nse_corr', 'kge_corr','me_diff', 'me', 'mae_diff', 'mae',
       'rmse_diff', 'rmse', 'kge_diff', 'kge', 'r2_diff', 'r2', 'nse_diff',
       'nse', 'mape_diff'], axis=1, inplace=True)

gdf = gpd.read_file("/content/europe-geoglows-catchment.shp")

intersections = gpd.sjoin(gdf, for_intersection, predicate='intersects')