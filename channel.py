from queue import Queue
from pickle import dumps
from hash import my_hash


class Channel:
    def __init__(self, F):
        """Initialize the channel with an optional random seed."""
        self.messages = Queue()
        self.F = F

    def send(self, message: dict[str, int | str]):
        """Send (store) a message in the channel."""
        self.messages.put(message)

    def receive(self):
        """Receive (retrieve) the last message sent."""
        return self.messages.get()

    def get_all_messages(self):
        """Retrieve all messages exchanged."""
        return list(self.messages.queue)

    def _get_hash(self):
        return my_hash("".join(map(lambda x: str(dumps(x)), self.messages.queue)))

    def receive_random_field_element(self, title: str = "Random Field Element"):
        # TODO change with nonce
        """Generate a random f"""
        random_field_element = self.F(int(self._get_hash(), 16))
        self.messages.put({
            "title": title,
            "data": str(random_field_element)
        })
        return random_field_element
