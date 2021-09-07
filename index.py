import random

class menu:
    def menu_1():
        m1 = input('''
        -------------------------------
        1  - Bloodstained Chivalry
        2  - Gladiator's Finale
        3  - Wanderer's Troupe
        4  - Pale Flame
        5  - Thundering Fury
        6  - Viridescent Venerer
        7  - Archaic Petra
        8  - Crimson Witch of Flames
        9  - Noblesse Oblige
        10 - Blizzard Strayer
        11 - Heart of Depth
        12 - Glacier and Snowfield
        13 - Retracing Bolide
        14 - Thundersoother
        15 - Lavawalker
        16 - Maiden Beloved
        17 - Tenacity of the Millelith
        18 - Shimenawa's Reminiscence
        19 - Emblem of Severed Fate

        0  - Exit
        -------------------------------
        
        ''')

        if m1 == '':
            m1 = 0

        return int(m1)

    def menu_2():
        m2 = input('''
        -------------------------------
        1  - Flower of Life
        2  - Plume of Death
        3  - Sands of Eon
        4  - Goblet of Eonothem
        5  - Circlet of Logos
        
        0  - Exit
        -------------------------------
        
        ''')

        if m2 == '':
            m2 = 0

        return int(m2)

class RNG:
    def test(m1,m2):

        art = -1
        Set=(
            "Bloodstained Chivalry",
            "Gladiator's Finale",
            "Wanderer's Troupe",
            "Pale Flame",
            "Thundering Fury",
            "Viridescent Venerer",
            "Archaic Petra",
            "Crimson Witch of Flames",
            "Noblesse Oblige",
            "Blizzard Strayer",
            "Heart of Depth",
            "Glacier and Snowfield",
            "Retracing Bolide",
            "Thundersoother",
            "Lavawalker",
            "Maiden Beloved",
            "Tenacity of the Millelith",
            "Shimenawa's Reminiscence",
            "Emblem of Severed Fate",
        )
        Art=(
            "Flower of Life",
            "Plume of Death",
            "Sands of Eon",
            "Goblet of Eonothem",
            "Circlet of Logos"
        )
        art=m2-1
        if art == 0:
            Stt = 'HP_'
        elif art == 1:
            Stt = 'ATK_'
        elif art == 2:
            stt=[
                'HP%',
                'DEF%',
                'ATK%',
                'ER',
                'EM'
            ]
            Stt=random.choice(stt)
        elif art == 3:
            stt=[
                'HP%',
                'ATK%',
                'DEF%',
                'Phy DMG',
                'Ele DMG',
                'EM'
            ]
            x=random.choice(stt)
            if x == 'Ele DMG':
                Ele_DMG=[
                    'Pyro DMG',
                    'Eletro DMG',
                    'Hydro DMG',
                    'Cryo DMG',
                    'Geo DMG',
                    'Anemo DMG'
                ]
                Stt=random.choice(Ele_DMG)
            else:
                Stt=x
        else:
            stt=[
                'HP%',
                'DEF%',
                'ATK%',
                'EM',
                'CR',
                'CD',
                'HB'
            ]
            Stt=random.choice(stt)

        print(Set[m1-1] + '\n' + Art[m2-1]+ '\n' +Stt)

    def Sub_Stat():
        art_sub=[
            ['HP_', 209,239,269,299],
            ['HP%', 4.1,4.7,5.3,5.8],
            ['ATK_',14,16,18,19],
            ['ATK%',4.1,4.7,5.3,5.8],
            ['DEF_',16,19,21,23],
            ['DEF%',5.1,5.8,6.6,7.3],
            ['EM',  16,19,21,23],
            ['ER',  4.5,5.2,5.8,6.5],
            ['CR',  2.7,3.1,3.5,3.9],
            ['CD',  5.4,6.2,7.0,7.8],
        ]
        for x in random.sample(art_sub,4):
            print(x)