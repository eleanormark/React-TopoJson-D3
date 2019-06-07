import React, {Component} from "react"
import {geoAlbersUsa, geoPath} from "d3-geo"
import {feature} from "topojson-client"
import STATES from "../components/utils/states"
import axios from 'axios';
import {Container} from "semantic-ui-react";

class UnitedStatesMap extends Component {
    constructor(props) {
        super(props)
        this.state = {
          unitedStatesData: [],
        }
      }
      projection() {
        return geoAlbersUsa()
          .scale(1280)
          .translate([ 960 / 2, 600 / 2 ])
      }
      componentDidMount() {
        axios.get("/united_states_topojson.json")
          .then(response => {
            this.setState({
              unitedStatesData: feature(response.data, response.data.objects.states).features,
            })
          })
          .catch((err) => { console.log(err); });
      }
      showTooltip(evt, stateIndex) {
        let tooltip = document.getElementById("tooltip");
        let {id} = this.state.unitedStatesData[stateIndex];
        let total;
        
        if(this.props.physiciansData[STATES[id]]){
          total = this.props.physiciansData[STATES[id]].total
        }
  
        if (total){
          tooltip.innerHTML = `State: ${STATES[id]} <br> Total Physicians: ${total}`;
          tooltip.style.display = "block";
          tooltip.style.left = evt.pageX + 10 + 'px';
          tooltip.style.top = evt.pageY + 10 + 'px';
        }
      }
      hideTooltip() {
        let tooltip = document.getElementById("tooltip");
        tooltip.style.display = "none";
      }
      render() {
        return (
          <Container>
            <div id="tooltip"></div>
            <svg width={960} height={600} >
              <g className="state">
                {
                  this.state.unitedStatesData.map((d,i) => (
                    <path
                      key={`path-${ i }`}
                      d={geoPath().projection(this.projection())(d)}
                      fill="#ECEFF1"
                      stroke="#607D8B"
                      strokeWidth={ 0.75 }
                      onClick={() => this.props.handleStateClick(this.state.unitedStatesData[i].id)}
                      onMouseEnter={(evt) => this.showTooltip(evt, i)}
                      onMouseLeave={() => this.hideTooltip()}
                    />
                  ))
                }
              </g>
            </svg>
          </Container>
        )
      }
}
export default UnitedStatesMap