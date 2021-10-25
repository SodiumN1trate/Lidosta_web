console.log("JS for forms scripts working");

// Dropdown

let last_opened_dropdowns_id;
let pressed_count = 0;
let sum = parseInt(document.getElementById("sum-of-all").innerHTML);
for (let input_index = 0; input_index < document.querySelectorAll("#dropdown-box").length; input_index++) {
    document.querySelectorAll("#dropdown-box #dropdown-box-value")[input_index].addEventListener("click", (e) =>{
        if (last_opened_dropdowns_id >= 0){
            document.querySelectorAll("#dropdown-box-select")[last_opened_dropdowns_id].style.display = "none";
        }
        document.querySelectorAll("#dropdown-box-select")[input_index].style.display = "block";
        for (let index = 0; index < document.querySelectorAll("#dropdown-box-select > .select-country").length; index++) {
            document.querySelectorAll("#dropdown-box-select > .select-country")[index].addEventListener("click", (e)=>{
                e.target.parentNode.parentNode.firstElementChild.innerHTML = e.target.value;
                if( input_index == 0){ // Flight class dropdown
                    if(e.target.value === "Biznesa klase"){
                        if(pressed_count === 0)
                            document.getElementById("sum-of-all").innerHTML = Math.ceil(sum / 2 + sum) ;
                            pressed_count += 1;
                    }
                    else{
                        document.getElementById("sum-of-all").innerHTML = sum ;
                        pressed_count = 0;
                    }
                }
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
    for (let index = 0; index < document.querySelectorAll("#booking-info-container").length; index++) {
        if(document.querySelector("#dropdown-box > #dropdown-box-value").innerHTML === "Izvēlēties lidojuma klasi"){
            gap = true;
        }
        else{
            flight_customization.push(document.querySelectorAll("#booking-info-container > #flight-info")[index].innerHTML);
        }
    }
    if(gap === true){
        alert("Aizpildiet visus dotos laukus!")
    }
    else{
        raise_popup();
        flight_customization.push(document.querySelector("#dropdown-box > #dropdown-box-value").innerHTML);
        flight_customization.push(document.querySelector("#sum-of-all-conatiner > #sum-of-all").innerHTML);
        console.log(flight_customization);
        document.cookie = `flight_customization=${Base64.encode(JSON.stringify(flight_customization))}`;
    }
    console.log(flight_customization);
    gap = false;
});

//pop up
function raise_popup() {
    document.getElementById("pop-up-passangers-info-data-accept").style.display = "block";
    document.querySelectorAll("#continue-button").forEach(element => {
        element.addEventListener("click", (e)=>{
            if( e.target.innerHTML === "Nē"){
                flight_customization = []
                document.getElementById("pop-up-passangers-info-data-accept").style.display = "none";
            };
        }); 
    });
};

