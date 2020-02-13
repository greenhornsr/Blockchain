# Client Miners

In the initial blockchain demonstration, we've created a small problem.  The `mine` endpoint is called on the server, which means we're the ones spending all of the electricity to generate a new block.  This won't do at all!

Furthermore, the amount of work needed to actually mine a block is a bit low.  We need it to be harder to preserve the integrity of the chain.


# Task List

*Server*
Modify the server we created to:
* # [checkbox:unchecked] Remove the `proof_of_work` function from the server.
* # [checkbox:checked] Change `valid_proof` to require *6* leading zeroes.
* # [checkbox:unchecked] Add an endpoint called `last_block` that returns the last block in the chain
* # [checkbox:unchecked] Modify the `mine` endpoint to instead receive and validate or reject a new proof sent by a client.
    * It should accept a POST
    * Use `data = request.get_json()` to pull the data out of the POST
        * Note that `request` and `requests` both exist in this project
    * Check that 'proof', and 'id' are present
        * return a 400 error using `jsonify(response)` with a 'message'
* # [checkbox:unchecked] Return a message indicating success or failure.  Remember, a valid proof should fail for all senders except the first.

*Client Mining*
Create a client application that will:
* # [checkbox:unchecked] Get the last block from the server
* # [checkbox:unchecked] Run the `proof_of_work` function until a valid proof is found, validating or rejecting each attempt.  Use a copy of `valid_proof` to assist.
* # [checkbox:unchecked] Print messages indicating that this has started and finished.
* # [checkbox:unchecked] Modify it to generate proofs with *6* leading zeroes.
* # [checkbox:unchecked] Print a message indicating the success or failure response from the server
* # [checkbox:unchecked] Add any coins granted to a simple integer total, and print the amount of coins the client has earned
* # [checkbox:unchecked] Continue mining until the app is interrupted.
* # [checkbox:unchecked] Change the name in `my_id.txt` to your name
* # [checkbox:unchecked] (Stretch) Handle non-json responses sent by the server in the event of an error, without crashing the miner
* # [checkbox:unchecked] Stretch: Add a timer to keep track of how long it takes to find a proof

