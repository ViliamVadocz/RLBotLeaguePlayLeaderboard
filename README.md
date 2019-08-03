# Automatic League Play Leaderboard Generator

Guide:

- Download this repo.
- Copy and paste the previous week's standings into `previous_week.txt`.
- Copy and paste this week's standings into `current_week.txt`.
- Open `main.py` and set `current_week` to the current week's number. (You can also change other parameters.)
- Run `main.py`.

Advanced options:

- Modify the symbol templates found in the subdirectory `templates`. Only white will be replaced with the division colour. (Size 80x80)
- Modify the palette in `symbols.py` for each division. (This won't change the tiles, only symbols and text.)
- Change the description of each symbol in `symbols.py`. (Used for creating legend.)
- Add or change the division emblems in the subdirectory `emblems`. Name should be the same as division. (Size 300x300)
- Change drawing parameters in `leaderboard.py` to move things around.

Feel free to leave feedback. Enjoy!
