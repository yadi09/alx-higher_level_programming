$('document').ready(function () {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (para) {
    $('DIV#hello').text(para.hello);});
});
