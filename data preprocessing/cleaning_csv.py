import pandas as pd
import ast
from collections import defaultdict
import os
import csv
from xml.etree.ElementTree import parse, Element, SubElement, ElementTree
import xml.etree.ElementTree as ET

df=pd.read_csv("annotation.csv")

xmin=[ast.literal_eval(i)[0] for i in df["bottom left"].values]
ymin=[ast.literal_eval(i)[1] for i in df["bottom right"].values]
xmax=[ast.literal_eval(i)[0] for i in df["bottom right"].values]
ymax=[ast.literal_eval(i)[1] for i in df["top right"].values]
w=[int(str(i).split("*")[0]) for i in df["resolution"].values]
h=[int(str(i).split("*")[1]) for i in df["resolution"].values]
#['NAME_ID', 'XMIN', 'YMIN', 'W', 'H', 'XMAX', 'YMAX']
df_new=pd.DataFrame()
df_new["NAME_ID"]=[i.strip() for i in df["NAME "].values]
df_new["XMIN"]=xmin
df_new["YMIN"]=ymin
df_new["W"]=w
df_new["H"]=h
df_new["XMAX"]=xmax
df_new["YMAX"]=ymax

df_new.to_csv("annotation-cleaned.csv",index=False)