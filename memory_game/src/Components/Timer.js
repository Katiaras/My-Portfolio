import React, { Component } from 'react';

class Timer extends Component {
  constructor(props){
    super(props);
    this.state = {
      time: 60
    }
   var timeInterval = setInterval(()=>{ this.setState({time:(this.state.time-1)}) }, 1000);
   var clearTimer = (this.state.time+.5)*1000; // time interval time with .5 sec delay 
   let dis = this;
   setTimeout(function(){
      alert("Time Out: GAME OVER, TRY AGAIN LATER");
      clearInterval(timeInterval);
      setTimeout(function(){
        // alert('Time to Change View');
        dis.props.reset();
      },2000);
    },clearTimer );
    console.log(this.props);
  }
  setTimer = function (){
      // console.log("On load");
  }
  render() {
    return (
        <div onLoad={this.setTimer.bind()} className="timer" >
            {this.state.time}
        </div>
    );
  }
  
}



export default Timer;
