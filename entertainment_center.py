import media
import fresh_tomatoes

# Generate movies with media.Movie, follow this key movie_title, movie_storyline, poster_image, trailer_youtube
TOY_STORY = media.Movie("Toy Story", "Toys riot.",
                        "https://www.movieposter.com/posters/archive/main/204/MPW-102287",
                        "https://www.youtube.com/watch?v=_iji49gNsp4")

AVATAR = media.Movie("Avatar", "Marine get's his legs.",
                     "http://cafmp.com/wp-content/uploads/2012/11/Avatar.jpg",
                     "https://www.youtube.com/watch?v=cX0R3mXaod8")

HOT_FUZZ = media.Movie("Hot Fuzz", "Two men take on the world",
                       "http://img.moviepostershop.com/hot-fuzz-movie-poster-2007-1010439412.jpg",
                       "https://www.youtube.com/watch?v=qDvlolD35-w")

# Add all my movies to a LIST and then open them via fresh_tomatoes. 
MOVIES = [TOY_STORY, AVATAR, HOT_FUZZ]
fresh_tomatoes.open_movies_page(MOVIES)
