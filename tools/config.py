"""Site-wide settings. Edit here, then run:  python tools/build.py
(This file is the one place for phone, domain, license, review link, etc.)"""
DOMAIN = "https://reliantconsultingandconstruction.com"
NAME = "Reliant Consulting and Construction"
PHONE_DISPLAY = "(770) 508-0971"
PHONE_TEL = "+17705080971"
LICENSE = "RLCO004774"
# Put the link to your Google reviews here once you have it (empty = button hidden)
HOURS_TEXT = "Mon-Fri 8:00 AM - 6:00 PM, closed weekends"
GOOGLE_REVIEWS_URL = "https://maps.google.com/?cid=6322770047744090751"
# Chosen Nov 16, 2026 from the Google reviews (word for word). The live Google list is no longer shown on the site,
# only the star rating and a link, so off-topic reviews do not appear.
# Real customer reviews: add as {"name": "...", "text": "...", "town": "..."}; nothing is invented.
REVIEWS = [
    {"name": "Mike Rhodes", "text": "Dylan and his team are professional and do exceptional work while keeping ongoing communication during the process."},
    {"name": "Sydni Rhodes", "text": "I've had nothing but great experiences with Dylan and his work. He's quick, reliable, reasonably priced, and does great work! I'm a real estate agent and have had him do everything from small painting jobs, pressure washing, and working on our sign that needed to be secured. Highly recommend!"},
]
TOWNS = [
    ("jasper", "Jasper", "Pickens County"),
    ("alpharetta", "Alpharetta", "Fulton County"),
    ("canton", "Canton", "Cherokee County"),
    ("woodstock", "Woodstock", "Cherokee County"),
    ("cumming", "Cumming", "Forsyth County"),
    ("milton", "Milton", "Fulton County"),
    ("ball-ground", "Ball Ground", "Cherokee County"),
    ("marietta", "Marietta", "Cobb County"),
]
