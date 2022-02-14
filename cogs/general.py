import nextcord
from nextcord.ext import commands
import placeholder_config as config

botver = "Placeholder-Chan v1.1"

async def get_dev(self):
    dev = self.bot.get_user(config.owner)

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f":ping_pong: Pong! **{self.bot.latency * 1000:.0f}**ms")

    @commands.command()
    async def pong(self, ctx):
        await ctx.send(f":ping_pong: Ping! **{self.bot.latency * 1000:.0f}**ms")

    @commands.command(pass_context=True, aliases=['sauce', 'i', 'info'])
    async def sources(self, ctx, *, arg):
        chars={
            'ajit': 'Metal Ajit Pai',
            'ajit pai': 'Metal Ajit Pai',
            'metal ajit pai': 'Metal Ajit Pai',
            '1': 'Metal Ajit Pai',
            '01': 'Metal Ajit Pai',
            'geno': 'Geno',
            '2': 'Geno',
            '02': 'Geno',
            'oth': 'Off the Hook ft. Paruko',
            'off the hook': 'Off the Hook ft. Paruko',
            'off the hook ft. paruko': 'Off the Hook ft. Paruko',
            'off the hook ft paruko': 'Off the Hook ft. Paruko',
            'paruko': 'Off the Hook ft. Paruko',
            '3': 'Off the Hook ft. Paruko',
            '03': 'Off the Hook ft. Paruko',
            'weird al': 'Weird Al',
            'al': 'Weird Al',
            'weird al yankovic': 'Weird Al',
            '4': 'Weird Al',
            '04': 'Weird Al',
            'pitbull': 'Pitbull',
            'aliens': 'Pitbull',
            'the aliens': 'Pitbull',
            'pitbull and the aliens': 'Pitbull',
            '5': 'Pitbull',
            '05': 'Pitbull',
            'nintendo power': 'Nintendo Power',
            'reggie': 'Nintendo Power',
            'bill': 'Nintendo Power',
            '6': 'Nintendo Power',
            '06': 'Nintendo Power',
            'mib': 'Men in Black',
            'men in black': 'Men in Black',
            '7': 'Men in Black',
            '07': 'Men in Black',
            'zun': 'ZUN',
            '8': 'ZUN',
            '08': 'ZUN',
            'thanos': 'Thanos',
            '9': 'Thanos',
            '09': 'Thanos',
            'wario': 'Wario Partners',
            'waluigi': 'Wario Partners',
            'wario partners': 'Wario Partners',
            'wario partners llp': 'Wario Partners',
            'wario partners, llp': 'Wario Partners',
            '10': 'Wario Partners',
            'ddd': 'King Dedede',
            'dedede': 'King Dedede',
            'king dedede': 'King Dedede',
            '11': 'King Dedede',
            'snake': 'Solid Snake',
            'solid snake': 'Solid Snake',
            '12': 'Solid Snake',
            'djpk': 'DJ Professor K',
            'professor k': 'DJ Professor K',
            'k': 'DJ Professor K',
            'dj professor k': 'DJ Professor K',
            '13': 'DJ Professor K',
            'quote': 'Quote',
            '14': 'Quote',
            'adam': 'Adam Levine',
            'adam levine': 'Adam Levine',
            '15': 'Adam Levine',
            'johnny': 'Johnny Bravo',
            'johnny bravo': 'Johnny Bravo',
            '16': 'Johnny Bravo',
            'krabs': 'Mr. Krabs',
            'mr krabs': 'Mr. Krabs',
            'mr. krabs': 'Mr Krabs',
            '17': 'Mr. Krabs',
            'mariya': 'Mariya Takeuchi',
            'mariya takeuchi': 'Mariya Takeuchi',
            '18': 'Mariya Takeuchi',
            'robotnik': 'Dr. Robotnik',
            'eggman': 'Dr. Robotnik',
            'dr. robotnik': 'Dr. Robotnik',
            'dr robotnik': 'Dr. Robotnik',
            '19': 'Dr. Robotnik',
            'daft punk': 'Daft Punk ft. Pharrell',
            'pharrell': 'Daft Punk ft. Pharrell',
            'daft punk ft pharrell': 'Daft Punk ft. Pharrell',
            'daft punk ft. pharrell': 'Daft Punk ft. Pharrell',
            '20': 'Daft Punk ft. Pharrell',
            'papyrus': 'Papyrus',
            '21': 'Papyrus',
            'jack & elmo': 'Jack & Elmo',
            'jack black': 'Jack & Elmo',
            'elmo': 'Jack & Elmo',
            '22': 'Jack & Elmo',
            'piccolo': 'Dr. Piccolo',
            'dr piccolo': 'Dr. Piccolo',
            'dr. piccolo': 'Dr. Piccolo',
            '23': 'Dr. Piccolo',
            'jack bros': 'Jack Bros.',
            'jack bros.': 'Jack Bros.',
            'jack frost': 'Jack Bros.',
            'mothman': 'Jack Bros.',
            '24': 'Jack Bros.',
            'jack': 'which jack',
            'hobart': 'HOBaRT',
            '25': 'HOBaRT',
            'rhythm masters': 'Rhythm Masters',
            '26': 'Rhythm Masters',
            'nico nico': 'Nico Nico',
            'nico': 'Nico Nico',
            '27': 'Nico Nico',
            'dk': 'Donkey Kong',
            'donkey kong': 'Donkey Kong',
            'expand dong': 'Donkey Kong',
            '28': 'Donkey Kong',
            'missingno': 'MissingNo.',
            'missingno.': 'MissingNo.',
            '29': 'MissingNo.',
            'jazz cats': 'The Jazz Cats',
            'the jazz cats': 'The Jazz Cats',
            '30': 'The Jazz Cats',
            'eminem': 'Eminem',
            '31': 'Eminem',
            'law & disorder': 'Law & Disorder',
            'l&o': 'Law & Disorder',
            'l&d': 'Law & Disorder',
            'phoenix': 'Law & Disorder',
            'phoenix wright': 'Law & Disorder',
            'monokuma': 'Law & Disorder',
            '32': 'Law & Disorder',
            'mr bean': 'Mr. Bean',
            'mr. bean': 'Mr. Bean',
            'meowth': 'Meowth',
            'uhc2': 'Unregistered HyperCam 2',
            'hypercam': 'Unregistered HyperCam 2',
            'unregistered hypercam 2': 'Unregistered HyperCam 2',
            'john': 'John Notwoodman',
            'wood man': 'John Notwoodman',
            'woodman': 'John Notwoodman',
            'notwoodman': 'John Notwoodman',
            'john notwoodman': 'John Notwoodman',
            'nice': 'John Notwoodman',
            'nice >:]': 'John Notwoodman',
            'nice >:3]': 'John Notwoodman',
            'etika': 'Etika',
            'desmond amofah': 'Etika',
            'desmond': 'Etika',
            'amofah': 'Etika',
            'joyconboyz': 'Etika',
            'coraline': 'Coraline',
            'marrow': 'Coraline',
            'fighting placeholder team': 'Fighting Placeholder Team',
            'fpt': 'Fighting Placeholder Team',
            'placeholder': 'which placeholder',
            'placeholder team': 'Fighting Placeholder Team',
            'placeholder man': 'Placeholder Man',
            'placeholder-man': 'Placeholder Man',
            'placeholder-chan': 'Placeholder-Chan',
            'placeholder chan': 'Placeholder-Chan',
            'cool meme team': 'Cool Meme Team',
            'cmt': 'Cool Meme Team',
            'big chungus': 'Cool Meme Team',
            'ugandan knuckles': 'Cool Meme Team',
            'crash': 'Cool Meme Team',
            'crash bandicoot': 'Cool Meme Team',
            
        }.get(arg.lower(), arg)
        if chars == 'which jack':
            return await ctx.send(':question: Did you mean **Jack & Elmo** or **Jack Bros.**? Please specify and try again.')
        elif chars == 'which placeholder':
            return await ctx.send(':question: Did you mean **Fighting Placeholder Team**, **Placeholder Man**, or **Placeholder-Chan**? Please specify and try again.')
        elif chars == 'Metal Ajit Pai':
            char_name = '#01 - Metal Ajit Pai'
            elim = "Metal Ajit Pai lost to Nico Nico in Round 1. He beat Adam Levine in Round 1 of the Loser's Bracket, and was eliminated by Wario Partners, LLP in Round 2."
            champ = None
            desc = 'After his crushing defeat in the last tournament, Ajit Pai, now a sentient pile of dust, comes back with a vengeance… and a giant mech sponsored by Reese’s® peanut butter. Armed with a massive Nerf gun and fidget spinner, he is equipped to rule the Internet with an iron fist… and, of course, finally make his dreams of a Harlem Shakeover a reality.'
            sauces = 'Rips featuring Ajit Pai-related memes\nMecha-related rips\nRips featuring latency (such as slow internet)'
            examples = "*Harlem Shake* by Baauer, the *Reese's Puffs* rap, fidget spinners\n*Gundam* franchise, *Neon Genesis Evangelion*, *Tengen Toppa Gurren Lagann*, *Transformers* franchise\n*Online Practice Stage* from *Super Smash Bros. Brawl*"
            img = 'https://mojo.highquality.rip/wp-content/uploads/2019/08/metal-ajit-pai.png'
            note = None
        elif chars == 'Geno':
            char_name = '#02 - Geno'
            desc = "Returning from the stars, Geno blasts back into action! This denizen of Star Road has once again sensed his calling at this gathering of powerful rivals, and this time around, he’s brought lots of jams from a certain “higher authority” — let’s wish upon a star that this extra help will boost him straight to the crown!"
            elim = "Geno lost to “Weird Al” Yankovic in Round 1. He was eliminated by Johnny Bravo in Round 1 of the Loser's Bracket."
            champ = None
            sauces = 'Rips featuring songs composed by Yoko Shimomura\nRips featuring music from *Super Mario RPG* and the *Paper Mario* and *Mario & Luigi* series'
            examples = '*Kingdom Hearts* series, *Street Fighter II*'
            img = 'https://mojo.highquality.rip/wp-content/uploads/2019/08/geno.png'
            note = None
        elif chars == 'Off the Hook ft. Paruko':
            char_name = '#03 - Off the Hook ft. Paruko'
            desc = "After a respectable second place finish in the last tournament, Off the Hook are looking to wow the crowd once more with an encore performance! Marina and Pearl are once again joined by Paruko, bringing her chiptune-rock flair to the stage. With their talents combined, these seaborn superstars are more motivated than ever to claim their turf on the throne once and for all!"
            elim = "Off the Hook ft. Paruko lost to King Dedede in Round 1. They were eliminated by Mariya Takeuchi in Round 1 of the Loser's Bracket. They were the first characters eliminated."
            champ = None
            sauces = 'Rips featuring songs from the *Splatoon* franchise\nRips featuring “God of ink”\nArrangements done in a *Splatoon* style'
            examples = '*Ebb & Flow*, *The Girl From Inkopolis*, *Octarmaments*, *Fly Octo Fly*'
            img = 'https://mojo.highquality.rip/wp-content/uploads/2019/06/off-the-hook-ft-paruko.png'
            note = "Paruko was previously known under the stage name “Glenna Nalira” but has opted to return to using her real name."
        elif chars == 'Weird Al':
            char_name = '#04 - “Weird Al” Yankovic'
            desc = "After his first-round loss in the last tournament, “Weird Al” Yankovic has returned for seconds! His burning desire for victory has manifested into a stand called 「BEAT IT」, which allows him to use the musical powers of the King of Pop himself in battle — hopefully, he’ll be the king of this tournament, too!"
            elim = "“Weird Al” Yankovic beat Geno in Round 1, beat Wario Partners, LLP in Round 2, and lost to Law & Disorder in Round 3. Yankovic beat Johnny Bravo in Round 4 of the Loser's Bracket, and was eliminated by Mariya Takeuchi in Round 5."
            champ = None
            sauces = 'Rips featuring songs Weird Al has composed or parodied\nRips featuring music by Michael Jackson'
            examples = '*Eat It*, *White & Nerdy*, *Dare to Be Stupid*, *Albuquerque*\n*Thriller*, *Billie Jean*, *Smooth Criminal*\nMusic from *Sonic 3 & Knuckles*'
            img = 'https://mojo.highquality.rip/wp-content/uploads/2019/09/weird-al-yankovic.png'
            note = None
        elif chars == 'Pitbull':
            char_name = '#05 - Pitbull and the Aliens'
            desc = "Mr. Worldwide is back, and this time, he’s got dancers to back him up! YEEEEOOOOO! Pitbull, Popoy, and Marcianito have overcome both controversy and heartbreak in order to make their return to this tournament, and they hope that their newfound alliance will bring the adoring masses the Hispanic flavor they don’t know they need. There will be two li’l aliens and Mr. 305 checking in for this remix. Dale!"
            elim = "Pitbull and the Aliens lost to Solid Snake in Round 1. They were eliminated by Thanos in Round 1 of the Loser's Bracket."
            champ = None
            sauces = 'Rips featuring songs by Pitbull (or songs he features on\nRips featuring songs by El Chombo or Antonio Rios\nRips featuring cumbia, reggaeton, or 2000s Latin pop music'
            examples = '*DJ Got Us Fallin’ in Love*, *Feel This Moment*\n*Dame tu Cosita*, *Nunca me Faltes*, *Chaccaron Maccaron*, *Yo me Estoy Enamorando*\n*Livin’ la Vida Loca*, *El Sonidito*, *Hips Don’t Lie*'
            img = 'https://mojo.highquality.rip/wp-content/uploads/2019/09/pitbull-and-the-aliens-v2r2.png'
            note = None
        elif chars == 'Nintendo Power':
            char_name = '#06 - Nintendo Power'
            desc = "No one’s body is ready for the true might of Nintendo Power! After Reggie retired, Miyamoto decided Reggie needed a boost from inside the company, and Bill Trinen is the perfect match. Now that these two gaming industry legends have brought their Joy-Cons together, this tournament has truly been switched on!"
            elim = "Nintendo Power beat HOBaRT in Round 1, and lost to DJ Professor K in Round 2. They were eliminated by Dr. Robotnik in Round 2 of the Loser's Bracket."
            champ = None
            sauces = 'Rips featuring music from the *Animal Crossing*, *The Legend of Zelda*, and *Wii* franchises (excluding *Wii Music*)\nRips featuring music from the *Fire Emblem* and *Xenoblade* franchises\nRips featuring music from Nintendo system software and presentations'
            examples = '*Mor Ardain 〜Roaming the Wastes〜*, songs by K.K. Slider\n*Wii Sports*, *Wii Play*, *Wii Fit*\nMusic from the *Nintendo eShop*, Wii channels, *Nintendo Direct* jingles'
            img = 'https://mojo.highquality.rip/wp-content/uploads/2019/09/Nintendo-Power.png'
            note = None
        elif chars == 'Men in Black':
            char_name = '#07 - Men in Black'
            desc = "It’s rewind time! Agent J (played by Will Smith) and Howard the Alien are here to investigate alien activity! Facing all-new threats they’ve never seen before — and a few that they definitely have — the pair will need the best of the best of MIB tech to turn their opponents into slime. Neuralyzers in hand, they will stop at nothing to keep the public safe from all extraterrestrial threats… except for Howard. He’s cool."
            elim = "The Men in Black lost to Daft Punk ft. Pharrell in Round 1. They were eliminated by Dr. Robotnik in Round 1 of the Loser's Bracket."
            champ = None
            sauces = 'Rips featuring aliens\nRips related to Will Smith\nRips featuring music by Lil Uzi Vert'
            examples = '*Metroid* series, *Half-Life* series, *Pikmin* series\n*The Fresh Prince of Bel-Air* soundtrack, *Wild Wild West*, *Gettin’ Jiggy wit It*\n*Money Longer*, *Bad and Boujee*, *XO Tour Llif3*'
            img = 'https://mojo.highquality.rip/wp-content/uploads/2019/11/mib-temp2.png'
            note = None
        elif chars == 'ZUN':
            char_name = '#08 - ZUN'
            desc = "With his imperishable love for alcohol, and his influences on his sleeve (along with the rest of his shirt), ZUN is ready to re-enter the tournament! He’s the embodiment of bullet heck with music that spans across the entire bullet hell genre. Anybody who crosses his path better be prepared for a carousel of agony!"
            elim = "ZUN beat Quote in Round 1, and lost to Law & Disorder in Round 2. He was eliminated by Mariya Takeuchi in Round 2 of the Loser's Bracket."
            champ = None
            sauces = 'Rips featuring songs composed by ZUN\nRips featuring music related to the *Touhou* franchise (including fan projects)\nRips featuring music from games in the bullet hell genre\nRips related to alcohol'
            examples = '*Beloved Tomboyish Daughter*, *Lunatic Eyes ~ Invisible Full Moon*\n*Hate not the Wind*, *Spring Blossoms*, *Far-East El Dorado*\n*DonPachi*, *Ikaruga*, *ESCHATOS*, *Radiant Silvergun*\n*U Was At The Club (Bottoms Up)*, *Tipsy*, *songs by Alestorm*, *VA-11 Hall-A: Cyberpunk Bartender Action*'
            img = 'https://mojo.highquality.rip/wp-content/uploads/2019/10/zun.png'
            note = None
        elif chars == 'Thanos':
            char_name = '#09 - Thanos'
            desc = "With the newfound power of Disney behind him, Thanos re-enters the fight! After the previous tournament upset the balance of the universe, this Deviant once again seeks to restore it. Gauntlet on his fist and mouse cap on his head, the Mad Titan is prepared to win the tournament, and, of course, celebrate by going to Disneyland with those sweet half-length lines — there is only a 1 in 14,000,605 chance that he won’t!"
            elim = "Thanos lost to Dr. Piccolo in Round 1. He beat Pitbull and the Aliens in Round 1 of the Loser's Bracket, and was eliminated by Donkey Kong in Round 2."
            champ = None
            sauces = 'Rips featuring music from *Marvel* properties\nRips featuring music from the Disnet animated canon and theme parks\nRips featuring music from *Walt Disney Pictures* and *Pixar* movies\nRips featuring music from *Star Wars*\nRips featuring *Fireflies* by Owl City'
            examples = '*The Avengers* theme, music from the *Guardians of the Galaxy* soundtracks\n*When You Wish Upon a Star*, *Hakuna Matata*, *Let it Go*\n*It’s a Small World*, *Grim Grinning Ghosts*\n*Cantina Band*, *Han Solo and the Princess*, *Duel of the Fates*'
            img = 'https://mojo.highquality.rip/wp-content/uploads/2019/09/THANOS-PORTRAIT.png'
            note = None
        elif chars == 'Wario Partners':
            char_name = '#10 - Wario Partners, LLP'
            desc = "Wario’s successful game development company has set the business world on fire, and a strategic partnership with a certain street food business has created the corporate merger of the century: Wario Partners, LLP! They’re wasting no time diversifying — now in addition to making games, they’re kicking ass and taking names. And thus, their first order of business: win that tournament and get all that sweet free advertising! Wahaha!"
            elim = "Wario Partners, LLP beat Johnny Bravo in Round 1, and lost to “Weird Al” Yankovic in Round 2. They beat Metal Ajit Pai in Round 2 of the Loser's Bracket, and were eliminated by Mariya Takeuchi in Round 3."
            champ = None
            sauces = 'Rips featuring music from *Wario* games\nRips featuring music from the *Mario Land* games and other Mario spin-offs (excluding *Super Mario RPG* and its descendants)'
            examples = '*Greenhorn Forest*, *Hurry Up!*, *Its-all Mine*\n*Muda Kingdom*, *Star Maze*\n*Coconut Mall*, *This Way That*, *Creative Exercise*'
            img = 'https://mojo.highquality.rip/wp-content/uploads/2019/08/wario-partners-llp.png'
            note = None
        elif chars == 'King Dedede':
            char_name = '#11 - King Dedede'
            desc = "After his loss in the last tournament, King Dedede has decided it’s time to reveal his secret weapons… his brand-new Dedede Hammer, and a cool mask to boot! He’s once again determined to win the right to truly call himself a king… and ready to eat his way through our entire tournament budget, too. Asshole."
            elim = "King Dedede beat Off the Hook ft. Paruko in Round 1, and lost to Jack Bros. in Round 2. He was eliminated by Papyrus in Round 2 of the Loser's Bracket."
            champ = None
            sauces = 'Rips featuring boss themes and other songs from the *Kirby* series'
            examples = '*Moonstruck Blossom*, *0²*, *The Greatest Warriot in the Galaxy*\n*Ripple Star*, *Iceberg*, the *Kirby: Right Back At Ya!* theme song'
            img = 'https://mojo.highquality.rip/wp-content/uploads/2019/06/masked-dedede.png'
            note = None
        elif chars == 'Solid Snake':
            char_name = '#12 - Solid Snake'
            desc = "Kept you waiting, huh? Solid Snake makes his miraculous return to the field of battle! He seems to have snatched a stylish outfit on his way here, and it’s a look only he could pull off. His weapons are also fully-loaded this time around! Get out there and show them what you’re made of, Snake! No regrets!"
            elim = "Solid Snake beat Pitbull and the Aliens in Round 1, and lost to Dr. Piccolo in Round 2. He was eliminated by Rhythm Masters in Round 2 of the Loser's Bracket."
            champ = None
            sauces = 'Rips from any franchise Hideo Kojima has worked on\nBox-related rips'
            examples = '*Metal Gear* series, *Silent Hill* series, *Castlevania* series\n*Snatcher*, *Zone of the Enders*, *Boktai: The Sun Is in Your Hand*\n*BOXBOY!* series, *Squeeze Box* by The Who, *Heart-Shaped Box* by Nirvana'
            img = 'https://mojo.highquality.rip/wp-content/uploads/2019/10/kept-u-waitin-huh.png'
            note = None
        elif chars == 'DJ Professor K':
            char_name = '#13 - DJ Professor K'
            desc = "He’s back, and he’s on the Up-Set Attack! The Professor has re-entered the building, and this time he’s brought his whole crew along for the ride! The Noise Tanks of this competition better watch out, because DJ Professor K is ready to enact his revenge with power grooves that will rock your soul!"
            elim = None
            champ = "DJ Professor K is the SiIvaGunner: King for Another Day Tournament Champion. He was never dropped to the Loser's Bracket. He won against MissingNo. in Round 1, Nintendo Power in Round 2, Dr. Piccolo in Round 3, Daft Punk ft. Pharrell in Round 4, Law & Disorder in Winner's Finals, and Mariya Takeuchi in the final battle. His channel takeover began on June 29th, 2020, and ended on July 7th, 2020."
            sauces = 'Rips featuring music from any SEGA game outside of the *Sonic* and *Puyo Puyo* series\nRips featuring music by or in the style of Hideki Naganuma (includes *Sonic Rush*)'
            examples = 'Songs from the *Jet Set Radio*, *Super Monkey Ball*, and *Sega Rally* series\n*Get It 2 Win It*, *LUV CAN SAVE U*, *AIN’T NOTHING LIKE A FUNKY BEAT*\nSongs from *Daytona USA*, *Space Channel 5*, *NiGHTS into Dreams...*, *Phantasy Star Online*\nSongs from the original *Bayonetta*, and the *Yakuza* series and its spinoffs'
            img = 'https://mojo.highquality.rip/wp-content/uploads/2019/06/dj-professor-k.png'
            note = None
        elif chars == 'Quote':
            char_name = '#14 - Quote'
            desc = "Huzzah! Quote is here, and he’s ready for this new adventure to begin! He may be silent, but his trusty Polar Star sure isn’t. Armed with that and music from classic indie platformers, nothing is going to stop him from claiming his rightful place as the king of indie games!"
            elim = "Quote lost to ZUN in Round 1. He was eliminated by Papyrus in Round 1 of the Loser's Bracket."
            champ = None
            sauces = 'Rips featuring music from games developed by Studio Pixel\nRips related to franchises published by Nicalis\nRips featuring music from classic indie platformers (2010 or earlier)'
            examples = '*Cave Story*, *Ikachan*, *Kero Blaster*\n*VVVVVV*, *The Binding of Isaac* series\n*Super Meat Boy*, *Spelunky*, *Braid*, *Within a Deep Forest*, *An Untitled Story*'
            img = 'https://mojo.highquality.rip/wp-content/uploads/2019/10/quote.png'
            note = None
        elif chars == 'Adam Levine':
            char_name = '#15 - Adam Levine'
            desc = "Invite received from on high, Adam Levine aims for the lead! Actually, at first, he wanted to be one of the judges for the tournament, but after he failed the interview by disapproving every contestant, we had to deny him such a position. Nonetheless, with his stubborn attitude and his Jagger-esque moves, he certainly isn’t messing around in, what he wishes was his, tournament."
            elim = "Adam Levine lost to The Jazz Cats in Round 1. He was eliminated by Metal Ajit Pai in Round 1 of the Loser's Bracket."
            champ = None
            sauces = 'Rips related to Maroon 5 or to current/former members of Maroon 5\nRips featuring 90s alternative rock music'
            examples = 'Songs by Square (James Valentine’s old band), Phantom Planet (Sam Farrar’s old band)\n90s songs by Pearl Jam, The Cardigans, Red Hot Chili Peppers, Weezer'
            img = 'https://mojo.highquality.rip/wp-content/uploads/2019/10/adam-levine.png'
            note = None
        elif chars == 'Johnny Bravo':
            char_name = '#16 - Johnny Bravo'
            desc = "Whoa, mama! Johnny Bravo steps into the ring, along with his charm, dance moves, dashingly good looks, and all the music from his fellow Cartoon Network superstars he could carry with him. (And, to be fair, that’s a lot; check the pecs!) Of course, he doesn’t care about the crown itself — he’s just in it because he knows he’ll easily get the adoration of all the women in the audience… or, at least, that’s what he thinks, anyway."
            elim = "Johnny Bravo lost to Wario Partners, LLP in Round 1. He beat Geno in Round 1 of the Loser's Bracket, Nico Nico in Round 2, and Papyrus in Round 3, and was eliminated by “Weird Al” Yankovic in Round 4."
            champ = None
            sauces = 'Rips featuring music from Cartoon Network original properties\nRips featuring music from Hanna-Barbera shows that have aired on Cartoon Network (excluding *The Flintstones* and *The Jetsons*)'
            examples = 'The *Johnny Bravo* theme\nMusic from the *Scooby-Doo* franchise\n*Adventure Time* songs\nCN bumper music like *Powerhouse* and the *Cartoon Cartoons* theme'
            img = 'https://mojo.highquality.rip/wp-content/uploads/2019/06/johnny-bravo.png'
            note = None
        elif chars == 'Mr. Krabs':
            char_name = '#17 - Mr. Krabs'
            desc = "Mr. Eugene H. Krabs has found great success as owner of the world-renowned Krusty Krab, but couldn’t pass up a chance to promote his business further… and a shot at that expensive looking crown! This crustaceous cheapskate’s greed knows no bounds; just don’t tell him that we don’t actually offer a cash prize."
            elim = "Mr. Krabs beat Dr. Robotnik in Round 1, and lost to Daft Punk ft. Pharrell in Round 2. He was eliminated by MissingNo. in Round 2 of the Loser's Bracket."
            champ = None
            sauces = 'Rips related to the *SpongeBob SquarePants* franchise\nPirate-themed rips\nRips related to crabs\nRips related to money'
            examples = '*Sweet Victory*, *Electric Zoo*, *Stadium Rave A*\nSea shanties, songs by Alestorm, music from *Pirates of the Caribbean*\n*Crab Rave*, *1NF3$+@+!0N*\n*Whales* by Hail Mary Mallon, *Money for Nothing* by Dire Straits'
            img = 'https://mojo.highquality.rip/wp-content/uploads/2019/06/mr-krabs.png'
            note = None
        elif chars == 'Mariya Takeuchi':
            char_name = '#18 - Mariya Takeuchi'
            desc = "Mariya Takeuchi, creator of the hit song “Plastic Love,” has made her way into the battle! Born in 1955, she is one of the oldest fighters on the roster, but we highly recommend that you don’t underestimate her. They say her music has the power to control the algorithm of life itself…"
            elim = "Mariya Takeuchi lost to Jack Bros. in Round 1. She beat Off the Hook ft. Paruko in Round 1 of the Loser's Bracket, ZUN in Round 2, Wario Partners, LLP in Round 3, Jack & Elmo in Round 4, and The Jazz Cats in Round 5. She proceeded to defeat MissingNo. in the Loser's Finals, and ultimately was eliminated by DJ Professor K in the final battle. She is a runner-up and she received a runner-up reward in the form of a [fusion collab](https://www.youtube.com/watch?v=Ulk_jBm5jCg)."
            champ = None
            sauces = 'Rips featuring music by Mariya Takeuchi...\n...or her husband, Tatsuro Yamashita\nRips related to/in the genres of *city pop* and *future funk*'
            examples = '*Plastic Love*, *Yume no Tsuzuki*, *Shiawase no Monosashi*\n*Ride on Time*, *Love talkin ‘honey it’s you’*, *Magic Ways*\n*Urusei Yatsura* opening/ending songs, *MACROSS 82-99* tracks'
            img = 'https://mojo.highquality.rip/wp-content/uploads/2019/06/mariya.png'
            note = None
        elif chars == 'Dr. Robotnik':
            char_name = '#19 - Dr. Robotnik'
            desc = "Snooping as usual, Dr. Robotnik invades the tournament! With his hands on that crown, Robotnik may finally be able to fulfill his dream of ruling Mobius, and capture that heinous hedgehog he hates so much… or at least he thinks. However, if he truly wants a chance to be king, he will have to give himself a promotion!"
            elim = "Dr. Robotnik lost to Mr. Krabs in Round 1. He beat the Men in Black in Round 1 of the Loser's Bracket, beat Nintendo Power in Round 2, and was eliminated by Rhythm Masters in Round 3."
            champ = None
            sauces = 'Rips featuring music from any *Sonic* cartoon before *Sonic X*\nRips featuring music from any *Sonic* game on a SEGA console (and *Sonic Mania*)\nRips featuring music from the *Puyo Puyo* series\nClassic-style YTP/edits that feature Dr. Robotnik'
            examples = 'VIDEOS CONTAINING WIN\n*Dr. Robotnik’s Mean Bean Machine* music\nRobotnik’s theme from *Adventures of Sonic the Hedgehog*'
            img = 'https://mojo.highquality.rip/wp-content/uploads/2019/06/dr-robotnik.png'
            note = None
        elif chars == 'Daft Punk ft. Pharrell':
            char_name = '#20 - Daft Punk ft. Pharrell'
            desc = "Like the legend of the phoenix, Daft Punk and Pharrell have risen up to the challenge! Thomas and Guy-Manuel have gotten some new gear, and they invited Skateboard P himself to help them out with the fight. With music of their own as well as from their friends at Ed Banger Records, they plan to win the tournament as swiftly as a gust of wind!"
            elim = "Daft Punk ft. Pharrell beat Men in Black in Round 1, Mr. Krabs in Round 2, and Jack & Elmo in Round 3. They lost to DJ Professor K in Round 4, and were eliminated by MissingNo. in Round 6 of the Loser's Bracket."
            champ = None
            sauces = 'Rips featuring music by *Daft Punk*\nRips featuring music by *Pharrell Williams* or *N.E.R.D.*, or music that includes him as a feature\nRips featuring vocoded vocals\nRips related to the *Despicable Me* franchise\nRips featruring music by artists signed to Ed Banger Records and other songs in the French Touch genre'
            examples = '*Get Lucky*, *Lose Yourself to Dance*, *Gust of Wind*\n*Harder Better Faster Stronger*, *Robot Rock*, *One More Time*\n*Happy*, *Frontin’*, *It Girl*\n*Baby I’m Yours*, *Waters of Nazareth*, *Music Sounds Better With You*'
            img = 'https://mojo.highquality.rip/wp-content/uploads/2019/09/Daft-Punk-ft.-Pharrell.png'
            note = None
        elif chars == 'Papyrus':
            char_name = '#21 - Papyrus'
            desc = "Nyeh heh heh! Everyone’s favorite soon-to-be member of the Royal Guard has put his human-hunting quest aside to join the competition! Equipped with his staple “battle body”, Papyrus will surely cook up a pasta dish that will trounce even the most fearsome opponents."
            elim = "Papyrus lost to Law & Disorder in Round 1. He beat Quote in Round 1 of the Loser's Bracket and King Dedede in Round 2, and was eliminated by Johnny Bravo in Round 3."
            champ = None
            sauces = 'Rips featuring Papyrus himself\nRips featuring music from puzzle games\nRips featuring music related to skeletons\nRips related to pasta'
            examples = '*Bonetrousle*, *Dating Start/Fight*, *Snowdin*\nSongs from *Skeleton Boomerang*, *Grim Fandango*, and *Mr. Bones*\n*Tetris: Type A*, Songs from the Picross series\n*Unfounded Revenge*'
            img = 'https://mojo.highquality.rip/wp-content/uploads/2019/06/papyrus-undertale.png'
            note = None
        elif chars == 'Jack & Elmo':
            char_name = '#22 - Jack & Elmo'
            desc = "Hey, how’s it going? He’s Jack, and with his friend Elmo, he’s going to educate the tournament on the magic of octagons! Complete with a stop sign and great tunes, Jack and Elmo will stop at nothing to become the kings of this tournament."
            elim = "Jack & Elmo beat Rhythm Masters in Round 1, and Donkey Kong in Round 2. They lost to Daft Punk ft. Pharrell in Round 3, and were eliminated by Mariya Takeuchi in Round 4 of the Loser's Bracket."
            champ = None
            sauces = 'YTPMVs of Jack Black, especially clips of his appearances on Sesame Street\nRips featuring music from Sesame Street and The Muppets\nRips featuring music by Tenacious D or otherwise related to Jack Black\nRips related to edutainment games'
            examples = '*Elmo’s World*, *Rubber Ducky*, *The Muppet Show* theme\n*Tribute*, *The Metal*, *Pick of Destiny*, songs from *Brutal Legend*\n*Brain Age*, games by *Humongous Entertainment*, *Math Blaster*, *Mario’s Time Machine*'
            img = 'https://mojo.highquality.rip/wp-content/uploads/2019/06/jack-and-elmo.png'
            note = None
        elif chars == 'Dr. Piccolo':
            char_name = '#23 - Dr. Piccolo'
            desc = "Dedicated to his cause, this Namekian medical genius has stepped up to spread his miracle cure across the globe. He won’t stop until he’s brought about the change he wants to see in the world — and as a side effect, his efforts will be bringing the power of anime to the entire tournament audience. Thanks, Doc!"
            elim = "Dr. Piccolo beat Thanos in Round 1, Solid Snake in Round 2, and lost to DJ Professor K in Round 3. He was eliminated by MissingNo. in Round 4 of the Loser's Bracket."
            champ = None
            sauces = 'Rips related to medical practices\nRips featuring *Green & Purple* by Kritikal\nRips featuring music from anything related to Shonen Jump'
            examples = '*Dragon Ball*, *My Hero Academia*, *JoJo’s Bizarre Adventure*, *Naruto*, *Yu-Gi-Oh!*\n*Dr. Mario*, *Trauma Center*, *Surgeon Simulator*'
            img = 'https://mojo.highquality.rip/wp-content/uploads/2019/09/dr-piccolo.png'
            note = None
        elif chars == 'Jack Bros.':
            char_name = '#24 - Jack Bros.'
            desc = "He may be small, he may melt under even the slightest bit of heat, and he may ho, but Jack Frost sure isn’t going to melt under this pressure. Armed with some weak Bufu skills, his pal Mothman’s piercing gaze, and just a couple of Life Stones to their names, they’re ready to give this contest a shot. Today the Shinjuku underground, tomorrow the world!"
            elim = "Jack Bros. beat Mariya Takeuchi in Round 1 and King Dedede in Round 2. They were defeated by The Jazz Cats in Round 3 and eliminated by Rhythm Masters ih Round 4 of the Loser's Bracket."
            champ = None
            sauces = 'Rips featuring music from games developed or published by Atlus'
            examples = 'Songs from *Megami Tensei* and its sequels/spinoffs, including *Persona* and *Devil Survivor*\nSongs from the *Etrian Odyssey*, *Trauma Center*, *Power Instinct*, and *Growlanser* series\nSongs from *Catherine*, *Radiant Historia*, *Odin Sphere*, or *BlaZeon*'
            img = 'https://mojo.highquality.rip/wp-content/uploads/2019/06/jack-bros.png'
            note = None
        elif chars == 'HOBaRT':
            char_name = '#25 - HOBaRT'
            desc = "Looking for the perfect contestant to stir things up a little bit? No problem! Our state of the art Hyper Operative Baking and Ripping Technology, or “HOBaRT” for short, comes straight from Australia with the power and durability to mix both the toughest doughs and the highest quality rips. Built to withstand any challenge that comes its way — HOBaRT is unstoppable."
            elim = "HOBaRT lost to Nintendo Power in Round 1, and was eliminated by MissingNo. in Round 1 of the Loser's Bracket."
            champ = None
            sauces = 'Rips featuring music related to or from Australia\nRips featuring cooking or food-related music\nRips featuring Hobart\nRips featuring music by Lil Jon'
            examples = '*Cooking by the Book* (LazyTown), songs from *Cooking Mama*\n*Down Under* by Men at Work, music from *Crash Bandicoot*\n*Hobart Drive* by Jerry Galeries'
            img = 'https://mojo.highquality.rip/wp-content/uploads/2019/08/hobart.png'
            note = None
        elif chars == 'Rhythm Masters':
            char_name = '#26 - Rhythm Masters'
            desc = "Brought together through the power of bangers, Hakuko and Don-chan set their sights on a perfect full combo all the way to the crown title. Whether it be by twisting knobs, tapping keys, or swiping at a washing machine, this duo can conquer any rhythmic challenge! Get ready for the ultimate tournament beatdown deluxe version, ta-don!"
            elim = "Rhythm Masters lost to Jack & Elmo in Round 1. They beat Eminem in Round 1 of the Loser's Bracket, Solid Snake in Round 2, Dr. Robotnik in Round 3, and Jack Bros. in Round 4. They were eliminated by MissingNo. in Round 5."
            champ = None
            sauces = 'Rips featuring music from rhythm games\nRips featuring music by artists with frequent appearances in rhythm games'
            examples = '*Dreams of Our Generation*, *Mausoleum Mash*, *Xepher*, *Brain Power*, *FREEDOM DIVE*\nSongs by Camellia, Sakuzyo, Shinji Hosoe (sampling masters MEGA)'
            img = 'https://mojo.highquality.rip/wp-content/uploads/2019/08/rhythm-masters.png'
            note = None
        elif chars == 'Nico Nico':
            char_name = '#27 - Nico Nico'
            desc = "Coming all the way from Japan, Nico Nico enters the battle! Don’t get too close to Terebi-chan, as many devious tricks are hidden behind the cute face on its screen. The voice samples it emits are just a small sample of the toolset this little television has prepared for the tournament. With the sounds of Miku, Aniki, and many more, this contestant is ready to win the crown and go MAD with power!"
            elim = "Nico Nico beat Metal Ajit Pai in Round 1 and lost to The Jazz Cats in Round 2. It was eliminated by Johnny Bravo in Round 2 of the Loser's Bracket."
            champ = None
            sauces = 'Rips featuring sources popular on *Nico Nico Douga*\nRips featuring music from popular late-2000s anime'
            examples = '*Inmu*, *Ippon Manzoku*, *Promise*, *Dance Robot Dance*, *Cheetahmen 2*\nIOSYS’ well-known Touhou remixes, e.g. *Cirno’s Perfect Math Class* or *Overdrive*\n*Fuwa Fuwa Time*, *Hare Hare Yukai*, *Luka Luka★Night Fever*'
            img = 'https://mojo.highquality.rip/wp-content/uploads/2019/09/nico-nico.png'
            note = None
        elif chars == 'Donkey Kong':
            char_name = '#28 - Donkey Kong'
            desc = "Here he comes, banana slamma! Straight from the hit CGI television series, Donkey Kong swings into action. He’s bigger, faster, and stronger than ever, and ready to prove himself ready to rule the isle of Kongo Bongo. With a sourcelist featuring all the awesome music from his TV show and more, he’s sure to take advantage of this rare opportunity!"
            elim = "Donkey Kong beat Eminem in Round 1 and lost to Jack & Elmo in Round 2. He beat Thanos in Round 2 of the Loser's Bracket, and was eliminated by MissingNo. in Round 3."
            champ = None
            sauces = 'Rips featuring music from the *Donkey Kong Country* cartoon and *Donkey Kong* games\nRips featuring music from pre-Microsoft RareWare games\nRips featuring monkey-related music'
            examples = '*Nobody’s Hero*, *Metal Head*, *I’m Gonna Be a Star*\nSongs from *Battletoads*, *Banjo-Kazooie*, *Conker’s Bad Fur Day*\nSongs from *Ape Escape*, *Bloons Tower Defense*; *Adventure of a Lifetime* by Coldplay'
            img = 'https://mojo.highquality.rip/wp-content/uploads/2019/09/Donkey-Kong.png'
            note = None
        elif chars == 'MissingNo.':
            char_name = '#29 - MissingNo.'
            desc = "Its legendary abilities spoken of in hushed tones on playgrounds all over the world, MissingNo. is joining the SiIvagunner King for Another Day Tournament. MissingNo. is bringing into the tournament the signature [REDACTED] it’s well known for, and with no doubt will try its very best to fly through the bracket, soaking all those who stand in its way in the process!"
            elim = "MissingNo. lost to DJ Professor K in Round 1. It beat HOBaRT in Round 1 of the Loser's Bracket, Mr. Krabs in Round 2, Donkey Kong in Round 3, Dr. Piccolo in Round 4, Rhythm Masters in Round 5, Daft Punk ft. Pharrell in Round 6, and was defeated by Mariya Takeuchi in the Loser's Finals. It is one of the runner-ups and is due to receive a runner-up prize, though it is still unknown what that prize will be."
            champ = None
            sauces = 'Rips featuring glitches, corruptions, and exploits, or of games particularly notable for glitches\nRips featuring unused content\nRips featuring music associated with gaming creepypasta\nRips featuring Glitch Hop and IDM music'
            examples = '*Sonic the Hedgehog (2006)*, *Big Rigs: Over the Road Racing*\n*calm4.ogg* from Minecraft, *Hidden Palace Zone* from Sonic 2\n*Sonic.exe*, *Ben Drowned*, *Petscop*'
            img = 'https://mojo.highquality.rip/wp-content/uploads/2019/09/MissingNo..png'
            note = None
        elif chars == 'The Jazz Cats':
            char_name = '#30 - The Jazz Cats'
            desc = "Sights set on winning, the Jazz Cats join the jam! Shades is ready to cut the competition with his nasty bebop licks. Milk Bowl is preparing the dirtiest chord you’ve ever heard. And sphelonious donk. These three felines will whip out any tune in the Real Book just to taste the catnip of victory."
            elim = "The Jazz Cats beat Adam Levine in Round 1, Nico Nico in Round 2, and Jack Bros. in Round 3. They were beaten by Law & Disorder in Round 4 and eliminated by Mariya Takeuchi in Round 6 of the Loser's Bracket."
            champ = None
            sauces = 'Jazz arrangements\nRips featuring jazz standards\nRips featuring modern jazz/funk\nRips featuring music related to cats'
            examples = '*‘Round Midnight*, *Don’t Get Around Much Anymore*, *So What* (Miles Davis)\nsongs by Louis Cole, Vulfpeck, Hiatus Kaiyote\n*The Lion Sleeps Tonight*, *Eye of the Tiger*, songs by Cat Stevens, The Pussycat Dolls\nThe Lick'
            img = 'https://mojo.highquality.rip/wp-content/uploads/2019/09/The-Jazz-Cats.png'
            note = None
        elif chars == 'Eminem':
            char_name = '#31 - Eminem'
            desc = "The real Slim Shady stands up to claim his rightful place as King! Sure, it may feel like a step down from Em’s former title of Rap God, but he needs all the publicity he can get to promote his new single called My Salsa. Decked out in his finest bullfighter attire, Marshall is not afraid to stir up a little controversy. And if you don’t like it… FUCK YOU."
            elim = "Eminem lost to Donkey Kong in Round 1. He was eliminated by Rhythm Masters in Round 1 of the Loser's Bracket."
            champ = None
            sauces = 'Rips featuring songs written, performed, or majorly sampled by Eminem\nRips featuring songs by rappers who Eminem has frequently collaborated with\nRips done in a salsa, flamenco, or mariachi style'
            examples = '*Without Me*, *The Real Slim Shady*, *My Name Is*\n*Dream On* by Aerosmith, *Thank You* by Dido\n*The Next Episode* by Dr. Dre\n*In Da Club* by 50 Cent\n*My Band* by D12 and Eminem’s brand new single, *My Salsa*'
            img = 'https://mojo.highquality.rip/wp-content/uploads/2019/09/Eminem.png'
            note = None
        elif chars == 'Law & Disorder':
            char_name = '#32 - Law & Disorder'
            desc = "Men of mystery Phoenix Wright and Monokuma have formed an unlikely partnership! [Mr. Bean](https://youtu.be/yxTvYwodMvg) has been attacked, Maya Fey has been framed, and it’s once again up to Phoenix Wright to defend his friend. With the help of the mischievous Monokuma, somehow also tangled up in this case, can they get the turnabout while also fighting for the crown?"
            elim = "Law & Disorder beat Papyrus in Round 1, ZUN in Round 2, “Weird Al” Yankovic in Round 3, The Jazz Cats in Round 4, and was eliminated by DJ Professor K in the Winner's Finals. They are a runner-up and are due to receive their runner-up prize. It was teased during the SiIvaSummer All-Star Festival in a [trailer for LAW & DISORDER: TURNABOUT DISPAIR](https://www.youtube.com/watch?v=wfPF-dAZcms)."
            champ = None
            sauces = 'Rips featuring music from the *Ace Attorney* and *Danganronpa* series\nRips featuring music from other mystery-based games\nRips related to mysteries and court cases'
            examples = 'The *Professor Layton* series, *L.A. Noire*, *Heavy Rain*, *Ghost Trick: Phantom Detective*\nTheme from *The People’s Court*, *Gravity Falls*, *Mystery Skulls*'
            img = 'https://mojo.highquality.rip/wp-content/uploads/2019/09/Law-and-Disorder.png'
            note = None
        elif chars == 'Mr. Bean':
            char_name = 'Bonus - Mr. Bean'
            desc = "~~Mr. Bean bumbles his way into the tournament! Representing British comedy and beans, you’ll have no words for the things this man can accomplish!~~\n\nNOTE: It turns out that Mr. Bean entered himself into the competition without anyone’s knowledge or express permission, and furthermore, [he has been grievously injured](https://www.youtube.com/watch?v=XFIjjIzoQrQ), and thus will not actually be participating. Please accept our humble apologies."
            champ = None
            elim = None
            sauces = 'Music from media starring Rowan Atkinson\nMusic associated with British comedy\nMusic associated with Green de la Bean'
            examples = '*Mr. Bean*, the *Johnny English* films, *Rat Race*\n*Monty Python*, *Wallace and Gromit*\n*U Guessed It*, *No Words*'
            img = 'https://mojo.highquality.rip/wp-content/uploads/2019/06/mr-bean.png'
            note = 'Bonus characters will not participate in the tournament, but will be able to receive arrangements.'
        elif chars == 'Meowth':
            char_name = 'Bonus - Meowth'
            desc = "That’s right! The talkative Scratch Cat Pokémon himself chimes in as the official interviewer of the King for Another Day Tournament! Taking a much-needed break from his misadventures with Team Rocket, he, alongside last year’s tournament winner Unregistered HyperCam 2, is here on the scene, interviewing all 32 contestants and asking them questions peppered with attitude. Make sure you don’t make him angry though, or Pay Day’s coming early!"
            champ = None
            elim = None
            sauces = None
            examples = None
            img = 'https://mojo.highquality.rip/wp-content/uploads/2019/11/meowth.png'
            note = 'Bonus characters will not participate in the tournament, but will be able to receive arrangements.'
        elif chars == 'Unregistered HyperCam 2':
            char_name = 'Bonus - Unregistered HyperCam 2'
            desc = "henlo mojo 2day i will show u how 2 become the host of king for another day. after winning last tournament that john guy let me host this one so ill b helping out with interviews n stuff every now and then. if u liked this mojo post pls r8 5 stars and subscribe thx 4 reading"
            champ = None
            elim = None
            sauces = None
            examples = None
            img = 'https://mojo.highquality.rip/wp-content/uploads/2019/11/unregisteredhypercam2.png'
            note = 'Bonus characters will not participate in the tournament, but will be able to receive arrangements.'
        elif chars == 'John Notwoodman':
            char_name = 'Bonus - John Notwoodman'
            desc = "The esteemed and very nice >:3] CEO of King for a Day Tournament Enterprises once more lends the tournament his daunting presence! Though he has passed hosting duties off to Unregistered HyperCam 2, he will still be around to announce all matches in his signature reverberating voice, and will crown the one most fearsome challenger the King\* for a Day!\n\n(\*or Kings, or Queen, or Queens, or Queen and King… or, uh… H-HOBaRT?)"
            champ = None
            elim = None
            sauces = None
            examples = None
            img = 'https://mojo.highquality.rip/wp-content/uploads/2019/11/john-notwoodman.png'
            note = 'Bonus characters will not participate in the tournament, but will be able to receive arrangements.'
        elif chars == 'Etika':
            char_name = 'Bonus - Etika'
            desc = "Desmond Amofah, more commonly known as Etika, was a YouTuber known for creating live streams, reaction videos, let's plays, and other video game-related content. His reaction videos have since become a minor meme on the SiIvaGunner channel. His YouTube channel, followed by his social media accounts, were removed on October 26, 2018. He then owned a new channel under the name of EtikaFRFX, which was removed as well on April 16, 2019. Finally, he owned two channels being TR1Iceman from his old channel and E Live for livestreams. \n\n Etika went missing on June 19, 2019. His death was confirmed on June 25. \n\n Etika was a competitor in the first King for a Day Tournament. He was selected by the SiIvaGunner Backroom, and [received a tribute rip](https://www.youtube.com/watch?v=domi1RZ-ydA) as part of the King for Another Day Tournament."
            champ = None
            elim = None
            sauces = None
            examples = None
            img = 'https://mojo.highquality.rip/wp-content/uploads/2019/12/ETIKAMojo.png'
            note = 'Bonus characters will not participate in the tournament, but will be able to receive arrangements. \n\n This character has no official description associated with them. This description is neither written nor endorsed by the SiIvaGunner team, and was taken from the SiIvaGunner Wiki page.'
        elif chars == 'Coraline':
            char_name = 'Bonus - Coraline'
            desc = "Coraline is a character from the StreetPass Mii Plaza game Ultimate Angler. She was commonly used as a profile picture by former SiIvaGunner backroom member Marrow, who sadly passed away on June 17th, 2019. Marrow loved the game Ultimate Angler, and so the National Go Fishing Day event was held as a tribute to him, and the King for Another Day Tournament was dedicated to him and Etika."
            champ = None
            elim = None
            sauces = None
            examples = None
            img = 'https://mojo.highquality.rip/wp-content/uploads/2019/12/Coraline.png'
            note = 'Bonus characters will not participate in the tournament, but will be able to receive arrangements. \n\n This character has no official description associated with them. This description is neither written nor endorsed by the SiIvaGunner team, and was written by the developer of the bot, PrincessLillie.'
        elif chars == 'Fighting Placeholder Team':
            char_name = 'Bonus - Fighting Placeholder Team'
            desc = "Fighting Placeholder Team is a team composed of Placeholder Man and Placeholder-Chan. It's believed Placeholder Man was used in the original King for a Day Tournament as a size reference for the artists. Placeholder-Chan was added in the King for Another Day Tournament, and the team [got a rip](https://www.youtube.com/watch?v=q2N_a0-TjSs)."
            champ = None
            elim = None
            sauces = None
            examples = None
            img = 'https://mojo.highquality.rip/wp-content/uploads/2019/08/fighting-placeholder-team.png'
            note = 'Bonus characters will not participate in the tournament, but will be able to receive arrangements. \n\n This character has no official description associated with them. This description is neither written nor endorsed by the SiIvaGunner team, and was written by the developer of the bot, PrincessLillie.'
        elif chars == 'Placeholder Man':
            char_name = 'Bonus - Placeholder Man'
            desc = "Placeholder Man is one half of Fighting Placeholder Team. It's believed he was used in the original King for a Day Tournament as a size reference for the artists. He was added into a team with Placeholder-Chan and [got a rip](https://www.youtube.com/watch?v=q2N_a0-TjSs) as part of the King for Another Day Tournament."
            champ = None
            elim = None
            sauces = None
            examples = None
            img = 'https://mojo.highquality.rip/wp-content/uploads/2019/08/placeholder-man.png'
            note = 'Bonus characters will not participate in the tournament, but will be able to receive arrangements. \n\n This character has no official description associated with them. This description is neither written nor endorsed by the SiIvaGunner team, and was written by the developer of the bot, PrincessLillie.'
        elif chars == 'Placeholder-Chan':
            char_name = 'Bonus - Placeholder-Chan'
            desc = "It's me, Placeholder-Chan! I'm half of Fighting Placeholder Team with the lovely Placeholder Man, and we were bonus characters in the King for Another Day Tournament! We even [got a rip](https://www.youtube.com/watch?v=q2N_a0-TjSs) as part of it!"
            champ = None
            elim = None
            sauces = None
            examples = None
            img = 'https://mojo.highquality.rip/wp-content/uploads/2019/08/placeholder-chan.png'
            note = 'Bonus characters will not participate in the tournament, but will be able to receive arrangements. \n\n This character has no official description associated with them. This description is neither written nor endorsed by the SiIvaGunner team, and was written by the developer of the bot, PrincessLillie.'
        elif chars == 'Cool Meme Team':
            char_name = 'Bonus - Cool Meme Team'
            desc = "Cool Meme Team is a team composed of Crash Bandicoot, Big Chungus, and Ugandan Knuckles. They were introduced in the fake-out [Beta Mix of the SiIvaGunner: King for Another Day Direct](https://www.youtube.com/watch?v=BYVytP-43_M) and were never intended to be actual characters, but ended up gaining traction in the fanbase and getting actual content (rips and MOJO!! posts) when the tournament began, making them qualify as bonus characters."
            champ = None
            elim = None
            sauces = None
            examples = None
            img = 'https://mojo.highquality.rip/wp-content/uploads/2019/11/The-Cool-Meme-Team-Updated-Art.png'
            note = 'Bonus characters will not participate in the tournament, but will be able to receive arrangements. \n\n This character has no official description associated with them. This description is neither written nor endorsed by the SiIvaGunner team, and was written by the developer of the bot, PrincessLillie.'
        else:
            return await ctx.send(f":x: I couldn't find a character by that name. Check your spelling and try again.")
        if desc == None:
            embed = nextcord.Embed(title=":information_source: Information for " + char_name, color=0xff9823)
        else:
            embed = nextcord.Embed(title=":information_source: Information for " + char_name, description=desc, color=0xff9823)
        if champ == None:
            pass
        else:
            embed.add_field(name="CHAMPION", value=champ, inline=False)
        if elim == None:
            pass
        else:
            embed.add_field(name="ELIMINATED", value=elim, inline=False)
        if sauces == None:
            pass
        else:
            embed.add_field(name="Sources", value=sauces, inline=False)
        if examples == None:
            pass
        else:
            embed.add_field(name="Examples", value=examples, inline=False)
        if note == None:
            pass
        else:
            embed.add_field(name="Note", value=note, inline=False)
        embed.set_thumbnail(url=img)
        embed.set_footer(text="Requested by " + ctx.author.name + "#" + ctx.author.discriminator + " - " + botver + " by PrincessLillie#2523", icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)

    @commands.command()
    async def links(self, ctx):
        emb1 = nextcord.Embed(title="SiIvaGunner: King for Another Day Tournament MOJO!!", url='https://mojo.highquality.rip', description="On the MOJO!!, you will find interviews, character information, and other content related to the King for Another Day Tournament.", color=0x7289da)
        emb1.set_thumbnail(url='https://mojo.highquality.rip/wp-content/themes/mojo/logo.png')
        emb1.set_footer(text="Requested by " + ctx.author.name + "#" + ctx.author.discriminator + " - " + botver + " by PrincessLillie#2523", icon_url=ctx.author.avatar.url)
        emb2 = nextcord.Embed(title="SiIvaGunner - YouTube", url='https://youtube.com/SiIvaGunner', description="I only upload high quality video game rips. Please read the channel description.", color=0x7289da)
        emb2.set_thumbnail(url='https://vignette.wikia.nocookie.net/siivagunner/images/e/e9/SiivaGunner_post-strike.png/revision/latest?cb=20190301022411')
        emb2.set_footer(text="Requested by " + ctx.author.name + "#" + ctx.author.discriminator + " - " + botver + " by PrincessLillie#2523", icon_url=ctx.author.avatar.url)
        await ctx.send(embed=emb1)
        await ctx.send(embed=emb2)
        
    @commands.command(aliases=['kfadinfo'])
    async def kfad(self, ctx):
        embed = nextcord.Embed(title=":question: What is King for Another Day?", url='https://mojo.highquality.rip/what-is-king-for-another-day/', description="The SiIvaGunner: King for Another Day Tournament was an event in which characters battled it out to become the host of SiIvaGunner for a day! It was the sequel to the original King for a Day Tournament, but with double the roster size, and double the excitement! The 32 characters ranged from famous video game icons, to cartoon characters, and even real life musicians and figures, each one bringing their own flair with their variety of audio and music sources. It was up to the viewers to push for what they wanted to hear! \n\n As the tournament progressed, original musical arrangements for every fighter were uploaded to SiIvaGunner. If the viewer liked the sound of a certain fighter, they could vote for them once voting opened for their matchup! The winner of each individual match was decided by popularity vote, and would move on to the next round of the bracket, while the loser is defeated. This time around, however, there was a loser’s bracket! This meant that fighters who met their end early could still have a chance to come back.\n\n Only one victor could reign over all. Once a winner was decided, they would receive their own respective event day, filled with high-quality rips based on their assigned source list! Unlike the first King for a Day, all four of the finalists would get prizes, including the king! \n\n The SiIvaGunner: King for Another Day Tournament was organized and held by the YouTube channel SiIvaGunner. It started on November 23rd, 2019, and ended on January 8th, 2020. DJ Professor K was the winner.", color=0x5a5a5a)
        embed.set_image(url='https://sks316.s-ul.eu/8QgGqUa1.png')
        embed.set_footer(text="Requested by " + ctx.author.name + "#" + ctx.author.discriminator + " - " + botver + " by PrincessLillie#2523", icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def help(self, ctx):
        embed = nextcord.Embed(title=botver, description="The command prefix is `p-`. To run a command, you must begin a message with `p-`.", color=0x7289da)
        embed.add_field(name="KFAD:", value="**p-sources** - Provides the source list for a specified character, among other information. Aliases: **p-i**, **p-info**\n**p-kfad** - Provides information about King for Another Day: What it is and who made it. Aliases: **p-kfadinfo**\n**p-links** - Posts links that may (or may not) be useful.", inline=False)
        embed.add_field(name="Other:", value="**p-botinfo** - See information about the bot, such as its uptime.\n**p-ping** - Returns the bot's latency. Aliases: **p-pong**\n**p-bug** - Submit a bug report if anything goes wrong. \n**p-suggest** - Want to see something added to the bot? Suggest it!", inline=False)
        embed.set_footer(text=botver + " by PrincessLillie#2523", icon_url=self.bot.user.avatar.url)
        await ctx.message.author.send(embed=embed)
        await ctx.message.add_reaction("✅")

def setup(bot):
    bot.add_cog(General(bot))
