def greedy_configuration(degree_distribution):
    
    #Creating graph
    G=nx.empty_graph()
    
    #Creating nodes
    nodes=list(np.arange(0,len(degree_distribution)))
    G.add_nodes_from(nodes)
    
    #The number of stubs per node will be exactly the same as the degree_distribution.
    stubs=degree_distribution.copy()
    for i in range(len(stubs)):
        
        #Getting the node with the highest degree
        current_node=stubs.index(max(stubs))
        
        #Checking if there is only one node left with stubs.
        if(sum(stubs)==stubs[current_node] and stubs[current_node]!=0) : 
            print('Only one node left with stubs : ', current_node,' with ' , sum(stubs),'stubs')
            return G
        
        #Checking if there are no more stubs
        if(stubs[current_node]==0) : 
            print('No more nodes with stubs!')
            return G
        
        #emptying the stubs of the current node to avoid self loop.
        degree=stubs[current_node]
        stubs[current_node]=0

        for j in range(degree):

            target_node=current_node
            
            #Make sure no self loop is created or no node with no more stubs is selected
            while((target_node==current_node or stubs[target_node]==0) and sum(stubs)!=stubs[target_node]):
                target_node=random.randint(0,len(nodes)-1)
            
            
            stubs[target_node]-=1
            
            #Adding an weight if the edge exists
            if(G.has_edge(current_node,target_node)) : 
                G.edge[current_node][target_node]['weight'] += 1
            
            #adding edge if the edge doesn't already exist
            else : 
                G.add_edge(current_node,target_node,weight = 1)

    return G