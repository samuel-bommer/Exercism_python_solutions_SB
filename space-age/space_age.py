class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds
        
    def on_earth(self) -> float:
        """
        Calculates seconds into years on earth
        """
        
        hour = self.seconds / (60*60)
        day = hour / 24
        year = day / 365.25
        
        return round(year, 2)
    
    def on_mercury(self) -> float:
        """
        On mercury
        """
        
        earth_years = self.on_earth()
        mercury_years = earth_years / 0.2408467
        return round(mercury_years, 2)
        
    def on_venus(self) -> float:
        """
        On venus
        """
        
        earth_years = self.on_earth()
        venus_years = earth_years / 0.6155
        return round(venus_years, 2)
    
    def on_mars(self) -> float:
        """
        On mars
        """
        
        earth_years = self.on_earth()
        mars_years = earth_years / 1.8808158
        return round(mars_years, 2)
    
    def on_jupiter(self) -> float:
        """
        On Jupyter
        """
        
        earth_years = self.on_earth()
        jupiter_years = earth_years / 11.862615
        return round(jupiter_years, 2)
    
    def on_saturn(self) -> float:
        """
        On Saturn
        """
        
        earth_years = self.on_earth()
        saturn_years = earth_years / 29.447498
        return round(saturn_years, 2)
    
    def on_uranus(self) -> float:
        """
        On uranus
        """
        
        earth_years = self.on_earth()
        uranus_years = earth_years / 84.016846
        return round(uranus_years, 2)
    
    def on_neptune(self) -> float:
        """
        On Neptune
        """
        
        earth_years = self.on_earth()
        neptune_years = earth_years / 164.79132
        return round(neptune_years, 2)
        