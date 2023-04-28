import pandas as pd
from zipfile import ZipFile
import glob
import os

# this should be a directory to the csv files that have the csvs created from buffering the skipped files and adding the upstream area
dir_streams = "/content/skipped/"

# this should be the file with all the streams split into their respective files before any streamID was added
dir = "/content/content/basins/*"

# this is the csv with all the points and their assigned basins - the csv created from originally intersecting the points with the tdxhydro basins
basins = pd.read_csv("/content/all_basins.csv")

still_skipped = []

for file in glob.glob(dir):
    num = file[-14:-4]
    print(num)
    all_points = pd.read_csv(file)
    points_dir = dir_streams + num + "_with_stream.csv"
    stream_id = pd.read_csv(points_dir)
    if len(stream_id.index) == 0:
        continue
    still_skipped.append(all_points.loc[~all_points['num'].isin(stream_id['num']), 'num'].tolist())
    stream_id["upstream_area_check"] = stream_id["DSContArea"] / 1000 / 1000
    stream_id["ratio"] = stream_id["upstream_area_check"] / stream_id["Upstream_area"]
    # Group the dataframe by the 'num' column
    grouped = stream_id.groupby('num')

    # Create an empty dataframe to store the selected rows
    selected_rows = pd.DataFrame()

    # Iterate through each group
    for name, group in grouped:
        # Find the row with the 'ratio' value closest to 1
        closest_row = group.loc[(group['ratio'] - 1).abs().idxmin()]
        # Add the closest row to the selected rows dataframe
        selected_rows = pd.concat([selected_rows, closest_row.to_frame().T])

    # Drop duplicate rows with respect to 'num'
    selected_rows.drop_duplicates(subset=['num'], inplace=True)
    selected_rows.drop(['Unnamed: 0.2', 'Unnamed: 0.1', 'Unnamed: 0', 'geometry',
                        'index_right', 'DSLINKNO', 'USLINKNO1', 'USLINKNO2',
                        'DSNODEID', 'strmOrder', 'Length', 'Magnitude', 'Length', 'Magnitude', 'strmDrop', 'Slope',
                        'StraightL', 'USContArea', 'WSNO', 'DOUTEND',
                        'DOUTSTART', 'DOUTMID', 'DSContArea'], axis=1, inplace=True)

    # return the csv with only the best ration value saved
    selected_rows.to_csv(f"/content/skipped_points_fixed/{num}_with_stream.csv")

values = [value for sublist in still_skipped for value in sublist]

subset = basins[basins['num'].isin(values)]
# this is the file of points that were still skipped
subset.to_csv("still_skipped_final.csv")
