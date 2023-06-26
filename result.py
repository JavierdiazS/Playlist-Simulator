from queueList import PlayList

x = PlayList()

#enqueue
x.enqueue('One', 'Metallica', '7:27')
x.enqueue('Bohemian Rhapsody', 'Queen', '5:55')
x.enqueue('Hotel California', 'Eagles', '6:30')
x.enqueue('Imagine', 'John Lennon', '3:03')
x.enqueue('Shape of You', 'Ed Sheeran', '3:53')
x.enqueue('Stairway to Heaven', 'Led Zeppelin', '8:02')
x.enqueue('Smells Like Teen Spirit', 'Nirvana', '5:01')
x.enqueue('Wonderwall', 'Oasis', '4:18')
x.enqueue('Billie Jean', 'Michael Jackson', '4:54')
x.enqueue('Sweet Child of Mine', 'Guns and Roses', '5:56')
x.enqueue('Hey Jude', 'The Beatles', '7:11')
x.enqueue('Bohemio Enamorado', 'Donato y Estéfano', '4:46')
x.enqueue('Hotel California', 'Eagles', '6:30')
x.enqueue('Imagine', 'John Lennon', '3:03')
x.enqueue('Shape of You', 'Ed Sheeran', '3:53')
x.enqueue('Stairway to Heaven', 'Led Zeppelin', '8:02')
x.enqueue('Smells Like Teen Spirit', 'Nirvana', '5:01')
x.enqueue('Wonderwall', 'Oasis', '4:18')
x.enqueue('Thriller', 'Michael Jackson', '5:57')
x.enqueue('Sweet Child o\' Mine', 'Guns N\' Roses', '5:56')

#Verificar el primer y segundo elemento agregado con enqueue
print(x.head.data.title, x.head.data.artist, x.head.data.duration, sep = ", ")
print(x.head.next.data.title, x.head.next.data.artist, x.head.next.data.duration, sep = ", ")

print('\n')

# dequeue
x.dequeue()
print(x.head.data.title, x.head.data.artist, x.head.data.duration, sep = ", ")

print('\n')

# peek
front = x.peek()
print(f"The first item in the list is --> {front}")

print('\n')

# pop
tail = x.pop()
print(f"It's playing --> {tail}")

print('\n')

#iter
for i in x.iter():
    print(i.title, i.artist, i.duration, sep = ", ")

print('\n')

#search
x.search('One')

print('\n')

#random_order
x.random_order()

#iter
for i in x.iter():
    print(i.title, i.artist, i.duration, sep = ", ")

#save_list
x.save_list("lista_reproduccion.txt")

