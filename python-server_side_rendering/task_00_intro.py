#!/usr/bin/env python3

def generate_invitations(template, attendees):
    """
    Generate personalized invitation files from template and attendee data.
    
    Args:
        template (str): Template string with placeholders
        attendees (list): List of dictionaries containing attendee data
    """
    # Check if template is a string and attendees is a list
    if not isinstance(template, str):
        print("Error: Template must be a string")
        return
    
    if not isinstance(attendees, list):
        print("Error: Attendees must be a list of dictionaries")
        return
    
    # Validate that attendees contains dictionaries
    for attendee in attendees:
        if not isinstance(attendee, dict):
            print("Error: Attendees must be a list of dictionaries")
            return
    
    # Check for empty template
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    
    # Check for empty attendees list
    if not attendees:
        print("No data provided, no output files generated.")
        return
    
    # Process each attendee
    for index, attendee in enumerate(attendees, 1):
        # Replace placeholders with actual values or "N/A"
        processed_template = template
        processed_template = processed_template.replace("{name}", attendee.get("name", "N/A"))
        processed_template = processed_template.replace("{event_title}", attendee.get("event_title", "N/A"))
        
        # Handle None values for event_date
        event_date = attendee.get("event_date")
        if event_date is None:
            event_date = "N/A"
        processed_template = processed_template.replace("{event_date}", str(event_date))
        
        processed_template = processed_template.replace("{event_location}", attendee.get("event_location", "N/A"))
        
        # Write to output file
        filename = f"output_{index}.txt"
        try:
            with open(filename, 'w') as file:
                file.write(processed_template)
            print(f"Generated {filename}")
        except IOError as e:
            print(f"Error writing to {filename}: {e}")
