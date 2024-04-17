#!/usr/bin/node
const axios = require('axios')

function getMovieCharacters (movieId) {
  const url = `https://swapi.dev/api/films/${movieId}/`
  return axios.get(url)
    .then(response => {
      const charactersUrls = response.data.characters
      return Promise.all(charactersUrls.map(characterUrl =>
        axios.get(characterUrl)
          .then(characterResponse => characterResponse.data.name)
          .catch(error => {
            console.error(`Failed to retrieve character data for URL: ${characterUrl}`)
            return null
          })
      ))
    })
    .catch(error => {
      console.error(`Failed to retrieve movie data for ID: ${movieId}`)
      return null
    })
}

function main () {
  const args = process.argv.slice(2)
  if (args.length !== 1) {
    console.error('Usage: node script.js <Movie ID>')
    process.exit(1)
  }

  const movieId = args[0]
  getMovieCharacters(movieId)
    .then(characters => {
      if (characters) {
        characters.forEach(character => console.log(character))
      }
    })
    .catch(error => console.error(error))
}

main()
