import random 

class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

class Node:
    def __init__(self, data, next = None, previous = None):
        self.data = data
        self.next = next
        self.previous = previous

class PlayList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def enqueue(self, title, artist, duration): # Agregar un elemento
        duration_split = duration.split(":")
        minutes = int(duration_split[0])
        seconds = int(duration_split[1])

        song = Song(title, artist, (minutes, seconds))
        new_node = Node(song, None, None)

        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.count += 1

    def dequeue(self): # Eliminar un elemento
        current = self.head

        if self.count == 1:
            self.count -= 1
            self.head = None
            self.tail = None
        elif self.count > 1:
            self.head = self.head.next
            self.head.previous = None
            self.count -= 1

        return current.data

    def peek(self): # Retornar el tail de la lista
        if self.tail:
            data = [self.tail.data.title, self.tail.data.artist, self.tail.data.duration]
            datas = ", ".join(map(str, data))
            return datas
        else:
            return "You don't have songs in this moment."
    
    def pop(self): # Extrae y "reproduce" la siguiente cancion de la cola
        if self.tail:
            data = [self.tail.data.title, self.tail.data.artist, self.tail.data.duration]
            datas = ", ".join(map(str, data))
            self.count -= 1

            if self.tail.previous:
                self.tail = self.tail.previous
            else:
                self.tail = None
            
            return datas
        else:
            return "You don't have more songs in this moment."   
        
    def iter(self): # Recorre todos los elementos del tail al head
        current = self.tail
        while current:
            val = current.data
            current = current.previous
            yield val

    def search(self, data): # Buscar una canción entre la lista
        found = False
        for node in self.iter():
            if data == node.title:
                print(f"I found: {data} by {node.artist}") 
                found = True  
                break

        if not found:
            print("I'm sorry. I can't found that song")

    def random_order(self): # Mezclar todos los elementos de la lista
        song_list = []
        actual_node = self.head

        while actual_node is not None:
            song_list.append(actual_node)
            actual_node = actual_node.next
        
        random.shuffle(song_list)

        self.head, self.tail = song_list[0], song_list[-1]  
        self.head.previous = None
        self.tail.next = None 

        for i in range(len(song_list) - 1):
            song_list[i].next, song_list[i + 1].previous = song_list[i + 1], song_list[i] # realiza el enlace bidireccional entre los nodos consecutivos de la lista enlazada, estableciendo las referencias next y previous adecuadamente.

    def save_list(self, name_archive): #Guardar la lista en un .txt
        with open(name_archive, 'w') as archive:
            actual_node = self.tail
            while actual_node is not None:
                song = actual_node
                archive.write(f"Título: {song.data.title}\n")
                archive.write(f"Artista: {song.data.artist}\n")
                archive.write(f"Duración: {song.data.duration}\n")
                archive.write("-------------------------\n")
                actual_node = actual_node.previous