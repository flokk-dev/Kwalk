/*
Creator: Flokk___
Date: 18/11/2022
Version: V1.0

Purpose:
*/

// IMPORT: react
import React, { useContext } from "react";
import { Link } from "react-router-dom";

// IMPORT: context
import AuthContext from "../context/authentification.js";

// IMPORT: components
import LoginComp from "./login.js";


const SidebarComp = () => {
    let {name} = useContext(AuthContext)

    return (
        <div>
            <p> Sidebar </p>
            <Link to="/"> Home </Link>
            <Link to="/inventory"> Inventory </Link>

            <p> Hello {name} </p>
            <LoginComp/>
        </div>
    )
}
export default SidebarComp;
