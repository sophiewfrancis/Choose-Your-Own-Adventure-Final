"""The functions necceessary for doing my project."""

user_facts = []
other_facts= []
cont_list = []

import sys
import pytest
# used to make output more readable and more like a game
from colorama import Fore
from colorama import Style

# in a few cases, the use of functions is more to organize the whole thing, than to actually utilize the structure of a function
ans1 = input ('Would you like to play a game? (yes/no) ')

# game is it's own function, so that if user wants to play again, it can restart the whole game
def game ():   
    
    """Launches the game
    
    Parameters
    ----------
    none
    
    Returns
    -------
    none
    """
    # slow_down function makes it so the code won't continue until the user types something, so that it doesn't print too many lines of code at once
    def slow_down():
        
        """Allows user to control the pace of the game
        
        Parameters
        ----------
        none
        
        Returns
        -------
        cont_list: list
            allows cont_list to be called later and use to run player_info
            
        """

        slower = input ('')
        
        cont_list.append (slower)
        
        while slower is not None:
            break
            
        return cont_list
        
    def feedback (): 
        
        """Asks player for feedback on the game
        
        Parameters
        -----------
        none
        
        Returns
        --------
        none
        """
        input ('What did you think of the game?')

        print ('Thanks for the feedback!')
        sys.exit()
        


    def player_info ():
        
        """Establishes basic info about the player
        
        Parameters
        ----------
        none
        
        Returns
        -------
        user_facts: list
            stores information about the player to be referenced later
        
        other_facts:
            stores more information about the player to be referenced later
        """

        name = input ("\n\nWhy don't you tell me a little about yourself then? What is your name? ")
        user_facts.append (name) 
        gender = input ('\nHello there ' + name + '.' + ' What is your gender? (male/female/nonbinary) ')
        if gender.lower().strip() == 'male':
        # I use lower and strip with each variable so that everything still works if the user uses capitals or accidentally has punctuation. Consistent throughout game
            casualref = 'guy'

        elif gender.lower().strip() == 'female':        
            casualref = 'girl'

        elif gender.lower().strip() == 'nonbinary':
            casualref = 'person'

        user_facts.append (gender)
        other_facts.append (casualref) 
        age = input ('\nGood to know! How old are you, '+ name + '? ')

        if int (age) >= 18:
            status= 'not a minor'

        elif int (age)< 18:
            status = 'minor'

        other_facts.append (status) 
        user_facts.append(int(age)) 
        
        print ("\n\nSome Useful Instructions: \n-Black Text is narration \n-You'll meet another character while playing \n-" + Fore.RED + "Red Text is them talking")
        print (Style.RESET_ALL +"-" + Fore.BLUE + 'Blue Text is you (the player) talking' + Style.RESET_ALL + '\n-'+Fore.GREEN + "Green Text is a third character talking" )
        print (Style.RESET_ALL + "-When given an empty input box, type anything to continue \n-Have fun!")
        print (Style.RESET_ALL+ "-When given two options, type your selection exactly as it appears") 
        
        slow_down()
        
        print ('\n\nAlright, '+ name + ' , '+ "let's get started.")
        # created user_facts as a list of important user info that will need to be called upon later
        return user_facts
        return other_facts
    
    if cont_list is not None:
        player_info()
    # condition is after function is defined so that it runs as written, this is consistent throughout game

  




    def play_again ():
        
        """allows user to play game again if they reach an ending
        
        Parameters
        ----------
        none
        
        Returns
        --------
        none
        """

        play = input ('Would you like to play again? (yes/no) ')

        if play.lower().strip() == 'yes':
            game()

        elif play.lower().strip() == 'no':
            print ('Goodbye then!')
            feedback()       




    def basic_info ():
        
        """establishs basic info about the storyling
        PARAMETERS
        ----------
        none
        
        RETURNS
        -------
        none
        
        """

        print ("\n\n\n\nIt's May 25, 2020, and for some reason, you're being marched to your prison cell.") 
        slow_down()
        print (Fore.BLUE +"\nMom would kill me if she found out about this"+ Style.RESET_ALL+ " you thought to yourself." )
        print ("\nBut the last thing you wanted right now was to get on anybody's bad side, so you kept your head down and stayed silent.")
        slow_down()
        print ("\nYou had never been good with directions, so eventually the left and right turns blurred and you zoned out until the clanking of bars broke you from your trance.") 
        slow_down()
        print (Fore.GREEN +"\nGet in." + Style.RESET_ALL+ " The surly guard didn't wait for compliance before tossing you into the cell. You stumbled inside and heard the door slam behind you.")
        print (Fore.GREEN+"\nSilence will get you far in here kid, already doing well." +Style.RESET_ALL+  " The guard laughed as he stalked off.")
        slow_down()
        print ("\n\nYou barely had time to sit on your sorry excuse for a bed when you hear a soft knock on the wall to your right." + Fore.RED +"\nHey new " + other_facts[0] + '!' + " Over here!"+Style.RESET_ALL)

        talk = (input (Style.RESET_ALL +'\n\nDo you want to talk to them? (yes/no) '))

        if talk.lower().strip() == 'no':
            print (Style.RESET_ALL + "\n\n\n\n\nENDING ONE: The Introvert.\nYou're going to try and do the whole prison thing alone? Good luck. Try and make some friends next time.")
            play_again()

    
        elif talk.lower().strip() == 'yes':
            print (Style.RESET_ALL +"\n\nYou decide to talk to your neighbor.")
            slow_down()
            print (Fore.BLUE+"\nRight here, what's up?") 
            print (Fore.RED + "\nNo way! I can't believe it! That cell's been empty for months! What are you in here for?" +Style.RESET_ALL)


    if user_facts is not None:
        basic_info()




    def which_crime():
        
        """allows user to choice which crime they committed, enhances storyline
         
        PARAMETERS
        ----------
        none
        
        RETURNS
        -------
        user_facts: list
            stores information about the player to be referenced later
        """ 
            
        if other_facts[1] == 'minor':
            crime = input (Style.RESET_ALL+ "\n\n" + user_facts[0] + ', '+ 'what did you do to end up in prison?' +Style.RESET_ALL + ' (loitering/possession of drugs) ')
                # narrator is asking to user
        else:
            crime = input (Style.RESET_ALL + "\n\n" + user_facts[0] + ' , '+ 'what did you do to end up in prison?' +Style.RESET_ALL + ' (loitering/vehicular manslaughter) ')

        user_facts.append(crime) 

        return user_facts

    if basic_info is not None:
        which_crime()




    def loitering():
        
        """dialogue to be used if user selects 'loitering' as crime
         
        PARAMETERS
        ----------
        none
        
        RETURNS
        -------
        none
        """ 

        print (Fore.RED+ "\n\nLoitering? That's it? Really? Something tells me that wouldn't put you in prison.")
        print (Style.RESET_ALL +"\nYou laughed, having thought the same thing.")
        slow_down()
        print (Fore.BLUE + "\nWell something tells me that whoever designed this game doesn't have much knowledge of prison and crimes. I'm just going to go with it.")

    if user_facts[3].lower().strip() == 'loitering':
        loitering ()




    def possession_of_drugs():
        
    # posession of drugs is only a crime option if user is under the age of 18
        """dialogue to be used if user selects 'possession of drugs' as crime
         
        PARAMETERS
        ----------
        none
        
        RETURNS
        -------
        none
        """ 

        print (Fore.RED + "\n\nOh boy, that's actually pretty serious. What did you have on you?" + Style.RESET_ALL + " They said curiously.")
        print (Fore.RED + "\nActually, you know what, don't tell me. Plausible deniability or whatever.")
        slow_down()
        print (Style.RESET_ALL + "\nYou just laugh."+Fore.BLUE+ " Yeah, something like that.")

    if user_facts[3].lower().strip()=='possession of drugs':
        possession_of_drugs()




    def vehicular_manslaughter():
    # vehicular manslaughter is only a crime option if user is 18 or older
    
        """dialogue to be used if user selects 'vehicular manslaughter' as crime
         
        PARAMETERS
        ----------
        none
        
        RETURNS
        -------
        none
        """ 

        print(Style.RESET_ALL+"\n\nYou hear a soft gasp come from the other side of the wall.")
        print (Fore.BLUE + "\nWould it make you feel any better if I told you it was an accident?")
        slow_down()
        print(Fore.RED + "\nTo be honest, not really.")

    if user_facts[3].lower().strip() == 'vehicular manslaughter':
        vehicular_manslaughter()




    def partner_info():
        
        """establishes information about your partner in the escape, based on your gender
         
        PARAMETERS
        ----------
        none
        
        RETURNS
        -------
        user_facts: list
        """ 

        print (Fore.BLUE +"\n\nI'm "+ user_facts[0] +',' + " by the way,"+Style.RESET_ALL+ " you offer.") 
        slow_down()
        print (Fore.BLUE + "\nWhat's your name? How long have you been here?")

        if user_facts[1] == 'male':
            print (Fore.RED +"\n\nI'm Damien, nice to meet you "+ user_facts[0] +". I've been here for a little over a year, got caught up in some tax evasion nonsense    last February.")
            part_name = 'Damien'

        elif user_facts [1] == 'female':
            print (Fore.RED +"\n\nI'm Amy, nice to meet you "+ user_facts[0] +". I've been here for a little over a year, got caught up in some tax evasion nonsense   last February.")
            part_name = 'Amy'

        elif user_facts [1 == 'nonbinary']:
            print (Fore.RED+"\n\nI'm Alex, nice to meet you "+ user_facts[0] +". I've been here for a little over a year, got caught up in some tax evasion nonsense last February.")
            part_name = 'Alex'
        # gender of partner is the same as user's own gender
        user_facts.append(part_name) 

        return user_facts


    if user_facts[3] is not None:
        partner_info()




    def idea():
    
        """dialogue to propose the idea of escaping
         
        PARAMETERS
        ----------
        none
        
        RETURNS
        -------
        none
        """ 

        ans2 = input (Fore.RED+"\n\nI know this may sound crazy, but I've been dreaming about breaking out of this place for months. Do you think you'd want to try and escape with me? I know we just met, but I couldn't do it without you." +Style.RESET_ALL + " (yes/no) ")

        if ans2.lower().strip() == 'no':
            print (Style.RESET_ALL + "\n\n\n\n\nENDING TWO: The Coward. \nReally? You don't want to get out? That's too bad.")
            play_again ()
            user_facts.append (ans2)
            #appended ans2 to user_facts so that i can test this function
        elif ans2.lower().strip()== 'yes':
            print (Fore.RED+"\nNo way? Really?!")
            user_facts.append(ans2)
    if user_facts[4] is not None:
        idea()




    def escape():
        
        """starts the main part (the escape) of the game
         
        PARAMETERS
        ----------
        none
        
        RETURNS
        -------
        none
        """ 

        print (Fore.RED + "\n\nOkay, this may sound crazy, but I've been wanting to break out of here for years.")
        print (Fore.RED + "\nIt's already getting late, I think we should try tonight.")
        slow_down()
        print (Fore.BLUE + "\nTonight?!" +Style.RESET_ALL + " You said incredulously.")
        print ("\n" + user_facts [4] + " chuckled." + Fore.RED + " Yes tonight! Glad to hear you're on board.")


        dig_or_pick = input (Fore.RED +"\n\nOkay, we have two basic options here. We can try and dig our way out, or I can show you how to pick a lock. Which one do you want to try?" +Style.RESET_ALL+ " (dig out/pick lock) ")

        if dig_or_pick.lower().strip() == 'dig out':
            print (Fore.RED + "\nYou want to dig out? Good plan.")
            dig_tool = input ("\nWhat do you want to try and use? You could maybe steal a spoon from the cafeteria, or you could get a rock hammer        smuggled in?"+ Style.RESET_ALL +" (spoon/hammer) ")

            if dig_tool.lower().strip() == 'spoon':
                print (Style.RESET_ALL + "\n\n\n\n\nENDING THREE: The Archeologist. \nDigging? Really? With a spoon? The floors are cement," + user_facts[0] + ". How did you think that would work?")
                play_again()

            elif dig_tool.lower().strip() == 'hammer':
                print (Style.RESET_ALL + "\n\n\n\n\nENDING SIXTEEN: The Shawshank. \nIf you don't get that reference, you should go watch The Shawshank Redemption starring Tim   Robbins and Morgan Freeman. Really good movie. But you can't dig your way out of this cell. Too Bad.")
                play_again()

        elif dig_or_pick.lower().strip() == 'pick lock':
            print (Fore.RED + "\n\nGood choice. If you go over to your bed, you may be able to find a loose screw you can use to jimmy the lock open.")
            print (Style.RESET_ALL + "\nSure enough, there was a narrow screw that was just loose enough that you could gently ease out of your bedframe.")
            slow_down()
            print (Style.RESET_ALL +"\nYou were able to slot this screw very carefully into the padlock of your door, and after surprisingly little effort,        the lock clicked open.")
            slow_down()
            print (Style.RESET_ALL +"\nYou stepped opened your door quietly, and saw " + user_facts[4] + " leaning up against the wall in between your cells.") 
            print (Fore.RED + "\nHigh security, huh.")
            slow_down()
            print (Style. RESET_ALL + "\n\nYou looked up and down the hallway, but couldn't see anything special at the end either direction.")
            print (Fore.BLUE + "\nNow what?" + Style.RESET_ALL + " You asked.")

            l_or_r = input (Fore.RED + "\n\nNow we pick a direction and hope. Which way do you want to go?" +Style.RESET_ALL +" (right/left) ")

        if l_or_r.lower().strip() == 'left':
            print (Fore.RED+ "\nLeft? Good choice.") 
            slow_down()
            print (Style.RESET_ALL + "\nThe two of you walk silently down the hallway to your left, both too scared to even breathe too heavily.")
            print (Style.RESET_ALL + "After barely making it 100 yards, " + user_facts[4] + " stops you.")
            slow_down()
            print (Fore.BLUE + "\nWhat's wrong?")
            print (Fore.RED + "\n\nShhhhh. There's a guard at the end of this hallway, see? It's just one so I think we can get past him, but I'm not sure how.")
            
            att_sneak = input (Fore.RED + "We could try and surprise him and attack, or we could try to create a diversion and sneak past. What do you think we should do?" +Style.RESET_ALL + " (attack/sneak) " )

            if att_sneak.lower().strip() == 'attack':
                print (Style.RESET_ALL + "\n\n\n\n\nENDING FOUR: The Assailant. \nYou decided to go out guns blazing. Against an armed prison guard. Good luck with that one.")
                play_again()

            elif att_sneak.lower().strip() == 'sneak':
                print (Fore.RED + "\n\nYeah, I definitely agree with that. Do you sill have that screw from your bed?")
                print (Style.RESET_ALL + "\nSuprisingly enough you were still clenching it in your fist.") 
                slow_down()
                print (Fore.BLUE + "\nI do, actually. Are we going to use a screw as a diversion?")
                print (Fore.RED + "\Oh yeah we are.")
                slow_down()
                print ("\n" +Style.RESET_ALL + user_facts[4]+ " grabbed the screw from your hand and pulled you into the shadows. You had barely figured out what was going to       happen before the screw was clattering on the ground and the guard had ran past to inspect it.")

        elif l_or_r.lower().strip() == 'right':
            print (Fore.RED+ "\nRight? Good choice.")
            slow_down()
            print (Style.RESET_ALL + "\nThe two of you walk silently down the hallway to your left, both too scared to even breathe too heavily.")
            print (Style.RESET_ALL + "\nAfter barely making it 100 yards, " + user_facts[4] +  " stops you.")
            slow_down()
            print (Fore.BLUE + "\nWhat's wrong?")
            print (Fore.RED + "\nShhhhh. There's a bunch of guards at the end of this hallway, see?") 
            slow_down()
            att_sneak2 = input (Fore.RED +"\n\nI bet we could get past them, but I'm not sure how. We could try and surprise them and attack, or we could try to create a diversion and sneak past. What do you think we should do?" +Style.RESET_ALL + " (attack/sneak) " )

            if att_sneak2.lower().strip() == 'attack':
                print (Style.RESET_ALL + "\n\n\n\n\nENDING FOUR: The Assailant. \nYou decided to go out guns blazing. Against armed prison guards. Good luck with that one.")
                play_again()

            elif att_sneak2.lower().strip() == 'sneak':
                print (Fore.RED + "\nYeah, I definitely agree with that. Do you sill have that screw from your bed?")
                print (Style.RESET_ALL + "\nSuprisingly enough you were still clenching it in your fist.") 
                slow_down()
                print (Fore.BLUE + "\nI do, actually. Are we going to use a screw as a diversion?")
                print (Fore.RED + "\nOh yeah we are.")
                slow_down()
                print ("\n" + Style.RESET_ALL + user_facts[4]+ " grabbed the screw from your hand and pulled you into the shadows. You had barely figured out what was going to happen   before the screw was clattering on the ground and the guard(s) had ran past to inspect it.")


        how_out = input (Fore.RED + "\n\nOkay, now we have a few options. We could either try to get out through the cafeteria, through the vents, or through the service tunnels under this place. Which do you think we should try?" + Style.RESET_ALL +" (cafeteria/vents/tunnels) ")

        if how_out.lower().strip() == 'cafeteria':
            print (Style.RESET_ALL + "\n\n\n\n\nENDING FIVE: The Socialite. It's the evening, and the janitorial crew is cleaning up the kitchen for the night. The two of you are immediately caught, and placed in solitary confinement. Maybe don't try one of the places that always has people in it." )
            play_again()

        elif how_out.lower().strip() == 'vents':
            print (Fore.RED + "\nGood idea. Coincidentally, there happens to be a vent opening right around this corner.")
            print (Fore.RED + "\nThank goodness there aren't more left or right turns to choose from in the way.")
            slow_down()
            print (Style.RESET_ALL + "\n\nWhen you approached the vent opening, it became immediately obvious that only one of you was going to fit in there at once. It was too small of an opening to go together.")
            print (Fore.RED + "\nYou know, I could probably get out of here quicker on good behavior, I'm already on their good side.")
            slow_down()      

            alone_tog = input (Fore.RED+"\n\nIf you want to go alone from here, I'll distract any other guards for you. Or you could always stay and we could try to figure out something else. What do you think?" +Style.RESET_ALL +" (go alone/stay together) ")

            if alone_tog.lower().strip() == 'stay together':
                print (Style.RESET_ALL +"\n\n\n\n\nENDING SIX: The Altruist. \nYou had your chance to make it out and you blew it. Brownie points for thinking about your friend, but that hesitation cost you your chance of escaping.")
                play_again ()

            elif alone_tog.lower().strip() == 'go alone':
                print ("\nYou decide to go alone, it will be faster that way, and you can always send someone back for " + user_facts[4] + " once you make it out.")
                print (Fore.RED +"\nGood luck, "+ user_facts[0]+ " you got this.")
                slow_down()
                print ("\n" + Style.RESET_ALL  + user_facts[4] + " helps you get the vent cover off, and you smile warmly before crawling in.")
                print (Style.RESET_ALL + "\nYou hear the cover slide back on behind you and the soft padding of footsteps and you know that you're on your own from here on out.")
                slow_down()

            print (Style.RESET_ALL + "\n\nYou had barely been squeezing your way through the vents for 3 minutes when you ran into a split.")

            lig_or_dark = input (Style.RESET_ALL + "\n\nDown the route to your left, there's a bright light, which could be coming from the outside, but you weren't sure. On the other side, the path is dark, and eerily silent. Which way are you going to go? (light/dark) ")

            if lig_or_dark.lower().strip() == 'light':
                print (Style.RESET_ALL +"\nYou go down the lighter path, hoping you've somehow already gotten to the exit. Unfortunately, the light was coming from the prison ward's office, that you are now kneeling right on top of.")
                print (Style.RESET_ALL + "\n\n\n\n\nENDING SEVEN: The Hopeful. \nThe well lit path had hope, but ended up dropping you right into the hands of the Big Kahuna. Good luck getting out on good behavior after that stunt.")
                play_again()

            elif lig_or_dark.lower().strip() == 'dark':
                print (Style.RESET_ALL +"\nEven though the dark path is worrying, you figure away from light is your best shot at avoiding people.")
                print (Style.RESET_ALL + "\nSoon, sunlight starts to fill the vent and you can start to see what's going on around you.")
                slow_down()


            print (Style.RESET_ALL + "\n\nYou had been crawling for quite some time before hitting the next fork.")
            creak_or_stable = input (Style.RESET_ALL +"\n\nThis time, you can see the horizon through one, you've almost made it out! But when you start to move that direction, the metal underneath you creaks and groans. The other way, you can't see a way out, but the bottom is firm and stable. Which way do you go? (short but creaky/long but stable) ")

            if creak_or_stable.lower().strip() == 'short but creaky':        
                print (Style.RESET_ALL +"\nYou decide to go with the shorter path, hoping that the floor will hold beneath you.")
                print (Style.RESET_ALL +"\nTesting it again, you wince at the squeak of the metal when you try to put weight on it.")
                slow_down()
                speed = input (Style.RESET_ALL +"\n\nYou could go slowly and risk getting caught, or go quickly to try get past the creaky part as soon as you can. What do you think you should do? (rush/slow) ")

                if speed.lower().strip() == 'rush':
                    print (Style.RESET_ALL +"\n\n\n\n\nENDING EIGHT: The Bull in a China Shop. \nYou go barrelling down the unsteady path, only to have one of the vent seams split underneath you. You crash down into a guards office. Good luck, " + user_facts[0] +".")
                    play_again()

                elif speed.lower().strip() == 'slow':
                    print (Style.RESET_ALL + "\nYou decide to slowly ease yourself down the pathway, and you make it to the end. You can see the recreation yard! Just a quick fence hop and you're out!")
                    print (Style.RESET_ALL + "\nWell, a quick fence hop, but before that there's a four story drop to the ground.")
                    print (Style.RESET_ALL +"\n\n\n\n\nENDING NINE: The Daredevil. \nYou attempt the jump, promptly breaking both of your legs. You won't be escaping from anywhere anytime soon.")
                    play_again()

            elif creak_or_stable.lower().strip() == 'long but stable':
                print (Style.RESET_ALL +"\nYou decide that if it's too good to be true it probably is, and you head down the longer, firmer vent route.")
                print (Style.RESET_ALL +"\nYou crawl for what feels like another eternity, and you start to notice the vent growing wider and wider, and gently sloping downwards.")
                slow_down()
                print (Style.RESET_ALL +"\nMore comfortable now, you pick up the pace, seeing light growing in the distance.")
                print (Style.RESET_ALL +"\nAfter a few more minutes, you approach what must be some sort of outdoor vent filter. You turn around and kick it out with your legs." )
                slow_down()
                print (Style.RESET_ALL +"\nThe filter easily clatters to the ground.")
                print (Fore.BLUE + "\nNo way." + Style.RESET_ALL + "You say aloud. You're only about seven feet off the ground, and in the distance you can see a security camera pointed in the exact opposite direction." + Fore.BLUE + "Maybe " + user_facts [4] + "did have your back.")
                        #************ENDING TEN*********
                print (Style.RESET_ALL + "\n\n\n\n\nENDING TEN: The Smooth Criminal. \nWith a small jump and a quick dig and shimmy under the fence, you're home free.")
                print ("\n\nCongratulations, " + user_facts[0] + "! You won the game!")
                play_again()       

        elif how_out.lower().strip() == 'tunnels':
            print (Fore.RED + "\nThe tunnels? Really? With all the sewage? No way you're getting me down there. You're on your own kid.")
            print (Fore.BLUE + "\nYou would seriously rather be in literal prison than get into some sewage? That's absurd.")
            slow_down()
            print (Fore.RED + "\nYeah, it's a no go from me. You can get into the tunnels by the weirdly placed indoor pothole around the corner. Best of luck, I'll be sure to cover for you if need be.")
            print (Style.RESET_ALL + "\n" +user_facts[4] + " nods at you before walking off and presumably returning to their cell. You turn and find the pothole, and struggle to get the lid off. Once you do, all you see is a rusty metal ladder leading into a dark pit.")
            slow_down()
            print (Fore.BLUE + "\n\nThis is disgusting " + Style.RESET_ALL + "you mutter to yourself.")
            print (Style.RESET_ALL + "As you descend down the ladder, the sound of running water grows louder and louder.")
            slow_down()     
            print (Style.RESET_ALL + "Sure enough, when you hop off the last rung you land in ankle deep running water. Thank god its too dark to see what's in it.")


            w_or_ag = input (Style.RESET_ALL +"\n\nWith no real light coming into the tunnels, the only way you know to get anywhere is either to follow the flow of the water, or to go against it. What are you going to do? (with/against) ")

            if w_or_ag.lower().strip() == 'against':
                print (Style.RESET_ALL +"\nYou decide to go against the flow of water, and after what feels like an eternity of hiking through sludge, the sound of running water grows louder and louder.")
                print (Style.RESET_ALL +"\nEventually, you come across a massive pipe dumping water into the river of sewage you've been following.")
                slow_down()
                print (Style.RESET_ALL +"\nYou only got yourself stuck deeper underground, with no real sense of direction. You get lost underneath the prison, and are discovered by guards no less than 15 minutes later")
                print (Style.RESET_ALL +"\n\n\n\n\nENDING ELEVEN: The Environmentally Inept. \nReally? Against the flow? Have you EVER seen a survival TV show?")
                play_again()

            elif w_or_ag.lower().strip() == 'with':
                print (Style.RESET_ALL +"\nYou decide to start trekking with the flow of the water. Definitely a good choice. It has to empty out somewhere? Right?")


        print(Style.RESET_ALL +"\n\nAfter what feels like an eternity of hiking through sludge, the tunnel splits off.")
        slow_down()
        lig_or_dark2 = input (Style.RESET_ALL +"\n\nThe right path descends into darkness, but there is a faint light coming from the left one. Which way are you going to  go? (light/dark)")

        if lig_or_dark2.lower().strip() == 'dark':
            print (Style.RESET_ALL +"\nYou opt to go down the dark path, hoping for it to sheild you from the guards that are inevitably on your tail.")
            print (Style.RESET_ALL +"\nBut very quickly, you start to get turned around, and completely lose track of where you are.")
            slow_down()
            print (Style.RESET_ALL + "\nWith the stream of sewage drying up, you have no way of knowing where you are, or what direction to go to get out.")
            print ("\n\n\n\n\nENDING TWELVE: The Failed Cartogropher. Good tip: don't get lost when you're trying to escape from people who know the area better than you.")
            play_again()

        elif lig_or_dark2.lower().strip()== 'light':
            print (Style.RESET_ALL +"\nYou opt to go down the path that's lit up. As you follow this path, you can hear the sound of a low growl growing in the distance.")


        print ("\n\nAfter a few short minutes of walking, you reach another fork.")
        loud_quiet = input ("The growling sounds are very clearly coming from one path, while the other is totally silent. Which one do you pick? (loud/silent) ")

        if loud_quiet.lower().strip() == 'loud':
            print (Style.RESET_ALL +"\nYou take a deep breath and decide to head down the louder tunnel, hoping whatever was growling will be in a different offshoot that you'll avoid at all costs.")
            print (Style.RESET_ALL +"\nYou hadn't even been walking for two minutes when you see the immistakable shadow of a crocodile.")
            slow_down()
            print (Style.RESET_ALL +"\nYour jaw hits the floor. You take a few deep breaths and inch closer, trying to figure out what to do.")
            slow_down()         

        print (Style.RESET_ALL +"\nYou realize that you've come too far to turn back now. You gather yourself and realize there's a decision you have to    make.")
        run_sneak = input (Style.RESET_ALL +"\n\nEither you can run past the crocodile and hope for the best, or you can try to slowly sneak past it. What are you going  to do? (run/sneak) ")

        if run_sneak.lower().strip() == 'run':
            print (Style.RESET_ALL +"\nYou start bouncing around to hype yourself up. The crocodile appears to be up against the left wall, so you hug the     right.")
            print (Style.RESET_ALL +"\nIt doesn't see you yet, so you think you actually may have a chance.")
            slow_down()
            print (Style.RESET_ALL +"\nYou take one final breath, and take off in a dead sprint down the tunnel.")
            print (Style.RESET_ALL +"\nOut of the corner of your eye, you see the crocodiles face rear up before it flips around to chase you, but the slapping of its feet against the cement becomes background noise as you fly past it.")
            print (Style.RESET_ALL +"\nYou run for dear life until you hit the pinprick of light that had been growing in the distance, and you promptly        faceplant in a massive, disgusting, sewage dumpster.")
            slow_down()
            print (Style.RESET_ALL +"\nCovered in bodily fluids that you don't even want to speculate about, you hop out of the dumpster, and without a security camera in sight, you dig and shimmy your way under the fence, and are home free.")
            print (Style.RESET_ALL +"\n\n\n\n\nENDING THIRTEEN: The Steve Irwin. \nYou're barely recognizable with all of the filth, but you don't bother slowing down until the prison is just a pinpoint in the horizon, at which point you promptly crash to the ground as you've been running for several miles.")
            print (Style.RESET_ALL +"\n\nCongratulations, " + user_facts[0] + "! You won the game!")
            play_again()

        elif run_sneak.lower().strip() == 'sneak':
            print (Style.RESET_ALL + "\nYou take deep breaths in an attempt to slow your breathing to the point that its almost silent, and press yourself up against the wall and tiptoe down the tunnel.")
            print (Style.RESET_ALL +"\nYou were a mere 5 feet away when the crocodile notices you, and promptly moves to block your path.")
            slow_down()
            print (Style.RESET_ALL +"\nYou freeze in you track, and suck in your final breath as the back of the crocodiles throat comes barrelling towards you.")
            print (Style.RESET_ALL +"\n\n\n\n\nENDING FOURTEEN: The Lunch. \nOkay, I'll admit that one was kind of gory. But exciting, right?")
            play_again()

        elif loud_quiet.lower().strip() == 'silent':
            print (Style.RESET_ALL +"\nWhat, are you crazy? There's no chance you're dealing with whatever is growling at the end of that tunnel.")
            print (Style.RESET_ALL +"\nYou continue along your way, having an astonishingly uneventful hike.")
            slow_down()
            print (Style.RESET_ALL +"\nYou had begun to lose track of time, when, out of nowhere, hundreds of footsteps come barrelling towards you.")
            print (Style.RESET_ALL +"\nYou can barely make out cross logo against their long red cloaks before you are trampled by the group.")
            slow_down()
            print (Style.RESET_ALL + "\nYou're nearly speechless in shock." +Fore.BLUE + "Is that...the Spanish Inquisition?")
            slow_down()
            print (Style.RESET_ALL +"\nTheir leagues are seemingly endless, and you're knocked out soon after your head slams against the concrete of the tunnels.")
            print (Style.RESET_ALL +"\n\n\n\n\nENDING FIFTEEN: The Monty Python. \nNOBODY expects the Spanish Inquisition.")
            print (Style.RESET_ALL + "Get it? Monty PYTHON, in a PYTHON class? You know what, nevermind.")
            play_again()



    if user_facts[3] is not None: 
        escape()

def feedback_2():
    """Asks player for feedback on the game, same as feedback function but callable outside of game
        
        Parameters
        -----------
        none
        
        Returns
        --------
        none
        """
    input ('What did you think of the game?')

    print ('Thanks for the feedback!')
    sys.exit()
        


if ans1.lower().strip() == 'yes':
    game()
else:
    print ("That's too bad. Have a nice day!")
    feedback_2()        

# this conditional has to go at the end because game needs to be defined for it to work, similar issue addressed in an above comment

