import React from 'react';

const BcTransactions = ({transaction}) => {
    return (
        <section>
            <p className="sec-trans" >Sender: {transaction.sender}</p>
            <p className="sec-trans" >Recipient: {transaction.recipient}</p>
            <p className="sec-trans" >Amount: {transaction.amount}</p>
        </section>
    )
}

export default BcTransactions