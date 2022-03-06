
[spec]

; Format and options of this spec file:
options = "+Freeciv-2.6-spec"

[info]

; Apolyton Tileset created by CapTVK with thanks to the Apolyton Civ2
; Scenario League.

; Special thanks go to:
; Alex Mor and Captain Nemo for their excellent graphics work
; in the scenarios 2194 days war, Red Front, 2nd front and other misc graphics. 
; Fairline for his huge collection of original Civ2 unit spanning centuries
; Bebro for his collection of mediveal units and ships

artists = "
    Bobomax
    Alex Mor [Alex]
    Allard H.S. Höfelt [AHS]
    Bebro [BB]
    Captain Nemo [Nemo][MHN]
    CapTVK [CT] <thomas@worldonline.nl>
    Fairline [GB]
    GoPostal [GP]
    Tanelorn [T]
    Andrew ''Panda´´ Livings [APL]
"

[file]
gfx = "StickCiv/units"

[grid_main]

x_top_left = 1
y_top_left = 1
dx = 64
dy = 48
pixel_border = 1

tiles = { "row", "column", "tag"
				; Scenario League tags in brackets
  0,  0, "u.armor"		; [Bobomax]
  0,  1, "u.howitzer"		; [Bobomax]
  0,  2, "u.battleship"		; [Nemo]
  0,  3, "u.bomber"		; [GB]
  0,  4, "u.cannon"		; [Bobomax]
  0,  5, "u.caravan"		; [Bobomax]
  0,  6, "u.carrier"		; [Bobomax]
  0,  7, "u.catapult"		; [Bobomax]
  0,  8, "u.horsemen"		; [Bobomax]
  0,  9, "u.chariot"		; [Bobomax]
  0, 10, "u.cruiser"		; [Nemo]
  0, 11, "u.diplomat"		; [Bobomax]
  0, 12, "u.fighter"		; [Bobomax]
  0, 13, "u.frigate"		; [BB]
  0, 14, "u.ironclad"		; [Bobomax]
  0, 15, "u.knights"		; [Bobomax]
  0, 16, "u.legion"		; [Bobomax]
  0, 17, "u.mech_inf"		; [GB]
  0, 18, "u.warriors"		; [Bobomax]
  0, 19, "u.musketeers"		; [Bobomax]
  1,  0, "u.nuclear"		; [Bobomax]
  1,  1, "u.phalanx"		; [Bobomax]
  1,  2, "u.riflemen"		; [Bobomax]
  1,  3, "u.caravel"		; [Bobomax]
  1,  4, "u.settlers"		; [Bobomax]
  1,  5, "u.submarine"		; [Bobomax]
  1,  6, "u.transport"		; [Nemo]
  1,  7, "u.trireme"		; [Bobomax]
  1,  8, "u.archers"		; [Bobomax]
  1,  9, "u.cavalry"		; [Bobomax]
  1, 10, "u.cruise_missile"	; [Bobomax]
  1, 11, "u.destroyer"		; [Nemo]
  1, 12, "u.dragoons"		; [Bobomax]
  1, 13, "u.explorer"		; [Bobomax]
  1, 14, "u.freight"		; [Bobomax]
  1, 15, "u.galleon"		; [Bobomax]
  1, 16, "u.partisan"		; [BB] & [CT]
  1, 17, "u.pikemen"		; [Bobomax]
  2,  0, "u.marines"		; [Bobomax]
  2,  1, "u.spy"		; [Bobomax]
  2,  2, "u.engineers"		; [Bobomax]
  2,  3, "u.artillery"		; [Bobomax]
  2,  4, "u.helicopter"		; [T]
  2,  5, "u.alpine_troops"	; [Bobomax]
  2,  6, "u.stealth_bomber"	; [Bobomax]
  2,  7, "u.stealth_fighter"	; [Nemo] & [AHS]
  2,  8, "u.aegis_cruiser"	; [GP]
  2,  9, "u.paratroopers"	; [Alex]
  2, 10, "u.elephants"		; [Bobomax]
  2, 11, "u.crusaders"		; [Bobomax]
  2, 12, "u.fanatics"		; [GB] & [CT]
  2, 13, "u.awacs"		; [APL]
  2, 14, "u.worker"		; [Bobomax]
  2, 15, "u.leader"		; [Bobomax]
  2, 16, "u.barbarian_leader"	; [Bobomax]
  2, 17, "u.migrants"		; [Bobomax]
;  2, 19, "u.train"		; [Bobomax]

}
