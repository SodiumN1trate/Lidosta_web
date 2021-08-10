let last_opened_content_id;
for (let index = 0; index < document.querySelectorAll(".admin-search-content-result").length; index++) {
    document.querySelectorAll(".admin-search-content-result")[index].addEventListener("click", (e)=>{
        if(document.querySelectorAll("form")[1].id === "flights"){
            document.querySelector(".admin-editing-popup-background").style.display = "table";
            document.querySelectorAll("#dropdown-box-value")[3].innerHTML = document.querySelectorAll(".admin-search-content-result")[index].childNodes[1].innerHTML;
            document.querySelectorAll("#dropdown-box-value")[4].innerHTML = document.querySelectorAll(".admin-search-content-result")[index].childNodes[3].innerHTML;
            document.querySelectorAll("#dropdown-box-value")[5].innerHTML = document.querySelectorAll(".admin-search-content-result")[index].childNodes[13].innerHTML;
            document.querySelectorAll("#departure_date")[1].value = document.querySelectorAll(".admin-search-content-result")[index].childNodes[5].innerHTML;
            document.querySelectorAll("#arrive_date")[1].value = document.querySelectorAll(".admin-search-content-result")[index].childNodes[7].innerHTML;
            document.querySelectorAll("#departure_time")[1].value = document.querySelectorAll(".admin-search-content-result")[index].childNodes[9].innerHTML;
            document.querySelectorAll("#arrive_time")[1].value = document.querySelectorAll(".admin-search-content-result")[index].childNodes[11].innerHTML;
            last_opened_content_id = document.querySelectorAll(".admin-search-content-result")[index].id;
        }

        else if(document.querySelectorAll("form")[1].id === "airplanes"){
            document.querySelector(".admin-editing-popup-background").style.display = "table";
            console.log(document.querySelectorAll(".admin-search-content-result")[index].childNodes[1].innerHTML);
            document.querySelectorAll("#dropdown-box-value")[1].innerHTML = document.querySelectorAll(".admin-search-content-result")[index].childNodes[7].innerHTML;
            document.querySelectorAll("#airplane_model")[1].value = document.querySelectorAll(".admin-search-content-result")[index].childNodes[1].innerHTML;
            document.querySelectorAll("#airplane_manufacture_year")[1].value = document.querySelectorAll(".admin-search-content-result")[index].childNodes[3].innerHTML;
            document.querySelectorAll("#airplane_seats_count")[1].value = document.querySelectorAll(".admin-search-content-result")[index].childNodes[5].innerHTML;
            last_opened_content_id = document.querySelectorAll(".admin-search-content-result")[index].id;
        }

        else if(document.querySelectorAll("form")[1].id === "airports"){
            document.querySelector(".admin-editing-popup-background").style.display = "table";
            console.log(document.querySelectorAll(".admin-search-content-result")[index].childNodes[1].innerHTML);
            document.querySelectorAll("#airport_name")[1].value = document.querySelectorAll(".admin-search-content-result")[index].childNodes[1].innerHTML;
            document.querySelectorAll("#airport_abbreviation")[1].value = document.querySelectorAll(".admin-search-content-result")[index].childNodes[3].innerHTML;
            document.querySelectorAll("#airport_address")[1].value = document.querySelectorAll(".admin-search-content-result")[index].childNodes[5].innerHTML;
            last_opened_content_id = document.querySelectorAll(".admin-search-content-result")[index].id;
        }
    }) 
}


// Get data from edited pop up
document.querySelectorAll("#submit-popup")[1].addEventListener("click", (e)=>{
    let data = [];
    if(document.querySelectorAll("form")[1].id === "flights"){
        data.push({
            "departure": document.querySelectorAll("#dropdown-box-value")[3].innerHTML,
            "arrive": document.querySelectorAll("#dropdown-box-value")[4].innerHTML,
            "departure_date": document.querySelectorAll("#departure_date")[1].value,
            "arrive_date": document.querySelectorAll("#arrive_date")[1].value,
            "departure_time": document.querySelectorAll("#departure_time")[1].value,
            "arrive_time": document.querySelectorAll("#arrive_time")[1].value,
            "airplane": document.querySelectorAll("#dropdown-box-value")[5].innerHTML,
            "title": document.querySelectorAll("form")[1].id,
            "id": last_opened_content_id
        });
    }
    else if(document.querySelector("form").id === "airports"){
        data.push({
            "airport_name":  document.querySelectorAll("#airport_name")[1].value,
            "airport_abbreviation":  document.querySelectorAll("#airport_abbreviation")[1].value,
            "airport_address":  document.querySelectorAll("#airport_address")[1].value,
            "title": document.querySelector("form").id,
            "id": last_opened_content_id
        });
    }
    else if(document.querySelector("form").id === "airplanes"){
        data.push({
            "airplane_model":  document.querySelectorAll("#airplane_model")[1].value,
            "airplane_manufacture_year": document.querySelectorAll("#airplane_manufacture_year")[1].value,
            "airplane_seats_count": document.querySelectorAll("#airplane_seats_count")[1].value,
            "airport": document.querySelectorAll("#dropdown-box-value")[1].innerHTML,
            "title": document.querySelector("form").id,
            "id": last_opened_content_id
        });
    }
    raise_popup();
    document.cookie = `edited_data=${JSON.stringify(data)}`;
})

function close_popup() {
    document.querySelector(".admin-editing-popup-background").style.display = "none";
}

//raise second pop up
function raise_popup() {
    document.querySelectorAll("#pop-up-passangers-info-data-accept")[1].style.display = "block";
    document.querySelectorAll("#continue-button").forEach(element => {
        element.addEventListener("click", (e)=>{
            if( e.target.innerHTML === "Nē"){
                document.querySelectorAll("#pop-up-passangers-info-data-accept")[1].style.display = "none";
            }
            else if( e.target.innerHTML === "Jā"){
                alert("Veiksmīgi tika izmainīti dati!");
            };
        }); 
    });
};
