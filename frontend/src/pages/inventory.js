/*
Creator: Flokk___
Date: 18/11/2022
Version: V1.0

Purpose:
*/

// IMPORT: react
import React, {useState, useEffect} from "react";


const InventoryPage = () => {
    let [cards, setCards] = useState([]);
    useEffect(() => {
        getCards()
    }, []);

    let getCards = async () => {
        let response = await fetch("http://127.0.0.1:8000/api/card/")
        let data = await response.json()

        console.log("DATA: ", data)
        setCards(data)
    }

    return (
        <div>
            <p> Our inventory </p>
        </div>
    )
}
export default InventoryPage
