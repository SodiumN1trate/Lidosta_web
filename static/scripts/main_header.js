// Banner trip box
const DEPARTURE_COUNTRIES_BOX = document.getElementById("departure-country-input"); // A container with countries of departure
const DEPARTURE_COUNTRIES_OPTIONS = document.querySelectorAll("#select-departure-countries .select-flight"); // Countries of departure
let departure_countries_box_status = false; // Toggle status of conatiner "display"
let departure_countries_input = document.getElementById("departure-country-input-value"); // Get value of country of departure input
DEPARTURE_COUNTRIES_BOX.addEventListener("click", (e) =>{
    if(departure_countries_box_status === false){
        document.getElementById("select-departure-countries").style.display = "initial";
        departure_countries_box_status = !departure_countries_box_status;
    }
    else{
        document.getElementById("select-departure-countries").style.display = "none";
        departure_countries_box_status = !departure_countries_box_status;
    }
});


let departure, arrive, departure_date, arrive_date, departure_time, arrive_time, price;


let trip_choosed = false;
for (let index = 0; index < DEPARTURE_COUNTRIES_OPTIONS.length; index++) {
    DEPARTURE_COUNTRIES_OPTIONS[index].addEventListener("click", (e) =>{
        departure = document.querySelectorAll("#flight-departure")[index].innerHTML;
        arrive = document.querySelectorAll("#flight-arrive")[index].innerHTML;
        departure_date = document.querySelectorAll("#flight-departure-date")[index].innerHTML;
        arrive_date = document.querySelectorAll("#flight-arrive-date")[index].innerHTML;
        departure_time = document.querySelectorAll("#departure-time")[index].innerHTML;
        arrive_time = document.querySelectorAll("#arrive-time")[index].innerHTML;
        airplane_model = document.querySelectorAll("#airplane-model")[index].innerHTML;
        price = document.querySelectorAll("#flight-price")[index].innerHTML;
        let msg = `${departure} -> ${arrive} | ${price}$`;
        departure_countries_input.innerHTML = msg;
        trip_choosed = true;
    })
}

document.getElementById("trip-search-button").addEventListener("click", (e)=>{
    let data;
    if(trip_choosed === false){
        data = "0";
    }
    else{
        data = [];
        data.push({
            "departure": departure,
            "arrive": arrive,
            "departure_date": departure_date,
            "arrive_date": arrive_date,
            "departure_time": departure_time,
            "arrive_time": arrive_time, 
            "airplane_model": airplane_model,
            "price": price
        });
    }
    document.cookie = `flight_data=${JSON.stringify(data)}`;
})


function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(';').shift();
}

const ALL_CARDS = document.querySelectorAll(".Card");

for (let index = 0; index < ALL_CARDS.length; index++) {
    ALL_CARDS[index].addEventListener("click", e =>{
        let arrive_data  = getCookie("cards").split("\"");
        let data = [{
            "departure": "Riga(Latvia), RIX",
            "arrive": document.querySelectorAll(".CardDestination")[index].innerHTML.trim(),
            "departure_date": document.querySelectorAll(".CardParametersFlightDate")[index].innerHTML.trim(),
            "arrive_date": arrive_data[2].replace("\\", "").trim(),
            "departure_time": document.querySelectorAll(".CardParametersFlightTime")[index].innerHTML.trim(),
            "arrive_time": arrive_data[4].replace("\\", "").trim(), 
            "airplane_model": arrive_data[6].replace("\\", "").trim(),
            "price": document.querySelectorAll(".CardCost")[index].innerHTML.slice(0, -1)}];
        document.cookie = `flight_data=${JSON.stringify(data)}`;
    })
    
}
