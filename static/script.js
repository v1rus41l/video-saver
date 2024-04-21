$(document).ready(function() {
    $('#saveButton').click(function() {
      var link = document.getElementById('userInput').value
  
      $.ajax({
        type: 'POST',
        url: '/process',
        data: { 'link': link }, // Отправляем значение на сервер
        success: function(response) {
          // Действия при успешной обработке запроса
          console.log(response);
        }
      });
    });
  });


function findVideo() {
	var link = document.getElementById('userInput').value
	var link = link.toString();
	var a = link.indexOf('/', 10);
	var link = link.substring(0, a + 1) + 'embed/' + link.substring(32) + '?controls=0';
	
	document.querySelector('iframe').setAttribute('src', link)
	// var button = document.createElement("button");
	// button.innerHTML = "Download in the best resolution";

	// // Находим элемент <div> по идентификатору
	// var divElement = document.getElementsByClassName("container2")[0];

	// // Добавляем кнопку внутрь <div>
	// divElement.appendChild(button);

	var button = document.getElementById('downloadBtn')
	button.style.display = 'block'


}