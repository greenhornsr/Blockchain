import React from 'react';

// importing component(s)
import BcChain from './BcChain';

// CHAIN Presentation Component
const BcChainList = (props) => {
    console.log("PROPS:", props)

    return (
        <div className="test-flex" >
            {props.blocks.map((block, i) => {
                return (<BcChain key={i} block={block} />)
            })}
        </div>
    )
}

export default BcChainList;