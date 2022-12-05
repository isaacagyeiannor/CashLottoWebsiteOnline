 //Onclick Number
 $( "#lottery_balls li img" ).on( "click", function(e) {
  var altText = e.target.alt;
  $("#selected_numbers").append('<li>'+altText+'</li>');
});

//Show or hide lottery 
$("select").on("change", function() {
	var lottery_type = $("select").find(":selected").val();
switch (lottery_type) {
  case "2 Direct ":
    $("#selected_numbers li").remove();
    $("#lottery_selected_text h3").remove();
    $("#lottery_selected_text").prepend(' <h3>You can select only 2 numbers</h3>');
    break;

  case "3 Direct":
    $("#selected_numbers li").remove();
    $("#lottery_selected_text h3").remove();
    $("#lottery_selected_text").prepend(' <h3>You can select only 3 numbers</h3>');
    break;

  case "Perm 2":
    $("#selected_numbers li").remove();
    $("#lottery_selected_text h3").remove();
    $("#lottery_selected_text").prepend(' <h3>You can select 3 to 24 numbers</h3>');
    break;
  
  case "Perm 3":
    $("#selected_numbers li").remove();
    $("#lottery_selected_text h3").remove();
    $("#lottery_selected_text").prepend(' <h3>You can select 4 to 17 numbers</h3>');
  break;

  case "Perm 4":
    $("#selected_numbers li").remove();
    $("#lottery_selected_text h3").remove();
    $("#lottery_selected_text").prepend(' <h3>You can select 5 to 13 numbers</h3>');
  break;

  case "Perm 5":
    $("#selected_numbers li").remove();
    $("#lottery_selected_text h3").remove();
    $("#lottery_selected_text").prepend(' <h3>You can select 6 to 12 numbers</h3>');
  break;


  default:
    alert("Select lottery type");
    $("#lottery_selected_text h3").remove();
    break;
}

});

//Lottery Calculation
var lines = function CalcLines(lottery_type){
  var lotteryLines;
if (lottery_type == 'Perm 2'){
  lotteryLines = 1;

} else if (lottery_type == 'Perm 3'){
  lotteryLines = 3;
}
else if (lottery_type == 'Perm 4'){
  lotteryLines = 6;
} else if(lottery_type == 'Perm 5'){

};
return lotteryLines;
};
// var lines = function (varName){
//   switch (lottery_type) {
//     case "2 Direct ":
//     1
//     break;

//   case "3 Direct":
    
//     break;

//   case "Perm 2":
    
//     break;
  
//   case "Perm 3":
    
//   break;

//   default:
//     alert("Select lottery type");
//     break;
//   }
// };
var amountGiven
var deposit;
var lotteryChosen;
var price = amount*lines;