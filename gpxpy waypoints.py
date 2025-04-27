import gpxpy

# This utility reads in a GPX file with waypoints and outputs an updated version in a format that 
# allows a Wahoo Elemnt Bolt GPS to use the waypoints as proximity alerts when traversing the track.
# 1. Parse the input file as a GPX using gpxpy
# 2. Sort the waypoints by name, so that they are in the correct order they will be passed when traversing the track. 
# 3. For each waypoint in turn, find the next trackpoint that is within 200m of the waypoint. Update the lon/lat co-ordinates
# of the waypoint to match those of the trackpoint. 
# 4. Write the output file from the updated GPX holder.

def wp_distance(wp, tp, radius_metres: int):
    '''Check whether the distance between the waypoint and the trackpoint is within the radius'''
    wp_dist = gpxpy.geo.haversine_distance(wp.latitude, wp.longitude, tp.latitude, tp.longitude)
    print(wp_dist)
    if wp_dist <= radius_metres:
        return True
    return False

def find_match(wp, tr_index):
    '''Loop through the trackpoints starting at the current index, checking whether the distance between the
       waypoint and the current trackpoint is within the radius.
       Returns the index needed for starting the next check'''
    while tr_index < len(tracklist): 
#        print(tr_index)
        if wp_distance(waypoint, tracklist[tr_index],200):
# We have a match, return the index so that next time this function is called, the 
# search begins from the next trackpoint rather than from the beginning again.
# We know this will work because we have ordered the waypoints already.            
            print(waypoint)        
            return tr_index
# This trackpoint didn't match so increment and try again
        tr_index += 1
# We reached the end of the trackpoints with no match, so display an error message and end the whole script.
    print('No match within radius for waypoint', waypoint.description)    

def update_waypoint(wp, tr_index: int):
    '''Updates the waypoint longitude and latitude from the matched trackpoint'''
    wp.longitude = tracklist[tr_index].longitude
    wp.latitude = tracklist[tr_index].latitude

# Load the GPX file
#with open('Waypoint test.gpx', 'r') as gpx_file:
with open('FTITHW 2025.gpx', 'r') as gpx_file:
    gpx = gpxpy.parse(gpx_file)

# Sort the waypoints by name
gpx.waypoints.sort(key=lambda waypoint: waypoint.name)

# Count the number of points
# Generally our input file will have a single track with a single segment, but handle the case of multiple.

tracklist = []
for track in gpx.tracks:
    for segment in track.segments:
        for point in segment.points:
            tracklist.append(point)


# For each waypoint, traverse through the track looking for a point that is with a certain radius (in metres) of the waypoint.
# find_match returns the current position in the track so that we don't start from the beginning each time.
trackindex = 0
for waypoint in gpx.waypoints:
    print(waypoint.description)
    trackindex = find_match(waypoint, trackindex)    
    update_waypoint(waypoint, trackindex)
    trackindex += 1
   


# Write the modified GPX data to a new file
with open('output.gpx', 'w') as gpx_file:
    gpx_file.write(gpx.to_xml())
