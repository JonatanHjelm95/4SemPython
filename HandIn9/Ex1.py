import urllib.request
import io
import gzip
import networkx as nx
import matplotlib.pyplot as plt

def downloadFile(URL, path):
    response = urllib.request.urlopen(URL)
    compressed_file = io.BytesIO(response.read())
    decompressed_file = gzip.GzipFile(fileobj=compressed_file)

    with open(path, 'wb') as outfile:
        outfile.write(decompressed_file.read())

def readData():
    with open('FacebookData', 'r') as o:
        data = o.read()
        dataSplit = data.split('\n')
        for ds in dataSplit:
            if len(ds) < 12:
                print(ds)
def createGraph():
    G=nx.Graph()
    G.add_nodes_from([2,3])
    nx.draw(G)
    plt.show()

if __name__ == "__main__":
    readData()
    #createGraph()
    #downloadFile('https://snap.stanford.edu/data/facebook.tar.gz', 'FacebookData')