
$( document ).ready(function(){
	$(".dropdown-button").dropdown();
	$(".button-collapse").sideNav();

	$('.dropdown_content').click(function(){
		console.log($(this)[0].text);
	});
});