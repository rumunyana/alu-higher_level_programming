#!/usr/bin/node

$.ajax({
  url: 'https://swapi-api.hbtn.io/api/films/?format=json',
  type: 'GET',
  dataType: 'json'
}).done((data) => {
  data.results.forEach((film) => {
    $('UL#list_movies').append(`<li>${film}</li>`);
  });
});
