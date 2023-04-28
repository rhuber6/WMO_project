import geopandas as gpd
import pandas as pd
import glob

dir = "/Users/rachel1/Downloads/grdc_points/"

dir_gpkg = "/Users/rachel1/Downloads/streamnet_grdc/*.gpkg"

for file in glob.glob(dir_gpkg):
    num = file[-18:-8]
    points_dir = dir + num + "_with_stream_grdc.csv"
    stream_points = pd.read_csv(points_dir)
    stream_points = stream_points.drop(["me_sim", "mae_sim", "rmse_sim", "r2_sim", "mape_sim", "nse_sim", "kge_sim", "me_corr", "mae_corr", "rmse_corr", "r2_corr", "mape_corr", "nse_corr", "kge_corr", "me_diff", "me", "mae", "rmse_diff", "rmse", "kge_diff", "kge", "r2_diff", "r2", "nse_diff", "nse", "mape_diff", "mape", "index_right"], axis=1)
    streams = gpd.read_file(file, ignore_geometry=True)
    print("finished reading file")
    upstream_area = []
    for val in stream_points["streamID"]:
        area = streams.loc[streams["LINKNO"] == val, "DSContArea"].values[0]
        upstream_area.append(area)
    print("finished loop")
    stream_points["upstream_area_check"] = upstream_area
    #stream_points["upstream_area_check"] = stream_points["upstream_area_check"] / 1000 / 1000
    #if "Upstream_area_" not in stream_points.columns:
        #stream_points["Upstream_area_"] = stream_points["Upstream_area"]
    #stream_points["ratio"] = stream_points["upstream_area_check"] / stream_points["Upstream_area_"]
    #stream_points_sorted = stream_points.sort_values(by=["ratio"])
    stream_points.to_csv(f"/Users/rachel1/Downloads/missed_upstream/{num}_upstream_grdc.csv")
    print(num)
