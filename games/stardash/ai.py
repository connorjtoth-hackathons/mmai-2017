# This is where you build your AI for the Stardash game.

from joueur.base_ai import BaseAI

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
import math
# you can add additional import(s) here
# <<-- /Creer-Merge: imports -->>

class AI(BaseAI):
    """ The AI you add and improve code inside to play Stardash. """

    @property
    def game(self):
        """The reference to the Game instance this AI is playing.

        :rtype: games.stardash.game.Game
        """
        return self._game # don't directly touch this "private" variable pls

    @property
    def player(self):
        """The reference to the Player this AI controls in the Game.

        :rtype: games.stardash.player.Player
        """
        return self._player # don't directly touch this "private" variable pls

    def get_name(self):
        """ This is the name you send to the server so your AI will control the
            player named this string.

        Returns
            str: The name of your Player.
        """
        # <<-- Creer-Merge: get-name -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        return "TeamName" # REPLACE THIS WITH YOUR TEAM NAME
        # <<-- /Creer-Merge: get-name -->>

    def start(self):
        """ This is called once the game starts and your AI knows its player and
            game. You can initialize your AI here.
        """
        # <<-- Creer-Merge: start -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        # replace with your start logic
        # <<-- /Creer-Merge: start -->>

    def game_updated(self):
        """ This is called every time the game's state updates, so if you are
        tracking anything you can update it here.
        """
        # <<-- Creer-Merge: game-updated -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        # replace with your game updated logic
        # <<-- /Creer-Merge: game-updated -->>

    def end(self, won, reason):
        """ This is called when the game ends, you can clean up your data and
            dump files here if need be.

        Args:
            won (bool): True means you won, False means you lost.
            reason (str): The human readable string explaining why your AI won
            or lost.
        """
        # <<-- Creer-Merge: end -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        # replace with your end logic
        # <<-- /Creer-Merge: end -->>
    def run_turn(self):
        """ This is called every time it is this AI.player's turn.

        Returns:
            bool: Represents if you want to end your turn. True means end your turn, False means to keep your turn going and re-call this function.
        """
        # <<-- Creer-Merge: runTurn -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        # Put your game logic here for runTurn
        return True
        # <<-- /Creer-Merge: runTurn -->>

    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you need additional functions for your AI you can add them here




    def turns_to_mine_mythicite(self):
        """ Returns bool: if we can mine mythicite"""
        if self.game().turns_to_orbit()
            pass

    def distance(self, objx, objy, obj2x, obj2y):
        """
        """
        return math.sqrt((objx - obj2x) ** 2 + (objy - obj2y) ** 2)


    # Closest X type of asteroid to the miner in n turns
    def closest_asteroid_to_position(self, position, n=0, asteroid_type=None, min_res=0):
        """
        position: a tuple (x, y) for the location of the position to calculate from
        n: the number of turns to calculate from now (default: 0)
        asteroid_type: the material type of asteroid to look for (default: any)
        min_res: the minimum acceptable number of resources acceptable on an asteroid
                 for consideration (default: 0)
        """

        # current unit is at position (x, y)
        x, y = position[0], position[1]
        
        # current list of asteroids of a certain type passed by parameter
        asteroids_of_type = [x for x in self.game().bodies() 
            if x.body_type() == 'asteroid' and 
            ((not x.material_type()) or (x.material_type() == asteroid_type)) and
            x.amount() > min_res]

        # return that which is the smallest one
        min_dist=None
        min_asteroid=None
        for asteroid in asteroids_of_type:
            dist = distance(position[0], position[1], asteroid.next_x(n), asteroid.next_y(n))
            if (not dist) or (dist < min_dist):
                min_dist = dist
                min_asteroid = asteroid
        return min_asteroid
    
    # Return to planet function
    def travel_towards_base_direct(self, unit):
        home_base = unit.owner().home_base()
        


    ## TOTH  HELPER FUNCTIONS ^^^^^^
    ## SAUER HELPER FUNCTIONS VVVVVV



    # <<-- /Creer-Merge: functions -->>
