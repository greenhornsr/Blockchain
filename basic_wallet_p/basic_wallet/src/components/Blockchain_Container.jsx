import React, {useState, useEffect} from 'react'
import axios from 'axios'

// importing component(s)
import BcChainList from './BcChainList';

// styling
import './component.css'

const Blockchain_Container = () => {
    const [bcdata, setBcdata] = useState()

    function getData(){
        axios.get('http://localhost:5000/chain/')
        .then(res => {
            // console.log("res: ", res)
            // console.log("res.data.chain", res.data.chain)
            setBcdata(res.data.chain)
        })
        .catch(err => {
            console.log(err)
        })
    }

    useEffect(() => {
        getData()
    }, [])
    

    return (
        <div className="bc-container" >
            {!bcdata ? (
            <h1>Loading...</h1>
            ) : (
            <div>
                <h1>Home Sweet Home</h1>
                <BcChainList blocks={bcdata} />
            </div>
            )}
        </div>
    )
}

export default Blockchain_Container