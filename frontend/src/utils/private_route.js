/*
Creator: Flokk___
Date: 18/11/2022
Version: V1.0

Purpose:
*/

// IMPORT: react
import { Route, Navigate } from "react-router-dom";


const PrivateRoute = ({children, ...rest}) => {
    const authenticated = false
    return (
        <Route {...rest}> {!authenticated ? <Navigate to="/inventory"/> : children} </Route>
    )
}
export default PrivateRoute;
