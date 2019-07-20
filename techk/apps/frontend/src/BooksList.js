import  React, { Component } from  'react';
import  BooksService  from  './BooksService';

const  booksService = new BooksService();

class  BooksList extends Component{

constructor(){
    super();
    this.state={
        books:[]
    };
}

componentDidMount() {
    var self = this;
    booksService.getBooks().then(function (result){
        console.log(result);
        self.setState({books: result})
    });
}

render() {
    return(
      <div className="bookslist">
          <table className="table">
              <thead key="thead">
              <tr>
                  <th>Category</th>
                  <th>Title</th>
                  <th>Price</th>
                  <th>Stock</th>
                  <th>Product Description</th>
                  <th>UPC</th>
              </tr>
              </thead>
              <tbody>
                  {this.state.books.map( b =>
                  <tr>
                  <td>{b.category_id}</td>
                  <td>{b.title}</td>
                  <td>{b.price}</td>
                  <td>{b.stock}</td>
                  <td>{b.product_description}</td>
                  <td>{b.upc}</td>
                  </tr>)}
              </tbody>
          </table>
      </div>
    );
  }
}
export default BooksList;
