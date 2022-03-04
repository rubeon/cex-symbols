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
Fire Emblem, Unboxed                                             55.00



Mega Drive Software <1055>
==========================
Micro Machines 2 Turbo Tournament, Boxed                         10.00
Mortal Kombat 3, Boxed                                           22.00



Master System Software <1059>
=============================



Dreamcast Games <51>
====================
Sonic Adventure, Boxed                                           15.00
Virtua Tennis, Boxed                                              6.00



Game Boy Software <1103>
========================
Pokemon: Red Version, Boxed                                     140.00



NES Software <1052>
===================
Super Mario Bros., Unboxed                                       12.00



Super NES Software <1037>
=========================
Street Fighter II, Unboxed                                       12.00
Stunt Race FX, Unboxed                                            5.00
Super Mario All Stars, Unboxed                                   15.00
Super Tennis, Unboxed                                             6.00
Tetris & Dr Mario, Unboxed                                       15.00



3DS Games <972>
===============
Animal Crossing: Happy Home Designer (No Card)                    8.00
Battleship                                                        3.00
Big Hero 6                                                        3.00
Bravely Second: End Layer Deluxe Collector's Ed. +Statue/Book/CD     30.00
Cars 2                                                            3.00
FIFA 14                                                           3.00
FIFA 15                                                           6.00
Green Lantern Rise Of The Manhunters                              3.00
Horrid Henry: Good, The Bad & The Bugly                           3.00
Ice Age 4 - Continental Drift                                     3.00
LEGO Batman 3: Beyond Gotham                                      5.00
LEGO Jurassic World (No Figure)                                   5.00
LEGO Marvel Super Heroes: Universe in Peril                       5.00
LEGO Ninjago: Shadow Of Ronin                                     6.00
Legend Of Zelda Ocarina Of Time 3D                               20.00
Legend Of Zelda: Link Between Worlds                             18.00
Lego City Undercover: The Chase Begins                            4.00
Lego Movie Videogame, The                                         4.00
Lego Pirates Of The Caribbean                                     6.00
Mario & Sonic At The London 2012 Olympic                          8.00
Mario Kart 7                                                     12.00
Mario Party: Island Tour                                         10.00
Mario Tennis Open                                                 6.00
Monster Hunter 4 Ultimate                                        10.00
New Super Mario Bros. 2                                          15.00
Nintendogs & Cats Golden Retriever                               10.00
Paper Mario Sticker Star                                         12.00
Pokemon Alpha Sapphire                                           32.00
Pokemon Moon                                                     12.00
Pokemon Omega Ruby                                               32.00
Pokemon Sun                                                      12.00
Pokemon X                                                        30.00
Pokemon Y                                                        28.00
Pro Evolution Soccer 2011 3D                                      1.00
Professor Layton & The Miracle Mask                               8.00
Shin Megami Tensei: Devil Summoner: Soul Hackers                 45.00
Sonic Generations                                                10.00
Super Mario 3D Land                                               8.00
Super Smash Bros.                                                12.00
Tomodachi life                                                   20.00
Yo-Kai Watch                                                      5.00
Yo-Kai Watch 3                                                  100.00
Yo-Kai Watch Blasters: Red Cat Corps                             30.00
Yo-Kai Watch Blasters: White Dog Squad                           25.00
Yoshi's New Island                                                8.00

```
[cex]:https://uk.webuy.com
