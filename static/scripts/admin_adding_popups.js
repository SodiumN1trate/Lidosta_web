document.querySelector(".admin-search-top-bar > img").addEventListener("click", (e) =>{
    document.querySelector(".admin-popup-background").style.display = "table";
})

// Dropdown
let last_opened_dropdowns_id;

for (let input_index = 0; input_index < document.querySelectorAll("#dropdown-box").length; input_index++) {
    document.querySelectorAll("#dropdown-box #dropdown-box-value")[input_index].addEventListener("click", (e) =>{
        if (last_opened_dropdowns_id >= 0){
            document.querySelectorAll("#dropdown-box-select")[last_opened_dropdowns_id].style.display = "none";
        }
        document.querySelectorAll("#dropdown-box-select")[input_index].style.display = "block";
        for (let index = 0; index < document.querySelectorAll("#dropdown-box-select > .select-country").length; index++) {
            document.querySelectorAll("#dropdown-box-select > .select-country")[index].addEventListener("click", (e)=>{
                e.target.parentNode.parentNode.firstElementChild.innerHTML = e.target.value;
                document.querySelectorAll("#dropdown-box-select")[input_index].style.removeProperty('display');
            });        
        }
        last_opened_dropdowns_id = input_index;
    }
)};


// Close pop up
for (let index = 0; index < document.querySelectorAll("#close-popup").length; index++) {
    document.querySelectorAll("#close-popup")[index].addEventListener('click', (e) =>{
        document.querySelector(".admin-popup-background").style.display = "none";
        document.querySelector(".admin-editing-popup-background").style.display = "none";
        document.querySelector("#delete-button-pop-up").style.display = "none";
    })    
}



// Get data from adding pop up
document.querySelector("#submit-popup").addEventListener("click", (e)=>{
    let data = [];
    if(document.querySelector("form").id === "flights"){
        data.push({
            "departure": document.querySelectorAll("#dropdown-box-value")[0].innerHTML,
            "arrive": document.querySelectorAll("#dropdown-box-value")[1].innerHTML,
            "departure_date": document.getElementById("departure_date").value,
            "arrive_date": document.getElementById("arrive_date").value,
            "departure_time": document.getElementById("departure_time").value,
            "arrive_time": document.getElementById("arrive_time").value,
            "airplane": document.querySelectorAll("#dropdown-box-value")[2].innerHTML,
            "price":  document.getElementById("price").value,
            "title": document.querySelector("form").id
        });
    }
    else if(document.querySelector("form").id === "airports"){
        data.push({
            "airport_name":  document.getElementById("airport_name").value,
            "airport_abbreviation":  document.getElementById("airport_abbreviation").value,
            "airport_address":  document.getElementById("airport_address").value,
            "title": document.querySelector("form").id
        });
    }
    else if(document.querySelector("form").id === "airplanes"){
        data.push({
            "airplane_model":  document.getElementById("airplane_model").value,
            "airplane_manufacture_year":  document.getElementById("airplane_manufacture_year").value,
            "airplane_seats_count":  document.getElementById("airplane_seats_count").value,
            "airport": document.querySelectorAll("#dropdown-box-value")[0].innerHTML,
            "title": document.querySelector("form").id
        });
    }
    else if(document.querySelector("form").id === "users"){
        data.push({
            "name":  document.getElementById("name").value,
            "lastname": document.getElementById("lastaname").value,
            "password": document.getElementById("password").value,
            "email": document.getElementById("email").value,
            "role": document.querySelectorAll("#dropdown-box-value")[0].innerHTML,
            "title": document.querySelector("form").id
        });
    }
    if(check_on_gaps(data[0]) === 1){
        alert("Aizpildiet visus laukumus!");
    }
    else{
        raise_add_popup();
        document.cookie = `data=${JSON.stringify(data)}`;
    }
})

function close_popup() {
    document.querySelector(".admin-popup-background").style.display = "none";
}

//raise second pop up
function raise_add_popup() {
    document.querySelectorAll("#pop-up-passangers-info-data-accept")[0].style.display = "block";
    document.querySelectorAll("#continue-button").forEach(element => {
        element.addEventListener("click", (e)=>{
            if( e.target.innerHTML === "Nē"){
                document.getElementById("pop-up-passangers-info-data-accept").style.display = "none";
            };
        }); 
    });
};

// Check dictionary on gaps
function check_on_gaps(obj) {
    let gap = 0;
    Object.values(obj).forEach(element => {
        if(element === ""){
            gap += 1;
        }
    });
    if(gap > 0){
        gap = 0;
        return 1;
    }
    else{
        gap = 0;
        return 0;
    }
}
