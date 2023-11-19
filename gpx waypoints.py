import xml.etree.ElementTree as ET
# Import the xml.etree.ElementTree module

# Define a function to parse a GPX file and return a list of points
def parse_gpx(file):
    # Create an empty list to store the points
    points = []
    # Parse the XML file using ElementTree
    tree = ET.parse(file)
    # Get the root element of the tree
    root = tree.getroot()
    # Find all the waypoint elements in the tree
    waypoints = root.findall(".//{http://www.topografix.com/GPX/1/1}wpt")
    # Loop through the waypoints
    for waypoint in waypoints:
        # Get the latitude and longitude attributes of the waypoint
        lat = waypoint.get("lat")
        lon = waypoint.get("lon")
        name = waypoint.find("{http://www.topografix.com/GPX/1/1}name")
        desc = waypoint.find("{http://www.topografix.com/GPX/1/1}desc")
        # Get the text content of the name and description elements, or use empty strings if they are None
        name_text = name.text if name is not None else ""
        desc_text = desc.text if desc is not None else ""
        # Create a tuple with the latitude and longitude, name and desc
        point = (lat, lon, name_text, desc_text)
        # Append the point to the list
        points.append(point)
    # Find all the trackpoint elements in the tree
    trackpoints = root.findall(".//{http://www.topografix.com/GPX/1/1}trkpt")
    # Loop through the trackpoints
    for trackpoint in trackpoints:
        # Get the latitude and longitude attributes of the trackpoint
        lat = trackpoint.get("lat")
        lon = trackpoint.get("lon")
        # Create a tuple with the latitude and longitude
        point = (lat, lon)
        # Append the point to the list
        points.append(point)
    # Return the list of points
    return points

# Example usage
# Assume the GPX file is named "example.gpx" and is in the same directory as this script
points = parse_gpx("Waypoint test.gpx")
# Print the list of points
print(points)
