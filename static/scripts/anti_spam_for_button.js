for (let index = 0; index < document.querySelectorAll("#anti-spam-button").length; index++) {
    document.querySelectorAll("#anti-spam-button")[index].addEventListener("click", (e) =>{
        document.querySelectorAll("#anti-spam-button")[index].innerHTML = `<img src="static/images/Gifs/loading.gif" width="40px">`;
    })   
}