import sys;
import os;
import gzip;

if __name__ == '__main__':
    # Read arguments from command line, or use sane defaults for IDE.
    argv_len = len(sys.argv)
    inputFile = 'locations.text'

# make this a dict instead of a list for time complexity
campusLocations = [ # will create an api for this
  { "name": "Agricultural Engineering Bldgs.", "children": ['Hatch', 'Holdsworth', 'Cold Storage Bldg.', 'Chenoweth', 'Bowditch Greenhouses'] },
  { "name": "Agricultural Learning Center", "children": [] },
  { "name": "Alfond", "children": ['Isenberg School of Management','Mahar Auditorium','Haigis Mall' ] },
  { "name": "Apiary Building", "children": ['Gorman', 'Wheeler' , 'New Africa'] },
  { "name": "Army ROTC Bldg.", "children": ['Berkshire', 'Boyden Gym', 'Melville'] },
  { "name": "Arnold", "children": ['Hamlin', 'Knowlton', 'Lederle Graduate Research Ctr.'] },
  { "name": "Astronomy Bldg.", "children": ['Gunness Engineering', 'Engineering Laboratory', 'Duda'] },
  { "name": "Athletic Fields", "children": ['Tennis Courts', 'Champions Center'] },
  { "name": "Auxiliary Services Warehouse", "children": ['Forest & Parks Buildings', 'PVTA Bus Garage'] },
  { "name": "Baker", "children": ['Chadbourne', 'Greenough' , 'Brooks'] },
  { "name": "Bartlett", "children": ['Tobin', 'Memorial Hall', 'Herter' ] },
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
  { "name": "Crotty Hall", "children": ['Gordon', 'SDT - Sigma Delta Tau', 'IGU - Iota Gamma Upsilon'] },
  { "name": "Dickinson Hall", "children": ['Sycamore', 'Recreation Center','Goodell', 'George N. Parks Marching Band Bld'] },
  { "name": "Dickinson House", "children": ['Webster', 'Grayson', "Chancellor's House", 'Observatory'] },
  { "name": "Draper", "children": ['Knowles', 'Goessmann', 'Bowker Auditorium (Stockbridge)', 'Lincoln Campus Center'] },
  { "name": "Du Bois Library, W.E.B.", "children": ['Old Chapel', 'South College', 'Machmer', 'Student Union', 'Campus Pond'] },
  { "name": "Duda", "children": ['Engineering Laboratory', 'Engineering Laboratory 2', 'Robotics', 'Gunness Engineering', 'Astronomy Bldg.'] },
  { "name": "Durfee Conservatory & Garden", "children": ['University Health Center', 'French'] },
  { "name": "Dwight", "children": ['Leach', 'Johnson', 'Totman'] },
  { "name": "East Experiment Station", "children": [] },
  { "name": "Elm", "children": [] },
  { "name": "Emerson", "children": [] },
  { "name": "Engineering Laboratory", "children": [] },
  { "name": "Engineering Laboratory 2", "children": [] },
  { "name": "Farley Lodge", "children": [] },
  { "name": "Fernald", "children": [] },
  { "name": "Field", "children": [] },
  { "name": "Fine Arts Center", "children": [] },
  { "name": "Flint Laboratory", "children": [] },
  { "name": "Forest & Parks Buildings", "children": [] },
  { "name": "Franklin Dining", "children": [] },
  { "name": "ATG - Alpha Tau Gamma", "children": [] },
  { "name": "CO - Chi Omega", "children": [] },
  { "name": "IGU - Iota Gamma Upsilon", "children": [] },
  { "name": "KKG - Kappa Kappa Gamma", "children": [] },
  { "name": "KS - Kappa Sigma", "children": [] },
  { "name": "PSK - Phi Sigma Kappa", "children": [] },
  { "name": "PKA - Pi Kappa Alpha", "children": [] },
  { "name": "PKP - Pi Kappa Phi", "children": [] },
  { "name": "SDT - Sigma Delta Tau", "children": [] },
  { "name": "SK - Sigma Kappa", "children": [] },
  { "name": "TC - Theta Chi", "children": [] },
  { "name": "French", "children": [] },
  { "name": "Furcolo", "children": [] },
  { "name": "Garber Field", "children": [] },
  { "name": "George N. Parks Marching Band Bld", "children": [] },
  { "name": "Goessmann", "children": [] },
  { "name": "Goodell", "children": [] },
  { "name": "Gordon", "children": [] },
  { "name": "Gorman", "children": [] },
  { "name": "Grayson", "children": [] },
  { "name": "Greenough", "children": [] },
  { "name": "Grinnell Arena", "children": [] },
  { "name": "Gunness Engineering", "children": [] },
  { "name": "Hadley Equestrian Farm", "children": [] },
  { "name": "Haigis Mall", "children": [] },
  { "name": "Hamlin", "children": [] },
  { "name": "Hampden Dining", "children": [] },
  { "name": "Hampshire", "children": [] },
  { "name": "Hampshire Dining", "children": [] },
  { "name": "Hasbrouck", "children": [] },
  { "name": "Hatch", "children": [] },
  { "name": "Health Center", "children": [] },
  { "name": "Herter", "children": [] },
  { "name": "Hicks Physical Education", "children": [] },
  { "name": "Hillel House", "children": [] },
  { "name": "Holdsworth", "children": [] },
  { "name": "Hotel", "children": [] },
  { "name": "Integrated Science Building", "children": [] },
  { "name": "Integrative Learning Center", "children": [] },
  { "name": "International Programs", "children": [] },
  { "name": "Intermed. Processing Fac. (IPF)", "children": [] },
  { "name": "Isenberg School of Management", "children": [] },
  { "name": "James", "children": [] },
  { "name": "John Adams", "children": [] },
  { "name": "John Q. Adams", "children": [] },
  { "name": "Johnson", "children": [] },
  { "name": "Kennedy", "children": [] },
  { "name": "Knowles", "children": [] },
  { "name": "Knowlton", "children": [] },
  { "name": "Leach", "children": [] },
  { "name": "Lederle Graduate Research Ctr.", "children": [] },
  { "name": "Lewis", "children": [] },
  { "name": "Library, W.E.B. Du Bois", "children": [] },
  { "name": "Life Science Lab C", "children": [] },
  { "name": "Lincoln Apartments", "children": [] },
  { "name": "Lincoln Campus Center", "children": [] },
  { "name": "Linden", "children": [] },
  { "name": "Lorden Field (Baseball)", "children": [] },
  { "name": "Lyon", "children": [] },
  { "name": "Machmer", "children": [] },
  { "name": "MacKimmie", "children": [] },
  { "name": "Mahar Auditorium", "children": [] },
  { "name": "Maple", "children": [] },
  { "name": "Marcus", "children": [] },
  { "name": "Marston", "children": [] },
  { "name": "Martin Jacobson Football", "children": [] },
  { "name": "Performance Center", "children": [] },
  { "name": "Mather", "children": [] },
  { "name": "McGuirk Alumni Stadium", "children": [] },
  { "name": "McNamara", "children": [] },
  { "name": "Melville", "children": [] },
  { "name": "Memorial Hall", "children": [] },
  { "name": "Middlesex", "children": [] },
  { "name": "Montague House", "children": [] },
  { "name": "Moore", "children": [] },
  { "name": "Morrill Science Center", "children": [] },
  { "name": "Mullins Center", "children": [] },
  { "name": "Mullins Practice Rink", "children": [] },
  { "name": "Munson", "children": [] },
  { "name": "New Africa", "children": [] },
  { "name": "Newman Center", "children": [] },
  { "name": "North A", "children": [] },
  { "name": "North B", "children": [] },
  { "name": "North C", "children": [] },
  { "name": "North D", "children": [] },
  { "name": "North Village Apartments", "children": [] },
  { "name": "Northeast Residential Area", "children": [] },
  { "name": "Oak", "children": [] },
  { "name": "Observatory", "children": [] },
  { "name": "Old Chapel", "children": [] },
  { "name": "Olver Design Bldg.", "children": [] },
  { "name": "Orchard Hill Residential Area", "children": [] },
  { "name": "Paige", "children": [] },
  { "name": "Parking Garage", "children": [] },
  { "name": "Parking Office", "children": [] },
  { "name": "Patterson", "children": [] },
  { "name": "Photo Laboratory", "children": [] },
  { "name": "Physical Plant", "children": [] },
  { "name": "Physical Sciences Bldg.", "children": [] },
  { "name": "Pierpont", "children": [] },
  { "name": "Police", "children": [] },
  { "name": "Prince", "children": [] },
  { "name": "PVTA Bus Garage", "children": [] },
  { "name": "Recreation Center", "children": [] },
  { "name": "Renaissance Center", "children": [] },
  { "name": "Residence Hall Security (Dickinson)", "children": [] },
  { "name": "Robotics", "children": [] },
  { "name": "Robsham Visitors Center", "children": [] },
  { "name": "Rudd Field (Soccer)", "children": [] },
  { "name": "Shade Tree Laboratory", "children": [] },
  { "name": "Skinner", "children": [] },
  { "name": "Sortino Softball Complex", "children": [] },
  { "name": "South College", "children": [] },
  { "name": "Southwest Residential Area", "children": [] },
  { "name": "Stockbridge", "children": [] },
  { "name": "Student Union", "children": [] },
  { "name": "Studio Arts Building", "children": [] },
  { "name": "Sycamore", "children": [] },
  { "name": "Sylvan Residential Area", "children": [] },
  { "name": "Telecommunications Office", "children": [] },
  { "name": "Tennis Courts", "children": [] },
  { "name": "Textbook Annex", "children": [] },
  { "name": "Thatcher", "children": [] },
  { "name": "Thompson", "children": [] },
  { "name": "Thoreau", "children": [] },
  { "name": "Tillson Farm", "children": [] },
  { "name": "Tobin", "children": [] },
  { "name": "Toddler House", "children": [] },
  { "name": "Totman", "children": [] },
  { "name": "Track & Field", "children": [] },
  { "name": "Transit Facility", "children": [] },
  { "name": "UMass Police Department", "children": [] },
  { "name": "University Club", "children": [] },
  { "name": "University Extension", "children": [] },
  { "name": "University Health Center", "children": [] },
  { "name": "University Press (E. Exp. Station)", "children": [] },
  { "name": "University Without Walls", "children": [] },
  { "name": "Van Meter", "children": [] },
  { "name": "Visitors Center", "children": [] },
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