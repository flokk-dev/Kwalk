/*
Creator: Flokk___
Date: 18/11/2022
Version: V1.0

Purpose:
*/

// IMPORT: react
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

// IMPORT: utils
import PrivateRoute from "./utils/private_route.js";

// IMPORT: context
import { AuthProvider } from "./context/authentification.js";

// IMPORT: pages
import HomePage from "./pages/home.js";
import InventoryPage from "./pages/inventory.js";

// IMPORT: components
import SidebarComp from "./components/sidebar.js";

// IMPORT: css
import "./App.css";


function App() {
    return (
        <div className="App">
            <Router>
                <AuthProvider>
                    <SidebarComp/>
                    <Routes>
                        <Route path="/" element={<HomePage/>} exact/>
                        <Route path="/inventory" element={<InventoryPage/>}/>
                    </Routes>
                </AuthProvider>
            </Router>
        </div>
    );
}

export default App;
