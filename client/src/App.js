import React, { Component } from "react"
import './App.css';
import axios from 'axios';
import STATES from './components/utils/states'

import UnitedStatesMap from "./components/UnitedStatesMap"
import StateSpecialtiesList from "./components/StateSpecialtiesList"

class App extends Component {
  constructor() {
    super()
    this.state = {
      physiciansData: {},
      stateSpecialtiesData: {},
      clickedState: ''
    }
    this.handleStateClick = this.handleStateClick.bind(this);
  }
  componentDidMount() {
    axios.get("/physicians")
      .then(response => {
        const objList = {};
        for (let obj of response.data.physicians){
          if (!objList[obj.state]) {
            objList[obj.state] = [];
            objList[obj.state].total = 0;
          } 
          objList[obj.state].push(obj)

          if (!obj.specialty) {
            objList[obj.state].total += obj.count;
          }  
      }
      this.setState({
        physiciansData: objList
      })
        
      }) 
      .catch((err) => { console.log(err); });
    }
    handleStateClick(id) {
      this.setState(
        {stateSpecialtiesData: this.state.physiciansData[STATES[id]]}
      )
      this.setState(
        {clickedState: STATES[id]}
      )
    }
    render() {
      return (
        <div>
          <UnitedStatesMap 
            physiciansData={this.state.physiciansData} 
            handleStateClick={this.handleStateClick}
            />
          <StateSpecialtiesList state={this.state.clickedState} stateSpecialties={this.state.stateSpecialtiesData}/>
        </div>
      );
    }
  }
export default App;
