#!/usr/bin/env python
import re, sys,os

#open xyz trajectory in the current in directory

directory=os.getcwd()

for filename in os.listdir(directory):
    if filename.endswith(".xyz"):
        f1_o = open(filename, "r")
        lines = f1_o.readlines()
        f1_o.close()

#get line of [Atoms]
n_atoms = int(lines[0]) +2
#print(n_atoms)


#generate an array of frames
frame=[]
frame_collection = []
for i in range(len(lines)):
    k=i%n_atoms
    frame.append(lines[i])
    if k==n_atoms-1:
        frame_collection.append(frame)
        frame=[]


#print(frame_collection)
i=0
for r in frame_collection:
    file2 = "x" + str(i).zfill(4) + ".xyz"
    f2_o = open(file2, "w")
    f2_o.writelines(r)
    i=i+1
    f2_o.close
