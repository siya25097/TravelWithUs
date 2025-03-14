document.addEventListener('DOMContentLoaded', function() {
    console.log('Welcome to the Travel Website!');
});

  const images = [
    "{% static 'images/hero.jpg' %}",
    "{% static 'images/hero1.jpg' %}",
    "{% static 'images/hero2.jpg' %}",
    "{% static 'images/hero3.jpg' %}",
  ];

  let currentIndex = 0;
  const heroSection = document.querySelector(".hero");

  function changeBackgroundImage() {
    heroSection.style.backgroundImage = `url(${images[currentIndex]})`;
    currentIndex = (currentIndex + 1) % images.length; 
  }

  
  setInterval(changeBackgroundImage, 5000);


  heroSection.style.backgroundImage = `url(${images[0]})`;

