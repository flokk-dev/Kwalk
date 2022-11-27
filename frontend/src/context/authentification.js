/*
Creator: Flokk___
Date: 18/11/2022
Version: V1.0

Purpose:
*/

// IMPORT: react
import { createContext, useState, useEffect } from "react";


const AuthContext = createContext(undefined)
export default AuthContext;

export const AuthProvider = ({children}) => {
    let [authTokens, setAuthTokens] = useState(null)
    let [user, setUser] = useState(null)

    let loginUser = async (e ) => {
        e.preventDefault()
        let response = fetch("http://127.0.0.1:8000/api/token/", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body:JSON.stringify({"username": e.target.username.value, "password": e.target.password.value})
        })

        let data = response.json
        console.log(response.status)
        if (response.status === 200){

        } else {
            alert("Something went wrong!")
        }

    }

    let contextData = {
        loginUser: loginUser
    }

    return (
        <AuthContext.Provider value={contextData}>
            {children}
        </AuthContext.Provider>
    )
}
