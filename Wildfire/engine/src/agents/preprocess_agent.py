from crewai import Agent

def create_preprocess_agent():
    return Agent(
        role='Satellite Imagery Preprocessor',
        goal='Prepare raw satellite data for AI inference',
        backstory='Specialist in radiometric calibration, cloud masking, and thermal anomaly extraction.',
        verbose=True,
        allow_delegation=False,
        tools=[] 
    )

def cloud_masking_routine(data_path):
    print(f"Applying cloud mask to {data_path}")
    return True
