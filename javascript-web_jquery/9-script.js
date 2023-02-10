#!/usr/bin/node

$.ajax({
  url: 'https://fourtonfish.com/hellosalut/?lang=fr',
  type: 'GET',
  dataType: 'json',
  success: (data) => {
    $('div#hello').text(data);
  }
});
