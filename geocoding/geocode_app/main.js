const APIKEY = "2300bc7b-1ba0-4c7b-8336-c9a2cff48a99";

let selection = "direct";
let text = "Gran vía, 68, Madrid";
let results, URL, response_status

function geocode() {
    const loading = new Promise( (resolve, reject) => { 
        updateLoading();
        setTimeout( function() {
            resolve()
          }, 250)
    });
    loading.then( (val) => getSelections()); 
}



function updateLoading() {
    document.getElementById("results_output").innerHTML = '<div class="spinner-border" role="status"><span class="sr-only">Loading...</span></div>';
    document.getElementById("status").innerHTML = '';
}

function getSelections() {
  selection = getRadioSelection();
  text = getTextInput();
    results = '';


  if (!text) {
    alert("Please, complete the input with coordinates or an address");
  } else {
    data = makeGeocodingRequest(selection, text);
      if (selection === "direct") {
        if (data.length === 0) {
          results = "No results";
        }
        else {
          for (var i = 0, l = data.length; i < l; i++) {
            results += `<div>${data[i].display_name}</div>`;
        }
        }
      } else {
        if (!data || data.length === 0) {
          results = "No results";
        } else {
          results = `<div>${data.display_name}</div>`;
        }
      }
      
      document.getElementById("results_output").innerHTML = results;
    }
}

function getRadioSelection() {
  let radios = document.getElementsByName("inlineRadioOptions");
  let selection = "direct";
  for (var i = 0, length = radios.length; i < length; i++) {
    if (radios[i].checked) {
      selection = radios[i].value;
      break;
    }
  }
  return selection;
}

function getTextInput() {
  return document.getElementById("to_geocode").value;
}

function makeGeocodingRequest(selection, text) {
    if (selection === 'direct') {
        URL = `https://cors-anywhere.herokuapp.com/https://api.mymappi.com/v1/geocoding/${selection}?apikey=${APIKEY}&q=${text}`
    } else {
        index = text.indexOf(',')
        URL = `https://cors-anywhere.herokuapp.com/https://api.mymappi.com/v1/geocoding/${selection}?apikey=${APIKEY}&lat=${text.substring(0,index)}&lon=${text.substring(index+1)}`
    }
  var xmlHttp = new XMLHttpRequest();
  xmlHttp.open(
    "GET",
    URL,
    false
  ); // false for synchronous request
  xmlHttp.onload = function () {
    response_status = xmlHttp.status
    if(xmlHttp.status !== 200) {
      text_error = `<span class="text-danger font-weight-bold">Ooops!! Response code ${response_status}. Check your browser log.</span>`
      document.getElementById("status").innerHTML = text_error;
    } else {
      text_error = `<span class="text-success font-weight-bold">Great! Response code ${response_status}.`
      document.getElementById("status").innerHTML = text_error;
    }
  };
  xmlHttp.send(null);
  return JSON.parse(xmlHttp.responseText).data;
}
