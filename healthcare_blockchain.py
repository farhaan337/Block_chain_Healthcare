import hashlib
import time

# Define a Block in the Blockchain
class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data  # Medical record data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)
        return hashlib.sha256(block_string.encode()).hexdigest()


# Define the Blockchain
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, time.ctime(), {"Message": "Genesis Block - First Medical Record"}, "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_data):
        latest_block = self.get_latest_block()
        new_block = Block(len(self.chain), time.ctime(), new_data, latest_block.hash)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True


# --------------------
# Demonstration
# --------------------

# Create blockchain for healthcare records
health_chain = Blockchain()

# Add some medical records
health_chain.add_block({"PatientID": 101, "Name": "Alice", "Diagnosis": "Diabetes", "Prescription": "Metformin"})
health_chain.add_block({"PatientID": 102, "Name": "Bob", "Diagnosis": "Hypertension", "Prescription": "Amlodipine"})
health_chain.add_block({"PatientID": 103, "Name": "Charlie", "Diagnosis": "Asthma", "Prescription": "Inhaler"})

# Print the blockchain
for block in health_chain.chain:
    print("\nIndex:", block.index)
    print("Timestamp:", block.timestamp)
    print("Data:", block.data)
    print("Hash:", block.hash)
    print("Previous Hash:", block.previous_hash)

# Validate blockchain
print("\nIs Blockchain Valid?", health_chain.is_chain_valid())
