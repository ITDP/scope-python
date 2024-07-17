import pandas as pd
import geopandas as gpd
import rasterstats


def get_country_list():
    #TODO: authoritative list of countries with known mapping to regions
    return ['China','India']

def get_cities_list(country):
    #TODO: use Atlas data to get list of urban areas within each country
    if country == 'China': return ['Beijing','Guangzhou']
    if country == 'India': return ['Delhi','Chennai']

def get_pop_growth_rate(cityname):
    return 0.05 #TODO get city specific rate from Atlas
    #ensure units are clearly defined (% per year?)

def get_mode_split(worldregion):
    #currently just returns % of travel by car
    #TODO: base on actual Compact Electrified data (or other source?)
    return {'China':0.5, 'India':0.2}[worldregion]

def get_pop_density(cityname):
    return 10000 #TODO: add pop density list from atlas by city

class BRTProject:
    def __init__(self, countryname, cityname, start_year):
        #things that have to be supplied by Sofnux
        self.worldregion = countryname #TODO: map country names to regions
        self.city_name = cityname
        self.start_year = start_year
        
        #things that we can prepopulate with defaults
        self.pop_growth_rate = get_pop_growth_rate(cityname)
        self.working_days = 260 #TODO -- provide user input option?? 
        self.city_modesplit = get_mode_split(self.worldregion) 
        self.pop_density = get_pop_density(cityname)
        self.occupancy = 1.2 #TODO -- add df of all occupancy rates
   
    
    def set_pnt_length(self, length_km):
        self.pnt = length_km * 1.6 * self.pop_density
        self.trip_length = self.length_km
     
    def set_pnt_geo(self, lines):
        #TODO: write fxn to calculate avg pop density within buffer area -> PNT
        pass 
    
    def set_ops_characteristics(self, fleetsize, speed):
        self.fleetsize = fleetsize
        self.speed = speed
        self.trip_length = self.length_km
        self.frequency = fleetsize * speed / self.length_km * 2
   
    #RIDERSHIP OPTION 1 ONLY
    def calc_ridership_1(self):     
        self.trip_length = self.length_km
        self.ridership = self.frequency * 100 + self.pnt * 0.01
 
    #RIDERSHIP OPTION 2 ONLY    
    def set_ridership_params(self, current_ridership, brtscore):
        self.current_ridership = current_ridership
        self.brtscore = brtscore
 
    #RIDERSHIP OPTION 2 ONLY
    def calc_ridership_2(self):
        self.ridership = self.current_ridership * 20 + self.brtscore * 500 + 350
    
    #OPTIONAL
    def set_custom_citylevel_modesplit(self, custom_mode_split):
        self.city_modesplit = custom_mode_split
    
    def calc_modal_shift_default(self):
        self.modeshift =  self.city_modesplit * 0.5 
        #TODO replace with actual split-to-shift relationship

    def set_custom_modal_shift(self, custom_modeshift):
        pass

    def set_custom_trip_length(self, custom_trip_length):
        self.trip_length = custom_trip_length
        
    def get_default_emissions_factors(self):
        self.emissions_per_vkt = 0.3
        
    def get_impact(self):
        impact = self.ridership * self.trip_length / self.occupancy * self.modeshift * self.emissions_per_vkt
        self.impact = impact
        return impact
        #TODO: unit conversion

