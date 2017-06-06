from qgis.core import QgsProject, QgsPoint, QgsRasterLayer, QgsMapLayerRegistry
from PyQt4.QtCore import QFileInfo
from qgis.utils import iface
import time

COORD_CENTER = QgsPoint(-5482440, -1884950)

def load_project():
    layer = QgsRasterLayer("/home/heltucosta/Desktop/GISData/my_file.xml", "map")
    QgsMapLayerRegistry.instance().addMapLayer(layer)
    while QgsMapLayerRegistry.instance().count() == 0:
	    pass
    print("load finished")
    iface.mapCanvas().setCenter(COORD_CENTER)
    iface.mapCanvas().zoomScale(180000)
    update_canvas()

def update_canvas():
    iface.addRasterLayer("/home/heltucosta/Desktop/GISData/homicidios_gyn.tiff", "homicidios")
    iface.addVectorLayer('/home/heltucosta/Desktop/GISData/cameras_2016_final.shp', 'cameras', 'ogr')
    iface.addVectorLayer('/home/heltucosta/Desktop/GISData/expansao_gyn_sirgas.shp', 'expansao', 'ogr')
    print('fim de update')

iface.actionShowPythonDialog().trigger()
iface.initializationCompleted.connect(load_project)
