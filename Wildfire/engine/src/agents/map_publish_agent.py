from crewai import Agent

def create_map_publish_agent():
    return Agent(
        role='Geospatial Data Publisher',
        goal='Update the system database with new wildfire detections',
        backstory='Database administrator specialized in PostGIS and real-time map updates.',
        verbose=True,
        tools=[] 
    )

def publish_to_db(detection_data):
    print(f"Writing {len(detection_data)} events to PostGIS...")
