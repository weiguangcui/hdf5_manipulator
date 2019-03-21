#! /bin/bash

path=/store/multidark/NewMD_3840_Planck1/Galacticus/latest/fat/
for i in ${path}*_results.hdf5
  do 
    fname=`basename "$i"`
    echo $fname
    ./extract.py --input $i  --output ./snapshot_125/$fname  --keys '/Outputs/Output79/nodeData'
    ./extract.py --input $i  --output ./snapshot_107/$fname  --keys '/Outputs/Output61/nodeData'
    ./extract.py --input $i  --output ./snapshot_092/$fname  --keys '/Outputs/Output46/nodeData'
    ./extract.py --input $i  --output ./snapshot_075/$fname  --keys '/Outputs/Output29/nodeData'
    ./extract.py --input $i  --output ./snapshot_052/$fname  --keys '/Outputs/Output6/nodeData'
  done
