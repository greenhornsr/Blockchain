# Explain in detail the workings of a dynamic array:
    ** a dynamic array is an array that automatically resizes. **

    What is the runtime complexity to access an array **O1 because you can go directly to the index **, add or remove from the front **O(n) due to having to shift everything over**
    , and add or remove from the back 
    **O(1) due to direct access to location and no impact to the rest of the array elements **
    ? 

    What is the worse case scenario if you try to extend the storage size of a dynamic array? 
    **O(n) because regardless of the change, it is still bound by a static number relative to n.**

# Explain how a blockchain is structured. What are the blocks, what is the chain? How is the data organized?
    **A blockchain is a cryptographic database maintained by a network of computers(nodes).  The blockchain consists of a sequence of blocks interconnected or linked by a hash of the previous block. It is the Bank Ledger. Each block represents a cryptocoin and holds a validated hash of the previous block + a nonce (aka salt, proof).  The data, hash, proof, prevhash, timestamp, transactions are stored in a dictionary that is then converted to a json string in order to sort the contents and hash it along with a proof for the next block**

# Explain how proof of work functions. How does it operate. How does this protect the chain from attack. What kind of attack is possible?
    ** the proof of work that is essentially the enforcer of the new block protocol and has an expected output of the hash; typically a hash value prefixed by some set of zeros.  The proof of work will check a hashed prior block + nonce to see if it's output matches the expected outcome pattern; if so, it proceeds with creating a new block, if not, it attempts again with a new nonce.  Each zero exponentially increases the difficulty of success which slows down the probability of success.  This prevents brute force attacks as the current computing power isn't capable of achieving success in any reasonable time.**
    **DDoS - Distributed Denial of Service; consumption of all processing resources by making numerous requests.**