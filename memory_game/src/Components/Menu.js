import React, { Component } from 'react';
import Game from './Game';
class Menu extends Component {
  constructor(){
    super();
    this.state = {
    menu: true,
     difficulty: "",
    };
    this.defaultState = {
        menu: true,
        difficulty: "",
    };
  }
  choice(dif){
    this.setState({menu:false,difficulty:dif });
  }
  renderMenu(){
    return(
    <div className="Menu">
        <button type="button" className="button button1" onClick={this.choice.bind(this,"easy")}>Easy</button> 
        <button type="button" className="button button2" onClick={this.choice.bind(this,"medium")}>Medium</button> 
        <button type="button" className="button button3" onClick={this.choice.bind(this,"hard")}>Hard</button> 
    </div>
    )
  }
  reset(){
      this.setState( this.defaultState)
  }
  renderGame(){
    return(
        <div>
          <Game difficulty={this.state.difficulty}  reset = {this.reset.bind(this)}/>
        </div>
      );
    }

  render() {
    return (
        <div>
            { this.state.menu ? this.renderMenu(): this.renderGame()}
        </div>
    );
  }
  
}



export default Menu;
