from network import send_message
from config import NODES
from message import AppendEntries

leader = list(NODES.values())[0]
send_message(leader, AppendEntries(1, "client"))
print("Request sent to leader")
