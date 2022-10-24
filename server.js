
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
  var addRegionID = req.body.region_id;

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
      country_name: deleteCountryName,
      region_id: deleteRegionID

    })
    .then(function(response) {
      console.log(response.data);
    })


  res.render('pages/submit')

});

//-------------------------------------------------------------------------------------------------------------


//state --------------------------------------------------------------------------------------------------------


app.get('/state', function(req, res) {
  axios.get(`http://127.0.0.1:5000/state/all`)
  .then((response)=>{
      
      var state = response.data;


      res.render('pages/state', {
          state: state
  });
});

app.post('/addstate', function(req, res){
  var addStateName = req.body.state_providence_name;
  var addCountryID = req.body.country_id;

  axios.post(`http://127.0.0.1:5000/addstate`,{
    
      state_providence_name: addStateName,
      country_id: addCountryID
    })
    .then(function(response) {
      console.log(response.data);
    })

  res.render('pages/submit')

});
});


app.put('/updatestate', function(req, res){
  var updateStateName = req.body.state_providence_name;
  var updateCountryID = req.body.country_id;

  axios.put(`http://127.0.0.1:5000/updatestate`,{
      id:5000,
      state_providence_name: updateStateName,
      country_id: updateCountryID
    })
    .then(function(response) {
      console.log(response.data);
    })

  res.render('pages/submit')

});



app.delete('/deletestate', function(req, res){
  var deleteStateName = req.body.state_providence_name;
  var deleteCountryID = req.body.country_id


  axios.delete(`http://127.0.0.1:5000/deletecountry`,{
      id:5000,
      state_providence_name: deleteStateName,
      country_id: deleteCountryID

    })
    .then(function(response) {
      console.log(response.data);
    })


  res.render('pages/submit')

});

//--------------------------------------------------------------------------------------------------------------


//vendor--------------------------------------------------------------------------------------------------------

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
  var addVendorPhone = req.body.vendor_phone;
  var addVendorEmail = req.body.vendor_email;
  var addSoftwareType = req.body.software_type;
  var addHardwareType = req.body.hardware_type;

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
  var updateVendorPhone = req.body.vendor_phone;
  var updateVendorEmail = req.body.vendor_email;
  var updateSoftwareType = req.body.software_type;
  var updateHardwareType = req.body.hardware_type;


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
  var deleteVendorPhone = req.body.vendor_phone;
  var deleteVendorEmail = req.body.vendor_email;
  var deleteSoftwareType = req.body.software_type;
  var deleteHardwareType = req.body.hardware_type;


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

//cloud server---------------------------------------------------------------------------

app.get('/server', function(req, res) {
  axios.get(`http://127.0.0.1:5000/server/all`)
  .then((response)=>{
      
      var server = response.data;


      res.render('pages/server', {
        server: server
  });
});

app.post('/addserver', function(req, res){
  var addVMType = req.body.vm_type;
  var addServerNumber = req.body.server_number;
  var addServerLocation = req.body.server_location;
  var addVendorID = req.body.vendor_id;

  axios.post(`http://127.0.0.1:5000/addserver`,{
    
      vm_type: addVMType,
      server_number: addServerNumber,
      server_location: addServerLocation,
      venodr_id: addVendorID
    })
    .then(function(response) {
      console.log(response.data);
    })

  res.render('pages/submit')

});
});


app.put('/updateserver', function(req, res){
  var updateVMType = req.body.vm_type;
  var updateServerNumber = req.body.server_number;
  var updateServerLocation = req.body.server_location;
  var updateVendorID = req.body.vendor_id;


  axios.put(`http://127.0.0.1:5000/updateserver`,{
      id:5000,
      vm_type: updateVMType,
      server_number: updateServerNumber,
      server_location: updateServerLocation,
      venodr_id: updateVendorID
    })
    .then(function(response) {
      console.log(response.data);
    })

  res.render('pages/submit')

});



app.delete('/deleteserver', function(req, res){
  var deleteVMType = req.body.vm_type;
  var deleteServerNumber = req.body.server_number;
  var deleteServerLocation = req.body.server_location;
  var deleteVendorID = req.body.vendor_id;


  axios.delete(`http://127.0.0.1:5000/deleteserver`,{
    id:5000,
    vm_type: deleteVMType,
    server_number: deleteServerNumber,
    server_location: deleteServerLocation,
    venodr_id: deleteVendorID
    })
    .then(function(response) {
      console.log(response.data);
    })


  res.render('pages/submit')

});

//-----------------------------------------------------------------------------------------

//product ---------------------------------------------------------------------------------

app.get('/product', function(req, res) {
  axios.get(`http://127.0.0.1:5000/product/all`)
  .then((response)=>{
      
      var product = response.data;


      res.render('pages/product', {
        product: product
  });
});

app.post('/addproduct', function(req, res){
  var addProductSKU = req.body.product_sku;
  var addProductName = req.body.product_name;
  var addProductDescription = req.body.product_description;
  var addCategory = req.body.category;
  var addServerID = req.body.server_id;
  var addClientID = req.body.client_id;
  var addProspectID = req.body.prospect_id;

  axios.post(`http://127.0.0.1:5000/addproduct`,{
    
      product_sku: addProductSKU,
      product_name: addProductName,
      product_description: addProductDescription,
      category: addCategory,
      server_id: addServerID,
      client_id: addClientID,
      prospect_id: addProspectID

    })
    .then(function(response) {
      console.log(response.data);
    })

  res.render('pages/submit')

});
});


app.put('/updateproduct', function(req, res){
  var updateProductSKU = req.body.product_sku;
  var updateProductName = req.body.product_name;
  var updateProductDescription = req.body.product_description;
  var updateCategory = req.body.category;
  var updateServerID = req.body.server_id;
  var updateClientID = req.body.client_id;
  var updateProspectID = req.body.prospect_id;

  axios.put(`http://127.0.0.1:5000/updateproduct`,{
      id:5000,
      product_sku: updateProductSKU,
      product_name: updateProductName,
      product_description: updateProductDescription,
      category: updateCategory,
      server_id: updateServerID,
      client_id: updateClientID,
      prospect_id: updateProspectID
    })
    .then(function(response) {
      console.log(response.data);
    })

  res.render('pages/submit')

});



app.delete('/deleteproduct', function(req, res){
  var deleteProductSKU = req.body.product_sku;
  var deleteProductName = req.body.product_name;
  var deleteProductDescription = req.body.product_description;
  var deleteCategory = req.body.category;
  var deleteServerID = req.body.server_id;
  var deleteClientID = req.body.client_id;
  var deleteProspectID = req.body.prospect_id;

  axios.delete(`http://127.0.0.1:5000/deleteproduct`,{
    id:5000,
    product_sku: deleteProductSKU,
    product_name: deleteProductName,
    product_description: deleteProductDescription,
    category: deleteCategory,
    server_id: deleteServerID,
    client_id: deleteClientID,
    prospect_id: deleteProspectID
    })
    .then(function(response) {
      console.log(response.data);
    })


  res.render('pages/submit')

});

//------------------------------------------------------------------------------------------

//department--------------------------------------------------------------------------------

app.get('/department', function(req, res) {
  axios.get(`http://127.0.0.1:5000/department/all`)
  .then((response)=>{
      
      var department = response.data;


      res.render('pages/department', {
        department: department
  });
});

app.post('/adddepartment', function(req, res){
  var addDepartmentName = req.body.department_name;


  axios.post(`http://127.0.0.1:5000/adddepartment`,{
    
    department_name: addDepartmentName,

    })
    .then(function(response) {
      console.log(response.data);
    })

  res.render('pages/submit')

});
});


app.put('/updatedepartment', function(req, res){
  var updateDepartmentName = req.body.department_name;

  axios.put(`http://127.0.0.1:5000/updatedepartment`,{
      id:5000,
      department_name: updateDepartmentName,

    })
    .then(function(response) {
      console.log(response.data);
    })

  res.render('pages/submit')

});



app.delete('/deletedepartment', function(req, res){
  var deleteDepartmentName = req.body.department_name;

  axios.delete(`http://127.0.0.1:5000/deletedepartment`,{
    id:5000,
    department_name: deleteDepartmentName,

    })
    .then(function(response) {
      console.log(response.data);
    })


  res.render('pages/submit')

});

//---------------------------------------------------------------------------

//employee status------------------------------------------------------------

app.get('/employee_status', function(req, res) {
  axios.get(`http://127.0.0.1:5000/employee_status/all`)
  .then((response)=>{
      
      var employee_status = response.data;


      res.render('pages/employee_status', {
        employee_status: employee_status
  });
});

app.post('/addemployee_status', function(req, res){
  var addEmployeeStatus = req.body.status_name;


  axios.post(`http://127.0.0.1:5000/addemployee_status`,{
    
    status_name: addEmployeeStatus,

    })
    .then(function(response) {
      console.log(response.data);
    })

  res.render('pages/submit')

});
});


app.put('/updateemployee_status', function(req, res){
  var updateEmployeeStatus = req.body.status_name;

  axios.put(`http://127.0.0.1:5000/updateemployee_status`,{
      id:5000,
      status_name: updateEmployeeStatus,

    })
    .then(function(response) {
      console.log(response.data);
    })

  res.render('pages/submit')

});



app.delete('/deleteemployee_status', function(req, res){
  var deleteEmployeeStatus = req.body.status_name;

  axios.delete(`http://127.0.0.1:5000/deleteemployee_status`,{
    id:5000,
    status_name: deleteEmployeeStatus,

    })
    .then(function(response) {
      console.log(response.data);
    })


  res.render('pages/submit')

});

//--------------------------------------------------------------------------


//client status ------------------------------------------------------------


app.get('/client_status', function(req, res) {
  axios.get(`http://127.0.0.1:5000/client_status/all`)
  .then((response)=>{
      
      var client_status = response.data;


      res.render('pages/client_status', {
        client_status: client_status
  });
});

app.post('/addclient_status', function(req, res){
  var addClientStatus = req.body.status_name;


  axios.post(`http://127.0.0.1:5000/addclient_status`,{
    
    status_name: addClientStatus,

    })
    .then(function(response) {
      console.log(response.data);
    })

  res.render('pages/submit')

});
});


app.put('/updateclient_status', function(req, res){
  var updateClientStatus = req.body.status_name;

  axios.put(`http://127.0.0.1:5000/updateclient_status`,{
      id:5000,
      status_name: updateClientStatus,

    })
    .then(function(response) {
      console.log(response.data);
    })

  res.render('pages/submit')

});



app.delete('/deleteclient_status', function(req, res){
  var deleteClientStatus = req.body.status_name;

  axios.delete(`http://127.0.0.1:5000/deleteclient_status`,{
    id:5000,
    status_name: deleteClientStatus,

    })
    .then(function(response) {
      console.log(response.data);
    })


  res.render('pages/submit')

});


//---------------------------------------------------------------------------

//sales----------------------------------------------------------------------


app.get('/sales', function(req, res) {
  axios.get(`http://127.0.0.1:5000/sales/all`)
  .then((response)=>{
      
      var sales = response.data;


      res.render('pages/sales', {
        sales: sales
  });
});

app.post('/addsales', function(req, res){
  var addEmployeeID = req.body.employee_id;
  var addProspectID = req.body.prospect_id;

  axios.post(`http://127.0.0.1:5000/addsales`,{
    
    employee_id: addEmployeeID,
    prospect_id: addProspectID

    })
    .then(function(response) {
      console.log(response.data);
    })

  res.render('pages/submit')

});
});


app.put('/updatesales', function(req, res){
  var updateEmployeeID = req.body.employee_id;
  var updateProspectID = req.body.prospect_id;

  axios.put(`http://127.0.0.1:5000/updatesales`,{
      id:5000,
      employee_id: updateEmployeeID,
      prospect_id: updateProspectID
  
    })
    .then(function(response) {
      console.log(response.data);
    })

  res.render('pages/submit')

});



app.delete('/deletesales', function(req, res){
  var deleteEmployeeID = req.body.employee_id;
  var deleteProspectID = req.body.prospect_id;

  axios.delete(`http://127.0.0.1:5000/deletesales`,{
    id:5000,
    employee_id: deleteEmployeeID,
    prospect_id: deleteProspectID

    })
    .then(function(response) {
      console.log(response.data);
    })


  res.render('pages/submit')

});

//--------------------------------------------------------------------------

//airline prospect ---------------------------------------------------------

app.get('/prospect', function(req, res) {
  axios.get(`http://127.0.0.1:5000/prospect/all`)
  .then((response)=>{
      
      var prospect = response.data;


      res.render('pages/prospect', {
        prospect: prospect
  });
});

app.post('/addprospect', function(req, res){
  var addAirlineName = req.body.airline_name;
  var addAddress = req.body.address;
  var addZipCode = req.body.zip_code;
  var addStateID = req.body.stateID;
  var addCountryID = req.body.country_id;
  var addRegionID = req.body.region_id;
  var addClientStatusID = req.body.address;

  axios.post(`http://127.0.0.1:5000/addprospect`,{
    
    airline_name: addAirlineName,
    address: addAddress,
    zip_code: addZipCode,
    state_id: addStateID,
    country_id: addCountryID,
    region_id: addRegionID,
    client_status_id: addClientStatusID

    })
    .then(function(response) {
      console.log(response.data);
    })

  res.render('pages/submit')

});
});


app.put('/updateprospect', function(req, res){
  var updateAirlineName = req.body.airline_name;
  var updateAddress = req.body.address;
  var updateZipCode = req.body.zip_code;
  var updateStateID = req.body.stateID;
  var updateCountryID = req.body.country_id;
  var updateRegionID = req.body.region_id;
  var updateClientStatusID = req.body.address;
  
  axios.put(`http://127.0.0.1:5000/updateprospect`,{
      id:5000,
      airline_name: updateAirlineName,
      address: updateAddress,
      zip_code: updateZipCode,
      state_id: updateStateID,
      country_id: updateCountryID,
      region_id: updateRegionID,
      client_status_id: updateClientStatusID
  
    })
    .then(function(response) {
      console.log(response.data);
    })

  res.render('pages/submit')

});



app.delete('/deleteprospect', function(req, res){
  var deleteAirlineName = req.body.airline_name;
  var deleteAddress = req.body.address;
  var deleteZipCode = req.body.zip_code;
  var deleteStateID = req.body.stateID;
  var deleteCountryID = req.body.country_id;
  var deleteRegionID = req.body.region_id;
  var deleteClientStatusID = req.body.address;

  axios.delete(`http://127.0.0.1:5000/deleteprospect`,{
    id:5000,
    airline_name: deleteAirlineName,
    address: deleteAddress,
    zip_code: deleteZipCode,
    state_id: deleteStateID,
    country_id: deleteCountryID,
    region_id: deleteRegionID,
    client_status_id: deleteClientStatusID

    })
    .then(function(response) {
      console.log(response.data);
    })


  res.render('pages/submit')

});

//--------------------------------------------------------------------------

//airline client -----------------------------------------------------------

app.get('/client', function(req, res) {
  axios.get(`http://127.0.0.1:5000/client/all`)
  .then((response)=>{
      
      var client = response.data;


      res.render('pages/client', {
        client: client
  });
});

app.post('/addclient', function(req, res){
  var addAirlineName = req.body.airline_name;
  var addAddress = req.body.address;
  var addZipCode = req.body.zip_code;
  var addStateID = req.body.stateID;
  var addCountryID = req.body.country_id;
  var addRegionID = req.body.region_id;
  var addClientStatusID = req.body.address;

  axios.post(`http://127.0.0.1:5000/addclient`,{
    
    airline_name: addAirlineName,
    address: addAddress,
    zip_code: addZipCode,
    state_id: addStateID,
    country_id: addCountryID,
    region_id: addRegionID,
    client_status_id: addClientStatusID

    })
    .then(function(response) {
      console.log(response.data);
    })

  res.render('pages/submit')

});
});


app.put('/updateclient', function(req, res){
  var updateAirlineName = req.body.airline_name;
  var updateAddress = req.body.address;
  var updateZipCode = req.body.zip_code;
  var updateStateID = req.body.stateID;
  var updateCountryID = req.body.country_id;
  var updateRegionID = req.body.region_id;
  var updateClientStatusID = req.body.address;
  
  axios.put(`http://127.0.0.1:5000/updateclient`,{
      id:5000,
      airline_name: updateAirlineName,
      address: updateAddress,
      zip_code: updateZipCode,
      state_id: updateStateID,
      country_id: updateCountryID,
      region_id: updateRegionID,
      client_status_id: updateClientStatusID
  
    })
    .then(function(response) {
      console.log(response.data);
    })

  res.render('pages/submit')

});



app.delete('/deleteclient', function(req, res){
  var deleteAirlineName = req.body.airline_name;
  var deleteAddress = req.body.address;
  var deleteZipCode = req.body.zip_code;
  var deleteStateID = req.body.stateID;
  var deleteCountryID = req.body.country_id;
  var deleteRegionID = req.body.region_id;
  var deleteClientStatusID = req.body.address;

  axios.delete(`http://127.0.0.1:5000/deleteclient`,{
    id:5000,
    airline_name: deleteAirlineName,
    address: deleteAddress,
    zip_code: deleteZipCode,
    state_id: deleteStateID,
    country_id: deleteCountryID,
    region_id: deleteRegionID,
    client_status_id: deleteClientStatusID

    })
    .then(function(response) {
      console.log(response.data);
    })


  res.render('pages/submit')

});

//--------------------------------------------------------------------------

//client employee ----------------------------------------------------------

app.get('/client_employee', function(req, res) {
  axios.get(`http://127.0.0.1:5000/client_employee/all`)
  .then((response)=>{
      
      var client_employee = response.data;


      res.render('pages/client_employee', {
        client_employee: client_employee
  });
});

app.post('/addclient_employee', function(req, res){
  var addFirstName = req.body.first_name;
  var addLastName = req.body.last_name;
  var addPhoneNumber = req.body.phone_number;
  var addEmail = req.body.email;
  var addClientID = req.body.client_id;

  axios.post(`http://127.0.0.1:5000/addclient_employee`,{
    
    first_name: addFirstName,
    last_name: addLastName,
    phone_number: addPhoneNumber,
    email: addEmail,
    client_id: addClientID

    })
    .then(function(response) {
      console.log(response.data);
    })

  res.render('pages/submit')

});
});


app.put('/updateclient_employee', function(req, res){
  var updateFirstName = req.body.first_name;
  var updateLastName = req.body.last_name;
  var updatePhoneNumber = req.body.phone_number;
  var updateEmail = req.body.email;
  var updateClientID = req.body.client_id;
  
  axios.put(`http://127.0.0.1:5000/updateclient_employee`,{
      id:5000,
      first_name: updateFirstName,
      last_name: updateLastName,
      phone_number: updatePhoneNumber,
      email: updateEmail,
      client_id: updateClientID
  
    })
    .then(function(response) {
      console.log(response.data);
    })

  res.render('pages/submit')

});



app.delete('/deleteclient_employee', function(req, res){
  var deleteFirstName = req.body.first_name;
  var deleteLastName = req.body.last_name;
  var deletePhoneNumber = req.body.phone_number;
  var deleteEmail = req.body.email;
  var deleteClientID = req.body.client_id;

  axios.delete(`http://127.0.0.1:5000/deleteclient_employee`,{
    id:5000,
    first_name: deleteFirstName,
    last_name: deleteLastName,
    phone_number: deletePhoneNumber,
    email: deleteEmail,
    client_id: deleteClientID

    })
    .then(function(response) {
      console.log(response.data);
    })


  res.render('pages/submit')

});

//--------------------------------------------------------------------------

//employee -----------------------------------------------------------------

app.get('/employee', function(req, res) {
  axios.get(`http://127.0.0.1:5000/employee/all`)
  .then((response)=>{
      
      var employee = response.data;


      res.render('pages/employee', {
        employee: employee
  });
});

app.post('/addemployee', function(req, res){
  var addFirstName = req.body.first_name;
  var addLastName = req.body.last_name;
  var addPhoneNumber = req.body.phone_number;
  var addEmail = req.body.email;
  var addAddress = req.body.address;
  var addZipCode = req.body.zip_code;
  var addStateID = req.body.stateID;
  var addCountryID = req.body.country_id;
  var addRegionID = req.body.region_id;
  var addDepartmentID = req.body.department_id;
  var addEmployeeStatusID = req.body.employee_status_id;
  var addClientEmployeeID = req.body.client_employee_id;

  axios.post(`http://127.0.0.1:5000/addemployee`,{
    
    first_name: addFirstName,
    last_name: addLastName,
    phone_number: addPhoneNumber,
    email: addEmail,
    address: addAddress,
    zip_code: addZipCode,
    state_id: addStateID,
    country_id: addCountryID,
    region_id: addRegionID,
    department_id: addDepartmentID,
    employee_status_id: addEmployeeStatusID,
    client_employee_id: addClientEmployeeID

    })
    .then(function(response) {
      console.log(response.data);
    })

  res.render('pages/submit')

});
});


app.put('/updateemployee', function(req, res){
  var updateFirstName = req.body.first_name;
  var updateLastName = req.body.last_name;
  var updatePhoneNumber = req.body.phone_number;
  var updateEmail = req.body.email;
  var updateAddress = req.body.address;
  var updateZipCode = req.body.zip_code;
  var updateStateID = req.body.stateID;
  var updateCountryID = req.body.country_id;
  var updateRegionID = req.body.region_id;
  var updateDepartmentID = req.body.department_id;
  var updateEmployeeStatusID = req.body.employee_status_id;
  var updateClientEmployeeID = req.body.client_employee_id;
  
  axios.put(`http://127.0.0.1:5000/updateemployee`,{
      id:5000,
      first_name: updateFirstName,
      last_name: updateLastName,
      phone_number: updatePhoneNumber,
      email: updateEmail,
      address: updateAddress,
      zip_code: updateZipCode,
      state_id: updateStateID,
      country_id: updateCountryID,
      region_id: updateRegionID,
      department_id: updateDepartmentID,
      employee_status_id: updateEmployeeStatusID,
      client_employee_id: updateClientEmployeeID
  
    })
    .then(function(response) {
      console.log(response.data);
    })

  res.render('pages/submit')

});



app.delete('/deleteemployee', function(req, res){
  var deleteFirstName = req.body.first_name;
  var deleteLastName = req.body.last_name;
  var deletePhoneNumber = req.body.phone_number;
  var deleteEmail = req.body.email;
  var deleteAddress = req.body.address;
  var deleteZipCode = req.body.zip_code;
  var deleteStateID = req.body.stateID;
  var deleteCountryID = req.body.country_id;
  var deleteRegionID = req.body.region_id;
  var deleteDepartmentID = req.body.department_id;
  var deleteEmployeeStatusID = req.body.employee_status_id;
  var deleteClientEmployeeID = req.body.client_employee_id;

  axios.delete(`http://127.0.0.1:5000/deleteemployee`,{
    id:5000,
    first_name: deleteFirstName,
    last_name: deleteLastName,
    phone_number: deletePhoneNumber,
    email: deleteEmail,
    address: deleteAddress,
    zip_code: deleteZipCode,
    state_id: deleteStateID,
    country_id: deleteCountryID,
    region_id: deleteRegionID,
    department_id: deleteDepartmentID,
    employee_status_id: deleteEmployeeStatusID,
    client_employee_id: deleteClientEmployeeID
    })
    .then(function(response) {
      console.log(response.data);
    })


  res.render('pages/submit')

});
//--------------------------------------------------------------------------

//---------------------------------------------------------------------------
// app listen
app.listen(PORT, () => {
  console.log(`StraWin listening at http://localhost:${PORT}/`)
});