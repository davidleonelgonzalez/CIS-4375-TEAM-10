var express = require('express');
var app = express();
const bodyParser  = require('body-parser');
// body parser in use

//creating axios to call on my rest api
const axios = require('axios');

//app will then use body parser
app.use(bodyParser.urlencoded());

//the app will set to view engine  to call ejs in view folder
app.set('view engine', 'ejs');


//home page start--------------------------------------------------------------------------------------------------------------------------------------------------------
// Now this is the start of my home page sever use

//using get for the app on route '/' 
//Created tagline to appear on home page
app.get('/', function(req, res) {


      res.render('pages/home', {

  });
});

app.listen(1234);
console.log('StraWin Loading Complete');