"""Eventbrite API

Usage:
Current attendees are saved in 'attendees.db'
"""
import cStringIO
import json
import pickle
import pycurl

c = pycurl.Curl()

PERSONAL_TOKEN =  ''
assert PERSONAL_TOKEN != '', 'Please provide a PERSONAL_TOKEN'

def get_current_attendees():
    try:
        attendees = pickle.load(open("attendees.db", "rb"))
    except IOError:
        attendees = {'attendees':[]}
        pickle.dump(attendees, open("attendees.db", "wb"))
    return attendees['attendees']

def set_current_attendees(attendee_list):
    attendee_dict = {'attendees': attendee_list}
    pickle.dump(attendee_dict, open("attendees.db", "wb"))

def get_new_attendees():
    curr = get_current_attendees()
    all_attendees_info = get_eventbrite_attendees()
    all_attendees = [user['profile']['company'] for user in all_attendees_info]
    new = list(set(all_attendees) - set(curr))
    return new

def get_eventbrite_attendees():
    buf = cStringIO.StringIO()
    url = "https://www.eventbriteapi.com/v3/events/15296139164/attendees/?token=" + PERSONAL_TOKEN
    c.setopt(c.URL, url)
    c.setopt(c.WRITEFUNCTION, buf.write)
    c.perform()
    jsonBuf = json.loads(buf.getvalue())
    return jsonBuf['attendees']

def main():
    pass

if __name__ == "__main__":
    main()
