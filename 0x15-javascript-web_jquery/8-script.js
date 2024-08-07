$.get('https://swapi.co/api/films/?format=json', function (para) {
  $('UL#list_movies').append(...para.results.map(video => `<li>${video.title}</li>`));
});
