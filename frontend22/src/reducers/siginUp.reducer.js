const initialState = {siginUps:[], siginUp:{}}
export const addSiginUpAction = siginUp => ({type: "ADD_SIGINUP", payload: siginUp})
const siginUpReducer = (state = initialState, action) => {
    switch(action.type){
        case 'ADD_SIGINUP': return {...state, siginUps:[...state.siginUps, action.payload]}
        default : return state
    }
}

export default siginUpReducer