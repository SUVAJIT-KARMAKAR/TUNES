# Importing the flask module in the workspace 
from flask import Flask, render_template, url_for, request, redirect
#################################################################################################################
# Initialization of the flask application 
application = Flask(__name__)
#################################################################################################################
# Sample data for demonstration purposes
playlists = [
    {"song_name": "Tranquil Twilight", "movie_name": "Serene Sundown", "release_year": 2023},
    {"song_name": "Lunar Lullaby", "movie_name": "Moonbeam Sonata", "release_year": 2015},
    {"song_name": "Mystic Mirage", "movie_name": "Enigmatic Mirage", "release_year": 2016},
    {"song_name": "Infinite Illusion", "movie_name": "Dreamscape Chronicles", "release_year": 2021},
    {"song_name": "Crimson Canvas", "movie_name": "Painted Passions", "release_year": 2019},
    {"song_name": "Aurora Borealis", "movie_name": "Northern Lights", "release_year": 2018},
    {"song_name": "Whirlwind Waltz", "movie_name": "Dancing Dreams", "release_year": 2014},
    {"song_name": "Solar Serenity", "movie_name": "Sunset Serenade", "release_year": 2011},
    {"song_name": "Echoes of Eternity", "movie_name": "Timeless Echo", "release_year": 2024},
    {"song_name": "Stellar Voyage", "movie_name": "Galactic Odyssey", "release_year": 2013},
    {"song_name": "Rhythm of the Rain", "movie_name": "Raindrop Melodies", "release_year": 2021},
    {"song_name": "Mystical Love", "movie_name": "Mystical Love", "release_year": 2016},
    {"song_name": "Silent Whispers", "movie_name": "Shadows of Silence", "release_year": 2019},
    {"song_name": "Neon Nights", "movie_name": "City of Sparks", "release_year": 2022},
    {"song_name": "Melancholy Meadows", "movie_name": "Nostalgic Horizons", "release_year": 2014},
    {"song_name": "Surreal Symphony", "movie_name": "Parallel Realities", "release_year": 2017},
    {"song_name": "Dancing on Stardust", "movie_name": "Celestial Rhythms", "release_year": 2018},
]
#################################################################################################################
# Page routing 
# Home page
@application.route("/home")
@application.route("/")
def home():
    return render_template('home.html')

# Registration page
@application.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        # Collect form data
        name = request.form.get('name')
        age = request.form.get('age')
        sex = request.form.get('sex')
        genre = request.form.get('genre')
        email = request.form.get('email')
        phone_number = request.form.get('phone_number')
        dob = request.form.get('dob')

        # Simple email and phone number validation using JavaScript
        return render_template('registration_success.html', name=name, age=age, sex=sex,genre=genre, email=email, phone_number=phone_number, dob=dob)

    return render_template('registration.html')


# Login page
@application.route('/login', methods=['GET', 'POST'])
def login():
    error_message = None

    if request.method == 'POST':
        # Authenticate user as admin and set password 
        if request.form['username'] == 'SUVAJIT' and request.form['password'] == '!suvajit':
            # Redirect to admin page on successful login
            return redirect(url_for('admin'))
        else:
            error_message = 'Invalid credentials. Please try again.'
    return render_template('login.html', error_message=error_message)

# Admin page
@application.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        # Handle form submission to add playlist
        song_name = request.form.get('song_name')
        movie_name = request.form.get('movie_name')
        release_year = request.form.get('release_year')

        # Validate the form data (add your validation logic here)

        # Add the playlist to the data
        playlists.append({"song_name": song_name, "movie_name": movie_name, "release_year": int(release_year)})
    return render_template('admin.html', playlists=playlists)

# Explore page
@application.route("/explore")
def explore():
    return render_template('explore.html')
######################################################################################################
# Starting point
if __name__ == '__main__':
    application.run(debug=True, port=8000)
######################################################################################################