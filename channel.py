import random
from hash_chain import HashChain

class Channel:
    def __init__(self, field_max_element: int, seed=None):
        """Initialize the channel with an optional random seed."""
        self.messages = [field_max_element]
        self.hash_chain = HashChain(seed)

    def send(self, message):
        """Send (store) a message in the channel."""
        self.messages.append(message)

    def receive(self):
        """Receive (retrieve) the last message sent."""
        return self.messages[-1] if self.messages else None

    def get_all_messages(self):
        """Retrieve all messages exchanged."""
        return self.messages

    def receive_random(self):
        """Generate a random f"""
        random_element = self.hash_chain.next()
        self.messages.append(random_element)
        return random_element