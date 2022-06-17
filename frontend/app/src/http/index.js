import axios from 'axios'


const http = axios.create(
    {
        baseURL: 'https://tinapiprojeto.herokuapp.com/',
        //baseURL: 'http://localhost:8000',
        headers: {
            'Accept': 'application',
            'Content': 'application/json'
        }
    }
);

http.interceptors.request.use(
    function(config) {
        console.log(`INTERCEPTOR REQUEST: ${config}`);
        return config;
    },

    function (erro) {
        console.log(`INTERCEPTOR REQUEST ERRO: ${erro}`);
        return Promise.reject(erro);
    }
);

export default http;