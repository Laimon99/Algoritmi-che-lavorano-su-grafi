#ALGOIRTMO ISOMAP
# Importa le librerie necessarie
from sklearn.datasets import make_swiss_roll
from sklearn.manifold import Isomap
import matplotlib.pyplot as plt

# Genera dati di esempio (un rollio svizzero tridimensionale)
X, _ = make_swiss_roll(n_samples=1000, noise=0.2, random_state=42)

# Crea un'istanza di Isomap con 2 componenti (riduzione a 2 dimensioni)
isomap = Isomap(n_components=2, n_neighbors=10)

# Adatta il modello ai dati
X_isomap = isomap.fit_transform(X)

# Visualizza i dati ridotti nella nuova dimensione
plt.scatter(X_isomap[:, 0], X_isomap[:, 1], cmap=plt.cm.Spectral)
plt.title("Riduzione della dimensionalità con Isomap")
plt.show()

#Importiamo le librerie necessarie, tra cui scikit-learn per l'implementazione di Isomap e Matplotlib per la visualizzazione.
#Generiamo dei dati di esempio tridimensionali utilizzando make_swiss_roll. Questi dati assomigliano a un "rollio svizzero" tridimensionale e contengono una struttura intrinseca non lineare.
#Creiamo un'istanza di Isomap con n_components=2, il che significa che vogliamo ridurre la dimensionalità dei dati a 2 dimensioni.
#Adattiamo il modello Isomap ai dati utilizzando fit_transform, ottenendo così una nuova rappresentazione dei dati con due dimensioni in X_isomap.
#Visualizziamo i dati ridotti nella nuova dimensione utilizzando un diagramma a dispersione (scatter plot) per visualizzare la struttura dei dati a dimensionalità inferiore.
#L'output finale sarà un grafico a dispersione bidimensionale che rappresenta la riduzione della dimensionalità dei dati originali mantenendo le relazioni di vicinanza tra i punti.