// myapi APIKEY, you can find yours in https://dashboard.mymappi.com/api/token
const APIKEY = <YOUR_API_KEY>;

// Some default and useful variables
let method = "direct";
let text = "Gran vía, 68, Madrid";
let URL, response_status, response_results;

/**
 * Geocode function
 * Call by Geocode HTML button
 */
function geocode() {
  const loading = new Promise((resolve) => {
    setLoadingSpinner();
    setTimeout(function () {
      resolve();
    }, 250);
  });
  // Once the spinner is set get user methods
  // and perform the API request
  loading.then(() => perform());
}

/**
 * Set loading on Results section while the APP
 * wait the response from the server
 */
function setLoadingSpinner() {
  // Set Loading Spinner HTML code from Bootstrap CSS Library
  document.getElementById("response_results").innerHTML =
    '<div class="spinner-border" role="status"><span class="sr-only">Loading...</span></div>';
  // Reset response status
  document.getElementById("response_status").innerHTML = "";
}

/**
 * Perform Geocode APP functionality
 * - Get user inputs
 * - Perform the request
 * - Handle the response
 */
function perform() {
  // Get, update or reset user inputs and global JS variables
  method = getRadioInput();
  text = getTextInput();
  response_results = "";

  // Check input completeness
  if (!text) {
    alert("Please, complete the input with coordinates or an address");
  } else {
    // Perform the request and handle the response
    handleResponse(performGeocodingRequest(method, text));
  }
}


/**
 * Get direct or reverse user radio input
 */
function getRadioInput() {
  // Get all radio buttons
  let radios = document.getElementsByName("inlineRadioOptions");
  // Check inputs
  for (var i = 0, length = radios.length; i < length; i++) {
    if (radios[i].checked) {
      // and update method
      method = radios[i].value;
      break;
    }
  }
  return method;
}

/**
 * Get text user input
 */
function getTextInput() {
  return document.getElementById("to_geocode").value;
}

/**
 * From users inputs perform API request
 * @param {*} method 
 * @param {*} text 
 */
function performGeocodingRequest(method, text) {
  // Set URL method depends
  if (method === "direct") {
    URL = `https://cors-anywhere.herokuapp.com/https://api.mymappi.com/v1/geocoding/${method}?apikey=${APIKEY}&q=${text}`;
  } else {
    // Latitude, Longitude separation
    index = text.indexOf(",");
    URL = `https://cors-anywhere.herokuapp.com/https://api.mymappi.com/v1/geocoding/${method}?apikey=${APIKEY}&lat=${text.substring(
      0,
      index
    )}&lon=${text.substring(index + 1)}`;
  }
  // Create HTTP Request
  var xmlHttp = new XMLHttpRequest();
  // Send the request
  xmlHttp.open("GET", URL, false);
  // Check Status response
  xmlHttp.onload = function () {
    // Update variable, it shows in HTML response
    response_status = xmlHttp.status;
    // Bad request != 200 :(
    if (xmlHttp.status !== 200) {
      text_error = `<span class="text-danger font-weight-bold">Ooops!! Response code ${response_status}. Check your browser log.</span>`;
    } else {
      text_error = `<span class="text-success font-weight-bold">Great! Response code ${response_status}.`;
    }
    document.getElementById("response_status").innerHTML = text_error;
  };
  // Close HTML Request
  xmlHttp.send(null);
  // Return data field from response to show on result section
  return JSON.parse(xmlHttp.responseText).data;
}

/**
 * Validate and prepare output from the response
 */
function handleResponse(data) {
  // Validate results undefined or length 
  if (!data || data.length === 0) {
    response_results = "No results";
  } else {
    // Handle direct or reverse response
    // - Direct contains an array of addresses
    // - Reverse contains one object
    if (method === "direct") {
      // Loop through the array
      for (var i = 0, l = data.length; i < l; i++) {
        response_results += `<div>${data[i].display_name}</div>`;
      }
    } else {
      // Reverse response
      response_results = `<div>${data.display_name}</div>`;
    }
  }
  // Show results
  document.getElementById("response_results").innerHTML = response_results;
}
