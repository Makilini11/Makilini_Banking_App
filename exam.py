from datetime import datetime

def show_current_date():
    current_date = datetime.now().strftime("%Y-%m-%d")
    print("Current Date:", current_date)
show_current_date()