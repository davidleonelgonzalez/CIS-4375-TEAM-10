var express = require('express');
var app = express();
var bodyParser  = require('body-parser');
// body parser in use

//creating axios to call on my rest api
const axios = require('axios');

//app will then use body parser
app.use(express.urlencoded({ extended: true }));
//app.use(express.static(path.join(__dirname, 'public')))
//the app will set to view engine  to call ejs in view folder
app.set('view engine', 'ejs');

var publicDir = require('path').join(__dirname,'/public'); 
app.use(express.static(publicDir));

const PORT = process.env.PORT || 8080;

//home----------------------------------------------------------------------------------------------------------------------------
app.get('/', function(req, res) {
  res.render('pages/home', {

});
});

//CRUD----------------------------------------------------------------------------------------------------------------------------

app.get('/add_client', function(req, res) {


  res.render('pages/add_client', {

});
});

app.get('/add_employee', function(req, res) {


  res.render('pages/add_employee', {

});
});

app.get('/add_product', function(req, res) {


  res.render('pages/add_product', {

});
});


app.get('/add_prospect', function(req, res) {


  res.render('pages/add_prospect', {

});
});


app.get('/add_sale', function(req, res) {


  res.render('pages/add_sale', {

});
});

app.get('/add_server', function(req, res) {


  res.render('pages/add_server', {

});
});

app.get('/add_vendor', function(req, res) {


  res.render('pages/add_vendor', {

});
});

app.get('/update_client', function(req, res) {


  res.render('pages/update_client', {

});
});

app.get('/update_employee', function(req, res) {


  res.render('pages/update_employee', {

});
});

app.get('/update_product', function(req, res) {


  res.render('pages/update_product', {

});
});

app.get('/update_prospect', function(req, res) {


  res.render('pages/update_prospect', {

});
});

app.get('/update_sale', function(req, res) {


  res.render('pages/update_sale', {

});
});

app.get('/update_server', function(req, res) {


  res.render('pages/update_server', {

});
});

app.get('/update_vendor', function(req, res) {


  res.render('pages/update_vendor', {

});
});

app.get('/delete_client', function(req, res) {


  res.render('pages/delete_client', {

});
});

app.get('/delete_employee', function(req, res) {


  res.render('pages/delete_employee', {

});
});

app.get('/delete_product', function(req, res) {


  res.render('pages/delete_product', {

});
});

app.get('/delete_prospect', function(req, res) {


  res.render('pages/delete_prospect', {

});
});

app.get('/delete_sale', function(req, res) {


  res.render('pages/delete_sale', {

});
});

app.get('/delete_server', function(req, res) {


  res.render('pages/delete_server', {

});
});

app.get('/delete_vendor', function(req, res) {


  res.render('pages/delete_vendor', {

});
});
/*
app.get('/test', function(req, res) {


  res.render('pages/test', {

});
});

*/
//region-------------------------------------------------------------------------------------------------------------------------

app.get('/region', function(req, res) {
  res.render('pages/region', {

  }); 
      
});

app.get('/getregion', function(req, res) {
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


app.all('/updateregion', function(req, res){
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



app.all('/deleteregion', function(req, res){
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

//---------------------------------------------------------------------------------------------------------------
//country---------------------------------------------------------------------------------------------------------------

app.get('/country', function(req, res) {
  axios.get(`http://127.0.0.1:5000/country/all`)
  res.render('pages/country', {

  });
});

app.get('/getcountry', function(req, res) {
  axios.get(`http://127.0.0.1:5000/country/all`)
  .then((response)=>{
      
      var country = response.data;


      res.render('pages/getcountry', {
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


app.all('/updatecountry', function(req, res){
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

app.all('/deletecountry', function(req, res){
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
    res.render('pages/country', {

  });
});

app.get('/getstate', function(req, res) {
  axios.get(`http://127.0.0.1:5000/state/all`)
  .then((response)=>{
      
      var state = response.data;


      res.render('pages/getstate', {
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


app.all('/updatestate', function(req, res){
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



app.all('/deletestate', function(req, res){
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


app.all('/updatevendor', function(req, res){
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



app.all('/deletevendor', function(req, res){
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

app.post('/addserver', function(req, res){
  var addVMName = req.body.vm_name;
  var addVMType = req.body.vm_type;
  var addServerNumber = req.body.server_number;
  var addServerLocation = req.body.server_location;
  var addVendorID = req.body.vendor_id;

  axios.post(`http://127.0.0.1:5000/addserver`,{
    vm_name: addVMName,
    vm_type: addVMType,
    server_number: addServerNumber,
    server_location: addServerLocation,
    vendor_id: addVendorID

    })
    .then(function(response) {
      console.log(response.data);
    })

  res.render('pages/submit')

});



app.all('/updateserver', function(req, res){
  var updateServerID = req.body.server_id;
  var updateServerName = req.body.vm_name;
  var updateVMType = req.body.vm_type;
  var updateServerNumber = req.body.server_number;
  var updateServerLocation = req.body.server_location;
  var updateVendorID = req.body.vendor_id;
  console.log(updateServerID)

  axios.put(`http://127.0.0.1:5000/updateserver`,{
    server_id: updateServerID,
    vm_name: updateServerName,
    vm_type: updateVMType,
    server_number: updateServerNumber,
    server_location: updateServerLocation,
    vendor_id: updateVendorID
    })
    .then(function(response) {
      console.log(response.data);
    })

  res.render('pages/submit')

});



app.all('/deleteserver', function(req, res){
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


app.all('/updateproduct', function(req, res){
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



app.all('/deleteproduct', function(req, res){
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



app.all('/updatedepartment', function(req, res){
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



app.all('/deletedepartment', function(req, res){
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


app.all('/updateemployee_status', function(req, res){
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



app.all('/deleteemployee_status', function(req, res){
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



app.all('/updateclient_status', function(req, res){
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



app.all('/deleteclient_status', function(req, res){
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
});

app.post('/addsales', function(req, res){
  var addEmployeeID = req.body.employee_id;
  var addProspectID = req.body.prospect_id;
  var addSalesStatus = req.body.sales_status;
  var addSalesAmount = req.body.sales_amount;
  var addOpportunityName = req.body.opportunity_name;

  axios.post(`http://127.0.0.1:5000/addsales`,{
    employee_id: addEmployeeID,
    prospect_id: addProspectID,
    sales_status: addSalesStatus,
    sales_amount: addSalesAmount,
    opportunity_name: addOpportunityName

    })
    .then(function(response) {
      console.log(response.data);
    })

  res.render('pages/submit')


});


// app.all('/updatesales', function(req, res){
//   var updateSalesID = req.body.sales_id;
//   var updateEmployeeID = req.body.employee_id;
//   var updateProspectID = req.body.prospect_id;
//   var updateSalesStatus = req.body.sales_status;
//   var updateSalesAmount = req.body.sales_amount;
//   var updateOpportunityName = req.body.opportunity_name;

//   axios.put(`http://127.0.0.1:5000/updatesales`,{
//       sales_id: updateSalesID,
//       employee_id: updateEmployeeID,
//       prospect_id: updateProspectID,
//       sales_status: updateSalesStatus,
//       sales_amount: updateSalesAmount,
//       opportunity_name: updateOpportunityName
  
//     })
//     .then(function(response) {
//       console.log(response.data);
//     })

//   res.render('pages/submit')

// });



app.all('/deletesales', function(req, res){
  var deleteSalesID = req.body.sales_id;

  axios.delete(`http://127.0.0.1:5000/deletesales`,{
    sales_id: deleteSalesID

    })
    .then(function(response) {
      console.log(response.data);
    })


  res.render('pages/submit')

});

//--------------------------------------------------------------------------

//airline prospect ---------------------------------------------------------

app.post('/addprospect', function(req, res){
  var addAddress = req.body.address;
  var addAirlineName = req.body.airline_name;
  var addClientStatusID = req.body.client_status_id;
  var addContactEmail = req.body.contact_email;
  var addContactFirstName = req.body.contact_first_name;
  var addContactLastName = req.body.contact_last_name;
  var addContactPhoneNumber = req.body.contact_phone_number;
  var addCountryID = req.body.country_id;
  var addEndDate = req.body.end_date;
  var addRegionID = req.body.region_id;
  var addStartDate = req.body.start_date;
  var addStateID = req.body.state_id;
  var addZipCode = req.body.zip_code;

  axios.post(`http://127.0.0.1:5000/addprospect`,{
    address: addAddress,
    airline_name: addAirlineName,
    client_status_id: addClientStatusID,
    contact_email: addContactEmail,
    contact_first_name: addContactFirstName,
    contact_last_name: addContactLastName,
    contact_phone_number: addContactPhoneNumber,
    country_id: addCountryID,
    end_date: addEndDate,
    region_id: addRegionID,
    start_date: addStartDate,
    state_id: addStateID,
    zip_code: addZipCode,

    })
    .then(function(response) {
      console.log(response.data);
    })

  res.render('pages/submit')

});



app.all('/updateprospect', function(req, res){
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



app.all('/deleteprospect', function(req, res){
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


app.post('/addclient', function(req, res){
  var addContactFirstName = req.body.contact_first_name;
  var addContactLastName = req.body.contact_last_name;
  var addContactPhoneNumber = req.body.contact_phone_number;
  var addContactEmail = req.body.contact_email;
  var addAirlineName = req.body.airline_name;
  var addAddress = req.body.address;
  var addZipCode = req.body.zip_code;
  var addStateID = req.body.state_id;
  var addCountryID = req.body.country_id;
  var addRegionID = req.body.region_id;
  var addClientStatusID = req.body.client_status_id;
  var addStartDate = req.body.start_date;
  var addEndDate = req.body.end_date;
  var addSubscriptionAmount = req.body.subscription_amount;

  axios.post(`http://127.0.0.1:5000/addclient`,{
    contact_first_name: addContactFirstName,
    contact_last_name: addContactLastName,
    contact_phone_number: addContactPhoneNumber,
    contact_email: addContactEmail,
    airline_name: addAirlineName,
    address: addAddress,
    zip_code: addZipCode,
    state_id: addStateID,
    country_id: addCountryID,
    region_id: addRegionID,
    client_status_id: addClientStatusID,
    start_date: addStartDate,
    end_date: addEndDate,
    subscription_amount: addSubscriptionAmount

    })
    .then(function(response) {
      console.log(response.data);
    })

    res.render('pages/submit')

});



app.all('/updateclient', function(req, res){
  var updateAirlineName = req.body.airline_name;
  var updateAddress = req.body.address;
  var updateZipCode = req.body.zip_code;
  var updateStateID = req.body.stateID;
  var updateCountryID = req.body.country_id;
  var updateRegionID = req.body.region_id;
  var updateClientStatusID = req.body.address;
  
  axios.put(`http://127.0.0.1:5000/updateclient`,{
      client_id:5000,
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



app.all('/deleteclient', function(req, res){


  axios.delete(`http://127.0.0.1:5000/deleteclient`,{
    client_id:24
  

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
});

app.post('/addclient_employee', function(req, res){
  var addClientID = req.body.client_id;
  var addEmployeeID = req.body.employee_id;
  
  axios.post(`http://127.0.0.1:5000/addclient_employee`,{
    

    client_id: addClientID,
    employee_id: addEmployeeID

    })
    .then(function(response) {
      console.log(response.data);
    })

  res.render('pages/submit')

});



app.all('/updateclient_employee', function(req, res){
  var updateClientID = req.body.client_id;
  var updateEmployeeID = req.body.employee_id;
  
  axios.put(`http://127.0.0.1:5000/updateclient_employee`,{

      client_id: updateClientID,
      employee_id: updateEmployeeID
  
  
    })
    .then(function(response) {
      console.log(response.data);
    })

  res.render('pages/submit')

});



app.all('/deleteclient_employee', function(req, res){

  var deleteClientID = req.body.client_id;
  var deleteEmployeeID = req.body.employee_id;

  axios.delete(`http://127.0.0.1:5000/deleteclient_employee`,{

    client_id: deleteClientID,
    employee_id: deleteEmployeeID


    })
    .then(function(response) {
      console.log(response.data);
    })


  res.render('pages/submit')

});

//--------------------------------------------------------------------------

//employee -----------------------------------------------------------------


app.post('/addemployee', function(req, res){
  var addFirstName = req.body.first_name;
  var addLastName = req.body.last_name;
  var addPhoneNumber = req.body.phone_number;
  var addEmail = req.body.email;
  var addAddress = req.body.address;
  var addZipCode = req.body.zip_code;
  var addStateID = req.body.state_id;
  var addCountryID = req.body.country_id;
  var addRegionID = req.body.region_id;
  var addDepartmentID = req.body.department_id;
  var addEmployeeStatusID = req.body.employee_status_id;
  var addClientEmployeeID = req.body.client_employee_id;
  var addStartDate = req.body.start_date;
  var addEndDate = req.body.end_date;


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
    client_employee_id: addClientEmployeeID,
    start_date: addStartDate,
    end_date: addEndDate

    })
    .then(function(response) {
      console.log(response.data);
    })

  res.render('pages/submit')

});



app.all('/updateemployee', function(req, res){
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



app.get('/deleteemployee', function(req, res){
  var deleteEmployeeID = {employee_id: req.body.employee_id}

  axios.delete(`http://127.0.0.1:5000/deleteemployee`,{data:{employee_id: deleteEmployeeID}})
    .then(function(response) {
      console.log(deleteEmployeeID);
    })


  res.render('pages/submit')

});
//--------------------------------------------------------------------------

//----------------------------------------------------------------------------


//Report 1 ------------------------------------------------------------------
app.get('/reports', function(req, res) {


  res.render('pages/reports', {

});
});

app.get('/report1', function(req, res) {
  axios.get(`http://127.0.0.1:5000/report1`)
  .then((response)=>{
      
      var report1 = response.data;


      res.render('pages/report1', {
        report1: report1
  });
});
})
//----------------------------------------------------------------------------

//Report 2 ------------------------------------------------------------------
app.get('/report2', function(req, res) {
  axios.get(`http://127.0.0.1:5000/report2`)
  .then((response)=>{
      
      var report2 = response.data;


      res.render('pages/report2', {
        report2: report2
  });
});
})
//----------------------------------------------------------------------------

//Report 3 ------------------------------------------------------------------
app.get('/report3', function(req, res) {
  axios.get(`http://127.0.0.1:5000/report3`)
  .then((response)=>{
      
      var report3 = response.data;


      res.render('pages/report3', {
        report3: report3
  });
});
})
//----------------------------------------------------------------------------

//Report 3 ------------------------------------------------------------------
app.get('/report4', function(req, res) {
  axios.get(`http://127.0.0.1:5000/report4`)
  .then((response)=>{
      
      var report4 = response.data;


      res.render('pages/report4', {
        report4: report4
  });
});
})
//----------------------------------------------------------------------------

//Report 5 ------------------------------------------------------------------
app.get('/report5', function(req, res) {
  axios.get(`http://127.0.0.1:5000/report5`)
  .then((response)=>{
      
      var report5 = response.data;


      res.render('pages/report5', {
        report5: report5
  });
});
})
//----------------------------------------------------------------------------

//Report 6 ------------------------------------------------------------------
app.get('/report6', function(req, res) {
  axios.get(`http://127.0.0.1:5000/report6`)
  .then((response)=>{
      
      var report6 = response.data;


      res.render('pages/report6', {
        report6: report6
  });
});
})
//----------------------------------------------------------------------------

//Report 7 ------------------------------------------------------------------
app.get('/report7', function(req, res) {
  axios.get(`http://127.0.0.1:5000/report7`)
  .then((response)=>{
      
      var report7 = response.data;


      res.render('pages/report7', {
        report7: report7
  });
});
})

//Report 8 ------------------------------------------------------------------
app.get('/report8', function(req, res) {
  axios.get(`http://127.0.0.1:5000/report8`)
  .then((response)=>{
      
      var report8 = response.data;


      res.render('pages/report8', {
        report8: report8
  });
});
})

//Report 9 ------------------------------------------------------------------
app.get('/report9', function(req, res) {
  axios.get(`http://127.0.0.1:5000/report9`)
  .then((response)=>{
      
      var report9 = response.data;


      res.render('pages/report9', {
        report9: report9
  });
});
})

//Report 10 ------------------------------------------------------------------
app.get('/report10', function(req, res) {
  axios.get(`http://127.0.0.1:5000/report10`)
  .then((response)=>{
      
      var report10 = response.data;


      res.render('pages/report10', {
        report10: report10
  });
});
})

//---------------------------------------------------------------------------
// app listen
app.listen(PORT, () => {
  console.log(`StraWin listening at http://localhost:${PORT}/`)
});