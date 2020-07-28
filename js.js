const dream = ( position ) => {
    if (position === "Data Analyst"){
        return "Now I can change this dp";
    }
    else{
        return "Work harder!!! You'll make it one day";
    }
}
const everyDay = 86400000;
setInterval (dream, everyDay);