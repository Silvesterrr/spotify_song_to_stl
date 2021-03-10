# spotify_song_to_stl
Spotify-song-to-stl is a python command-line based program designed to get .stl file of 'spotify code' based on spotify url.

# Usage
`spotify_song_to_stl.py [spotify-url] [code-height] [base-height]` <br><br>

# Example
You start by copying spotify song url as below.
![alt text](https://github.com/Silvesterrr/spotify_song_to_stl/blob/main/example.jpg?raw=true)

Than you run python file from console <br>
`spotify_song_to_stl.py spotify:track:5W3cjX2J3tjhG8zb6u0qHn 1 4.5`  
Number 1 is height of only code and 4.5 is height of base. So full height will be 5.5 (Unit is mm obviously) <br>
And after this we get something like this:<br>
![alt text](https://github.com/Silvesterrr/spotify_song_to_stl/blob/main/example2.jpg?raw=true)
As you can see model needs some repairing so i put it on this webside https://tools3d.azurewebsites.net/  
In future this feature may be included in the code.  
And bum just like that we got this model:  
![alt text](https://github.com/Silvesterrr/spotify_song_to_stl/blob/main/example3.jpg?raw=true)

# Requirements and Other
- You have to have python installed.  
- You have to install selenium and pillow (`pip install selenium`, `pip install Pillow`)
- Make sure that `chromedriver` added in the files is in thesame folder as python file
- Make sure that you have chrome browser installed.
- If the `chromedriver` is added in the files won't work download it from this webside https://chromedriver.chromium.org/downloads (version equal to your chrome version).

This code is really sketchy. Im still learning.
Hope You like it.  
If you have any problems, or you have any suggestions feel free to contact me at: `sylwesterjarosz50@gmail.com`
