import React from 'react';

const BcTransactions = ({transaction}) => {
    return (
        <section>
            <p>Sender: {transaction.sender}</p>
            <p>Recipient: {transaction.recipient}</p>
            <p>Amount: {transaction.amount}</p>
        </section>
    )
}

export default BcTransactions