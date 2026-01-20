import socket
import threading
import time
import random
import pickle

from config import NODES, ELECTION_TIMEOUT, HEARTBEAT_INTERVAL, MAJORITY
from message import RequestVote, AppendEntries
from network import send_message


class RaftNode:
    def __init__(self, node_id):
        self.node_id = node_id
        self.term = 0
        self.voted_for = None
        self.state = "Follower"
        self.leader_id = None
        self.votes = 0
        self.last_heartbeat = time.time()
        self.last_logged_leader = None


        self.host, self.port = NODES[node_id]
        threading.Thread(target=self.run_server, daemon=True).start()
        threading.Thread(target=self.election_timer, daemon=True).start()

    def run_server(self):
        s = socket.socket()
        s.bind((self.host, self.port))
        s.listen()
        while True:
            conn, _ = s.accept()
            msg = pickle.loads(conn.recv(4096))
            response = self.handle_message(msg)
            conn.sendall(pickle.dumps(response))
            conn.close()

    def election_timer(self):
        while True:
            time.sleep(0.1)
            if self.state == "Leader":
              continue

            if time.time() - self.last_heartbeat > random.randint(*ELECTION_TIMEOUT):
               self.start_election()


    def start_election(self):
        self.state = "Candidate"
        self.term += 1
        self.votes = 1
        self.voted_for = self.node_id
        print(f"[Node {self.node_id}] Election term {self.term}")

        for nid, addr in NODES.items():
            if nid != self.node_id:
                vote = send_message(addr, RequestVote(self.term, self.node_id))
                if vote:
                    self.votes += 1

        if self.votes >= MAJORITY:
            self.state = "Leader"
            self.leader_id = self.node_id
            print(f"[Node {self.node_id}] LEADER")
            threading.Thread(target=self.send_heartbeat, daemon=True).start()

    def send_heartbeat(self):
        while self.state == "Leader":
            for nid, addr in NODES.items():
                if nid != self.node_id:
                    send_message(addr, AppendEntries(self.term, self.node_id))
            time.sleep(HEARTBEAT_INTERVAL)


    def handle_message(self, msg):
    # Terima heartbeat / AppendEntries
         if isinstance(msg, AppendEntries):
            self.last_heartbeat = time.time()
            self.leader_id = msg.leader_id
            self.state = "Follower"
            self.term = msg.term

            if getattr(self, "last_logged_leader", None) != msg.leader_id:
               print(f"[Node {self.node_id}] Following leader {msg.leader_id}")
               self.last_logged_leader = msg.leader_id

               return True

    # Terima RequestVote dari kandidat
         if isinstance(msg, RequestVote):
        # Tolak kalau term lebih kecil
            if msg.term < self.term:
               return False

            if msg.term > self.term:
               self.term = msg.term
               self.voted_for = None
               self.state = "Follower"

            if self.voted_for is None or self.voted_for == msg.candidate_id:
               self.voted_for = msg.candidate_id
               self.last_heartbeat = time.time()
               print(f"[Node {self.node_id}] Voted for {msg.candidate_id}")
               return True

            return False


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python node.py <node_id>")
        sys.exit(1)

    node_id = int(sys.argv[1])
    RaftNode(node_id)

    while True:
        time.sleep(1)
