#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Luke
#
# Created:     12/11/2012
# Copyright:   (c) Luke 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from py2neo import neo4j
from py2neo import gremlin
import string, os, csv
import simplejson as json

def main():
    pass

#change to present working directory
os.chdir('C:\Documents and Settings\Luke\Desktop\supplier_buyer_graph')

#database connection
db = neo4j.GraphDatabaseService("http://ec2-23-20-102-175.compute-1.amazonaws.com:7474/db/data/")

#dictionary of all of the nodes
neo_index = csv.reader(open('graph_nodes.txt'), delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

neo_dict ={}

for company in neo_index:
    neo_dict[company[0]] = int(company[1])

table = csv.reader(open('relationships.csv'), delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
next(table)

for row in table:
    try:
        #subject
        user = "%s" % (row[0])
        node_start = neo_dict[user]

        #object
        user_sells = row[12]
        user_buys = row[13]

        #predicates
        #may be plural
        supplier_to = 'supplier_to'
        buyer_of = 'buyer_of'

        #create lists from csv
        reader = csv.reader([user_sells], delimiter=',',skipinitialspace=True)
        for r in reader:
            seller_list = r

        reader2 = csv.reader([user_buys], delimiter=',',skipinitialspace=True)
        for r in reader2:
            buyer_list = r


        #simulation of relationships

            #make true/false nodes
            #b2b
            #b2c
            #every_strategy
            #every_role

            #get the properties of the starting node
            #get the properties of the ending node
            #case or if/then add_link

        #execution script
        for buyer in seller_list:
            gremlin_script = "g.addEdge(g.v(%s),%s, %s)" % (node_start, supplier_to, buyer)
            print gremlin_script

        for seller in buyer_list:
            gremlin_script2 = "g.addEdge(g.v(%s),%s, %s)" % (node_start, buyer_of, seller)
            print gremlin_script2

        #gremlin.execute(gremlin_script, db)

    except:
        print "error" + user
        continue


if __name__ == '__main__':
    main()
