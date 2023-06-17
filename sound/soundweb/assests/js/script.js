// Start interview
var s = 0;
function start_int(){
  if(s == 0){
    $('#InterviewPage').append('<audio controls autoplay ontimeupdate = "change_focus1(this)"><source src="./assests/audio/final.mp3" type="audio/mpeg"></source></audio>');
    $('.narrator').addClass('rise-up appear');
    $('.doctor').addClass('rise-up appear');
    s == 1;
  }
}
// interview
var state = 0;
function video_play(){
  document.getElementsByTagName('audio')[0].currentTime = 174;
  document.getElementsByTagName('audio')[0].play();
  setTimeout(() => {
    document.getElementsByTagName('audio')[0].pause();
  }, 5000);
  state = 1;
}
function change_focus1(event) {
  var time1 = event.currentTime;
  if((0 < time1 && time1 < 24)){
    $('.narrator-back').css('opacity', '0');
    $('.doctor-back').css('opacity', '0');
  } else if((time1 > 24 && time1 < 49) || (time1 > 51 && time1 < 64) || (time1 > 81 && time1 < 89) || (time1 > 106 && time1 < 113) || (time1 > 128 && time1 < 137) || (time1 > 153 && time1 < 160.5) || (time1 > 172 && time1 < 174.5)   || (time1 > 189 && time1 < 196) || (time1 > 214 && time1 < 221)){
    $('.narrator-back').css('opacity', '0');
    $('.doctor-back').css('opacity', '0.8');
    $('.narrator').css('z-index', '3');
    $('.doctor').css('z-index', '2');
    $('.narrator-back').removeClass('fade1-out');
    $('.narrator-back').addClass('fade1-in');
    $('.doctor-back').removeClass('fade1-in');
    $('.narrator-back').css('width', '49%');
    $('.doctor-back').addClass('fade1-out');
  } else if((time1 > 49 && time1 < 51) || (time1 > 64 && time1 < 81) || (time1 > 89 && time1 < 106) || (time1 > 113 && time1 < 128) || (time1 > 137 && time1 < 153) || (time1 > 160.5 && time1 < 172) || (time1 > 174.5 && time1 < 189)   || (time1 > 196 && time1 < 214)){
    $('.narrator-back').css('opacity', '0.8');
    $('.doctor-back').css('opacity', '0'); 
    $('.narrator').css('z-index', '2');
    $('.doctor').css('z-index', '3');
    $('.narrator-back').removeClass('fade1-in');
    $('.narrator-back').addClass('fade1-out');
    $('.doctor-back').removeClass('fade1-out');
    $('.narrator-back').css('width', '49%');
    $('.doctor-back').addClass('fade1-in');
  } else if(time1 > 221){
    $('.narrator-back').css('opacity', '0');
    $('.doctor-back').css('opacity', '0');
  }
  if(document.getElementsByTagName('audio')[0].ended == true){
    const element1 = document.getElementsByClassName('credit1')[0].offsetTop;
    window.scrollTo({
      top: element1,
      behavior: 'smooth'
    });
  }
  if(time1 > 174 && time1 < 189 && state == 0){
    document.getElementsByTagName('audio')[0].pause();
    $('.narrator-back').css('opacity', '0.8');
    $('.narrator-back').css('width', '51%');
    $('.doctor-back').css('opacity', '0.8');
    $('#InterviewPage').append('<a class="toquestion" href="#quiz" onclick="video_play()">Click me</a>');
  } else {
    $('.toquestion').hide();
  }
}
// 173.981842
// Get the answer buttons
const btnA = document.getElementById('btnA');
const btnB = document.getElementById('btnB');
const btnC = document.getElementById('btnC');
const answerContainer = document.getElementById('answer-buttons');

// Add click event listeners to the buttons
btnA.addEventListener('click', checkAnswer);
btnB.addEventListener('click', checkAnswer);
btnC.addEventListener('click', checkAnswer);

let answerSelected = false; // Flag variable to track answer selection

// Function to check the selected answer
function checkAnswer(event) {
  if (answerSelected) {
    return; // Exit the function if an answer has already been selected
  }
 else {
  $('#quiz').append('<audio autoplay><source src="./assests/audio/audio2.mp3" type="audio/mpeg"></source></audio>')
   const selectedButton = event.target;
 
   // Check if the selected answer is correct
   if (selectedButton === btnC) {
     // Correct answer
     selectedButton.classList.add('correct');
   } else {
     // Incorrect answer
     selectedButton.classList.add('incorrect');
     btnC.classList.add('correct');
   }
   setTimeout(() => {
    const element = document.getElementById('InterviewPage').offsetTop;
    window.scrollTo({
      top: element,
      behavior: 'smooth'
    });
    $('a').remove();
    document.getElementsByTagName('audio')[0].currentTime = 187;
    document.getElementsByTagName('audio')[0].play();
    console.log('123456')
   }, 8000);
 }

  // Disable the answer buttons
  btnA.disabled = true;
  btnB.disabled = true;
  btnC.disabled = true;

  answerSelected = true; // Set the flag to indicate answer selection
  answerContainer.classList.add('answer-selected'); // Add the CSS class to the container
}