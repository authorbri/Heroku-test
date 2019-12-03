<html><head>
  <meta charset='utf-8'>
  <title>Гороскоп на сегодня</title>
  <link
    rel="stylesheet"
    href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css"
    integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO"
    crossorigin="anonymous"
  />
  <!-- <script src="http://code.jquery.com/jquery-3.3.1.min.js"></script> -->
  </head>
  <body>
    <div class="container">
      <h1>Что день {{ date }} готовит</h1>

      % if special_date:
      <h2>Сегодня супер особенный день!</h2>
      % end

      % for pred in predictions:
      <p>{{ pred }}</p>
      % end

    </div>

  <!-- <div class="row">
  <div class="col" id="p-0">
  </div>
  <div class="col" id="p-1">
  </div>
</div>

<div class="row">
  <div class="col" id="p-2">
  </div>
  <div class="col" id="p-3">
  </div>
</div>

<div class="row">
  <div class="col" id="p-4">
  </div>
  <div class="col" id="p-5">
  </div>
</div> -->

  </body>
  <!-- <script language="javascript"> -->
    // <!-- console.log( {{ x }} ); -->
    
    <!-- function set_content_in_divs(paragraphs) {
  $.each(paragraphs, function(i, d) {
    p = $("#p-" + i)
    p.html("<p>" + d + "</p>")
  })
}

$.getJSON("localhost:8080/api/forecasts", set_content_in_divs(paragraphs), function() {console.log("Что-то пошло не так...")})
  </script> -->
</html>