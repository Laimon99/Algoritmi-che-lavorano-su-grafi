#RAGGRUPPAMENTO SPETTRALE
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import SpectralClustering

# Creazione di un set di dati casuale con due cluster
X, y = make_blobs(n_samples=300, centers=2, random_state=0, cluster_std=0.60)

# Visualizzazione del set di dati
plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='viridis')
plt.title('Set di dati casuale con due cluster')
plt.show()

# Applicazione dell'algoritmo di raggruppamento spettrale
spectral_clustering = SpectralClustering(n_clusters=2, affinity='nearest_neighbors', random_state=0)
cluster_labels = spectral_clustering.fit_predict(X)

# Visualizzazione dei risultati del raggruppamento
plt.scatter(X[:, 0], X[:, 1], c=cluster_labels, s=50, cmap='viridis')
plt.title('Risultati del Raggruppamento Spettrale')
plt.show()


#In questo codice:
#Creiamo un set di dati casuale con due cluster utilizzando make_blobs dalla libreria scikit-learn.
#Visualizziamo il set di dati iniziale per avere un'idea di come sono distribuiti i punti nei due cluster.
#Applichiamo l'algoritmo di raggruppamento spettrale utilizzando SpectralClustering dalla libreria scikit-learn. Specifichiamo il numero desiderato di cluster (in questo caso, 2) e l'affinità tra i punti (usiamo 'nearest_neighbors' per misurare la similarità).
#Visualizziamo i risultati del raggruppamento spettrale, colorando i punti in base all'appartenenza ai cluster.