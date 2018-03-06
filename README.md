# PageRanking-in-Python

The links that were obtained from crawling are used for this code.

A graph is made out of the links that were obtained by running BFS and DFS in the webcrawler code(Available on this repository)

The file "codetomakegraph" is used to develop the graph which acts as an input for the PageRank code.

The graphs obtained are : bfsgraph and dfsgraph

The pagerank algorithm generates a file with  the pagerank of the top 50 links and also a file with the inlink counts.

This code also calcuates the perplexity until pagerank is converged. PageRank can be considered as converged if the change in perplexity is
less than 1 for at least four consecutive iterations.

