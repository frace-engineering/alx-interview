#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (!movieId || isNaN(movieId)) {
  console.error('Please provide a valid movie ID as the first argument.');
  process.exit(1);
}

const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error occurred while making the request:', error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error('Failed to fetch movie data. Status code:', response.statusCode);
    process.exit(1);
  }

  const movieData = JSON.parse(body);
  const characters = movieData.characters;

  if (!characters || characters.length === 0) {
    console.log('No character information found for this movie.');
    process.exit(0);
  }
  const fetchCharacterData = (characterUrl) => {
    return new Promise((resolve, rejwct) => {
      request(characterUrl, (error, response, body) => {
        if (error) {
          reject('Error occurred while fetching character data: ' + error);
        return;
      }

      if (response.statusCode !== 200) {
        reject('Failed to fetch character data. Status code: ' + response.statusCode);
        return;
      }

      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  });
};

const characterPromises = characters.map(fetchCharacterData);
Promise.all(characterPromises)
  .then(characterNames => {
    characterNames.forEach(name => console.log(name));
  })
  .catch(error => {
    console.error(error);
  });
});
