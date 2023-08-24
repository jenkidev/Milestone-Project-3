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


// Script for sending email through email.js
const form = document.getElementById("contactForm");

function sendMail(contactForm) {
    emailjs.send("service_1wd0gcf", "template_y3nsvji",
    {"from_name": contactForm.first_name.value + contactForm.last_name.value,
     "from_email": contactForm.email.value,
     "query": contactForm.query.value
    },
    "Iw8TFysbugKKsDqz7")
    .then(function(response) {
        console.log('SUCCESS!', response.status, response.text);
        alert("Your message has been sent");
     }, function(error) {
        console.log('FAILED...', error);
     });
     setTimeout(function() {
      form.reset();
    }, 3000);
     return false;
}