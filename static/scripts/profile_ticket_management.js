// Open popup
let last_opened_content_index = -1;
for (let index_1 = 0; index_1 < document.querySelectorAll(".ticket-info").length; index_1++) {
    document.querySelectorAll(".ticket-info")[index_1].addEventListener("click", (e) =>{
        for (let index = 0; index < document.querySelectorAll(".admin-editing-popup-background").length; index++) {
            if( document.querySelectorAll(".admin-editing-popup-background")[index].id === document.querySelectorAll(".ticket-info")[index_1].id && last_opened_content_index === -1){
                document.querySelectorAll(".admin-editing-popup-background")[index].style.display = "table";     
                last_opened_content_index = index_1;
            }
        }
    })
    
}
// Close popup
for (let index = 0; index < document.querySelectorAll("#close-popup").length; index++) {
    document.querySelectorAll("#close-popup")[index].addEventListener("click", (e) =>{
        document.querySelectorAll(".admin-editing-popup-background")[last_opened_content_index].style.display = "none";
        last_opened_content_index = -1;
    })    
}


// let last_opened_content_id;
// for (let index = 0; index < document.querySelectorAll(".ticket-info").length; index++) {
//     document.querySelectorAll(".ticket-info")[index].addEventListener("click", (e)=>{
//             console.log(document.querySelectorAll(".ticket-info")[index].id)
//             for (let index = 0; index <  document.querySelectorAll(".admin-editing-popup-background").length; index++) {
//                 if(document.querySelectorAll(".admin-editing-popup-background")[index].id === document.querySelectorAll(".ticket-info")[index].id){
//                     document.querySelectorAll(".admin-editing-popup-background")[index].style.display = "none";
//                     document.querySelectorAll(".admin-editing-popup-background")[index].style.display = "table";
//                     last_opened_content_index = document.querySelectorAll(".ticket-info")[index];
//                     last_opened_content_id = document.querySelectorAll(".ticket-info")[index].id;
//                 }
                
//             }
//         }) 
// }


// // Close pop up
// for (let index = 0; index < document.querySelectorAll("#close-popup").length; index++) {
//     document.querySelectorAll("#close-popup")[index].addEventListener('click', (e) =>{
//         document.querySelectorAll(".admin-editing-popup-background")[last_opened_content_index].style.display = "none";
//         document.querySelectorAll("#delete-button-pop-up").style.display = "none";
//     })    
// }


// document.querySelectorAll("#dropdown-box-value")[3].innerHTML = document.querySelectorAll(".admin-search-content-result")[index].childNodes[1].innerHTML;
//             document.querySelectorAll("#dropdown-box-value")[4].innerHTML = document.querySelectorAll(".admin-search-content-result")[index].childNodes[3].innerHTML;
//             document.querySelectorAll("#dropdown-box-value")[5].innerHTML = document.querySelectorAll(".admin-search-content-result")[index].childNodes[13].innerHTML;
//             document.querySelectorAll("#departure_date")[1].value = document.querySelectorAll(".admin-search-content-result")[index].childNodes[5].innerHTML;
//             document.querySelectorAll("#arrive_date")[1].value = document.querySelectorAll(".admin-search-content-result")[index].childNodes[7].innerHTML;
//             document.querySelectorAll("#departure_time")[1].value = document.querySelectorAll(".admin-search-content-result")[index].childNodes[9].innerHTML;
//             document.querySelectorAll("#arrive_time")[1].value = document.querySelectorAll(".admin-search-content-result")[index].childNodes[11].innerHTML;
//             document.querySelectorAll("#price")[1].value = document.querySelectorAll(".admin-search-content-result")[index].childNodes[15].innerHTML;
