

//Show or hide lottery 

$( "#lottery_balls li img" ).unbind().on( "click", function(e) {
  if( ($("select").find(":selected").val()) == ''){
    alert('Select lottery type');
  }

});

$("select").on("change", function() {
	var lottery_type = $("select").find(":selected").val();
  let numberOfSelection = 0;
switch (lottery_type) {
  case "2 Direct ":
    numberOfSelection = 2;
    $("#selected_numbers li").remove();
    $("#lottery_selected_text h3").remove();
    $("#lottery_selected_text").prepend(' <h3>You can select only 2 numbers</h3>');

    //function
    LotterySelection()
    
    break;

  case "3 Direct":
    numberOfSelection = 3;
    $("#selected_numbers li").remove();
    $("#lottery_selected_text h3").remove();
    $("#lottery_selected_text").prepend(' <h3>You can select only 3 numbers</h3>');

    //function
    LotterySelection();
    break;

  case "Perm 2":
    numberOfSelection = 2;
    $("#selected_numbers li").remove();
    $("#lottery_selected_text h3").remove();
    $("#lottery_selected_text").prepend(' <h3>You can select 3 to 24 numbers</h3>');

    //function
    LotterySelection();
    break;
  
  case "Perm 3":
    numberOfSelection = 3;
    $("#selected_numbers li").remove();
    $("#lottery_selected_text h3").remove();
    $("#lottery_selected_text").prepend(' <h3>You can select 4 to 17 numbers</h3>');

    //function
    LotterySelection();
  break;

  case "Perm 4":
    numberOfSelection = 5;
    $("#selected_numbers li").remove();
    $("#lottery_selected_text h3").remove();
    $("#lottery_selected_text").prepend(' <h3>You can select 5 to 13 numbers</h3>');

    //function
    LotterySelection();
  break;

  case "Perm 5":
    numberOfSelection = 5;
    $("#selected_numbers li").remove();
    $("#lottery_selected_text h3").remove();
    $("#lottery_selected_text").prepend(' <h3>You can select 6 to 12 numbers</h3>');

    //function
    LotterySelection();
  break;

  case "":
    $("#selected_numbers li").remove();
    $("#lottery_selected_text h3").remove();
    //function
    $( "#lottery_balls li img" ).unbind().on( "click", function(e) {
        alert("Select lottery type");

    });
  break;


  default:
    alert("Select lottery type");
    $("#selected_numbers li").remove();
    $("#lottery_selected_text h3").remove();
    $("#selected_numbers").prepend(' <li>?</li><li>?</li><li>?</li>');
    break;

  
}
//Lottery Selection Function
function LotterySelection() {
  $( "#lottery_balls li img" ).unbind().on( "click", function(e) {
    if( ($("#selected_numbers li").length) < numberOfSelection){
      var selectedItems = [];
      $("#selected_numbers li").each(function() { selectedItems.push($(this).text()) });
      var altText = e.target.alt;
      if (selectedItems.includes(altText)){
        var selectedValueNumber = selectedItems.indexOf(altText);
        $("#selected_numbers li")[selectedValueNumber].remove();
      }else {
      $("#selected_numbers").append('<li>'+altText+'</li>');
      };
    }else if(($("#selected_numbers li").length) == numberOfSelection) {
      var selectedItems = [];
      $("#selected_numbers li").each(function() { selectedItems.push($(this).text()) });
      var altText = e.target.alt;
      if (selectedItems.includes(altText)){
        var selectedValueNumber = selectedItems.indexOf(altText);
        $("#selected_numbers li")[selectedValueNumber].remove();
      }else {
        alert("Selection full");
      }
    }else {
      alert("Selection full")
    }

    

  });
}
  

});

