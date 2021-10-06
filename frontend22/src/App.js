import './App.css';
import { Route, Redirect, Switch } from 'react-router-dom'
import { BackTracking, BruteForce, DivideConquer, DynamicProgramming, Greedy } from 'algorithm';
import { Navigation, Home, Counter, Todo, SiginUp, UserJoin} from 'common';
import { Linear, Mathmatics, NonLinear } from 'datastucture';
import {createStore, combineReducers} from 'redux'
import {Provider} from 'react-redux'
import { todoReducer, siginUpReducer } from 'reducers';
const rootReducer = combineReducers({todoReducer, siginUpReducer})
const store = createStore(rootReducer)
const App = () => (
  <Provider store={store}>
    <Navigation/>
      <Switch>
        <Route exact path='/'component = {Home}/>
        <Redirect from='/home'to = {'/'}/>
        <Route exact path='/counter'component = {Counter}/>
        <Route exact path='/todo'component = {Todo}/>
        <Route exact path='/siginUp'component = {SiginUp}/>
        <Route exact path='/backTracking'component = {BackTracking}/>
        <Route exact path='/bruteForce'component = {BruteForce}/>
        <Route exact path='/divideConquer'component = {DivideConquer}/>
        <Route exact path='/dynamicProgramming'component = {DynamicProgramming}/>
        <Route exact path='/greedy'component = {Greedy}/>
        <Route exact path='/mathMatics'component = {Mathmatics}/>
        <Route exact path='/linear'component = {Linear}/>
        <Route exact path='/nonLinear'component = {NonLinear}/>
      </Switch>
  </Provider>
) 

export default App
