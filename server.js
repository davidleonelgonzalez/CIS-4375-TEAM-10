
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

const PORT = process.env.PORT || 5000;

//login--------------------------------------------------------------------------------------------------------------------------

app.get('/login', function(req, res) {

    var username = req.body.username

    var password = req.body.password

    console.log(username)


    res.render('pages/login', {

  });
});
//-------------------------------------------------------------------------------------------------------------------------------

//home----------------------------------------------------------------------------------------------------------------------------

app.get('/', function(req, res) {


  res.render('pages/home', {

});
});


//-------------------------------------------------------------------------------------------------------------------------------

//region-------------------------------------------------------------------------------------------------------------------------


app.get('/region', function(req, res) {
  axios.get(`http://127.0.0.1:5000/region/all`)
  .then((response)=>{
      
      var region = response.data;


      res.render('pages/region', {
          region: region
  });
});

app.post('/addregion', function(req, res){
  var addRegionName = req.body.region_name;

  axios.post(`http://127.0.0.1:5000/addregion`,{
    
      region_name: addRegionName
    })
    .then(function(response) {
      console.log(response.data);
    })

    res.render('pages/submit')

});
});


app.put('/updateregion', function(req, res){
  var updateRegionName = req.body.region_name;

  axios.put(`http://127.0.0.1:5000/updateregion`,{
      id:5000,
      region_name: updateRegionName
    })
    .then(function(response) {
      console.log(response.data);
    })

  res.render('pages/submit')

});



app.delete('/deleteregion', function(req, res){
  var deleteRegionName = req.body.region_name;


  axios.delete(`http://127.0.0.1:5000/deleteregion`,{
      id:5000,
      region_name: deleteRegionName

    })
    .then(function(response) {
      console.log(response.data);
    })


    res.render('pages/submit')

});


//----------------------------------------------------------------------------------------------------------------------


//country---------------------------------------------------------------------------------------------------------------


app.get('/country', function(req, res) {
  axios.get(`http://127.0.0.1:5000/country/all`)
  .then((response)=>{
      
      var country = response.data;


      res.render('pages/country', {
          country: country
  });
});

app.post('/addcountry', function(req, res){
  var addCountryName = req.body.country_name;
  var addRegionID =req.body.region_id;

  axios.post(`http://127.0.0.1:5000/addcountry`,{
    
      country_name: addCountryName,
      region_id: addRegionID
    })
    .then(function(response) {
      console.log(response.data);
    })

  res.render('pages/submit')

});
});


app.put('/updatecountry', function(req, res){
  var updateCountryName = req.body.country_name;
  var updateRegionID = req.body.region_id;

  axios.put(`http://127.0.0.1:5000/updatecountry`,{
      id:5000,
      country_name: updateCountryName,
      region_id: updateRegionID
    })
    .then(function(response) {
      console.log(response.data);
    })

  res.render('pages/submit')

});



app.delete('/deletecountry', function(req, res){
  var deleteCountryName = req.body.country_name;
  var deleteRegionID = req.body.region_id


  axios.delete(`http://127.0.0.1:5000/deletecountry`,{
      id:5000,
      country_name: deleteCountryName
      region_id: deleteRegionID

    })
    .then(function(response) {
      console.log(response.data);
    })


  res.render('pages/submit')

});

//-------------------------------------------------------------------------------------------------------------


//vendor------------------------------------------------------------------------------------

app.get('/vendor', function(req, res) {
  axios.get(`http://127.0.0.1:5000/vendor/all`)
  .then((response)=>{
      
      var vendor = response.data;


      res.render('pages/vendor', {
        vendor: vendor
  });
});

app.post('/addvendor', function(req, res){
  var addVendorName = req.body.vendor_name;
  var addVendorPhone =req.body.vendor_phone;
  var addVendorEmail =req.body.vendor_email;
  var addSoftwareType =req.body.software_type;
  var addHardwareType =req.body.hardware_type;

  axios.post(`http://127.0.0.1:5000/addvendor`,{
    
      vendor_name: addVendorName,
      vendor_phone: addVendorPhone,
      vendor_email: addVendorEmail,
      software_type: addSoftwareType,
      hardware_type: addHardwareType
    })
    .then(function(response) {
      console.log(response.data);
    })

  res.render('pages/submit')

});
});


app.put('/updatevendor', function(req, res){
  var updateVendorName = req.body.vendor_name;
  var updateVendorPhone =req.body.vendor_phone;
  var updateVendorEmail =req.body.vendor_email;
  var updateSoftwareType =req.body.software_type;
  var updateHardwareType =req.body.hardware_type;


  axios.put(`http://127.0.0.1:5000/updatevendor`,{
      id:5000,
      vendor_name: updateVendorName,
      vendor_phone: updateVendorPhone,
      vendor_email: updateVendorEmail,
      software_type: updateSoftwareType,
      hardware_type: updateHardwareType
    })
    .then(function(response) {
      console.log(response.data);
    })

  res.render('pages/submit')

});



app.delete('/deletevendor', function(req, res){
  var deleteVendorName = req.body.vendor_name;
  var deleteVendorPhone =req.body.vendor_phone;
  var deleteVendorEmail =req.body.vendor_email;
  var deleteSoftwareType =req.body.software_type;
  var deleteHardwareType =req.body.hardware_type;


  axios.delete(`http://127.0.0.1:5000/deletevendor`,{
    id:5000,
    vendor_name: deleteVendorName,
    vendor_phone: deleteVendorPhone,
    vendor_email: deleteVendorEmail,
    software_type: deleteSoftwareType,
    hardware_type: deleteHardwareType
    })
    .then(function(response) {
      console.log(response.data);
    })


  res.render('pages/submit')

});

//---------------------------------------------------------------------------------------





app.listen(PORT, () => {
  console.log(`StraWin listening at http://localhost:${PORT}/`)
});