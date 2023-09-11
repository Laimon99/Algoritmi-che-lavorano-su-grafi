#ALGORITMO DI DIFFUSIONE DELLE INFORMAZIONI
# Definizione della rete (lista di nodi)
network = {
    'Nodo A': [],
    'Nodo B': [],
    'Nodo C': [],
    'Nodo D': [],
}

# Funzione per la diffusione delle informazioni
def broadcast_info(sender, message, network):
    for node in network:
        if node != sender:
            print(f"{sender} invia '{message}' a {node}")

# Esempio di utilizzo
if __name__ == "__main__":
    sender_node = 'Nodo A'
    message_to_broadcast = 'Messaggio importante'

    broadcast_info(sender_node, message_to_broadcast, network)

#Definiamo una rappresentazione della rete come un dizionario Python, dove le chiavi sono i nomi dei nodi e i valori sono le liste dei nodi a cui ogni nodo è connesso. In questo esempio, assumiamo che nessun nodo sia connesso a nessun altro.
#Definiamo una funzione broadcast_info che accetta tre argomenti: il mittente, il messaggio da inviare e la rete. Questa funzione itererà attraverso tutti i nodi nella rete (escludendo il mittente) e invierà il messaggio a ciascuno di essi.
#Nell'esempio di utilizzo, specificiamo il nodo mittente come 'Nodo A' e il messaggio da inviare come 'Messaggio importante'. Chiamiamo quindi la funzione broadcast_info per inviare il messaggio a tutti gli altri nodi nella rete.