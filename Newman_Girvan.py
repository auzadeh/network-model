import networkx as nx
from networkx import *
import operator
from operator import itemgetter
import sys
import math
import random
from random import choice

#import psyco
#psyco.full()

class CreateNetwork(object):
    ''' ref : Girvan, Michelle, and Mark EJ Newman. Community structure in social and biological networks.
    Proceedings of the National Academy of Sciences 99, no. 12 (2002): 7821-7826.'''
    def newman_girvan_graph(self,node_count,edge_count,community_count,pin,pout):
		
        newmanGraph = nx.Graph()
        newmanGraph.add_nodes_from(range(node_count))
        newmanGraph.name="newman_randomCluster_graph(%s,%s)"%(node_count,edge_count)
        if node_count ==1:
            return newmanGraph
        max_edges=node_count*(node_count-1)
        max_edges/=2.0
        if edge_count>=max_edges:
            return complete_graph(node_count,create_using=newmanGraph)
        nlist=newmanGraph.nodes()
        nodes = {}
        edge_in = pin * edge_count
        edge_out = pout * edge_count

        for community in range(community_count):
            for i in range(node_count/community_count):
                selectedNode = random.choice(nlist)
                nodes[selectedNode]= community #[community,pin,pout]
                nlist.remove(selectedNode)
        nlist=newmanGraph.nodes()
        edge_count=0
        edge_in_count =0
        edge_out_count = 0
        while edge_count < edge_count:
            # generate random edge,u,v
            u = random.choice(nlist)
            v = random.choice(nlist)
            if u==v or newmanGraph.has_edge(u,v):
                continue
            else:
                if nodes[u] == nodes[v]:
                    if edge_in_count <= edge_in:                            
                        newmanGraph.add_edge(u,v)
                        edge_count=edge_count+1
                        edge_in_count +=1
                    else:
                        continue
                else:
                    if edge_out_count < edge_out:
                        newmanGraph.add_edge(u,v)
                        edge_count=edge_count+1
                        edge_out_count +=1
                    else:
                        continue
        return newmanGraph, nodes

    def generateGraph(self,node_count,edge_count,z,community_count,pin,pout):
        graphI , nodes = self.newman_girvan_graph(node_count,edge_count,community_count,pin,pout)
        return graphI , nodes

if __name__ == '__main__':
    node_count =1024
    z=20
    edge_count= node_count * z /2
    pin = 0.8
    pout=0.2
    community_count = 4
    networkModelObj = CreateNetwork()
    graph,node = networkModelObj.generateGraph(node_count,edge_count,z, community_count,pin,pout)
    print graph.nodes()
    print node
