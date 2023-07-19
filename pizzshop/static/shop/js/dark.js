let t=0
let dark = document.querySelector(".button");
dark.addEventListener("click", () => {
    console.log("hi");
    let dis = document.getElementsByClassName("card");
        // console.log(dis)
    if(t==0){
        for(i of dis){
            i.style.backgroundColor= "black";
            i.style.color= "white";
        }
    t=1
    }
    else{
        for(i of dis){
            i.style.backgroundColor= "white";
            i.style.color= "black";
        }  
    t=0
    }

});