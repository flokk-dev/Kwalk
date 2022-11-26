/*
Creator: Flokk___
Date: 18/11/2022
Version: V1.0

Purpose:
*/

// IMPORT: components
import InventoryPage from "./pages/inventory.js";

// IMPORT: components
import Header from "./components/header.js";


// IMPORT: css
import "./App.css";

function App() {
    return (
        <div className="App">
            <Header/>
            <InventoryPage/>
        </div>
    );
}

export default App;
