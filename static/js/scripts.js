$(document).ready(function(){
    //Initialise sidenav
    $(".sidenav").sidenav({edge: "right"});
    
    //Initialise form select
    $('select').formSelect();
    
    //Initialise modal
    $('.modal').modal();
    
    //Initialise collapsible card
    $('.collapsible').collapsible();
    
    //Initialise datepicker
    $('.datepicker').datepicker();
  
});

/*Script for displaing current date in add article form code taken from the following post 
(https://stackoverflow.com/questions/51690498/how-can-i-insert-current-date-as-a-value-in-an-input-form-field)*/

var months = ["January", "February", "March", "April", "May", "June",
  "July", "August", "September", "October", "November", "December"
];
var n = new Date();
var y = n.getFullYear();
var m = n.getMonth();
var d = n.getDate();
document.getElementById("article_date").value = d + " " + months[m] + " " + y;
