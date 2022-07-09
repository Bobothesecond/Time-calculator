
days = [ "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday",
        "sunday"]

def get_days_later(days):
  
  if days == 1:
    return "(next day)"
  elif days > 1:
    return f"({days} days later)"
  return ""

def add_time(start, duration, day=False):



 
  days_later = 0
  whole_day = 24
  half_day = 12
  hours, minutes = start.split(":")
  minutes, period = minutes.split(" ")
  dh, dm = duration.split(":")

  hours = int(hours)
  minutes = int(minutes)
  dh = int(dh)
  dm = int(dm)
  period = period.strip().lower()
  
  total_minutes = minutes + dm
  total_hours = hours + dh

  if total_minutes >= 60:
    total_hours += int(total_minutes/60)
    total_minutes = int(total_minutes % 60)

  if dh or dm:  
    if period == "pm" and total_hours > half_day:
      if total_hours % whole_day >= 1.0:
        days_later += 1

    if total_hours >= half_day:
      hours_remaining = total_hours / whole_day
      days_later += int(hours_remaining)

    tth = total_hours
    while True:
        if tth < half_day:
            break
        if tth >= half_day:
          if period == "am":
              period = "pm"
          elif period == "pm":
              period = "am"
          tth -= half_day
        
  remaining_hours = int(total_hours % half_day) or hours + 1
  remaining_minutes = int(total_minutes % 60)

  results = f'{remaining_hours}:{remaining_minutes:02} {period.upper()}'
  if day:
    day = day.strip().lower()
    selected_day = int((days.index(day) + days_later) % 7)
    current_day = days[selected_day]
    results += f', {current_day.title()} {get_days_later(days_later)}'

  else:
    results = " ".join((results, get_days_later(days_later)))

  return results.strip()

