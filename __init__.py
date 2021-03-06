# -*- coding: utf-8 -*-
"""
/***************************************************************************
 FTM
                                 A QGIS plugin
 plugin om het FTM te gebruiken
                             -------------------
        begin                : 2015-10-08
        copyright            : (C) 2015 by John van Dam
        email                : jpcvandam@gmai.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load FTM class from file FTM.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .FTM import FTM
    return FTM(iface)
