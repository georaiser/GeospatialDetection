from crewai import Agent

def create_alert_agent():
    return Agent(
        role='Emergency Notification Dispatcher',
        goal='Rapidly disseminate validated fire alerts to relevant stakeholders',
        backstory='Crisis communication coordinator responsible for high-priority alerts.',
        verbose=True,
        tools=[] 
    )

def send_alert(alert_data):
    # This would likely call the Backend API
    print(f"Dispatching alert: {alert_data}")
