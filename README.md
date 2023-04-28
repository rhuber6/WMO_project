# WMO_project
These are the scripts I used when doing the WMO project. I am putting them here in hopes they can be helpful when the project is done again in the future. All the files are on box under WMO State of Water

##Basic Work Flow followed:

1. Intersect points with hydro tdx basins on arcgis/qgis to get the hydrobasin that corresponds with each point - or use intersect_grdc.py
2. Seperate the points into their corresponding basins by making a csv for each one.  The code for this should be in seperate.py and just the directories will need to be changed.
3. Intersect all the points with the basin files from the tdx hydro  - this was originally done on a remote aws computer that had all the geopackages for the basins already saved on it. These shapefiles take up a lot of space. The script should be the main.py script, but it may need some alterations, because it has been edited a bit since the original time it was run.
4. Add the upstream area to the the points from our model. Use the upstream.py file for this. You will need to have access to the geopackages of all the streamnets. The upstream area is saved in these files. Then used the csvs from the previous files that already have the streamIDs attached to them.
5. Go through and edit by hand the files with the bad ratios. Make changes in the csvs and then also record elsewhere - our recorded changes are saved in box.
6. Some of the points will have been skipped because they are on the coast, so you will need to go back and get those values - unless you figure out how to do this in an earlier step. We didn't realize this would happen, so this was done in the next step. I made a csv with all the missed points from the original file. I used the file that already had them assigned to a hydrotdx basin. We accounted for these points by buffering them and then running the intersection again - use main.py but just uncomment the information about buffering.
7. Get the upstream area again for all these points - use upstream.py
8. Loop through and figure out with upstream area produced the best ratio because some may have intersected with multiple stream after being buffered. - skipped_ratio.py. This file will also output a list a folder of any points that were still skipped.
9. Go through and fix the bad ratios by hand in arcGIS or QGIS - record the changes
10. Make the final csv by merging all the files together, deleting unnecessary columns. Check for any missed points again. Check for duplicate points
