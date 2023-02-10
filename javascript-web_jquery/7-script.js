#!/usr/bin/node

$.ajax({
  url: 'https://swapi-api.hbtn.io/api/films/?format=json',
  type: 'GET',
  success: (data) => {
    $('#character').text(data.name);
  }
});
