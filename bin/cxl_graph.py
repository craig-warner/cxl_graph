#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
CXL Graph
author: Craig Warner
    A program to develop really large graphs to stress test CXL memory systems
"""

import igraph as ig
import argparse
import matplotlib.pyplot as plt

from version import __version__

def DoSample():
    # Construct a graph with 5 vertices
    n_vertices = 5
    edges = [(0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 3), (1, 4), (3, 4)]
    g = ig.Graph(n_vertices, edges)

    # Set attributes for the graph, nodes, and edges
    g["title"] = "Small Social Network"
    g.vs["name"] = ["Daniel Morillas", "Kathy Archer", "Kyle Ding", "Joshua Walton", "Jana Hoyer"]
    g.vs["gender"] = ["M", "F", "F", "M", "F"]
    g.es["married"] = [False, False, False, False, False, False, False, True]

    # Set individual attributes
    g.vs[1]["name"] = "Kathy Morillas"
    g.es[0]["married"] = True

    # Plot in matplotlib
    # Note that attributes can be set globally (e.g. vertex_size), or set individually using arrays (e.g. vertex_color)
    fig, ax = plt.subplots(figsize=(5,5))
    ig.plot(
        g,
        target=ax,
        layout="circle", # print nodes in a circular layout
        vertex_size=30,
        vertex_color=["steelblue" if gender == "M" else "salmon" for gender in g.vs["gender"]],
        vertex_frame_width=4.0,
        vertex_frame_color="white",
        vertex_label=g.vs["name"],
        vertex_label_size=7.0,
        edge_width=[2 if married else 1 for married in g.es["married"]],
        edge_color=["#7142cf" if married else "#AAA" for married in g.es["married"]]
    )

    plt.show()

    # Save the graph as an image file
    fig.savefig('data/sample/social_network.png')
    fig.savefig('data/sample/social_network.jpg')
    fig.savefig('data/sample/social_network.pdf')

    # Export and import a graph as a GML file.
    g.save("data/sample/social_network.gml")
    g = ig.load("data/sample/social_network.gml")

def DoAnalyze(ifile):
    if args.verbose:
        print("Info: Loading Graph")
    g = ig.load(ifile)
    if args.verbose:
        print("Info: Done Loading Graph")
        print("Info: Total Verticies=",g.vcount())
        print("Info: Total Edges=",g.ecount())
    if args.verbose:
        print("Info: Generating Neighbors")
    neis=[] 
    vn=0
    for v in g.vs: 
        l_neis = g.neighbors(vn)
        print("Info: Vertice:",v," has ",len(l_neis)," neighbors")
        neis.append(l_neis)
        for nv in l_neis:
            print ("    ",nv)
        vn=vn+1
    if args.verbose:
        print("Info: Done Generating Neighbors")


# CLI Parser
parser = argparse.ArgumentParser(description='CXL Graph')
parser.add_argument("--ifile", help="Graph file (.gml)", default="data/sample/social_network.gml")
parser.add_argument("--gen_sample", help="Generate a sample", action = "store_true")
parser.add_argument("--analyze_graph", help="Analyze a graph", action = "store_true")
parser.add_argument("-v", "--verbose", help="Increase output verbosity",action ="store_true") 
parser.add_argument('-V', '--version', action='version', version="%(prog)s ("+__version__+")")
args = parser.parse_args()

if args.gen_sample:
    DoSample()
elif args.analyze_graph:
    DoAnalyze(args.ifile)
