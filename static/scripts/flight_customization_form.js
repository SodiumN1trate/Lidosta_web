console.log("JS for forms scripts working");

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

// Gap checker
let gap = false;

let flight_customization = [];

document.querySelector("#continue-button > .submit-button").addEventListener("click", (e)=>{
    for (let index = 0; index < document.querySelectorAll("#dropdown-box").length; index++) {
        if( document.querySelectorAll("#dropdown-box")[index].children[0].innerHTML === "No:" || document.querySelectorAll("#dropdown-box")[index].children[0].innerHTML === "Uz:" || document.querySelectorAll("#dropdown-box")[index].children[0].innerHTML === "Izvēlēties lidojuma klasi" || document.querySelectorAll("#dropdown-box")[index].children[0].innerHTML === "Izvēlēties izlidošanas datumu"){
            gap = true;
        }
        else{
            flight_customization.push(document.querySelectorAll("#dropdown-box")[index].children[0].innerHTML);
        }
    }
    if(gap === true){
        alert("Aizpildiet visus dotos laukus!")
    }
    else{
        raise_popup();
        flight_customization.push(document.querySelector("#booking-info-container > #arrive-date").innerHTML);
        flight_customization.push(document.querySelector("#sum-of-all-conatiner  #sum-of-all").innerHTML);
        document.cookie = `flight_customization=${Base64.encode(JSON.stringify(flight_customization))}`;
    }
    gap = false;
});

//pop up
function raise_popup() {
    document.getElementById("pop-up-passangers-info-data-accept").style.display = "block";
    document.querySelectorAll("#continue-button").forEach(element => {
        element.addEventListener("click", (e)=>{
            if( e.target.innerHTML === "Nē"){
                document.getElementById("pop-up-passangers-info-data-accept").style.display = "none";
            };
        }); 
    });
};

