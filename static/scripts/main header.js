console.log("Js working!");


// Banner trip box
const DEPARTURE_COUNTRIES_BOX = document.getElementById("departure-country-input"); // A container with countries of departure
const ARRIVAL_COUNTRIES_BOX = document.getElementById("arrival-country-input"); // A container with countries of arrival
const DEPARTURE_COUNTRIES_OPTIONS = document.querySelectorAll("#select-departure-countries .select-country"); // Countries of departure
const ARRIVAL_COUNTRIES_OPTIONS = document.querySelectorAll("#select-arrival-countries .select-country"); //  Countries of arrival
let departure_countries_box_status = false; // Toggle status of conatiner "display"
let arrival_countries_box_status = false; // Toggle status of conatiner "display"
let departure_countries_input = document.getElementById("departure-country-input-value"); // Get value of country of departure input
let arrival_countries_input = document.getElementById("arrival-country-input-value"); // Get value of country of arrival input   

DEPARTURE_COUNTRIES_BOX.addEventListener("click", (e) =>{
    if(departure_countries_box_status === false){
        document.getElementById("select-departure-countries").style.display = "initial";
         document.getElementById("select-arrival-countries").style.display = "none";
        departure_countries_box_status = !departure_countries_box_status;
        arrival_countries_box_status = false;
    }
    else{
        document.getElementById("select-departure-countries").style.display = "none";
        departure_countries_box_status = !departure_countries_box_status;
    }
});

ARRIVAL_COUNTRIES_BOX.addEventListener("click", (e) =>{
    if(arrival_countries_box_status === false){
        document.getElementById("select-arrival-countries").style.display = "initial";
        document.getElementById("select-departure-countries").style.display = "none";
        arrival_countries_box_status = !arrival_countries_box_status;
        departure_countries_box_status = false; 
    }
    else{
        document.getElementById("select-arrival-countries").style.display = "none";
        arrival_countries_box_status = !arrival_countries_box_status;
    }
});

for (let index = 0; index < DEPARTURE_COUNTRIES_OPTIONS.length; index++) {
    DEPARTURE_COUNTRIES_OPTIONS[index].addEventListener("click", (e) =>{
        departure_countries_input.innerHTML = DEPARTURE_COUNTRIES_OPTIONS[index].value;
    })
    
}

for (let index = 0; index < ARRIVAL_COUNTRIES_OPTIONS.length; index++) {
    ARRIVAL_COUNTRIES_OPTIONS[index].addEventListener("click", (e) =>{
        arrival_countries_input.innerHTML = ARRIVAL_COUNTRIES_OPTIONS[index].value;
    })
    
}
