var express = require('express')
const app = express()
app.use(express.json())

app.get('/',function(req,res) {

    console.log("GET Request Received");
    res.send('<h2 style="font-family: Verdana; color: blue;"> Welcome to ExpressJS</h2>');
})

app.post('/addcourse', function(req,res) {
    console.log("POST Request Received");
    res.send(' <h2 style="font-family: Verdana; color:green"> A new course has been added </h2>');
})

app.delete('/delete', function(req,res) {
    console.log("DELETE Request Received");
    res.send(' <h2 style="font-family: Verdana; color:red"> A new course has been deleted </h2>');
})

app.get('/course', function(req,res) {
    console.log("GET Request Received");
    res.send(' <h2 style="font-family: Verdana; color:blue"> Course Available </h2>');
})

//PORT ENVIRONMENT VARIABLE
const port = process.env.PORT || 8080;
app.listenerCount(port, ()=> console.log(`Listening to Port ${port}`));
