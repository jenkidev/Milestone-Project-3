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
     }, function(error) {
        console.log('FAILED...', error);
     });
     alert("Your message has been sent");
     setTimeout(function() {
      form.reset();
    }, 2000);
     return false;
}