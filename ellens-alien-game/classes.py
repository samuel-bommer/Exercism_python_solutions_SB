"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes:
        (class) total_aliens_created (int): Total number of Alien instances.
        x_coordinate (int): Position on the x-axis.
        y_coordinate (int): Position on the y-axis.
        health (int): Number of health points.

    Methods:
        hit(): Decrement Alien health by one point.
        is_alive(): Return a boolean for if Alien is alive (if health is > 0).
        teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
        collision_detection(other): Implementation TBD.

    """

    total_aliens_created = 0
    
    def __init__(self, xcor, ycor):
        self.x_coordinate = xcor
        self.y_coordinate = ycor
        self.health = 3
        
        Alien.total_aliens_created += 1
    
    def hit(self):
        if self.health >= 1:
            self.health -= 1
        else:
            self.health = 0
        
    def is_alive(self):
        if self.health >=1:
            return True
        return False
    
    def teleport(self, xcor, ycor):
        self.x_coordinate = xcor
        self.y_coordinate = ycor
        return self.x_coordinate, self.y_coordinate
    
    def collision_detection(self, other_object):
        pass
    

def new_aliens_collection(alien_start_positions):
    
    aliens_list = []
    for position in alien_start_positions:
        alien_in = Alien(position[0], position[1])
        aliens_list.append(alien_in)
    return aliens_list

#(Student): Create the new_aliens_collection() function below to call your Alien class with a list of coordinates
alien_start_positions_example = [(4,7), (-1, 0)]
aliens_instances = new_aliens_collection(alien_start_positions_example)

for alien in aliens_instances:
    print((alien.x_coordinate, alien.y_coordinate))
    print(alien.health)