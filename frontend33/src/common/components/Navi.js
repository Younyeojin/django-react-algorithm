import React from "react"
import {Link} from 'react-router-dom'
import styled from 'styled-components'

const Navigation = () => (
    <>
    <Nav>
        <NavList>
            <NavtItem><Link to="/counter-old">counter-old</Link></NavtItem>
            <NavtItem><Link to="/todo">Todo</Link></NavtItem>
            <NavtItem><Link to="/signUp">siginUp</Link></NavtItem>
            <NavtItem><Link to="/mathMatics">mathMatics</Link></NavtItem>
            <NavtItem><Link to="/linear">linear</Link></NavtItem>
            <NavtItem><Link to="/nonLinear">nonLinear</Link></NavtItem>
            <NavtItem><Link to="/bruteForce">bruteForce</Link></NavtItem>
            <NavtItem><Link to="/divideConquer">divideConquer</Link></NavtItem>
            <NavtItem><Link to="/greedy">greedy</Link></NavtItem>
            <NavtItem><Link to="/dynamicProgramming">dynamicProgramming</Link></NavtItem>
            <NavtItem><Link to="/backTracking">backTracking</Link></NavtItem>
        </NavList>
    </Nav>
    </>
)
export default Navigation;

const Nav = styled.div`
    width:100%;
    height:30px;
 
    `                                                                
const NavList = styled.ul`
    width:1080px;
    display: flex;
    margin: 0 auto;
`
const NavtItem = styled.li`
    width: 70px auto;
    margin-left: 30px;
    margin-top: 10px;
    display: flex;
`