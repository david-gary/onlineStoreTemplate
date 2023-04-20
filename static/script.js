//END POINTS FOR GENRE FILTERING
const allMoviesEndPoint = '/movies';
const actionMoviesEndPoint = '/movies/action';
const horrorMoviesEndPoint = '/movies/horror';
const comedyMoviesEndPoint = '/movies/comedy';
const historyMoviesEndPoint = '/movies/history';

//
function scrollHandler(idName) {
    function leftButton() {
        document.getElementById(idName).scrollLeft -= 1000
    }
    function rightButton() {
        document.getElementById(idName).scrollLeft += 1000
    }
    return { leftButton, rightButton }
}
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
    const purchaseDiv = document.createElement('div')
    purchaseDiv.className = 'pop-up'
    //**************purchase div contents***************
    // needed so other elements wont get deleted
    const closeButton = document.createElement('button')
    const purchasePictureDiv = document.createElement('div')
    const purchasePicture = document.createElement('img')
    const purchaseSummary = document.createElement('a')
    const purchaseButton = document.createElement('button')
    //adding classes and other attributes to purchase div elements
    closeButton.className = 'movie-button'
    closeButton.textContent = 'O'
    purchasePictureDiv.className = 'picture-container'
    purchasePicture.src = picture
    purchaseSummary.textContent = summary
    purchaseButton.textContent = 'Buy'
    purchaseButton.className = 'purchase-button'
    purchaseDiv.append(purchaseSummary, purchaseButton)
    //************************************************************** */
    closeButton.addEventListener('click', () => {
        console.log('i am being clicked')
        if (purchaseDiv.style.display === 'block') {
            movieDiv.style.flex = '0 0 0'
            movieDiv.style.flexDirection = 'column'
            purchaseDiv.style.display = 'none'
            closeButton.textContent = 'O'
        } else {
            movieDiv.style.flex = '0 0 auto'
            purchaseDiv.style.display = 'block'
            movieDiv.style.flexDirection = 'column'
            movieDiv.classList.toggle("visible");
            closeButton.textContent = '<'
        }
    })
    movieDiv.className = 'movie-container'
    purchaseDiv.className = 'purchase-container'
    movieDiv.setAttribute('id', title)
    const movie_title = document.createElement('h5')
    const movie_picture = document.createElement('img')
    const pictureDiv = document.createElement('div')
    pictureDiv.className = 'picture-container'
    //appending the data to the elements
    movie_title.textContent = title
    movie_picture.src = picture
    //appending elements to main div
    pictureDiv.append(movie_picture)
    //purchaseDiv.appendChild(movie_picture)
    movieDiv.append(pictureDiv, movie_title, purchaseDiv, closeButton)
    document.getElementById(divID).appendChild(movieDiv)
}
document.addEventListener('DOMContentLoaded', () => {
    //Refatored buttons using closure to debloat the code and makes it easier to read
    document.getElementById('left-all-movies').onclick = () => scrollHandler('scroll-bar').leftButton()
    document.getElementById('right-all-movies').onclick = () => scrollHandler('scroll-bar').rightButton()
    document.getElementById('left-horror-movies').onclick = () => scrollHandler('horror-bar').leftButton()
    document.getElementById('right-horror-movies').onclick = () => scrollHandler('horror-bar').rightButton()
    document.getElementById('left-history-movies').onclick = () => scrollHandler('history-bar').leftButton()
    document.getElementById('right-history-movies').onclick = () => scrollHandler('history-bar').rightButton()
    document.getElementById('left-comedy-movies').onclick = () => scrollHandler('comedy-bar').leftButton()
    document.getElementById('right-comedy-movies').onclick = () => scrollHandler('comedy-bar').rightButton()
    document.getElementById('left-action-movies').onclick = () => scrollHandler('action-bar').leftButton()
    document.getElementById('right-action-movies').onclick = () => scrollHandler('action-bar').rightButton()
    generateMovies(allMoviesEndPoint, 'scroll-bar')
    generateMovies(horrorMoviesEndPoint, 'horror-bar')
    generateMovies(comedyMoviesEndPoint, 'comedy-bar')
    generateMovies(historyMoviesEndPoint, 'history-bar')
    generateMovies(actionMoviesEndPoint, 'action-bar')
})
    //pullMovies();



