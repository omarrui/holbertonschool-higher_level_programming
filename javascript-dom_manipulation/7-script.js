#!/usr/bin/node
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then(response => response.json())
    .then(data=>{
        constmoviesList = document.querySelector("#list_movies");
        data.results.forEAch(movie =>{
            const listItem = document.createElement('li');
            listItem.textContent = movie.title;
            movieslist.appendchild(listItem);
        });
    });
