import os

n_estimators=[100,200,220,150]
max_depth=[10,16,22,3]
for n in n_estimators:
    for m in max_depth:
        os.system(f"python basic_mlmodel.py -n {n} -m {m}")
    