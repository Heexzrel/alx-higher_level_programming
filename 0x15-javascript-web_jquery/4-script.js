// Toggles the class of HTML tag 'HEADER' when user clicks the
// div#toggle_header tag
const $ = window.$;
$('DIV#toggle_header').click(function () {
  $('HEADER').toggleClass('green red');
});
