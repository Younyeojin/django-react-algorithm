import { TodoList, TodoInput } from "features/todos"
import React from "react"

export default function Todo(){
    return(
        <div>
            <TodoInput/>
            <TodoList/>
        </div>
    )
}