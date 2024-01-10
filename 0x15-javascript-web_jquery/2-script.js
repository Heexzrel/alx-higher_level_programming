// Uses jQuery API to change color of div#red_header to red on click

const $ = window.$;
$('DIV#red_header').click(function () {
  $('HEADER').css('color', '#FF0000');
});
