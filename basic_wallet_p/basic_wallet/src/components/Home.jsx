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
                    <p><span role="img" aria-label="eye" >👁 </span>"/chain/": to see the chain. </p>
                    <p><span role="img" aria-label="eye" >👁 </span> "/last_block/": to see the last block. </p>
            </section>
            <section className="sec-methods">
                <h3>METHOD: "POST"</h3>
                <p><span role="img" aria-label="sent-message" >📩 </span>"/mine/": to mine new blocks.</p>
                <p><span role="img" aria-label="sent-message" >📩 </span>"/transactions/new": to make a transaction.</p>
            </section>
        </div>
    )
}

export default Home;