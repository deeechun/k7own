import React from 'react';

class App extends React.Component{
    constructor(props){
        super(props);
        this.state = {
            requestFailed: false
        }
    }
    componentWillMount(){
        var url = "http://138.197.212.128:80/api/homes?callback=?";
        fetch(url)
            .then(response => response.json())
            .then(response => {
            this.setState({
                postData: response
            });
        });
    }
    render(){
        if (!this.state.postData) return(
            <p>Loading ...</p>
        );
        return(
            <div>
                <h2>{this.state.postData.homes}</h2>
            </div>
        );
    }
}

export default App;

