import networkx as nx

from networkx import *
import operator
from operator import itemgetter
import sys
import math
import random
from random import choice

import networkx as nx
#import psyco
#psyco.full()

class CreateNetwork(object):

    def ranking_model_graph(self,node_count, alpha, avrgDegree,seed=None):
        my_graph = nx.Graph()
        my_graph.add_edges_from([(1,2)])
        random.seed(seed)
        while len(my_graph)<node_count:
            node_degree = my_graph.degree()
            degree_nodes_map = {}
            for node in node_degree:
                degree_nodes_map.setdefault(node_degree[node], []).append(node)
            degree_sortedlist =sorted(degree_nodes_map.iterkeys(),reverse=True)
            new_node = len(my_graph.nodes())+1
            min_rank= len(degree_sortedlist)
            sum_rank =0.0
            rank = 1
            for degree in degree_sortedlist:
                sum_rank += math.pow(float(1)/rank,alpha)* len(degree_nodes_map[degree])
                rank += len(degree_nodes_map[degree])
            my_graph.add_node(new_node)
            new_node_edge_count = round(avrgDegree)/2
            rank =1
            m = 0
            node_prob ={}
            for degree in degree_sortedlist:
                for other_node in degree_nodes_map[degree]:
                    node_prob[other_node] = float(math.pow(float(1)/rank, alpha)) / sum_rank
                rank += len(degree_nodes_map[degree])
            p_sump={}
            for node in node_prob:
                if node ==1:
                    p_sump[node]=node_prob[node]
                else:
                    p_sump[node] =p_sump[node-1] + node_prob[node]
            count_edges = 0
            seen_list = []
            if new_node >new_node_edge_count:
                while count_edges < new_node_edge_count:
                    random_number = random.random()
                    for node in sorted(p_sump.iteritems(), key=operator.itemgetter(1)):
                        if random_number < node[1]:
                            if not node[0] in seen_list:
                                my_graph.add_edge(new_node, node[0])
                                count_edges +=1
                                seen_list.append(node[0])
                            break
            else:
                for node in p_sump:
                    my_graph.add_edge(new_node, node)
        return my_graph



    def generateGraph(self,node_count,rm_alpha,z):
	    graph = self.ranking_model_graph(node_count, rm_alpha, z,seed=None)
	    return graph


if __name__ == '__main__':
    
    node_count =1024
    z=20
    edge_count= node_count * z /2
    alpha= 0.5
    networkModelObj = CreateNetwork()
    graph = networkModelObj.generateGraph(node_count, alpha,z)
    print graph.nodes()
    degree_count ={}
    for node in graph.nodes():
        if not degree_count.has_key(graph.degree(node)):
            degree_count[graph.degree(node)]=1
        else:
            degree_count[graph.degree(node)]+=1
    for degree in degree_count:
        degree_count[degree] /= float(node_count)
    dic_count= sorted(degree_count.iteritems())
    print dic_count









