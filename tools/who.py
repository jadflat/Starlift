"""The who's-who page's rows (the intro of each stage). make_card.py writes them into each world's record on the card;
make_sprites.py numbers their pictures (Sprites.h: CS) along with those the game's code names."""
# picture, dx, dy, the enemy that must be about (Game.h's EnKind: 4 a turret, 5 a worm; 0 always) or a hazard, message, colour
WHO = [('MAN_WAVE1', 10, 0, 0, 'R_COLONIST', 'GREEN'), ('SAUCER0', 6, 2, 0, 'R_UFO', 'RED'), ('SNATCH0', 10, 0, 0, 'R_STINGER', 'RED'),
       ('MINE0', 13, 1, 0, 'R_MINE', 'GOLD'), ('TURRET', 11, 3, 4, 'R_TURRET', 'RED'), ('WORM_UP', 10, -2, 5, 'R_WORM', 'RED'),
       ('IHZ_LEAK', 12, 2, 'LEAK', 'R_LEAK', 'GOLD'), ('IHZ_SNIPER', 12, 1, 'SNIPER', 'R_SNIPER', 'RED'), ('IHZ_TUNNEL', 12, 1, 'TUNNEL', 'R_TUNNEL', 'WHITE'),
       ('IHZ_MAG', 12, 1, 'MAG', 'R_MAG', 'GOLD'), ('IHZ_VENTS', 12, 2, 'VENTS', 'R_VENTS', 'RED'), ('IHZ_METEORS', 12, 1, 'METEORS', 'R_METEOR', 'GOLD'),
       ('IHZ_EVAC', 12, 1, 'EVAC', 'R_EVAC', 'RED')]
