import  React, { Component } from  'react';
import { BrowserRouter } from  'react-router-dom'
import { Route} from  'react-router-dom'
import  BooksList  from  './BooksList'
import  './App.css';

const BaseLayout = () => (
<div class="container-fluid">
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse"  id="navbarNavAltMarkup">
        <div class="navbar-nav">
            <a class="nav-item nav-link"  href="/">Inicio</a>
        </div>
    </div>
    </nav>
    <div class="content">
        <Route path="/" exact component={BooksList}/>
    </div>
</div>
)

class App extends Component {
  render() {
    return (
      <BrowserRouter>
        <BaseLayout/>
      </BrowserRouter>
    );
  }
}

export default App;
