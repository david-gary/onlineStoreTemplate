//END POINTS FOR GENRE FILTERING
const allMoviesEndPoint = 'http://127.0.0.1:5000/movies';
const actionMoviesEndPoint = 'http://127.0.0.1:5000/movies/action';
const horrorMoviesEndPoint = 'http://127.0.0.1:5000/movies/horror';
const comedyMoviesEndPoint = 'http://127.0.0.1:5000/movies/comedy';
const historyMoviesEndPoint = 'http://127.0.0.1:5000/movies/history';
//BUTTONS FOR SCROLLING THROUGH MOVIES
const leftScrollButton = document.getElementById('left-all-movies')
const rightScrollButton = document.getElementById('right-all-movies')
const horrorScrollLeft = document.getElementById('left-horror-movies')
const horrorScrollRight = document.getElementById('right-horror-movies')
const historyScrollLeft = document.getElementById('left-history-movies')
const historyScrollRight = document.getElementById('right-history-movies')
const comedyScrollLeft = document.getElementById('left-comedy-movies')
const comedyScrollRight = document.getElementById('right-comedy-movies')
const actionScrollLeft = document.getElementById('left-action-movies')
const actionScrollRight = document.getElementById('right-action-movies')
//GENERATES JSON DATA AND INPUTS THEM IN MOVIE GENERATOR
const generateMovies = async (url, divID) => {
    const response = await fetch(url).
        then().
        catch(err => console.log(err))
    const jsonData = await response.json()
    for (let i = 0; i < jsonData.length; i++) {
        movieGenerator(jsonData[i].genre, jsonData[i].movie_title, jsonData[i].picture, jsonData[i].summary, jsonData[i].rating, divID)
    }
}
//Creates the movies you see in the first section of the website
function movieGenerator(genre, title, picture, summary, rating, divID) {
    // creating elements needed
    const movieDiv = document.createElement('div')
    movieDiv.className = 'movie-container'
    movieDiv.setAttribute('id', title)
    const movie_title = document.createElement('h5')
    const movie_picture = document.createElement('img')
    const description = document.createElement('div')
    const movie_genre = document.createElement('h5')
    const movie_rating = document.createElement('h2')
    const divButton = document.createElement('div')
    const button = document.createElement('button')
    const pictureDiv = document.createElement('div')
    description.className = 'summary-container'
    divButton.className = 'purchase-div'
    pictureDiv.className = 'picture-container'
    //appending the data to the elements
    movie_title.textContent = title
    movie_picture.src = picture
    description.textContent = summary
    movie_genre.textContent = genre
    movie_rating.textContent = rating
    button.textContent = 'Purchase'
    //appending elements to main div
    divButton.append(button)
    pictureDiv.append(movie_picture)
    movieDiv.append(pictureDiv, movie_title)
    document.getElementById(divID).appendChild(movieDiv)
}
//Used to scroll left and right on the webpage
leftScrollButton.onclick = () => { document.getElementById('scroll-bar').scrollLeft -= 1000 }
rightScrollButton.onclick = () => { document.getElementById('scroll-bar').scrollLeft += 1000 };
horrorScrollLeft.onclick = () => { document.getElementById('horror-bar').scrollLeft -= 1000 }
horrorScrollRight.onclick = () => { document.getElementById('horror-bar').scrollLeft += 1000 }
comedyScrollRight.onclick = () => { document.getElementById('comedy-bar').scrollLeft += 1000 }
historyScrollRight.onclick = () => { document.getElementById('history-bar').scrollLeft += 1000 }
actionScrollRight.onclick = () => { document.getElementById('action-bar').scrollLeft += 1000 }
comedyScrollLeft.onclick = () => { document.getElementById('comedy-bar').scrollLeft -= 1000 }
historyScrollLeft.onclick = () => { document.getElementById('history-bar').scrollLeft -= 1000 }
actionScrollLeft.onclick = () => { document.getElementById('action-bar').scrollLeft -= 1000 }
//-------- USING SETTIMEOUT TO PREVENT THIS ERROR FROM THE BACKEND-----ProgrammingError: Recursive use of cursors not allowed.
generateMovies(allMoviesEndPoint, 'scroll-bar')
setTimeout(async () => await generateMovies(horrorMoviesEndPoint, 'horror-bar'), 500)
setTimeout(async () => await generateMovies(comedyMoviesEndPoint, 'comedy-bar'), 1000)
setTimeout(async () => await generateMovies(historyMoviesEndPoint, 'history-bar'), 1500)
setTimeout(async () => await generateMovies(actionMoviesEndPoint, 'action-bar'), 2000)




