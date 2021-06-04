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
                            <input type="text" name="name" placeholder="Vārds">
                            <input type="text" name="lastname" placeholder="Uzvārds">
                            <span id="date-text">Dzimšanas datums:</span>
                            <div id="form-for-birthday-date">
                                <input type="text" name="year" placeholder="Gads">
                                <input type="text" name="month" placeholder="Mēnesis">
                                <input type="text" name="date" placeholder="Diena">
                            </div>
                            <input type="text" name="person_id" placeholder="Personas kods">
                            <input type="email" name="email" placeholder="E-pasts">
                            <input type="text" name="telephone_number" placeholder="Tālr.:">
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
    const REMOVE_PERSON_BUTTON = document.querySelectorAll("#remove-person");
    console.log(REMOVE_PERSON_BUTTON);
    for (let index = 0; index < REMOVE_PERSON_BUTTON.length; index++) {
        REMOVE_PERSON_BUTTON[index].addEventListener("click", (e) => {
            e.target.parentNode.parentNode.parentNode.parentNode.remove();
            console.log("Tests!");
    });     
    }  
};

