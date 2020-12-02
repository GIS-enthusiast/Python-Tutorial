##Creating a simple Message Box
#
#mb = QMessageBox()
#mb.setText('Click OK to confirm')
#mb.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
#return_value = mb.exec()
#
#if return_value == QMessageBox.Ok:
#    print('You pressed ok')
#elif return_value == QMessageBox.Cancel:
#    print('You pressed cancel')

## Calculating Distance of a line defined by three points.
san_francisco = (37.7749, -122.4194)
new_york = (40.661, -73.944)
las_vegas = (36.1699, -115.1398)

d = QgsDistanceArea()
d.setEllipsoid('WGS84')

lat1, lon1 = san_francisco
lat2, lon2 = new_york
lat3, lon3 = las_vegas

point1 = QgsPointXY(lat1, lon1)
point2 = QgsPointXY(lat2, lon2)
point3 = QgsPointXY(lat3, lon3)

#line1 = QgsGeometry.fromPolyline([point1, point2, point3])#QgsGeometry.length is cartisan and we need geographic, ie. QgsDistanceArea.

distance1 = d.measureLine(point1, point3)
distance2 = d.measureLine(point3, point2)
total_distance = distance1 + distance2

#instantiating an object of the QgsUnitTypes class. The method DistanceUnit() below can return the distance in miles.
units = QgsUnitTypes()

print(f'the distance in kilometers is {total_distance/1000}')

print(f'The distance in miles is {d.convertLengthMeasurement((total_distance), units.DistanceUnit(5))}') #miles = 5, kilometres = 1

## Change the title to MyQIS
title = iface.mainWindow().windowTitle()
new_title = title.replace('QGIS', 'MyQGIS')
iface.mainWindow().setWindowTitle(new_title)

## Change the QGIS logo 
import os

icon = 'qgis-black.png'
data_dir = r'C:\Users\Shane Rich\Downloads\pyqgis_in_a_day\pyqgis_in_a_day'
icon_path = os.path.join(data_dir, icon)
icon = QIcon(icon_path)
iface.mainWindow().setWindowIcon(icon)

## Add something to the menu (in this case help menu)

import webbrowser

def open_gis_se():
    webbrowser.open('https://gis.stackexchange.com')

iface.helpMenu().addSeparator()

gis_se_action = QAction('Go to gis.stackexchange')
iface.helpMenu().addAction(gis_se_action)
gis_se_action.triggered.connect(open_gis_se)

