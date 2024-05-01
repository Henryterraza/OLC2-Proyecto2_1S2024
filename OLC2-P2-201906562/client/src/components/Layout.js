import React from "react";
import Navbar from "./Navbar";
import Editor from "../pages/Home";
import Home from "../pages/Home";


function Layout() {
    // codigo de js

    return (
        <React.Fragment>
            <Navbar></Navbar>
            <Home></Home>
        </React.Fragment>
    );
}

export default Layout