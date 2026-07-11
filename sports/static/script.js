
		var x = document.getElementById('qty');
	var y = document.getElementById(id);


function dltRow(y) {
        document.getElementById(y).style.display = 'none';
}

 function increase_by_one(y) {
 x = parseInt(document.getElementById(y).value);
 document.getElementById(y).value = x + 1;
}
 
function decrease_by_one(y) {
 x = parseInt(document.getElementById(y).value);
 if (x > 1) {
     document.getElementById(y).value = x - 1;
 }
}