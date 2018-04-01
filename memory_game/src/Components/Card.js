import React, { Component } from 'react';

class Card extends Component {
  constructor(){
    super();
    this.state = {
      classname : "card"
    }
  }
  render() {
    return (
        <div className="card-container" >
            <div className={this.props.flipState? "card flip": "card"} onClick={this.props.flip.bind(this, this.props.index)}>
                <div className="side"> <img alt="Back View" src="UNO-Back.png" /></div>
                <div className={this.props.guessed?"side back guessed":"side back"}>  <img alt={"Back View: "+this.props.character} src={this.props.character+".png"} /></div>
            </div>
        </div>
    );
  }
  
}



export default Card;
