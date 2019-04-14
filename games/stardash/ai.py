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
        
        # track if it is at the target asteroid
        # status: returning, arriving, mining
        
        # maps (unit) -> (asteroid) that it should be mining or (unit) -> (base) if returning
        self.targets = {unit : None for unit in self.player.units}
        
        
        
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
        
        # 

        buyFleet()
        for unit in player.units:
            if unit.job.title == 'miner':
                # mining logic
                target = self.targets[unit]

                if not target:
                    choice = None
                    choices = ['legendarium','rarium','genarium', None] if turns_to_mine_mythicite() > 1 else ['mythicite', 'legendarium','rarium','genarium', None]
                    for oretype in choices:
                        if choice:
                            break
                        else:
                            choice = closest_asteroid_to_position((unit.x, unit.y, n=3, asteroid_type=oretype, min_res=20)
                    self.targets[unit] = choice

                # target is now set

                # first, we try to reach the target if we are not with it anymore
                if not self.distance_between(unit, target) < target.radius:
                    self.travel_towards_target_direct(unit, dashable=False)

                # if we are at the target, then we will do our specified action
                if self.distance_between(unit, target) < target.radius:
                    # do the action

                    if target.body_type == 'asteroid':
                        # mine if we have capacity, flee back home if not
                        if unit.capacity_left() < self.game.mining_speed:
                            unit.mine(target)
                        else:
                            self.targets[unit] = player().home_base()
                
                    elif target.body_type == 'planet':
                        # let off resources and rest to regain some energy if needed
                        self.targets[unit]=None
                
                    # final push to get to the resources we need


            else:
                #other logic
                pass

        # Put your game logic here for runTurn
        return True
        # <<-- /Creer-Merge: runTurn -->>

    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you need additional functions for your AI you can add them here




    def turns_to_mine_mythicite(self):
        """ Returns bool: if we can mine mythicite
        """
        return self.game.current_turn - this.game.orbits_protected + 1

    def distance(self, objx, objy, obj2x, obj2y):
        """
        """
        return math.sqrt((objx - obj2x) ** 2 + (objy - obj2y) ** 2)

    def distance_between(self, obj, obj2):
        """
        """
        return math.sqrt((obj.x - obj2.x) ** 2 + (obj.y - obj2.y) ** 2)

    def direction(self, initx, inity, destx, desty):
        """
        Going from (initx, inity) to (destx, desty)
        """
        diff = (destx-initx, desty-inity)
        magnitude = distance(0, 0, diff[0], diff[1])
        return (diff[0]/magnitude, diff[1]/magnitude)  # unit vector



    # Closest X type of asteroid to the miner in n turns
    def closest_asteroid_to_position(self, position, n=0, asteroid_type=None, min_res=0):
        """
        position: a tuple (x, y) for the location of the position to calculate from
        n: the number of turns to calculate from now (default: 0)
        asteroid_type: the material type of asteroid to look for (default: any)
        min_res: the minimum acceptable number of resources acceptable on an asteroid
                 for consideration (default: 0)

        RETURNS: asteroid that is closest and meets parameters
        """

        # current unit is at position (x, y)
        x, y = position[0], position[1]
        
        # current list of asteroids of a certain type passed by parameter
        asteroids_of_type = [x for x in self.game.bodies
            if x.body_type() == 'asteroid' and 
            ((not x.material_type) or (x.material_type == asteroid_type)) and
            x.amount > min_res]

        # return that which is the smallest one
        min_dist=None
        min_asteroid=None
        for asteroid in asteroids_of_type:
            dist = distance(position[0], position[1], asteroid.next_x(n), asteroid.next_y(n))
            if (not dist) or (dist < min_dist):
                min_dist = dist
                min_asteroid = asteroid
        return min_asteroid
    
    # calculate maximum distance given a certain amount of energy to use
    def max_dash_dist_with_energy(self, energy):
        """ """
        game = self.game
        return game.dash_distance * ((energy + 1) / game.dash_cost)   
    
    # Return to planet function
    def travel_towards_base_direct(self, unit, min_retaining_energy=21, dashable=True):
        """ Sends the given unit back towards its base"""
        home_base = unit.owner.home_base
        return travel_towards_location_direct(unit, home_base.x, home_base.y, home_base.radius, min_retaining_energy, dashable)

    # travel direct to target
    def travel_towards_target_direct(self, unit, min_retaining_energy=21, dashable=True):
        """ Sends the unit towards its given target in the self.targets table"""
        target = targets[unit]
        if target:
            return travel_towards_location_direct(unit, target.x, target.y, target.radius, min_retaining_energy, dashable)
        else:
            return None


    # Generalized traveling function
    def travel_towards_location_direct(self, unit, x, y, r=0, min_retaining_energy=21, dashable=True):
        """ Sends the given unit back towards a specified location
        
            unit: unit to move
            x,y: location to move to
            r: radius needed to be within for the given position to be valid (default: 0)
            min_retaining_energy: the amount of energy we require be available at the end of travel (default: 21)
        """

        # direction of the base from us
        direction = direction(unit.x, unit.y, x, y)
        distance = distance(unit.x, unit.y, x, y) - r + 1

        max_dist_without_dash = unit.moves
        energy_without_dash = unit.energy

        max_dashing_energy = energy_without_dash - min_retaining_energy
        max_dashable_dist = max_dash_dist_with_energy(max_dashing_energy)


        # check if the distance can be made without a dash
        if distance <= max_dist_without_dash:
            # we can move without a dash and we will
            unit.move(direction[0] * distance, direction[1] * distance)
        
        #if not, we will check if we can make it with a dash
        elif distance <= max_dashable_dist + max_dist_without_dash and dashable:
            unit.move(direction[0] * max_dist_without_dash, direction[1] * distance)
            unit.dash(direction[0] * (distance - max_dist_without_dash),
                      direction[1] * (distance - max_dist_without_dash))

        # otherwise, we will simply go towards it
        else:
            unit.move(direction[0] * max_dist_without_dash, direction[1] * max_dist_without_dash)


        


    ## TOTH  HELPER FUNCTIONS ^^^^^^
    ## SAUER HELPER FUNCTIONS VVVVVV
    def buyFleet():
        planet_x = player.home_base.x
        planet_x = player.home_base.y
        planet_radius = player.home_base.radius
        spawn_x = planet_x + (planet_radius if planet_x < 0 else 0-planet_radius)
        while(player.home_base.amount>200):
            player.home_base.spawn(spawn_x,y,"miner")
        return

    def attackFleet(units):
        x,y
        for unit in units:
            x+=unit.x
            y+=unit.y
        x/=len(unit)
        x/=len(unit)
        players = game.players
        enemy = (players[0] if players[0] != units[0].owner() else players[1])

        for unit in units:
            unit.move()
        return

    # <<-- /Creer-Merge: functions -->>
