import React from "react"
import styled from 'styled-components'
import { useSelector} from 'react-redux'
export default function UserList(){
    const siginUps = useSelector(state=>state.siginUpReducer.siginUps)
    return(
        <Div>
            {siginUps.length === 0 && (<h1>회원가입 정보가 없습니다</h1>)}
            {siginUps.length !== 0 && (<h1>{siginUps.length} 개의 회원정보가 있습니다 </h1>)}
        </Div>
        
    )
}

const Div = styled.div`text-align: center`