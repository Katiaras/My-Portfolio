import React, { Component } from 'react';
import _ from 'lodash';
import Card from './Card';
import Timer from './Timer';
import Score from './Score';
import shuffle from 'shuffle-array';
class Game extends Component {
  constructor(props){
    super(props);
    
   
    this.defaultStates ={//8 Cards
        easy: shuffle( [
          {character: 'a',flipState: false, id:0, guessed: false },
          {character: 'b',flipState: false, id:1, guessed: false },
          {character: 'a',flipState: false, id:2, guessed: false },
          {character: 'b',flipState: false, id:3, guessed: false },
          // {character: 'c',flipState: false, id:4, guessed: false },
          // {character: 'd',flipState: false, id:5, guessed: false },
          // {character: 'c',flipState: false, id:6, guessed: false },
          // {character: 'd',flipState: false, id:7, guessed: false },
        ]),
        medium: shuffle( [//12 Cards
          {character: 'a',flipState: false, id:0, guessed: false },
          {character: 'b',flipState: false, id:1, guessed: false },
          {character: 'a',flipState: false, id:2, guessed: false },
          {character: 'b',flipState: false, id:3, guessed: false }, 
          {character: 'c',flipState: false, id:4, guessed: false },
          {character: 'd',flipState: false, id:5, guessed: false },
          {character: 'c',flipState: false, id:6, guessed: false },
          {character: 'd',flipState: false, id:7, guessed: false },
          {character: 'e',flipState: false, id:8, guessed: false },
          {character: 'f',flipState: false, id:9, guessed: false },
          {character: 'e',flipState: false, id:10, guessed: false },
          {character: 'f',flipState: false, id:11, guessed: false },
        ]),
        hard: shuffle( [//12 Cards
          {character: 'a',flipState: false, id:0, guessed: false },
          {character: 'b',flipState: false, id:1, guessed: false },
          {character: 'a',flipState: false, id:2, guessed: false },
          {character: 'b',flipState: false, id:3, guessed: false }, 
          {character: 'c',flipState: false, id:4, guessed: false },
          {character: 'd',flipState: false, id:5, guessed: false },
          {character: 'c',flipState: false, id:6, guessed: false },
          {character: 'd',flipState: false, id:7, guessed: false },
          {character: 'e',flipState: false, id:8, guessed: false },
          {character: 'f',flipState: false, id:9, guessed: false },
          {character: 'e',flipState: false, id:10, guessed: false },
          {character: 'f',flipState: false, id:11, guessed: false },
          {character: 'g',flipState: false, id:12, guessed: false },
          {character: 'g',flipState: false, id:13, guessed: false },
          {character: 'h',flipState: false, id:14, guessed: false },
          {character: 'h',flipState: false, id:15, guessed: false },
          {character: 'i',flipState: false, id:16, guessed: false },
          {character: 'i',flipState: false, id:17, guessed: false },
        ])
    };

   
  
    if(this.props.difficulty==="easy"){
      this.state ={
        easy: this.defaultStates.easy,
        count : 0, 
        guesses: []
        };
    }
    else if (this.props.difficulty==="medium") {
      this.state ={
        easy: this.defaultStates.medium,
        count : 0, 
        guesses: []
        };
    } else {
      this.state ={
        easy: this.defaultStates.hard,
        count : 0, 
        guesses: []
        };
    }   
  }
 
  renderCards(){
    return _.map(this.state.easy, (card, index) => <Card key={index} index={index} {...card}  flip = {this.flip.bind(this)}/>);
  }
  renderWon(){
    let dis = this; 
    setTimeout(function(){
      // alert('Time to Change View');
      dis.props.reset();
    },5000);
    return(
      <div>
        <h1>Congratulations!!!!  </h1> <br/>
        <h1> YOU WON </h1>
        <Score difficulty={this.props.difficulty} />
      </div>
    );
  }
 
  //-------------------PROMISES-------------------
  promisePaintGreen(guesses, dis){ 
    return new Promise(function(resolve,reject){
      // If Guessed, first paint the blocks to Green
      let temp = dis.state.easy.slice();
      guesses[0].guessed = true;
      guesses[1].guessed = true;
      //Find the index of the arrays by ID
      let tempIndex =[ dis.state.easy.findIndex(el => el.id===guesses[0].id),
      dis.state.easy.findIndex(el => el.id===guesses[1].id)
      ];

      temp[tempIndex[0]]=guesses[0];
      temp[tempIndex[1]]=guesses[1];
      dis.setState({easy: temp});
      console.log("Paint Green Resolved");
      //Set State, bit only resolve after 1 second
      setTimeout(resolve, 1500);
    });
  };
  reset(){

    console.log("Resetting...");
    this.setState({count: 0});
    let arr = this.state.easy;
    arr.forEach(function(element) {
      element.flipState= false;
    });
    this.setState({easy: arr, guesses:[]});
    return new Promise(function(resolve,reject){
      console.log("Reset Resolved");
      setTimeout(function(){
        resolve("Reset Resolved");
      },1000);
    });
  }
  checkWinningConditions(){
    let guesses = this.state.guesses;
    var dis = this;
    console.log(guesses);

    //Guessing Condition must be 2 Different Blocks
    if(guesses[0].character === guesses[1].character && guesses[0].id !== guesses[1].id  ){
      
      this.promisePaintGreen(guesses, this).then(function(){
        return  dis.reset();
        }).then(function(result){
        return new Promise(function(resolve, reject){
          let temp = dis.state.easy.slice();
          _.remove(temp, {character: guesses[0].character});
          dis.setState({easy: temp});

          console.log("Remove the Guessed from The game");
          resolve("Remove the Guessed from The game");
        });
      });
    }
    else{
      setTimeout(function() { this.reset(); }.bind(this), 1500);
    }
  }
  flip(index)
  {
    const flip = this.state.easy;
    flip[index].flipState=!flip[index].flipState;
    // flip.splice(index, 1);
    this.setState({easy: flip});
    this.state.guesses.push(this.state.easy[index]);
    // console.log(this.state.count);
    this.state.count++;
    if(this.state.count===2){
      this.checkWinningConditions();
      // setTimeout(function() { this.reset(); }.bind(this), 1500);
    }   
  }

  render() {
    return (
      <div className="App">
        <Timer  reset = {this.props.reset.bind(this)} />
        {this.state.easy.length>1 ? this.renderCards(): this.renderWon()}
        
      </div>
      
    );
  }
}

export default Game;
