import geocoder

def get_location():
    g = geocoder.ip('me')
    if g.ok:
        return f"You are currently in {g.state}, {g.country}."
    return "I couldn't detect your location."



