#coding= utf-8
"""-----------------------------------------------------------------------------
  Script Name: Analyzing movement patterns of wolf
  Description: Generate Minimum bounding geometry for all wolf types
  Created By:  Gifty. E. A. Attiah
  Date:        28 May, 2019.
-----------------------------------------------------------------------------"""
import arcpy
import os
import sys
from arcpy import env

arcpy.env.overwriteOutput = True

Database = arcpy.GetParameterAsText(0)

Query = arcpy.GetParameterAsText(1)

inputFile = arcpy.GetParameterAsText(2)

outDir = arcpy.env.workspace = arcpy.GetParameterAsText(3)

newDir = arcpy.GetParameterAsText(4)

arcpy.Select_analysis (Database, inputFile, Query) 


# Reads shapefile for different values in the attribute
rows = arcpy.SearchCursor(inputFile)
row = rows.next()
attribute_types = set([])

while row:
    attribute_types.add(row.Genetik_ag) 
    row = rows.next()

# Output a Shapefile for each different attribute
for each_attribute in attribute_types:
    arcpy.Select_analysis (inputFile, os.path.join(outDir, each_attribute), "\"Genetik_ag\" = '" + each_attribute + "'") 


Wolf_Shapes = arcpy.ListFeatureClasses("*.shp")

for Wolf_Shape in Wolf_Shapes:
    if Wolf_Shape.startswith("GW"):
        Wolfshape = Wolf_Shape
        name = Wolf_Shape.split("_MBG")[0] # Extract part of the name
        out_feature_class = os.path.join(newDir,name)
        arcpy.MinimumBoundingGeometry_management(Wolfshape, out_feature_class, "CONVEX_HULL")
    arcpy.Delete_management(Wolf_Shape)
   
arcpy.Delete_management(inputFile)

    
del rows, row, attribute_types


#END
