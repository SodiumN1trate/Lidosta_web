console.log(document);
// Add person
remove_button_render();

// Remove person button render
function remove_button_render() {
    const REMOVE_PERSON_BUTTON = document.querySelectorAll("#remove-person > img");
    for (let index = 0; index < REMOVE_PERSON_BUTTON.length; index++) {
        REMOVE_PERSON_BUTTON[index].addEventListener("click", (e) => {
            e.target.parentNode.parentNode.parentNode.parentNode.remove();
        });     
    }
    console.log("All user remove buttons have been rendered!");

};




// Get data from user inputs
console.log(1);
let persons = [];
console.log(2);
let gaps = false;
console.log(3);
document.querySelector("#continue-button > .submit-button").addEventListener("click", (e) =>{
    console.log("aa");
    for (let index = 0; index < document.querySelectorAll('#login').length; index++) {
        if (document.querySelectorAll('#name')[index].value === "" || document.querySelectorAll('#lastname')[index].value === "" || document.querySelectorAll('#birth-year')[index].value === "" || document.querySelectorAll('#birth-month')[index].value === "" || document.querySelectorAll('#birth-day')[index].value === "" || document.querySelectorAll('#person-id')[index].value === "" || document.querySelectorAll('#telephone-number')[index].value === ""){
            gaps = true;
        }
        else{
            persons.push({
                    "name":document.querySelectorAll('#name')[index].value,
                    "lastname":document.querySelectorAll('#lastname')[index].value,
                    "birth-year":document.querySelectorAll('#birth-year')[index].value,
                    "birth-month":document.querySelectorAll('#birth-month')[index].value,
                    "birth-day":document.querySelectorAll('#birth-day')[index].value,
                    "person-id":document.querySelectorAll('#person-id')[index].value,
                    "telephone-number":document.querySelectorAll('#telephone-number')[index].value
                });
        }
    }
    if(gaps === false){
        raise_popup();
        document.cookie = `persons=${Base64.encode(JSON.stringify(persons))}`;
    }
    else{
        alert("Aizpildiet visus laukus!");
    }
    gaps = false;
})


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
}