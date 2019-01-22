//jQuery time
var current_fs, next_fs, previous_fs; //fieldsets
var left, opacity, scale; //fieldset properties which we will animate
var animating; //flag to prevent quick multi-click glitches

var site_1 = document.getElementById("site_1");
var weiterButton = document.getElementById("step_1_okButton");

var site_2 = document.getElementById("site_2");
var weiterButtonSite2 = document.getElementById("step_2_okButton");
var submit = document.getElementById("submit");

var fields = $('#site_1').find("select, textarea, input");
var fieldsSite2 = $('#site_2').find("select, textarea, input");
var fieldSite3 = $('#site_3').find("select, textarea, input");

var flag = true;
var flagSite2 = true;
var flagSubmit = true;

var site = false;

function scanEachField(fields, flag){
  var z = 0;
  $.each(fields, function(i, field){
    if (!field.value || field.value == "#"){
        flag = false;
        flagSite2 = false;
        flagSubmit = false;
        weiterButton.style.opacity = "0.5";
        weiterButtonSite2.style.opacity = "0.5";
        submit.style.opacity = "0.5";
        z++;
    }
    else if (z < 1){
        flag = true;
        flagSite2 = true;
        flagSubmit = true;
        weiterButton.style.opacity = "";
        weiterButtonSite2.style.opacity = "";
        submit.style.opacity = "";
        console.log("FLAG: TRUE :: z<1 :: " + field.value);
      }
  });
  return flag;
};

// EventListener
$("#msform").ready(function(){
  flag  = scanEachField(fields, flag);
  flagSite2 = scanEachField(fieldsSite2, flagSite2);
  flagSubmit = scanEachField(fieldSite3, flagSubmit);
});

site_1.addEventListener('mousedown', (event) => {
  flag = scanEachField(fields, flag);
});

site_1.addEventListener('keydown', (event) => {
  flag = scanEachField(fields, flag);
});

site_2.addEventListener('mousedown', (event) => {
  flagSite2 = scanEachField(fieldsSite2, flagSite2);
});

site_2.addEventListener('keydown', (event) => {
  flagSite2 = scanEachField(fieldsSite2, flagSite2);
});

site_3.addEventListener('keydown', (event) => {
  flagSubmit = scanEachField(fieldSite3, flagSubmit)
});

submit.addEventListener('mouseover', (event) =>{
  submitEvent = scanEachField(fieldSite3, flagSubmit)
});

// function change to next site
function changeToNextSite(current_fs, next_fs){
  //activate next step on progressbar using the index of next_fs
  $("#progressbar li").eq($("fieldset").index(next_fs)).addClass("active");

  //show the next fieldset
  next_fs.show();
    //hide the current fieldset with style
      current_fs.animate({opacity: 0}, {
        step: function(now, mx) {
          //as the opacity of current_fs reduces to 0 - stored in "now"
          //1. scale current_fs down to 80%
          scale = 1 - (1 - now) * 0.2;
          //2. bring next_fs from the right(50%)
          left = (now * 50)+"%";
          //3. increase opacity of next_fs to 1 as it moves in
          opacity = 1 - now;
          current_fs.css({
            'transform': 'scale('+scale+')',
            'position': 'absolute'
          });
          next_fs.css({'left': left, 'opacity': opacity});
        },
          duration: 800,
          complete: function(){
          current_fs.hide();
          animating = false;
          },
  });
}

// Input value abfrage wenn true nächste Seite
$(".next").click(function(){
  if (flagSite2 == true && site == true){

    animating = true;

    current_fs = $(this).parent();
    next_fs = $(this).parent().next();

    changeToNextSite(current_fs, next_fs);

  }
  else if (flag != false && site == false){

    animating = true;
    site = true;

    current_fs = $(this).parent();
    next_fs = $(this).parent().next();

    changeToNextSite(current_fs, next_fs);
  }
});

$(".previous").click(function(){
  if(animating) return false;
  animating = true;

  current_fs = $(this).parent();
  previous_fs = $(this).parent().prev();

  //de-activate current step on progressbar
  $("#progressbar li").eq($("fieldset").index(current_fs)).removeClass("active");

  //show the previous fieldset
  previous_fs.show();
  //hide the current fieldset with style
  current_fs.animate({opacity: 0}, {
    step: function(now, mx) {
      //as the opacity of current_fs reduces to 0 - stored in "now"
      //1. scale previous_fs from 80% to 100%
      scale = 0.8 + (1 - now) * 0.2;
      //2. take current_fs to the right(50%) - from 0%
      left = ((1-now) * 50)+"%";
      //3. increase opacity of previous_fs to 1 as it moves in
      opacity = 1 - now;
      current_fs.css({'left': left});
      previous_fs.css({'transform': 'scale('+scale+')', 'opacity': opacity});
    },
    duration: 800,
    complete: function(){
      current_fs.hide();
      animating = false;
    },
    //this comes from the custom easing plugin
    // easing: 'easeInOutBack'
  });
});

$(".submit").click(function(){
  if (flagSubmit == false){
    return false;
  }
  else{
    return true;
  }
});

$("#msform").keypress(
  function(event){
     if (event.which == '13') {
        event.preventDefault();
      }
});
