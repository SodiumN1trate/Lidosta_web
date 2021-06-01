console.log("JS for forms scripts working");

// Flying customization
const FLYING_COMFORT_CLASS_BOX = document.getElementById("flying-class-input");
let flying_comfort_class_input_value = document.getElementById("flying-class-input-value");
let flying_comfort_class_box_status = false;
let flying_comfort_class_options = document.getElementById("select-flying-class");

FLYING_COMFORT_CLASS_BOX.addEventListener("click", (e) => {
    if( flying_comfort_class_box_status === false )
    {
        flying_comfort_class_options.style.display = "initial";
        flying_comfort_class_box_status = !flying_comfort_box_status;
    }
    else{
         flying_comfort_class_box_status = !flying_comfort_box_status;
    }
})
