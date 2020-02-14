# Paste your version of blockchain.py from the client_mining_p
# folder here
# Paste your version of blockchain.py from the basic_block_gp
# folder here
import hashlib
import json
from time import time
from uuid import uuid4

from flask import Flask, jsonify, request
from flask_cors import CORS


class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

        # Create the genesis block
        self.new_block(previous_hash=1, proof=100)

    def new_block(self, proof, previous_hash=None):
        """
        Create a new Block in the Blockchain

        A block should have:
        * Index
        * Timestamp
        * List of current transactions
        * The proof used to mine this block
        * The hash of the previous block

        :param proof: <int> The proof given by the Proof of Work algorithm
        :param previous_hash: (Optional) <str> Hash of previous Block
        :return: <dict> New Block
        """

        block = {
            # TODO
            "index": len(self.chain) + 1,
            "timestamp": time(),
            "transactions": self.current_transactions,
            "proof": proof,
            "previous_hash": previous_hash or self.hash(self.chain[-1]),
        }

        # Reset the current list of transactions
        self.current_transactions = []
        # Append the chain to the block
        self.chain.append(block)
        # Return the new block
        return block
        
    def new_transaction(self, sender, recipient, amount):
        """
        :param sender: <str> Address of the Recipient
        :param recipient: <str> Address of the Recipient
        :param amount: <int> Amount
        :return: <int> The index of the `block` that will hold this transaction
        """
        transaction = {
            "sender": sender, 
            "recipient": recipient,
            "amount": amount
        }

        self.current_transactions.append(transaction)
        return self.last_block['index'] + 1


    def hash(self, block):
        """
        Creates a SHA-256 hash of a Block

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
        # json.dumps stringifies the json object, in this case block; and sort_keys = True keeps the keys in the same order so when we hash the object, it is deterministic (always the same)
        string_object = json.dumps(block, sort_keys=True)
        # python strings are not really strings, they are still objects and have metadata.  So while we did the json.dumps above, we still need to further stringify it.
        block_string = string_object.encode()

        # TODO: Hash this string using sha256
        # hashes the fully stringified block
        raw_hash = hashlib.sha256(block_string) 
        # use built-in hex_digest to get the hex_hash
        hex_hash = raw_hash.hexdigest()

        # By itself, the sha256 function returns the hash in a raw string
        # that will likely include escaped characters.
        # This can be hard to read, but .hexdigest() converts the
        # hash to a string of hexadecimal characters, which is
        # easier to work with and understand

        # TODO: Return the hashed block string in hexadecimal format
        return hex_hash

    @property
    def last_block(self):
        return self.chain[-1]



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
        # TODO
        guess = f"{block_string}{proof}".encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:6] == "000000"


# Instantiate our Node
app = Flask(__name__)

# Cors
CORS(app)

# Generate a globally unique address for this node
node_identifier = str(uuid4()).replace('-', '')

# Instantiate the Blockchain
blockchain = Blockchain()
print(blockchain.chain)
print(blockchain.hash(blockchain.last_block))

# change user id
@app.route('/user/', methods=['POST'])
def add_user():
    data = request.get_json()
    # breakpoint()
    required = ['user',]
    print("mY TESt: ....", data, required)
    if not all(k in data for k in required):
        #TODO: error handling for wrong data
        return "must send a user", 400

    user = data['user']
    # breakpoint()
    # Load user ID
    l = open("../client_mining_p/my_id.txt", "r")
    # traverse through users in file and compare to user
    # if str(user).encode() in l.readlines():
    if user in l.readlines():
        print("********!user found!: ***********\n\n", user)
        # compare request user to users in my_id.txt file
        print("ID is", user)
        response = {
            "user": f"found user, {user}"
        }
        l.close()
        return jsonify(response), 200
    else: 
        l = open("../client_mining_p/my_id.txt", "a")
        # save the user
        l.write("\n" + str(user))
        l.close()
        response = {
        "success": "USER ADDED!  SUCCESS!"
    }
    return jsonify(response), 200

    # # Save NEW user ID
    # f = open("../client_mining_p/my_id.txt", "a")
    # f.write("\n" + str(user))
    # f.close()
    


# add a transaction
@app.route('/transactions/new/', methods=['POST'])
def receive_new_transaction():
    """
    * use `request.get_json()` to pull the data out of the POST
    * check that 'sender', 'recipient', and 'amount' are present
        * return a 400 error using `jsonify(response)` with a 'message'
    * upon success, return a 'message' indicating index of the block
        containing the transaction
    """
    data = request.get_json()
    required = ['sender', 'recipient', 'amount']
    if not all(k in data for k in required):
        # TODO: Better error handling
        return "missing values", 400
    
    index = blockchain.new_transaction(data['sender'], data['recipient'], data['amount'])
    response = {'message': f"Transactions will be included in block {index}."}

    return jsonify(response), 200


# Receive content from a client via POST
@app.route('/mine/', methods=['POST'])
def mine():
    # Run the proof of work algorithm to get the next proof
    # proof = blockchain.proof_of_work(blockchain.last_block)
    # get the json object request data from client
    data = request.get_json()
    proof = data['proof']
    last_block = blockchain.last_block
    last_block_string = json.dumps(last_block, sort_keys=True)
    if blockchain.valid_proof(last_block_string, proof):
        previous_hash = blockchain.hash(blockchain.last_block)

        block_index = blockchain.new_transaction(0, data['id'], 1)

        new_block = blockchain.new_block(proof, previous_hash)

        response = {
            # TODO: Send a JSON response with the new block
            "block": new_block,
            "reward": f"REWARD paid in block {block_index}."
        }
        return jsonify(response), 200
    else:
        response = {
            "ERROR": "Must include valid proof and id."
        }
        return jsonify(response), 400
    # Forge the new Block by adding it to the chain with the proof
    print("THIS IS THE request.get_json: ", data['id'])



@app.route('/chain/', methods=['GET'])
def full_chain():
    response = {
        # TODO: Return the chain and its current length
        "chain": blockchain.chain,
        "length": len(blockchain.chain),
    }
    return jsonify(response), 200

# Returns last block in chain
@app.route('/last_block/', methods=['GET'])
def last_block():
    response = {
        "last_block": blockchain.last_block
    }
    return jsonify(response), 200

# Run the program on port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
