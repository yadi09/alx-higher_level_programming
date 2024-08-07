$.get('https://swapi.co/api/people/5/?format=json', function (para) {
  $('DIV#character').text(para.name);
});
