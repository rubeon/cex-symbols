# CeX-Symbols

This little utility lets you quickly check your local [CeX][cex]'s stock for
retro games.

It can be modified to check any categories you like, but you'll need to figure
out the category IDs your self.

To run, first make sure you have the dependences satisfied, then run the main
python script.

## Example:

```bash

$ mkdir -p ~/code/myenv
$ cd ~/code/myenv
$ python3 -mvenv .
$ . bin/activate
(myenv)$ git clone https://github.com/rubeon/cex-symbols.git
(myenv)$ cd cex-symbols
(myenv)$ python ./webuy.py

Got 7 categories
Gameboy Advance Software <1049>
===============================
Super Mario World: Super Mario Advance 2, Unboxed                15.00
Pokemon Ruby, Unboxed                                            20.00



Mega Drive Software <1055>
==========================
Sonic Spinball, Boxed                                             6.00
Sonic 2, Boxed                                                    4.00
Sonic 3, Boxed                                                   20.00
Ristar, Boxed                                                    45.00
Ren & Stimpy, Unboxed                                             8.00
Primal Rage, Boxed                                               10.00
Mighty Morphin Power Rangers, Unboxed                             6.00
Lion King, Boxed                                                 10.00
Lemmings, Unboxed                                                 6.00
Dynamite Headdy, Boxed                                           15.00
Comix Zone, Boxed                                                28.00
Alien Storm, Boxed                                               12.00



Master System Software <1059>
=============================
Wonder Boy, Unboxed                                              12.00
Super Space Invaders, Boxed                                       6.00
Sonic The Hedgehog 2, Boxed                                       3.50
Secret Command, Unboxed                                           3.00
R-Type, Unboxed                                                   6.00
Paperboy, Unboxed                                                 4.00
Fantasy Zone, Unboxed                                             8.00



Dreamcast Games <51>
====================
Rez, Boxed                                                       65.00



Game Boy Software <1103>
========================
World Cup USA 94, Unboxed                                         2.50
Wario Land: Super Mario Land 3, Unboxed                           8.00
Tetris, Unboxed                                                   5.00
Tetris 2, Unboxed                                                 5.00
Super Mario Land, Unboxed                                         8.00
Super Mario Land 2: 6 Golden Coins, Unboxed                       6.00
Pokemon: Yellow Version: Special Pikachu Edition, Unboxed        18.00
Pokemon: Yellow Version: Special Pikachu Edition, Boxed          42.00
Pokemon: Red Version, Unboxed                                    20.00
Paperboy, Unboxed                                                 6.00
Pac-Man, Unboxed                                                  8.00
Mortal Kombat II, Unboxed                                         6.00
International Superstar Soccer, Unboxed                           2.00
Hook, Unboxed                                                     5.00
Dr. Mario, Boxed                                                 25.00



NES Software <1052>
===================



Super NES Software <1037>
=========================
Top Gear, Unboxed                                                 6.00
Super Star Wars, Unboxed                                         10.00
Super Metroid, Unboxed                                           32.00
Super Mario World, Unboxed                                        8.00
Super Mario Kart, Unboxed                                        15.00
Super Mario Kart, Boxed                                          25.00
Super Mario All Stars, Unboxed                                    8.00
Super Mario All Stars & Super Mario World, Unboxed               12.00
Street Fighter II, Unboxed                                        6.00
Starwing, Unboxed                                                 4.00
Nintendo Scope 6, Unboxed                                         1.00
NBA Jam, Unboxed                                                  4.00
Mortal Kombat 2, Unboxed                                         12.00
Mickey Mania, Unboxed                                             8.00
Lion King, Unboxed                                                8.00
Lemmings, Unboxed                                                 6.00
Legend of Zelda, The: A Link to the Past, Unboxed                28.00
Killer Instinct, Unboxed                                          6.00
Earthworm Jim, Unboxed                                           12.00
Donkey Kong Country, Unboxed                                     10.00
Donkey Kong Country 2, Unboxed                                   18.00
Alien 3, Unboxed                                                  8.00
Aladdin, Unboxed                                                 15.00
Addams Family, Boxed                                             25.00

```
[cex]:https://uk.webuy.com
