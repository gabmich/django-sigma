import os, json, random
import pandas as pd
from django.conf import settings
from django.shortcuts import render


def index(request, filename, first_column_name, second_column_name):
    """
    
    """
    # init empty nodes and edges
    nodes, edges = [], []

    # load file in 'media' folder (at project root)
    file_path = os.path.join(settings.MEDIA_ROOT, filename)
    abi_df = pd.read_excel(file_path)

    mon_set_de_numeros = set()
    
    for index, row in abi_df.iterrows():
        mon_set_de_numeros.add(str(row[first_column_name]))
        mon_set_de_numeros.add(str(row[second_column_name]))

    for i in mon_set_de_numeros:
        node = {
                "id": i,
                "label": i,
                "x": random.randint(0, 100),
                "y": random.randint(0, 100),
                "size": 1,
                "color": "blue"
        } 
        nodes.append(node)

    for index, row in abi_df.iterrows():
        edge = {
            "id": f"edge{random.randint(0,9999999)}",
            "source": str(row[first_column_name]),
            "target": str(row[second_column_name]),
            "type": 'dotted'
        }
        edges.append(edge)

    # prepare a 'data' object with nodes and edges lists
    data = {'nodes':json.dumps(nodes), 'edges':json.dumps(edges)}

    return render(request,'sigma/index.html',data)
