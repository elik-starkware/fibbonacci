from queue import Queue
from pickle import dumps
from hash import my_hash


class Channel:
    def __init__(self, F, N):
        """Initialize the channel with an optional random seed."""
        self.messages = []
        self.decommit_idx = None
        self.F = F
        self.N = N

    def start_decommit(self):
        assert not self.decommit_idx, "Decommitment already started"
        assert len(self.messages) > 0
        self.decommit_idx = len(self.messages)

    def send(self, message: dict[str, int | str]):
        """Send (store) a message in the channel."""
        self.messages.append(message)

    def receive_commitment(self):
        """Receive (retrieve) the last message sent."""
        return self.messages[:self.decommit_idx] if self.decommit_idx else self.messages

    def receive_decommitment(self):
        """Receive (retrieve) the last message sent."""
        assert self.decommit_idx, "Decommitment not started"
        return self.messages[self.decommit_idx:]

    def get_all_messages(self):
        """Retrieve all messages exchanged."""
        return self.messages

    def _get_hash(self):
        return my_hash("".join(map(lambda x: str(dumps(x)), self.messages)))

    def receive_random_query(self, title: str = "Random Query"):
        idx = int(self._get_hash(), 16) % self.N
        self.messages.append({
            "title": title,
            "data": idx
        })
        return idx
    
    def receive_random_field_element(self, title: str = "Random Field Element"):
        # TODO change with nonce
        """Generate a random f"""
        random_field_element = self.F(int(self._get_hash(), 16))
        self.messages.append({
            "title": title,
            "data": random_field_element
        })
        return random_field_element
