import React, { Component } from 'react';

class Score extends Component {
  constructor(props){
    super(props);
    console.log("(Score) Difficulty is: "+this.props.difficulty);
    if(this.props.difficulty==="easy"){ 
      this.state = {
        difficultyCoeficent : 1
      };
    }
    else if(this.props.difficulty==="medium"){ 
      this.state = {
        difficultyCoeficent : 2
      };
    }
    else { 
      this.state = {
        difficultyCoeficent : 3
      };
    }
  }
  render() {
    return (
        <div className="Score" >
            {"Your Score is: "+(this.state.difficultyCoeficent *100)}
        </div>
    );
  }
  
}



export default Score;
