var menu = document.querySelector('#icon');
var umenu = document.querySelector('#umenum');
var menu_fold = true;
icon.onclick = function(){
    if(menu_fold == true){
        icon.style.color = 'black';
        umenu.style.visibility = 'visible';
    }
    else{
        icon.style.color = 'white';
        umenu.style.visibility = 'hidden';
    }
    menu_fold = ~menu_fold;
};
var show = false;
