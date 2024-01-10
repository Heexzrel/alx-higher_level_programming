// Fetches and replaces the name of the API data then replaces the name
// of the character in the DIV#character tag text

const $ = window.$;
$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data) {
  $('DIV#character').text(data.name);
});
