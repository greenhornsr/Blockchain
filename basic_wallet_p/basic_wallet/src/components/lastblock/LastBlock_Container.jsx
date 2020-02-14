import React, { useState, useEffect } from 'react';
import axios from 'axios';

// importing Component(s)
import BcTransactions from "../chain/BcTransactions";

// styling
import '../components.css'

const LastBlock_Container = () => {
const [lastblock, setLastBlock] = useState()

// use of async/await instead of .then/.catch.  
async function getLastBlock(){
    const last_block = await axios.get('http://localhost:5000/last_block/')
    console.log(last_block)
    setLastBlock(last_block.data.last_block)
}
console.log("The LAST BLOCK STATE: ", lastblock)

useEffect(() => {
    getLastBlock()
},[])

    return (
        <div className="lastblock-container" >
            {!lastblock ? (
                <h1 className="h1-centers" >Loading...</h1>
            ) : (
                <section>
                    <h1 className="h1-centers" >Last Block Mined</h1>
                    <p>Index: {lastblock.index}</p>
                    <p>Previous_hash: {lastblock.previous_hash}</p>
                    <p>Proof: {lastblock.proof}</p>
                    <p>Timestamp: {lastblock.timestamp}</p>
                    {lastblock.transactions.length > 0 ? (
                        <section><p>Transactions: </p>
                            {lastblock.transactions.map((transaction, i) => {
                                                        return <BcTransactions key={i} transaction={transaction} />
                                                    })}</section>
                    ) : (
                        <p>no transactions</p>
                    )}
                        </section>
                    )}
        </div>
    )
}
export default LastBlock_Container;