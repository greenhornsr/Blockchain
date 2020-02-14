import React from 'react';

// importing component(s)
import BcTransactions from './BcTransactions';

// CHAIN Presentation Component
const BcChain = ({block}) => {
    console.log("PROPS:", block)
    return (
        <div className="block-disp" >
            <p>Index: {block.index}</p>
            <p>Previous_hash: {block.previous_hash}</p>
            <p>Proof: {block.proof}</p>
            <p>Timestamp: {block.timestamp}</p>
            {block.transactions.length > 0 ? (
                <section><p>Transactions: </p>
                    {block.transactions.map((transaction, i) => {
                                                return <BcTransactions key={i} transaction={transaction} />
                                            })}</section>
            ) : (
                <p>no transactions</p>
            )}
        </div>
    )
}

export default BcChain;