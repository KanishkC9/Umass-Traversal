import sys;
import os;
import gzip;

if __name__ == '__main__':
    # Read arguments from command line, or use sane defaults for IDE.
    argv_len = len(sys.argv)
    inputFile = 'locations.text'

#Add Curry Hicks 
# make this a dict instead of a list for time complexity 
campusLocations = [ # will create an api for this
  { "name": "Agricultural Engineering Bldgs.", "children": ['Hatch', 'Holdsworth', 'Cold Storage Bldg.', 'Chenoweth', 'Bowditch Greenhouses'] },
  { "name": "Agricultural Learning Center", "children": [] },
  { "name": "Alfond", "children": ['Isenberg School of Management','Mahar Auditorium','Haigis Mall', 'Robsham Visitors Center' ] },
  { "name": "Apiary Building", "children": ['Gorman', 'Wheeler' , 'New Africa'] },
  { "name": "Army ROTC Bldg.", "children": ['Berkshire', 'Boyden Gym', 'Melville'] },
  { "name": "Arnold", "children": ['Hamlin', 'Knowlton', 'Lederle Graduate Research Ctr.'] },
  { "name": "Astronomy Bldg.", "children": ['Gunness Engineering', 'Engineering Laboratory', 'Duda'] },
  { "name": "Athletic Fields", "children": ['Tennis Courts', 'Champions Center'] },
  { "name": "Auxiliary Services Warehouse", "children": ['Forest & Parks Buildings', 'PVTA Bus Garage'] },
  { "name": "Baker", "children": ['Chadbourne', 'Greenough' , 'Brooks'] },
  { "name": "Bartlett", "children": ['Tobin', 'Memorial Hall', 'Herter' , 'Hicks Physical Education'] },
  { "name": "Berkshire", "children": ['Army ROTC Bldg.', 'Hampshire', 'Middlesex'] },
  { "name": "Berkshire Dining", "children": ['Moore', 'John Adams', 'John Q. Adams', 'Hampden Dining'] },
  { "name": "Birch", "children": ['Sycamore', 'Maple', 'Recreation Center'] },
  { "name": "Blaisdell", "children": ['Photo Laboratory', 'Thompson', 'George N. Parks Marching Band Bld'] },
  { "name": "Bowditch Greenhouses", "children": ['Bowditch Hall', 'Physical Plant', 'Agricultural Engineering Bldgs.' ] },
  { "name": "Bowditch Hall", "children": ['Bowditch Greenhouses', 'Holdsworth'] },
  { "name": "Bowditch Lodge", "children": ['Farley Lodge', 'Toddler House'] },
  { "name": "Bowker Auditorium (Stockbridge)", "children": ['Hatch', 'Chenoweth', 'Draper', 'Flint Laboratory'] },
  { "name": "Boyden Gym", "children": ['Linden', 'Oak', 'Garber Field', 'Army ROTC Bldg.'] },
  { "name": "Brett", "children": ['Wheeler', 'Brooks', 'University Health Center', 'Franklin Dining'] },
  { "name": "Brooks", "children": ['Brett','University Health Center', 'New Africa', 'Baker'] },
  { "name": "Brown", "children": ['Cashin', 'McNamara', 'North A' ] },
  { "name": "Butterfield", "children": ['Van Meter'] },
  { "name": "Campus Center", "children": ['Hasbrouck', 'Integrative Learning Center', 'Student Union', 'Campus Center Parking Garage'] },
  { "name": "Campus Center Parking Garage", "children": ['Campus Center', 'Student Union', 'Machmer', 'Flint Laboratory'] },
  { "name": "Campus Pond,", "children": ['Du Bois Library, W.E.B', 'Old Chapel', 'Memorial Hall', 'Fine Arts Center', 'Integrative Learning Center', 'Student Union'] },
  { "name": "Cance", "children": ['Pierpont', 'Washington', 'Berkshire Dining' ] },
  { "name": "Cashin", "children": ['Brown', 'McNamara', 'UMass Police Department'] },
  { "name": "Central Heating Plant", "children": ['Lorden Field (Baseball)', 'Tennis Courts'] },
  { "name": "Central Stores (Physical Plant)", "children": ['Bowditch Greenhouses', 'Textbook Annex', 'Mullins Practice Rink'] },
  { "name": "Chabad House", "children": ['Prince', 'Crampton', 'Lincoln Apartments'] },
  { "name": "Chadbourne", "children": ['Van Meter', 'Greenough', 'Baker'] },
  { "name": "Champions Center", "children": ['Recreation Center', 'Mullins Center'] },
  { "name": "Chancellor's House", "children": ['Dickinson', 'Webster'] },
  { "name": "Chenoweth", "children": ['Agricultural Engineering Bldgs.', 'Cold Storage Bldg.', 'Flint Laboratory','Bowker Auditorium (Stockbridge)', 'Hatch'] },
  { "name": "Clark", "children": ['Franklin Dining', 'Shade Tree Laboratory', 'Olver Design Bldg.', 'Morrill Science Center'] },
  { "name": "Cold Storage Bldg.", "children": ['Chenoweth', 'Textbook Annex', 'Flint Laboratory', 'Agricultural Engineering Bldgs.'] },
  { "name": "Communication Disorders", "children": ['PKA - Pi Kappa Alpha'] },
  { "name": "Computer Science Bldg.", "children": ['Engineering Laboratory', 'Engineering Laboratory 2', 'PVTA Bus Garage'] },
  { "name": "Conte Polymer Research Center", "children": ['Marcus', '"Lederle Graduate Research Ctr.', 'KS - Kappa Sigma'] },
  { "name": "Coolidge", "children": ['Hampshire Dining', 'Hampden Dining', 'Kennedy', 'Prince', 'Crampton']},
  { "name": "Crabtree", "children": ['Knowlton', 'Lyon', 'Worcester Dining', 'Arnold'] },
  { "name": "Crampton", "children": ['MacKimmie', 'Coolidge','Prince','Hampden Dining'] },
  { "name": "Crotty Hall", "children" : ['Gordon', 'SDT - Sigma Delta Tau', 'IGU - Iota Gamma Upsilon']},
  { "name": "Dickinson Hall", "children": ['Sycamore', 'Recreation Center','Goodell', 'George N. Parks Marching Band Bld'] },
  { "name": "Dickinson House", "children": ['Webster', 'Grayson', "Chancellor's House", 'Observatory'] },
  { "name": "Draper", "children": ['Knowles', 'Goessmann', 'Bowker Auditorium (Stockbridge)', 'Lincoln Campus Center'] },
  { "name": "Du Bois Library, W.E.B.", "children": ['Old Chapel', 'South College', 'Machmer', 'Student Union', 'Campus Pond'] },
  { "name": "Duda", "children": ['Engineering Laboratory', 'Engineering Laboratory 2', 'Robotics', 'Gunness Engineering', 'Astronomy Bldg.'] },
  { "name": "Durfee Conservatory & Garden", "children": ['University Health Center', 'French'] },
  { "name": "Dwight", "children": ['Leach', 'Johnson', 'Totman'] },
  { "name": "East Experiment Station", "children": ['West Experiment Station', 'Worcester Dining', 'Integrated Science Building', 'Knowlton'] },
  { "name": "Elm", "children": ['Sycamore', 'Goodell', 'Tobin'] },
  { "name": "Emerson", "children": ['James', 'Hampshire Dining', 'Sortino Softball Complex'] },
  { "name": "Engineering Laboratory", "children": ['Computer Science Bldg.', 'Engineering Laboratory 2', 'Duda', 'Astronomy Bldg.'] },
  { "name": "Engineering Laboratory 2", "children": ['Engineering Laboratory', 'Duda', 'PVTA Bus Garage', 'Computer Science Bldg.'] },
  { "name": "Farley Lodge", "children": ['Bowditch Lodge', 'Toddler House', 'Martin Jacobson Football Performance Center' ] },
  { "name": "Fernald", "children": ['Franklin Dining', 'Olver Design Bldg.', 'Wheeler', 'Studio Arts Building'] },
  { "name": "Field", "children": ['Webster', 'Grayson'] },
  { "name": "Fine Arts Center", "children": ['Herter', 'Memorial Hall', 'Isenberg School of Management', 'Olver Design Bldg.', 'Campus Pond'] },
  { "name": "Flint Laboratory", "children": ['Cold Storage Bldg.', 'Parking Garage', 'Bowker Auditorium (Stockbridge)', 'Chenoweth'] },
  { "name": "Forest & Parks Buildings", "children": ['Auxillary Services Warehouse', 'Parking Office', 'Transit Facility'] },
  { "name": "Franklin Dining", "children": ['French', 'Fernald', 'Clark', 'Brett', 'Shade Tree Laboratory','Wheeler'] },
  { "name": "ATG - Alpha Tau Gamma", "children": ['Patterson', 'Cance'] },
  { "name": "CO - Chi Omega", "children": ['UMass Police Department', 'Grayson'] },
  { "name": "IGU - Iota Gamma Upsilon", "children": ['Crotty Hall', 'Hillel House'] },
  { "name": "KKG - Kappa Kappa Gamma", "children": ['PKP - Pi Kappa Phi', 'Lincoln Apartments', 'SK - Sigma Kappa'] },
  { "name": "KS - Kappa Sigma", "children": ['Totman'] },
  { "name": "PSK - Phi Sigma Kappa", "children": ['TC - Theta Chi', 'Isenberg School Of Management', 'Studio Arts Building'] },
  { "name": "PKA - Pi Kappa Alpha", "children": ['Hillel House', 'Communication Disorders','SK - Sigma Kappa'] },
  { "name": "PKP - Pi Kappa Phi", "children": ['KKG - Kappa Kappa Gamma', 'Robsham Visitors Center', 'Lincoln Apartments', 'Crotty Hall'] },
  { "name": "SDT - Sigma Delta Tau", "children": ['Gordon', 'Crotty Hall', 'IGU - Iota Gamma Upsilon', 'International Programs'] },
  { "name": "SK - Sigma Kappa", "children": ['Hillel House', 'Crotty Hall', 'KKG - Kappa Kappa Gamma', 'PKA - Pi Kappa Alpha'] },
  { "name": "TC - Theta Chi", "children": ['Newman Center', 'PSK - Phi Sigma Kappa', 'Mahar Auditorium', 'Isenberg School Of Management'] },
  { "name": "French", "children": ['Franklin Dining', 'Durfee Conservatory & Garden', 'University Club', 'University Health Center','Wilder'] },
  { "name": "Furcolo", "children": ['Montague House', 'Wysocki House'] },
  { "name": "Garber Field", "children": ['Boyden Gym', 'Tobin', 'Oak', 'Middlesex', 'Hicks Physical Education'] },
  { "name": "George N. Parks Marching Band Bld", "children": ['Grinnel', 'Dickinson Hall', 'Blaisdell', 'Thompson', 'South College'] },
  { "name": "Goessmann", "children": ['Knowles', 'Marcus', 'Physical Sciences Bldg.', 'West Experiment Station'] },
  { "name": "Goodell", "children": ['Elm', 'Sycamore', 'Old Chapel', 'Bartlett', 'South College'] },
  { "name": "Gordon", "children": ['Crotty Hall', 'SDT - Sigma Delta Tau', 'Newman Center', 'Robsham Visitors Center'] },
  { "name": "Gorman", "children": ['International Programs', 'Apiary Building', 'Studio Arts Building'] },
  { "name": "Grayson", "children": ['Dickinson House', 'Field', 'UMASS Police Department'] },
  { "name": "Greenough", "children": ['Baker', 'Chadbourne', 'Van Meter'] },
  { "name": "Grinnell Arena", "children": ['Recreation Center', 'George N. Parks Marching Band Bld', 'Blaisdell'] },
  { "name": "Gunness Engineering", "children": ['Marston', 'Astronomy Bldg.', 'Duda', 'Conte Polymer Research Center', ''] },
  { "name": "Hadley Equestrian Farm", "children": ['Track & Field'] },
  { "name": "Haigis Mall", "children": ['Alfond', 'Whitmore Administration Bldg.', 'Isenberg School Of Management','Robsham Visitors Center'] },
  { "name": "Hamlin", "children": ['Arnold','Leach','Lederle Graduate Research Ctr.'] },
  { "name": "Hampden Dining", "children": ['Crampton', 'MacKimmie','John Q. Adams','Coolidge'] },
  { "name": "Hampshire", "children": ['Berkshire', 'Middlesex', 'Whitmore Administration'] },
  { "name": "Hampshire Dining", "children": ['James', 'Emerson', 'Coolidge', 'Kennedy', 'Thoreau', 'Melville'] },
  { "name": "Hasbrouck", "children": ['Lincoln Campus Center', 'Integrative Learning Center', 'Integrated Science Building', 'Skinner'] },
  { "name": "Hatch", "children": ['Holdsworth', 'Bowker Auditorium (Stockbridge)', 'Agricultural Engineering Bldgs.'] },
  { "name": "Health Center", "children": ['Brooks', 'Brett', 'Durfee Conservatory & Garden'] },
  { "name": "Herter", "children": ['Fine Arts Center', 'Munson', 'Memorial Hall', 'Hicks Physical Education'] },
  { "name": "Hicks Physical Education", "children": ['Herter', 'Munson', 'Garber Field', 'Bartlett'] },
  { "name": "Hillel House", "children": ['SK - Sigma Kappa', 'PKA - Pi Kappa Alpha', 'IGU - Iota Gamma Upsilon'] },
  { "name": "Holdsworth", "children": ['Hatch', 'Bowditch', 'Paige', 'Agricultural Engineering Bldgs.'] },
  { "name": "Hotel", "children": ['Hasbrouck', 'Integrative Learning Center', 'Student Union', 'Draper', 'Parking Garage'] },
  { "name": "Integrated Science Building", "children": ['Hasbrouck', 'Life Science Lab', 'East Experiment Station', 'Skinner'] },
  { "name": "Integrative Learning Center", "children": ['Hasbrouck', 'Student Union', 'Lincoln Campus Center', 'Skinner', 'Morrill Science Center', 'Campus Pond'] },
  { "name": "International Programs", "children": ['Gorman', 'SDT - Sigma Delta Tau', 'Newman Center'] },
  { "name": "Isenberg School of Management", "children": ['Mahar Auditorium','Alfond', 'TC - Theta Chi','PSK - Phi Sigma Kappa', 'Fine Arts Center','Haigis Mall'] },
  { "name": "James", "children": ['Melville', 'Hampshire Dining', 'Emerson'] },
  { "name": "John Adams", "children": ['Washington', 'Patterson', 'John Q. Adams', 'Berkshire Dining'] },
  { "name": "John Q. Adams", "children": ['Berkshire Dining', 'Hampden Dining', 'MacKimmie', 'John Adams'] },
  { "name": "Johnson", "children": ['Dwight', 'Lewis', 'North D'] },
  { "name": "Kennedy", "children": ['Thoreau', 'Prince', 'Hampshire Dining', 'Coolidge',] },
  { "name": "Knowles", "children": ['Paige', 'Marcus', 'Goessmann'] },
  { "name": "Knowlton", "children": ['Arnold', 'Crabtree', 'Physical Sciences Bldg.', 'East Experiment Station', 'Worcester Dining'] },
  { "name": "Leach", "children": ['Hamlin', 'Dwight', 'Totman'] },
  { "name": "Lederle Graduate Research Ctr.", "children": ['Arnold', 'Physical Sciences Bldg.', 'Conte Polymer Research Center', 'Hamlin', 'Marcus'] },
  { "name": "Lewis", "children": ['Johnson', 'Thatcher',] },
  { "name": "Life Science Lab", "children": ['Skinner', 'Integrated Science Building',] },
  { "name": "Lincoln Apartments", "children": ['Chabad House','PKP - Pi Kappa Phi','KKG - Kappa Kappa Gamma'] },
  { "name": "Lincoln Campus Center", "children": ['Student Union', 'Integrative Learning Center', 'Hasbrouck', 'Parking Garage', 'Draper', 'Goessmann'] },
  { "name": "Linden", "children": ['Oak', 'Maple', 'Boyden Gym', 'Athletic Fields'] },
  { "name": "Lorden Field (Baseball)", "children": ['Mullins Practice Rink', 'Central Heating Plant', 'Tennis Courts', 'Parking Office'] },
  { "name": "Lyon", "children": ['Thatcher', 'Crabtree', 'Worcester Dining',] },
  { "name": "Machmer", "children": ['Parking Gargage', 'Student Union', 'Thompson', 'Photo Laboratory', 'Du Bois Library, W.E.B.'] },
  { "name": "MacKimmie", "children": ['Crampton', 'Hampden Dining', 'John Q. Adams'] },
  { "name": "Mahar Auditorium", "children": ['Alfond', 'Newman Center', 'Isenberg School of Management'] },
  { "name": "Maple", "children": ['Oak', 'Linden', 'Birch'] },
  { "name": "Marcus", "children": ['Marston', 'Knowles', 'Conte Polymer Research Center', 'Lederle Graduate Research Center', 'Goessmann'] },
  { "name": "Marston", "children": ['Marcus', 'Robotics', 'Gunness Engineering'] },
  { "name": "Martin Jacobson Football Performance Center", "children": ['McGuirk Alumni Stadium', 'Farley Lodge'] },
  { "name": "McGuirk Alumni Stadium", "children": ['Martin Jacobson Football Performance Center'] },
  { "name": "McNamara", "children": ['Brown', 'Cashin'] },
  { "name": "Melville", "children": ['James', 'Thoreau','Army ROTC Bldg.'] },
  { "name": "Memorial Hall", "children": ['Old Chapel', 'Herter', 'Campus Pond', 'Fine Arts Center', 'Bartlett'] },
  { "name": "Middlesex", "children": ['Berkshire', 'Hampshire','Whitmore Administration','Munson'] },
  { "name": "Montague House", "children": ['Furcolo', 'North C'] },
  { "name": "Moore", "children": ['Pierpont', 'Berkshire Dining', 'Hampden dining', 'Emerson'] },
  { "name": "Morrill Science Center", "children": ['Wilder', 'University Club', 'Shade Tree Laboratory', 'Clark', 'Integrative Learning Center', 'Skinner', 'Life Science Lab'] },
  { "name": "Mullins Center", "children": ['Mullins Practice Rink', 'Champions Center', 'Tennis Courts']},
  { "name": "Mullins Practice Rink", "children": ['Lorden Field', 'Mullins Center', 'Physical Plant', 'Parking Office'] },
  { "name": "Munson", "children": ['Herter', 'Whitmore Administration', 'Garber Field', 'Middlesex'] },
  { "name": "New Africa", "children": ['Wheeler', 'Apiary Building', 'Baker'] },
  { "name": "Newman Center", "children": ['Mahar Auditorium', 'TC - Theta Chi', 'International Programs'] },
  { "name": "North A", "children": ['North B', 'North C', 'Brown', ''] },
  { "name": "North B", "children": ['North D', 'North A', 'Johnson'] },
  { "name": "North C", "children": ['North A', 'North D', 'Montague House'] },
  { "name": "North D", "children": ['North C', 'North B', 'Totman'] },
  { "name": "Oak", "children": ['Tobin', 'Maple', 'Linden'] },
  { "name": "Observatory", "children": ['Dickinson House'] },
  { "name": "Old Chapel", "children": ['Memorial Hall', 'Du Bois Library, W.E.B.', 'Campus Pond', 'Goodell'] },
  { "name": "Olver Design Bldg.", "children": ['Studio Arts Building', 'Fernald', 'Clarke', 'Fine Arts Center', 'Morrill Science Center'] },
  { "name": "Paige", "children": ['Knowles', 'Robotics', 'Holdsworth'] },
  { "name": "Parking Garage", "children": ['Flint Laboratory', 'Machmer', 'Student Union'] },
  { "name": "Parking Office", "children": ['Forest & Parks Building', 'Transit Facility', 'Lorden Field'] },
  { "name": "Patterson", "children": ['Washington', 'John Adams', 'ATG - Alpha Tau Gamma'] },
  { "name": "Photo Laboratory", "children": ['Machmer', 'Thompson', 'Blaisdell'] },
  { "name": "Physical Plant", "children": ['Textbook Annex', 'Bowditch Greenhouses', 'Mullins Practice Rink'] },
  { "name": "Physical Sciences Bldg.", "children": ['West Experiment Station', 'Goessmann', 'Lederle Graduate Research Center', 'Knowlton'] },
  { "name": "Pierpont", "children": ['Cance', 'Moore', 'Berkshire Dining', 'Toddler House'] },
  { "name": "Police", "children": ['Cashin', 'Grayson'] },
  { "name": "Prince", "children": ['Chabad House', 'Kennedy', 'Crampton', 'Coolidge'] },
  { "name": "PVTA Bus Garage", "children": ['Transit Facility', 'Auxillary Services Warehouse', 'Engineering Laboratory 2', 'Computer Science Bldg.']},
  { "name": "Recreation Center", "children": ['Birch', 'Grinnell', 'Dickinson Hall', 'Champions Center', 'Sycamore', 'Mullins Center'] },
  { "name": "Renaissance Center", "children": ['UMass Police Department'] },
  { "name": "Dickinson Hall", "children": ['George N. Parks Marching Band Bld','Goodell', 'Sycamore', 'Grinnell', 'South College','Recreation Center'] },
  { "name": "Robotics", "children": ['Duda', 'Marston', 'Paige', 'Engineering Laboratory 2'] },
  { "name": "Robsham Visitors Center", "children": ['Alfond', 'PKP - Pi Kappa Phi', 'Gordan'] },
  { "name": "Rudd Field", "children": ['Track & Field', 'Sortino Softball Complex','Bowditch Lodge'] },
  { "name": "Shade Tree Laboratory", "children": ['Clark', 'University Club', 'Franklin Dining', 'Morrill Science Center', 'French'] },
  { "name": "Skinner", "children": ['Life Science Laboratory', 'Integrated Science Building', 'Hasbrouck', 'Integrative Learning Center','Morrill Science Center'] },
  { "name": "Sortino Softball Complex", "children": ['Rudd Field', 'Bowditch Lodge','Emerson'] },
  { "name": "South College", "children": ['Du Bois Library, W.E.B.', 'George N. Parks Marching Band Bld', 'Thompson', 'Goodell'] },
  { "name": "Stockbridge", "children": ['Hatch','Draper', 'Chenoweth','Agricultural Engineering Bldgs.', 'Flint Laboratory'] },
  { "name": "Student Union", "children": ['Integrative Learning Center', 'Campus Pond', 'Lincoln Campus Center', 'Du Bois Library, W.E.B.', 'Parking Garage', 'Machmer'] },
  { "name": "Studio Arts Building", "children": ['Olvr Design Bldg', 'PSK - Phi Sigma Kappa','TC - Theta Chi','Gorman', 'Fernald'] },
  { "name": "Sycamore", "children": ['Birch', 'Elm', 'Oak', 'Dickinson Hall', 'Recreation Center'] },
  { "name": "Tennis Courts", "children": ['Mullins Center', 'Lorden Field', 'Central Heating Plant', 'Athletic Fields'] },
  { "name": "Textbook Annex", "children": ['Physical Plant', 'Cold Storage Bldg.', 'Photo Laboratory'] },
  { "name": "Thatcher", "children": ['Lewis', 'Lyon', 'Worcester Dining'] },
  { "name": "Thompson", "children": ['Machmer', 'Photo Laboratory', 'Blaisdell', 'George N. Parks Marching Band Bld', 'South College'] },
  { "name": "Thoreau", "children": ['Melville', 'Kennedy', 'Hampshire Dining', 'Army ROTC Bldg.'] },
  { "name": "Tobin", "children": ['Oak', 'Bartlett', 'Garber Field', 'Elm'] },
  { "name": "Toddler House", "children": ['Bowditch Lodge', 'Farley Lodge','Pierpont'] },
  { "name": "Totman", "children": ['North D', 'Dwight', 'Leach', 'KS - Kappa Sigma'] },
  { "name": "Track & Field", "children": ['Rudd Field'] },
  { "name": "Transit Facility", "children": ['PVTA Bus Garage', 'Forest & Parks Buildings', 'Bowditch', 'Parking Office'] },
  { "name": "UMass Police Department", "children": ['Renaissance Center', 'Cashin', 'Grayson', 'CO - Chi Omega'] },
  { "name": "University Club", "children": ['Shade Tree Laboratory', 'Wilder', 'Morrill Science Center', 'French'] },
  { "name": "University Health Center", "children": ['Brooks', 'Brett', 'Durfee Conservatory & Garden', "Chancellor's House", 'French'] },
  { "name": "Van Meter", "children": ['Greenough', 'Chadbourne', 'Butterfield'] },
  { "name": "Washington", "children": [] },
  { "name": "Webster", "children": [] },
  { "name": "West Experiment Station", "children": [] },
  { "name": "Wheeler", "children": [] },
  { "name": "Whitmore Administration Bldg.", "children": [] },
  { "name": "Wilder", "children": [] },
  { "name": "Worcester Dining", "children": [] },
  { "name": "Wysocki House", "children": [] },
]


def populate():
    with open(inputFile) as locationFile:
        content = locationFile.readlines()
        for location in content:
            location = location.strip()
            resultName = ''
            for char in location:
                if(char.isnumeric()):
                    resultName = resultName[:-2]
                else:
                    resultName+=char
            campusLocations.append({'name': resultName , 'children' : []})

    
    print(campusLocations)

## populate() used initially to populate the campusLocationsList