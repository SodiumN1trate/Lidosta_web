// Add person
remove_button_render();

const ADD_PERSON_BUTTON = document.getElementById("add-person");

ADD_PERSON_BUTTON.addEventListener("click", (e) =>{
    let blank = `<article id="login">
                    <div id="article-header">
                        <span id="article-name">Pasažiera informācija</span>
                    </div>
                    <div id="article-content">
                        <form>
                            <input type="text" name="name" placeholder="Vārds" id="name">
                            <input type="text" name="lastname" placeholder="Uzvārds" id="lastname">
                            <span id="date-text">Dzimšanas datums:</span>
                            <div id="form-for-birthday-date">
                                <input type="text" name="year" placeholder="Gads" id="birth-year" maxlength="4">
                                <input type="text" name="month" placeholder="Mēnesis" id="birth-month" maxlength="2">
                                <input type="text" name="date" placeholder="Diena" id="birth-day" maxlength="2">
                            </div>
                            <input type="text" name="person_id" placeholder="Personas kods" id="person-id">
                            <input type="text" name="telephone_number" placeholder="Tālr.:" id="telephone-number">
                            <div id="remove-person">
                                <img src="static/Vector/RemoveSign.svg">
                                Noņemt cilvēku
                            </div>
                        </form>
                    </div>
                </article>`;
    document.getElementById("form-container").innerHTML += blank;
    remove_button_render();
});

// Remove person button render
function remove_button_render() {
    const REMOVE_PERSON_BUTTON = document.querySelectorAll("#remove-person > img");
    for (let index = 0; index < REMOVE_PERSON_BUTTON.length; index++) {
        REMOVE_PERSON_BUTTON[index].addEventListener("click", (e) => {
        e.target.parentNode.parentNode.parentNode.parentNode.remove();
    });     
    }  
};




// Get data from user inputs
let persons = [];
let gaps = false;
document.querySelector("#continue-button > .submit-button").addEventListener("click", (e) =>{
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