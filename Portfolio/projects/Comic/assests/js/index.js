var panel1 = document.getElementsByClassName("panel1")[0];
var panel3 = document.getElementsByClassName("panel3")[0];
var panel4 = document.getElementsByClassName("pn4_div")[0];
var panel5 = document.getElementsByClassName("panel5")[0];
var panel6 = document.getElementsByClassName("panel6")[0];
var panel4_box = document.getElementsByClassName("pn4_box")[0];
var pn4_fire1 = document.getElementsByClassName("pn4-fire1")[0];
var pn4_fire2 = document.getElementsByClassName("pn4-fire2")[0];
var time_sci = document.getElementsByClassName("time_sci")[0];
var pn3_man = document.getElementsByClassName("pn3_man")[0];
var pn3_man_1 = document.getElementsByClassName("pn3_man_1")[0];
var pn3_man_2 = document.getElementsByClassName("pn3_man_1")[1];
var wonder = document.getElementsByClassName("wonder")[0];
var sprite_2 = document.getElementsByClassName("sprite-2")[0];
var sprite_3 = document.getElementsByClassName("sprite-3")[0];
var sprite_4 = document.getElementsByClassName("sprite-4")[0];
var time_machine = document.getElementsByClassName("timemachine")[0];
var walk_1 = document.getElementsByClassName("walk1")[0];
var walk_2 = document.getElementsByClassName("walk2")[0];
var walk_3 = document.getElementsByClassName("walk3")[0];
var statement5_1 = document.getElementsByClassName("statement5_1")[0];
var statement5_s = document.getElementsByClassName("statement5_s")[0];
var pn5_nxt = document.getElementsByClassName("pn5_nxt")[0];
var pn3_nxt = document.getElementsByClassName("next_btn")[0];
var cnt_1 = 0; var cnt_2 = 0; var cnt_3 = 0; var cnt_4 = 0; var cnt_5 = 0; var cnt_6 = 0; var cnt_7 = 0, pn5_cnt = 0; 




/* *********************************************************
  Shaking animation 
********************************************************* */


function shakeImage() {
	console.log("yes")
	var image = document.getElementById("myImage");
    $('#myImage').append('<audio autoplay><source src="./assests/sound/bang.wav" type="audio/wav"></audio>');
	image.classList.add("shake-image");

	image.addEventListener("animationend", function() {
		image.classList.remove("shake-image");
		$("#shake-button").hide();
		image.style.backgroundImage = "url('./assests/images/panel1/background1.jpg')";
        $('.panel1').show()
        setTimeout(() => {
            $('.time_sci').show();
        }, 2000);
        setTimeout(() => {
            $('.alert').show();
        }, 3000);
	}, {once: true});
}

function timemachine(){
    if(time_sci.style.display == "block"){
        $('.panel1').append('<audio autoplay><source src="./assests/sound/bang.wav" type="audio/wav"></audio>');
        $('.panel1').append('<audio autoplay><source src="./assests/sound/panel2.mp3" type="audio/mpeg"></audio>');
        document.getElementsByClassName('mainlab1')[0].classList.add('shake-image');
        setTimeout(() => {
            $('.panel1').hide();
            $('.timemachine').show();
        }, 1000)
        setTimeout(panel2_end, 3000);
    }
}
function panel2_end(){
    $('.panel3').append('<audio autoplay loop><source src="./assests/sound/water.mp3" type="audio/mpeg"></audio>');
    $('.panel3').append('<audio autoplay loop><source src="./assests/sound/birdflysound.wav" type="audio/wav"></audio>');
    $('.panel3').append('<audio autoplay loop><source src="./assests/sound/birdsoundandpflysound.wav" type="audio/wav"></audio>');
    time_machine.style.display = "none";
    panel3.style.display = "block";
    setTimeout(() => {
        pn3_man.style.display = "none";
        pn3_man_1.style.display = "block";
    }, 3000)
    setTimeout(() => {
        pn3_man_1.style.display = "none";
        pn3_man_2.style.display = "block";
        wonder.style.display = "block";
        pn3_nxt.style.display = "block";    
    }, 5000);
}
function panel3_end(){
    
    switch(cnt_1){
        case 0:
            wonder.innerHTML = "These creatures are far more friendly than I ever imagined.";
            cnt_1++;
            break;
        case 1:
            wonder.innerHTML = "I can see the time machine, let me get back to the Lab!";
            cnt_1++;
            break;
        case 2:
            $('audio').remove();
            panel3.style.display = "none";
            panel4.style.display = "block";
            $('.pn4_div').append('<audio autoplay><source src="./assests/sound/panel3.wav" type="audio/wav"></audio>');
            setTimeout(() => {
                $(".pn4_box1").fadeOut();
                $(".pn4_box2").fadeIn();
                $('.pn4_div').append('<audio autoplay loop><source src="./assests/sound/crowd.wav" type="audio/wav"></audio>')
            }, 2000);
        
            setTimeout(() => {
                $(".pn4_box2").fadeOut();
                $(".pn4_box3").fadeIn();
        
                $(".pn4_sprite").click(function() {
                    $('.pn4_div').append('<audio autoplay><source src="./assests/sound/panel4.wav" type="audio/wav"></audio>');
                    console.log("OK");
                    $(".pn4_box3").fadeOut();
                    $(this).css('background', 'url(./assests/images/panel4/Layer_1.png)');
                    $(this).css("background-repeat", "no-repeat");
                    setTimeout(() => {
                        $(this).css('background', 'url(./assests/images/panel4/Layer_2.png)');
                        $(this).css("background-repeat", "no-repeat");

                    }, 300);
                    setTimeout(() => {
                        $(this).css('background', 'url(./assests/images/panel4/Layer_3.png)');
                        $(this).css("background-repeat", "no-repeat");
                    }, 600);
                    setTimeout(() => {
                        $(this).css('background', 'url(./assests/images/panel4/Layer_4.png)');
                        $(this).css("background-repeat", "no-repeat");
                    }, 900);
                    setTimeout(() => {
                        $(this).css('background', 'url(./assests/images/panel4/Layer_5.png)');
                        $(this).css("background-repeat", "no-repeat");
                    }, 1200);
                    setTimeout(() => {
                        $(this).css('background', 'url(./assests/images/panel4/Layer_6.png)');
                        $(this).css("background-repeat", "no-repeat");
                    }, 1500);
                    setTimeout(() => {
                        $(this).css('background', 'url(./assests/images/panel4/Layer_7.png)');
                        $(this).css("background-repeat", "no-repeat");
                    }, 1800);
                    setTimeout(() => {
                        $(this).css('background', 'url(./assests/images/panel4/stand.png)');
                        $(this).css("background-repeat", "no-repeat");
        
                        $(".pn4-fire1").show();
                        $(".pn4-fire2").show();
                
                        $(".pn4-fire1").animate({
                            left: '1200rem',
                            top: '400rem'
                        }, 3000);
                        $(".pn4-fire2").animate({
                            left: '1200rem',
                            top: '400rem'
                        }, 3000);
                    }, 2000);
                    setTimeout(() => {
                        $('audio').remove();
                        $('.pn4_div').append('<audio autoplay><source src="./assests/sound/bang.wav" type="audio/wav"></audio>')
                    }, 5000);
                    setTimeout(() => {
                        $('audio').remove();
                        $('.pn4_div').append('<audio autoplay><source src="./assests/sound/bang.wav" type="audio/wav"></audio>')
                        $(".pn4_sprite").hide();
                        $(".pn4_div").css("background", "url(./assests/images/panel4/flash.gif)");
                        $(".pn4_div").css("background-size", "100% 100%");
                        $(".pn4_div").css("background-repeat", "no-repeat");
                
                        $(".pn4_box").hide();
                        $(".pn4-fire1").hide();
                        $(".pn4-fire2").hide();
        
                        setTimeout(() => {
                            $('audio').remove();
                            $('.panel5').append('<audio autoplay loop><source src="./assests/sound/allow.wav" type="audio/wav"></audio>')
                            $('.panel5').append('<audio autoplay><source src="./assests/sound/horsesound.wav" type="audio/wav"></audio>')

                            panel4.style.display = "none";
                            panel5.style.display = "block";
                            walking();
                        }, 1000);
                    }, 6000);
                });
            }, 5000);
        }
   
}


function pn5_btnclk() {
    if(pn5_cnt == 0) {
        pn5_cnt = 1;
        $('.statement5_s').text('Perfect!');
        $('.statement5_1').hide();
        $('.statement5_s').css('left','700rem');
        $('.pn5_text').show();
    } else if (pn5_cnt == 1) {
        console.log("afseewfw");
        $('audio').remove();
        $('.panel6').append('<audio autoplay><source src="./assests/sound/panel3.wav" type="audio/wav"></audio>')
        $('.panel5').hide();
        $('.timemachine').show();
        $('.noplan').hide();
        setTimeout(() => {
            $('.timemachine').hide();
            $('.mainlab').show();
            $('.mainlab').addClass('shake-image');
            $('.panel6').append('<audio autoplay><source src="./assests/sound/bang.wav" type="audio/wav"></audio>')
        }, 2000);
        setTimeout(() => {
            $('.last_sci').show();
        }, 3000);
        setTimeout(() => {
            $('.final').show();
        }, 4000)
    }
}

function walking(){
    setTimeout(walk_sci_2, 1000);
    setTimeout(walk_sci_3, 2000);
}

function walk_sci_2(){
    walk_1.style.display = "none";
    walk_2.style.display = "block";
}
function walk_sci_3(){
    walk_2.style.display = "none";
    walk_3.style.display = "block";
    statement5_s.style.display = "block";
    setTimeout(() => { statement5_1.style.display = "block"; pn5_nxt.style.display = "block";}, 2000);
}
function changealert(){
    statement5_1.innerHTML = "You can go to your lab by clicking the above letter - GENERAL STORE."
}
function gotolab(){
    panel5.style.display = "none";
    panel6.style.display = "block";
}