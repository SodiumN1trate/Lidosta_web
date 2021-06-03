console.log("JS for forms scripts working");

// Flight comfort class select
const FLYING_COMFORT_CLASS_BOX = document.getElementById("flying-class-input");
let flying_comfort_class_input_value = document.getElementById("flying-class-input-value");
let flying_comfort_class_box_status = false;
let flying_comfort_class_options = document.getElementById("select-flying-class");
FLYING_COMFORT_CLASS_BOX.addEventListener("click", (e) => {
    if( flying_comfort_class_box_status === false )
    {
        flying_comfort_class_options.style.display = "initial";
        deparature_time_options.style.display = "none";
        deparature_time_box_status = false;
        flying_comfort_class_box_status = !flying_comfort_class_box_status;
    }
    else{
        flying_comfort_class_options.style.display = "none";
        flying_comfort_class_box_status = !flying_comfort_class_box_status;
    }
})

for (let index = 0; index < document.querySelectorAll("#select-flying-class > .select-country").length; index++) {
    document.querySelectorAll("#select-flying-class > .select-country")[index].addEventListener("click", (e) => {
        flying_comfort_class_input_value.innerHTML = document.querySelectorAll("#select-flying-class > .select-country")[index].value;
    })
    
}


// Deparature time select
const DEPARATURE_TIME_BOX = document.getElementById("departure-date-input");
let deparature_time_input_value = document.getElementById("departure-date-input-value");
let deparature_time_box_status = false;
let deparature_time_options = document.getElementById("select-departure-date");
DEPARATURE_TIME_BOX.addEventListener("click", (e) => {
    if( deparature_time_box_status === false )
    {
        deparature_time_options.style.display = "initial";
        flying_comfort_class_options.style.display = "none";
        flying_comfort_class_box_status = false;
        deparature_time_box_status = !deparature_time_box_status;
    }
    else{
        deparature_time_options.style.display = "none";
        deparature_time_box_status = !deparature_time_box_status;
    }
})

for (let index = 0; index <  document.querySelectorAll("#select-departure-date > .select-country").length; index++) {
    document.querySelectorAll("#select-departure-date > .select-country")[index].addEventListener("click", (e) => {
        deparature_time_input_value.innerHTML = document.querySelectorAll("#select-departure-date > .select-country")[index].value;
    })
    
}
