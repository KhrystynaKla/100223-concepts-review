import {useEffect, useState} from 'react'

function GiftList(){
    const [gifts,setGifts]=useState([])
    useEffect(()=>{
        fetch('/gifts')
        .then(res=>res.json())
        .then(data => setGifts(data))
    },[])


    return (
        <div>
            {gifts.map(g=> <li>{g.name} - ${g.price}</li>)}
        </div>
    )
}

export default GiftList