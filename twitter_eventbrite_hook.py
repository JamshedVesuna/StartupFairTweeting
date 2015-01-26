from eventbrite import get_and_set_new_attendees
from random import choice
from send_email import send_email
from tweeper import update_status

happy_words = ['Happy', 'Glad', 'Excited', 'Thrilled']
incomplete_sentences = [
    'Happy to have {0} joining us at the UCB Startup Fair!',
    'Excited to announce that {0} is coming to the Startup Fair!',
    'Glad to have {0} at the Startup Fair this year!',
    'Welcoming {0} to the UCB Startup Fair!',
    '{0} just signed up for the U.C. Berkeley Starup fair!',
    '{0} is coming to the UCB Startup Fair!',
    'Come check out {0} at the UCB Startup Fair!',
    ]

new = get_and_set_new_attendees()
for attendee in new:
    phrase = choice(incomplete_sentences)
    update_status(phrase.format(attendee))
