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
EVENTBRITE_EVENT_ID = ''
assert PERSONAL_TOKEN != '', 'Please provide a PERSONAL_TOKEN'
assert EVENTBRITE_EVENT_ID != '', 'Please provide a EVENTBRITE_EVENT_ID'

def get_current_attendees():
    try:
        attendees = pickle.load(open("attendees.db", "rb"))
    except IOError:
        attendees = {'attendees':[]}
        pickle.dump(attendees, open("attendees.db", "rb"))
    return attendees['attendees']

def set_current_attendees(attendee_list):
    attendee_dict = {'attendees': attendee_list}
    pickle.dump(attendee_dict, open("attendees.db", "wb"))

def get_new_attendees():
    curr = get_current_attendees()
    all_attendees_info = get_eventbrite_attendees()
    all_attendees = [user['profile']['company'] for user in all_attendees_info]
    if not curr:
        return all_attendees
    if not all_attendees:
        return []
    return list(set(all_attendees) - set(curr))

def get_eventbrite_attendees():
    buf = cStringIO.StringIO()
    url = "https://www.eventbriteapi.com/v3/events/{0}/attendees/?token={1}".format(EVENTBRITE_EVENT_ID, PERSONAL_TOKEN)
    c.setopt(c.URL, url)
    c.setopt(c.WRITEFUNCTION, buf.write)
    c.perform()
    jsonBuf = json.loads(buf.getvalue())
    return jsonBuf['attendees']

def get_all_attendees():
    curr = get_current_attendees()
    new = get_new_attendees()
    if not curr:
        return new
    curr.extend(new)
    return curr

def get_and_set_new_attendees():
    new = get_new_attendees()
    set_current_attendees(get_all_attendees())
    return new

def main():
    pass

if __name__ == "__main__":
    main()
