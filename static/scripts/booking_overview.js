document.querySelector("#book-button-container > #book-button").addEventListener("click", (e) =>{
    raise_popup();
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

