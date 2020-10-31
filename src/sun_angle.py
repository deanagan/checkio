from datetime import datetime as dt
from math import floor

def sun_angle(time: str) -> [int, str]:
    ref_time = dt.strptime('06:00', '%H:%M')
    fmt_time = dt.strptime(time, '%H:%M')
    angle = floor((fmt_time - ref_time).seconds // 60 * 0.25)
    return angle if 0 <= angle <= 180 else "I don't see the sun!"
