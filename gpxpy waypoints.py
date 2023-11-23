import gpxpy

def wp_distance(wp, tp, radius_metres):
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
    while tr_index < tot_points: 
        print(tr_index)
        if wp_distance(waypoint, tracklist[tr_index],200):
# If we have a match, update the waypoint, then increment the index so that next time this function is called, the 
# search begins from the next trackpoint rather than from the beginning again.
# We know this will work because we have ordered the waypoints already.            
            print(waypoint)        
            return tr_index
# This trackpoint didn't match so increment and try again
        tr_index += 1
# We reached the end of the trackpoints with no match, so display an error message and end the whole script.
    print('No match within radius for waypoint', waypoint.description)    

def update_waypoint(wp, tr_index):
    '''Updates the waypoint longitude and latitude from the matched trackpoint'''
    wp.longitude = tracklist[tr_index].longitude
    wp.latitude = tracklist[tr_index].latitude

# Load the GPX file
with open('Waypoint test.gpx', 'r') as gpx_file:
    gpx = gpxpy.parse(gpx_file)

# Sort the waypoints by name
gpx.waypoints.sort(key=lambda waypoint: waypoint.description)

# Count the number of points
# Generally our input file will have a single track with a single segment, but handle the case of multiple.
tot_points = 0
tracklist = []
for track in gpx.tracks:
    for segment in track.segments:
        tot_points += len(segment.points)
        for point in segment.points:
            tracklist.append(point)


# For each waypoint, traverse through the track looking for a point that is with a certain radius (in metres) of the waypoint.
trackindex = 0
for waypoint in gpx.waypoints:
    print(waypoint.description)
    trackindex = find_match(waypoint, trackindex)    
    update_waypoint(waypoint, trackindex)
    trackindex += 1
   


# Save the modified GPX data to a new file
with open('waypoint test fixed.gpx', 'w') as gpx_file:
    gpx_file.write(gpx.to_xml())
