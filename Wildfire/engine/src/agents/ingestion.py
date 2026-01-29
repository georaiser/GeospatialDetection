from crewai import Agent

def create_ingestion_agent():
    return Agent(
        role='Satellite Data Ingestion Specialist',
        goal='Download and normalize GOES-16/18 and VIIRS satellite imagery',
        backstory='Expert in remote sensing data acquisition pipelines.',
        verbose=True,
        allow_delegation=False,
        tools=[] # To be populated with ingestion tools
    )
