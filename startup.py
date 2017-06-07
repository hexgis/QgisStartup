from qgis.core import QgsProject, QgsPoint, QgsRasterLayer, QgsMapLayerRegistry
from PyQt4.QtCore import QFileInfo
from qgis.utils import iface
import time, os

COORD_CENTER = QgsPoint(-5482440, -1884950)
home_path = os.path.realpath(QgsProject.instance().readPath("./"))

def load_project():
    layer = QgsRasterLayer(home_path + "/GISData/my_file.xml", "map")
    QgsMapLayerRegistry.instance().addMapLayer(layer)
    print("")
    iface.mapCanvas().setCenter(COORD_CENTER)
    iface.mapCanvas().zoomScale(180000)
    update_canvas()

def update_canvas():
    iface.addRasterLayer(home_path + "/GISData/homicidios_gyn.tiff", "homicidios")
    iface.addVectorLayer(home_path + '/GISData/cameras_2016_final.shp', 'cameras', 'ogr')
    iface.addVectorLayer(home_path + '/GISData/expansao_gyn_sirgas.shp', 'expansao', 'ogr')
    #print('fim de update')

iface.actionShowPythonDialog().trigger()
iface.initializationCompleted.connect(load_project)
