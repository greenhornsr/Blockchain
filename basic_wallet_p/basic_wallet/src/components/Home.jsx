import React from 'react'

// Styling
import './components.css'

const Home = () => {
    return (
        <div className="home-contain" >
            <h1 className="h1-centers" >WELCOME TO SR-COIN BLOCKCHAIN</h1>
            <h2>Site Map:</h2>
            <section className="sec-methods">
                <h3>METHOD: "GET"</h3>
                    <p>👁 "/chain/": to see the chain. </p>
                    <p>👁 "/last_block/": to see the last block. </p>
            </section>
            <section className="sec-methods">
                <h3>METHOD: "POST"</h3>
                <p>📩 "/mine/": to mine new blocks.</p>
                <p>📩 "/transactions/new": to make a transaction.</p>
            </section>
        </div>
    )
}

export default Home;