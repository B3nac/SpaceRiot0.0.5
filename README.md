Windows exe here --> http://b3nac.itch.io/space-riot. Development blog here --> http://b3nac.tumblr.com/ Current bug fixes and development details below.

SpaceRiot0.0.5
Bug fixes

Fixed asteroid and enemy spawn to be more scattered.
Implemented image_cache function.
converted all image loads to local and not global to be more efficient.
SpaceRiot0.0.4
Bug fixes/tweaks.

Score loop. This was looping until the start screen was exited. fixed this by moving to an after an "For after click statement." So it's only called once.

Exit Window being clicked but not exiting all the way. Fixed this by calling exit() after pygame.quit so if you exit the window it doesn't start the game, it exits all the way.

Added a speed boost pickup class.

Added laser graphics.

Code organizing and optimization. #Can not get enough of this.

Added fullscreen mode. Enter fullscreen mode by pressing f and exit with f.

Lots of graphical updates.
