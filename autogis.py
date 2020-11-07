import geopandas as gpd
import pandas as pd
import datetime


data = gpd.read_file(
    r"C:\Users\Shane Rich\Auto_GIS\final-assignment-GIS-enthusiast\5785642")

# Select data.
# Removes no value data, as no data value = -1.
selection = data.loc[(data['pt_r_t'] >= 0) & (data['car_r_t'] >= 0)]
selection = selection[['pt_r_t', 'car_r_t', 'geometry']]
selection['diff'] = selection['pt_r_t'] - selection['car_r_t']
print(selection.head())

# Return results as a number of Shapefiles or a Geopackage with multiple layers.
if output_format == "shp":
    data.to_file(Path(
        output_folder,
        Path(path).stem[-7:])
    )  # output_folder, Path(path).stem,
elif output_format == "gpk":
    # save to the same geopackage and label the layers as per the ID using Path().stem[-7:]
    data.to_file(Path(
        output_folder,
        "TravelMatrix.gpkg"),
        driver="GPKG",
        layer=Path(path).stem[-7:])
