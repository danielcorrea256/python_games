import socket
from _thread import *
import pickle
from Game import Game

server = "Your IPv4"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen()
print("Waiting for connection, Server Started")

connected = set()
games = {}
idCount = 0

def threaded_client(conn, p, game_id):
    global idCount
    conn.send(str.encode(str(p)))

    reply = ""
    while True:
        try:
            data = conn.recv(4096).decode()

            if game_id in games:
                game = games[game_id]

                if not data:
                    break
                else:
                    if data == "reset":
                        game.resetWent()
                    elif data != "get":
                        game.play(p, data)
                
                    conn.sendall(pickle.dumps(game))
            else:
                break
        except:
            break

    print("Lost connection")

    try:
        del games[game_id]
        print("Closing Game", game_id)
    except:
        pass
    idCount -= 1
    conn.close()



while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    idCount += 1
    p = 0
    gameId = (idCount - 1) // 2

    print("games", games)
    print("gameId",gameId)
    print("p", p)

    if  idCount % 2 == 1:
        games[gameId] = Game(gameId)
        print("Creating a new game ...")
    else:
        games[gameId].ready = True
        p = 1

    start_new_thread(threaded_client, (conn, p, gameId))
