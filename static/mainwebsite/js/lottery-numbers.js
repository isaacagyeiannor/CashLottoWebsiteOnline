//Show or hide lottery 
$("select").on("change", function() {
	var lottery_type = $("select").find(":selected").val();
switch (lottery_type) {
  case "2 Direct ":
    $("#fifth_number, #fourth_number, #third_number").hide();
    $("#first_number, #second_number").show();
    break;

  case "3 Direct":
    $("#fifth_number, #fourth_number").hide();
    $("#first_number, #second_number, #third_number").show();
    break;

  case "Perm 2":
    $("#fifth_number, #fourth_number, #third_number").hide();
    $("#first_number, #second_number").show();
    break;
  
  case "Perm 3":
    $("#fifth_number, #fourth_number").hide();
    $("#first_number, #second_number, #third_number").show();
  break;

  default:
    alert("Select lottery type");
    break;
}

});

//Insert Number clicked
$('#lottery_balls img').on ( "click", function(){
  var ballClickedNum = document.querySelectorAll("#lottery_balls img").firstChild;
  alert(ballClickedNum);
});

// $('click', function(){
//   alert("click is working");
// });
document.querySelectorAll("#lottery_balls img");