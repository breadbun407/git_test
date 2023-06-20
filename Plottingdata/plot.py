import matplotlib.pyplot as plt
import seaborn as sns

# Sample data (replace this with your extracted and prepared data)
timeline_data = [
    {"event": "Event 1", "start_date": "2023-06-01", "end_date": "2023-06-05"},
    {"event": "Event 2", "start_date": "2023-06-08", "end_date": "2023-06-10"},
    {"event": "Event 3", "start_date": "2023-06-12", "end_date": "2023-06-15"},
    # Add more timeline data
]

# Set Seaborn style
sns.set()

# Plotting the timeline
fig, ax = plt.subplots()

for index, event in enumerate(timeline_data):
    start_date = event["start_date"]
    end_date = event["end_date"]
    event_name = event["event"]
    
    # Plot a horizontal bar for each event
    ax.barh(index, width=(end_date - start_date), left=start_date, height=0.5, align='center')
    # Add event name as a label
    ax.text(start_date, index, event_name, ha='right', va='center')

# Customize the plot as needed (e.g., axis labels, title, etc.)
plt.xlabel('Date')
plt.ylabel('Event')
plt.title('Timeline View')

# Adjust the appearance of the timeline
ax.invert_yaxis()  # Invert the y-axis to have events listed from top to bottom
ax.xaxis_date()  # Format the x-axis as dates

# Show the plot
plt.show()
