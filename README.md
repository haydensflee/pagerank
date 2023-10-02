# pagerank
Python implementation of the PageRank algorithm on the [web-Google dataset](http://snap.stanford.edu/data/web-Google.html)

## Context
PageRank (PR) is an algorithm used by Google Search to rank websites in their search engine results. PageRank was named after Larry Page, one of the founders of Google. PageRank is a way of measuring the importance of website pages. According to Google:

_PageRank works by counting the number and quality of links to a page to determine a rough estimate of how important the website is. The underlying assumption is that more important websites are likely to receive more links from other websites._

**Algorithm** 
The PageRank algorithm outputs a probability distribution used to represent the likelihood that a person randomly clicking on links will arrive at any particular page. PageRank can be calculated for collections of documents of any size. It is assumed in several research papers that the distribution is evenly divided among all documents in the collection at the beginning of the computational process. The PageRank computations require several passes, called “iterations”, through the collection to adjust approximate PageRank values to more closely reflect the theoretical true value.

## Program
The implementation makes use of a node class that was written, which is a data structure that contains key information about a node such as its number, old and new pageranks, lists of incoming and outgoing nodes, and the size of these lists.
The first thing the program does is read in the input text file and convert all the provided information into the node dictionary data structure. This data structure stores nodes in a <key,value> pair, whereby the key is the node number and the value is the node object. For each line that is read from the text file, the program checks whether the FromNodeID and ToNodeID exists in the node dictionary (nodeDict), and either creates a new entry or updates the node object with the appropriate information. Afterwards, the initial pagerank values are set for all nodes and the actual algorithmic calculations can be performed
Before the mathematical logic was implemented the algorithm efficiency and methods for addressing with spider traps and dead ends were considered. Firstly the transition matrix method introduced in the lectures was considered. However, it became apparent that this was not an appropriate method to pursue, as there was a total number of 875713 nodes. Creating a transition matrix would need over 700 billion elements, of which only a tiny fraction is non-zero. When this was implemented, the runtime was exceedingly slow and meant that this method was ultimately unfeasible. Instead the pagerank algorithm was implemented using the mathematical equation that uses the total number of nodes and each node’s incoming and outgoing nodes. This mathematical equation also incorporated a damping factor, β=0.85, to perform taxation. This technique is a modified process of random surfer that allows the program to handle dead ends and spider traps by giving it a small probability to ‘teleport’ to a random page. Ultimately, the mathematical computation of each node’s pagerank is given by:

![image](https://github.com/haydensflee/pagerank/assets/89950637/5d043466-63a4-458c-b1c1-2e5272811df2)

- 𝑑 is the damping factor
- 𝑁 is the total number of pages
- 𝑝𝑖 is the page under consideration
- 𝑝𝑗 is the inbound page to 𝑝𝑖
- 𝑃𝑅 is the pagerank
- 𝐿 is the outgoing page count.

This was performed for 50 iterations which was sufficient for the pageranks to converge.
The pagerank information is stored into a dictionary that stores <nodenumber, pagreank>. This was then sorted in descending order of pageranks and written to two text files, one for the top 10 pageranks and one for all 875713 nodes.
