time_string = '1h 45m,360s,25m,30m 120s,2h 60s'

def transformed_times(time):
    time_values = time.split(',')

    total_minutes = 0

    for time_value in time_values:
        components = time_value.replace(' ', ',').split(',')
    
        for component in components:
            if 'h' in component:
                hours = int(component.replace('h', ''))
                total_minutes += hours * 60
            elif 'm' in component:
                minutes = int(component.replace('m', ''))
                total_minutes += minutes
            elif 's' in component:
                seconds = int(component.replace('s', ''))
                total_minutes += seconds // 60
    return round(total_minutes)

