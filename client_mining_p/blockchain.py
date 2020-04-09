# Paste your version of blockchain.py from the basic_block_gp
# folder here
import hashlib
import json
from time import time
from uuid import uuid4

from flask import Flask, jsonify, request


class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

        # Create the genesis block
        self.new_block(previous_hash=1, proof=100)

    def new_block(self, proof, previous_hash=None):
        """
        Create a new Block in the Blockchain
​
        A block should have:
        * Index
        * Timestamp
        * List of current transactions
        * The proof used to mine this block
        * The hash of the previous block
​
        :param proof: <int> The proof given by the Proof of Work algorithm
        :param previous_hash: (Optional) <str> Hash of previous Block
        :return: <dict> New Block
        """

        if len(self.chain) > 0:
            # json.dumps (pronounced json.dump s) turns the json to a string; we then use the sort_keys property to sort by setting to True.  This is done to keep the hash consistent.
            block_string = json.dumps(self.last_block, indent=4, sort_keys=True)

            # print("my last_block string:", block_string)

            # declaring a variable to hold the latest guess which is done by combining the now json string version of the block with the current proof and encoding it (default: ASCII).  The proof is what modifies the encoded guess would change based on the proof/salt changing.
            guess = f'{block_string}{proof}'.encode()
            # print(f"the guess: {guess}")

            # hashing the current guess using sha256, readable version is achieved by accessing the hexdigest method.  current_hash is ultimately going to represent the hash of the previous block & proof(aka salt).
            current_hash = hashlib.sha256(guess).hexdigest()
        else:
            # this is done for the genesis block; since the genesis block is the original block, it wouldn't have an actual current hash.
            current_hash = ""

        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.last_block),
            'hash': current_hash,
        }

        # Reset the current list of transactions
        self.current_transactions = []
        # Append the block to the chain
        self.chain.append(block)
        # Return the new block
        return block

    def new_transaction(self, sender, recipient, amount):
        self.current_transactions.append({
            "sender": sender, 
            "recipient": recipient,
            "amount": amount
        })
        return self.last_block['index'] + 1

    # this custom hash method is done to provide a hexdigest/readable version within the new block
    def hash(self, block):
        """
        Creates a SHA-256 hash of a Block
​
        :param block": <dict> Block
        "return": <str>
        """

        # Use json.dumps to convert json into a string
        # Use hashlib.sha256 to create a hash
        # It requires a `bytes-like` object, which is what
        # .encode() does.
        # It converts the Python string into a byte string.
        # We must make sure that the Dictionary is Ordered,
        # or we'll have inconsistent hashes

        # TODO: Create the block_string
        string_object = json.dumps(block, indent=4, sort_keys=True)
        block_string = string_object.encode()

        # TODO: Hash this string using sha256
        raw_hash = hashlib.sha256(block_string)
        hex_hash = raw_hash.hexdigest()

        # By itself, the sha256 function returns the hash in a raw string
        # that will likely include escaped characters.
        # This can be hard to read, but .hexdigest() converts the
        # hash to a string of hexadecimal characters, which is
        # easier to work with and understand

        # TODO: Return the hashed block string in hexadecimal format
        return hex_hash

    # method to access / reference the last block in the chain.
    @property
    def last_block(self):
        return self.chain[-1]

    # method for incrementing / changing the proof/salt until you get a matching / successful proof/salt.
    # def proof_of_work(self):
    #     """
    #     Simple Proof of Work Algorithm
    #     Stringify the block and look for a proof.
    #     Loop through possibilities, checking each one against `valid_proof`
    #     in an effort to find a number that is a valid proof
    #     :return: A valid proof for the provided block
    #     """
    #     block_string = json.dumps(self.last_block, indent=4, sort_keys=True)
    #     proof = 0
    #     while not self.valid_proof(block_string, proof):
    #         proof += 1
    #     return proof

    # method for validating success of the proof/salt used.  in this case, a guess is generated by hashing the json string of the previous block + proof(aka salt).  Success is considered to be a hash that contains five leading zeros.
    @staticmethod
    def valid_proof(block_string, proof):
        """
        Validates the Proof:  Does hash(block_string, proof) contain 3
        leading zeroes?  Return true if the proof is valid
        :param block_string: <string> The stringified block to use to
        check in combination with `proof`
        :param proof: <int?> The value that when combined with the
        stringified previous block results in a hash that has the
        correct number of leading zeroes.
        :return: True if the resulting hash is a valid proof, False otherwise
        """
        guess = f"{block_string}{proof}".encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        # return even occurs when the hash starts with 000000 (six zeros).  the lower the number, the faster the success return event, the higher the number, the longer it takes!
        # result = bool(guess_hash[:6] == "000000")
        # print(result)
        return guess_hash[:6] == "000000"


# Instantiate our Node
app = Flask(__name__)

# Generate a globally unique address for this node
node_identifier = str(uuid4()).replace('-', '')

# Instantiate the Blockchain
blockchain = Blockchain()

# Flask API
@app.route('/', methods=['GET'])
def home():
    response = "URL path options", {
        "/chain": "shows the blockchain.",
        "/mine": "mine to add new block to the blockchain."
    }
    return jsonify(response), 200

@app.route('/mine', methods=['POST'])
def mine():
    # Run the proof of work algorithm to get the next proof
    # proof = blockchain.proof_of_work()

    # getting JSON/dictionary request from client
    data = request.get_json()
    proof = data["proof"]

    if 'proof' not in data or 'id' not in data:
        response = {"ALERT":  "Request must contain 'proof' and 'id'."}
        return jsonify(response), 400

    # Determine if the proof is valid
    last_block = blockchain.last_block
    last_block_string = json.dumps(last_block, indent=4, sort_keys=True)

    if blockchain.valid_proof(last_block_string, proof):
        blockchain.new_transaction(sender="0", recipient=data["id"].strip(), amount=1)

        # Forge the new Block by adding it to the chain with the proof
        previous_hash = blockchain.hash(blockchain.last_block)
        block = blockchain.new_block(proof, previous_hash)

        response = {
            'message': "New Block Forged",
            'index': block['index'],
            'transactions': block['transactions'],
            'proof': block['proof'],
            'previous_hash': block['previous_hash'],
        }

        return jsonify(response), 200

    else: 
        response = {"ALERT":  "Invalid Proof"}
        return jsonify(response), 400


@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'length': len(blockchain.chain),
        'chain': blockchain.chain
    }
    return jsonify(response), 200

@app.route('/last_block', methods=['GET'])
def last_block_route():
    response = {
        "last_block": blockchain.last_block
    }
    return jsonify(response), 200

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    values = request.get_json()

    required = ['sender', 'recipient', 'amount']
    if not all(k in values for k in required):
        return 'Missing Values', 400

    index = blockchain.new_transaction(values["sender"],
                                        values["recipient"],
                                        values["amount"])

    response = {'message': f"Transaction will be added to Block {index}"}
    return jsonify(response), 200


# Run the program on port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

# Curl command to test endpoints via cli.
# cli command: curl -X POST -H "Content-Type: application/json" -d '{"sender":"Br80", "recipient": "Brian", "amount": 1}' localhost:5000/transactions/new

