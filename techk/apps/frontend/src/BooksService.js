import axios from 'axios';
const API_URL = 'http://localhost:8000';

export default class BooksService{

    getBooks() {
        const url = `${API_URL}/api/books/`;
        return axios.get(url).then(response => response.data);
    }
    getCategory() {
        const url = `${API_URL}/api/categories/`;
        return axios.get(url).then(response => response.data);
    }
}
