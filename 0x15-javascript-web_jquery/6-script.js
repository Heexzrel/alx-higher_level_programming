// Updates the text of the header tag with a new header when the DIV#update_header tag is clicked
const $ = window.$;
$('DIV#update_header').click(function () {
  $('HEADER').text('New Header!!!');
});
