#smiley faces for aaron approximately 15/15

class SpaceShip(object):
    def __init__(self):
        self.cloaking_device = False
        self.weapons = []
        self.engine_type = None
        self.color = None
        self.shield_strength = 0
        self.location = "space"
        self.speed = "impulse"
        self.shields_up = False
        self.destroyed = False

    def fire_phasers(self,target):
        self.check_destroyed("fire phasers")
        if target.speed == "warp": return
        if target.shield_strength <= 0:
            target.hull_strength = target.hull_strength - self.phaser_strength
        else:
            target.shield_strength = target.shield_strength - self.phaser_strength
        if target.hull_strength <= 0:
            target.destroyed = True

    def fire_photon_torpedos(self,target):
        self.check_destroyed("fire photons")
        if target.speed == "warp": return
        if target.shield_strength <= 0:
            target.hull_strength = target.hull_strength - self.photon_strength
        else:
            target.shield_strength = target.shield_strength - self.photon_strength
        if target.hull_strength <= 0:
            target.destroyed = True

    def go_to_warp(self,destination):
        self.check_destroyed("go_to_warp")
        self.speed = "warp"
        self.location = destination

    def raise_shields(self):
        self.check_destroyed("raise_shields")
        self.shields_up = True
        self.shield_strength = self.max_shield_strength

    def lower_shields(self):
        self.check_destroyed("lower_shields")
        self.shields_up = False
        self.shield_strength = 0

    def check_destroyed(self, msg):
        if self.destroyed:
            raise Exception("Can't %s : Ship is destoryed." % msg)

    def print_status(self):
        print self.__class__.__name__
        print "\tshield_strength = %s" % self.shield_strength
        print "\thull_strength = %s" % self.hull_strength
        print "\tlocation = %s" % self.location
        print "\tspeed = %s" % self.speed
        print "\tshields_up = %s" % self.shields_up
        print "\tdestroyed = %s" % self.destroyed


class Constitution(SpaceShip):
    def __init__(self):
        SpaceShip.__init__(self)
        self.weapons = ['phaser', 'phaser', 'photon']
        self.engine_type = "fixed"
        self.color = "grey"
        self.max_shield_strength = 150
        self.phaser_strength = 20
        self.photon_strength = 50
        self.hull_strength = 100

class BirdofPrey(SpaceShip):
    def __init__(self):
        SpaceShip.__init__(self)
        self.cloaking_device = True
        self.weapons = ['disruptor', 'disruptor', 'photon']
        self.engine_type = "moveable"
        self.color = "green"
        self.max_shield_strength = 100
        self.disruptor_strength = 30
        self.photon_strength = 60
        self.hull_strength = 80

    def cloak(self):
        self.check_destroyed("cloak")
        self.is_cloaked = True

    def decloak(self):
        self.check_destroyed("decloak")
        self.is_cloaked = False

class Excelsior(SpaceShip):
    def __init__(self):
        SpaceShip.__init__(self)
        self.weapons = ['phaser', 'phaser', 'photon', 'photon']
        self.engine_type = "fixed"
        self.color = "grey"
        self.max_shield_strength = 150
        self.phaser_strength = 25
        self.photon_strength = 50
        self.hull_strength = 150



enterprise = Constitution()
excelsior = Excelsior()
changs_ship = BirdofPrey()

#they should combat eachother
enterprise.print_status()
changs_ship.print_status()

raw_input("Press Any Key...")
print " "
print "Chang's ship decloaks. The Enterprise raises it's shields."
print "Chang's ship follows suit."
print "The Enterprise fires phasers and photon torpedos."
print " "
changs_ship.decloak()
enterprise.raise_shields()
changs_ship.raise_shields()
enterprise.fire_phasers(changs_ship)
enterprise.fire_photon_torpedos(changs_ship)
enterprise.print_status()
changs_ship.print_status()

raw_input("Press Any Key...")
print " "
print "Chang's ship fires back with a photon torpedo."
print "The Excelsior joins the fray and fires phasers."
print "The Enterprise fires photon torpedoes."
changs_ship.fire_photon_torpedos(enterprise)
excelsior.fire_phasers(changs_ship)
enterprise.fire_photon_torpedos(changs_ship)
enterprise.fire_photon_torpedos(changs_ship)
#b2.raise_shields()
#b2.go_to_warp("Khitomer")


enterprise.print_status()
changs_ship.print_status()
