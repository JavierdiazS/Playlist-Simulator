# Playlist_Simulator

A music playlist simulator was created that utilizes Node-based Queues, offering several advantages and benefits. The reasons for using Node-based Queues are as follows:

- **Appropriate data structure:** Queues are an efficient data structure for managing a list of elements that follows the "first in, first out" (FIFO) principle. This is ideal for simulating a music playlist since songs are played in the order they were added.

- **Flexibility in manipulation:** By implementing a Node-based Queue, you can easily access and manipulate elements in the playlist. You can add new songs to the end of the list, play the next song, remove played songs, or change the playback order with ease.

- **Efficient insertion and removal:** Node-based queues allow for efficient insertion and removal of elements at both ends of the list. You can add new songs to the end of the playlist without reorganizing the entire data structure. Additionally, when playing a song, you simply remove it from the beginning of the list without affecting the other songs.

- **Ability to simulate real-time events:** By using a Node-based Queue, you can simulate real-time events such as playing songs in order, adding new songs while the list is playing, or even shuffling the playlist randomly. This provides flexibility to simulate different scenarios and behaviors of a real music playlist.

-  **Scalability:** Implementing a Node-based Queue allows you to handle playlists of any size. You can add an unlimited number of songs, and the data structure will remain efficient and fast in its operations.

<details>
    <summary>🐍 queueList.py</summary> 
  
          Contains the following methods:
            Method for adding elements to the list (enqueue).
            Method for removing elements from the list (dequeue).
            Method for displaying the first element of the list.
            Method for sequentially playing and extracting the song.
            Method for displaying the current playlist.
            Method for searching for a song by name or artist.
            Method for randomly shuffling the playlist.
            Method for saving the playlist to a file.
</details>
<details>
    <summary>💻 result.py</summary> 
  
          Will contain the application of these methods to test them in our terminal.
</details>
<details>
    <summary>📄 Lista_reproduccion.txt</summary> 
  
          Will contain all the songs created with the enqueue method. This .txt file was created using the save_list() method.
</details>

In summary, using Node-based Queues to simulate a music playlist provides an appropriate data structure, flexibility in list manipulation, efficiency in insertion and removal operations, the ability to simulate real-time events, and scalability to handle playlists of any size. These advantages make it a solid and effective choice for developing a music playlist simulator.

## Contributing

Please feel free to use it if you want to contributing directly to the code base.

## License

Playlist Simulator is released under the MIT license. See the [LICENSE](/LICENSE) file for details.
