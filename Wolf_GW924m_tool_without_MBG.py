#coding= utf-8
"""-----------------------------------------------------------------------------
  Script Name: Analyzing movement patterns of the GW924m
  Description: Extract GW924m from wolf data
               Selecting up to and after January,2019 movement points on definition query
               Showing movement direction of GW924m
               Table generation with distances between points
  Created By:  Gifty E. A. Attiah
  Date:        28 May, 2019.
-----------------------------------------------------------------------------"""
import arcpy
import os
import sys
from arcpy import env

arcpy.env.overwriteOutput = True

#WOLF SCRIPT

#DATA INPUTS AND OUTPUTS
Wolfdatenbank = arcpy.GetParameterAsText(0)

#Name and location of Wolf type
GW924m = arcpy.GetParameterAsText(1)

#Name and location of Data till January
GW924m_untill_Jan = arcpy.GetParameterAsText(2)

#Name and location of Data from February
GW924m_from_Feb = arcpy.GetParameterAsText(3)

#Name and location of Movement
Movement_GW924m = arcpy.GetParameterAsText(4)

#Name and location of Movement till Janurary
Movement_GW924m_untill_Jan = arcpy.GetParameterAsText(5)

#Name and location of Movement from February
Movement_GW924m_from_Feb = arcpy.GetParameterAsText(6)



#Query to select kind of  Wolf
Wolf_Query = where_clause = "Genetik_ag = 'GW 924m' OR Genetik_ag = 'GW924m'"

#Query to extract data till January
Till_Jan_Query = where_clause ="DATUM < date '2019-02-01 00:00:00'"

#Query to extract data from February
From_feb_Query = where_clause ="DATUM > date '2019-01-30 00:00:00'"


#DATA ANALYSIS


#Extraction by type of wolf
arcpy.Select_analysis(Wolfdatenbank,"GW924m",Wolf_Query)


#Extraction of data till January
arcpy.Select_analysis("GW924m","GW924m_untill_Jan",Till_Jan_Query)


#Extraction of data from february
arcpy.Select_analysis("GW924m","GW924m_from_Feb",From_feb_Query)

#Sort Fields

arcpy.Sort_management("GW924m",GW924m,"DATUM ASCENDING","UR")


arcpy.Sort_management("GW924m_untill_Jan",GW924m_untill_Jan,"DATUM ASCENDING","UR")


arcpy.Sort_management("GW924m_from_Feb",GW924m_from_Feb,"DATUM ASCENDING","UR")


#Add field
arcpy.AddField_management(GW924m,"Distance","DOUBLE")

arcpy.AddField_management(GW924m_untill_Jan,"Distance","DOUBLE")

arcpy.AddField_management(GW924m_from_Feb,"Distance","DOUBLE")


#Calculate distance

arcpy.CalculateField_management(GW924m,"Distance", "dist( !Shape! )","PYTHON","count = 0\ndef dist(shape):\n    global prev\n    global count\n    point = arcpy.PointGeometry(shape.getPart(0))\n    if count > 0:\n        distance = point.distanceTo(prev)\n    else:\n        distance = 0\n    prev = point\n    count = count+1\n    return distance")

arcpy.CalculateField_management(GW924m_untill_Jan,"Distance", "dist( !Shape! )","PYTHON","count = 0\ndef dist(shape):\n    global prev\n    global count\n    point = arcpy.PointGeometry(shape.getPart(0))\n    if count > 0:\n        distance = point.distanceTo(prev)\n    else:\n        distance = 0\n    prev = point\n    count = count+1\n    return distance")

arcpy.CalculateField_management(GW924m_from_Feb,"Distance", "dist( !Shape! )","PYTHON","count = 0\ndef dist(shape):\n    global prev\n    global count\n    point = arcpy.PointGeometry(shape.getPart(0))\n    if count > 0:\n        distance = point.distanceTo(prev)\n    else:\n        distance = 0\n    prev = point\n    count = count+1\n    return distance")



#Movement for selected data
arcpy.PointsToLine_management(GW924m,Movement_GW924m, Line_Field="", Sort_Field="DATUM", Close_Line="NO_CLOSE")

#Movement till Jan
arcpy.PointsToLine_management(GW924m_untill_Jan,Movement_GW924m_untill_Jan, Line_Field="", Sort_Field="DATUM", Close_Line="NO_CLOSE")

#Movement from Feb
arcpy.PointsToLine_management(GW924m_from_Feb, Movement_GW924m_from_Feb, Line_Field="", Sort_Field="DATUM", Close_Line="NO_CLOSE")








