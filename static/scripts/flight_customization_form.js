console.log("JS for forms scripts working");

// Dropdown

let last_opened_dropdowsn_id;

for (let input_index = 0; input_index < document.querySelectorAll("#dropdown-box").length; input_index++) {
    document.querySelectorAll("#dropdown-box #dropdown-box-value")[input_index].addEventListener("click", (e) =>{
        if (last_opened_dropdowsn_id >= 0){
            document.querySelectorAll("#dropdown-box-select")[last_opened_dropdowsn_id].style.display = "none";
        }
        document.querySelectorAll("#dropdown-box-select")[input_index].style.display = "block";
        for (let index = 0; index < document.querySelectorAll("#dropdown-box-select > .select-country").length; index++) {
            document.querySelectorAll("#dropdown-box-select > .select-country")[index].addEventListener("click", (e)=>{
                e.target.parentNode.parentNode.firstElementChild.innerHTML = e.target.value;
                document.querySelectorAll("#dropdown-box-select")[input_index].style.removeProperty('display');
            });        
        }
        last_opened_dropdowsn_id = input_index;
    }
)};
