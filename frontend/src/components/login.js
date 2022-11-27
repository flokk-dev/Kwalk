/*
Creator: Flokk___
Date: 18/11/2022
Version: V1.0

Purpose:
*/

// IMPORT: react
import React, { useContext } from "react";

// IMPORT: context
import AuthContext from "../context/authentification.js";


const LoginComp = () => {
    let {loginUser} = useContext(AuthContext)

    return (
        <div>
            <form onSubmit={loginUser}>
                <input type="text" name="username" placeholder="enter a username"/>
                <input type="password" name="password" placeholder="enter a password"/>
                <input type="submit"/>
            </form>
        </div>
    )
}
export default LoginComp;
