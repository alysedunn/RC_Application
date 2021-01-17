#!/usr/bin/env python3

"""
This is a short program that I wrote to solve a problem that I encountered during my time in the professional women's
organization. The Cru (https://www.thecru.com/). As a member of The Cru, you are assigned a 'Cru', which is a group of
10 or fewer other women with whom you meet with on a regular (usually monthly) basis. During the meetings, each member
takes a few minutes to present on a problem that they'd like help with. While one participant presents, a different
participant must take notes for the speaker, and a different participant must keep time for the speaker (so one speaker,
one participant taking notes, one participant keeping time, and everyone else listening and providing feedback). Within
our Cru, we were consistently wasting time at the beginning of each meeting trying to designate who would take notes
for whom, and who would keep time for whom. So, I developed this short script that takes a list of Cru attendees as the
input (because all member of the Cru might not attend each week), and creates assignments for who will takes notes for
whom, and who will keep time for whom. Other criteria that this script takes into account:
 - The first person to present during a Cru meeting should be randomized, so that the same person doesn't end up going
   first too often
 - Cru members who just presented should not have to immediately keep time or take notes right after their presentation,
   in order to give the presenter some time and space to digest their presentation feedback.


This program can be run with Python 2 or Python 3. Depending on your environment setup, the program can be run with one
(or both) of the following commands:

$ python2 cru_rotation.py --members_present 'Alyse' 'Amber' 'Gretchen' 'Kaydene' 'Alexis' 'Jessica' 'Monica' 'Adrian'
$ python3 cru_rotation.py --members_present 'Alyse' 'Amber' 'Gretchen' 'Kaydene' 'Alexis' 'Jessica' 'Monica' 'Adrian'

Example output:




Alyse Dunn
alyse.dunn@gmail.com
February 2021
"""

import argparse
import logging
import random
from collections import deque
from copy import copy

logging.basicConfig(format="%(message)s", level=logging.INFO)


parser = argparse.ArgumentParser(description='List of attendees.')
parser.add_argument(
    '--members_present',
    type=str,
    nargs='*',
    help='A list of the first names of all Cru members present at the meeting.'
)


def main(members_present):
    """
    Returns a rotation of presenters, notetakers, and timekeepers
    :param members_present: A list of the first names of Cru members who are present at the current meeting
    :return: None, but prints a list of presenters, notetakers, and timekeepers, in order
    """
    presentation_tuples = []

    logging.debug("Cru members present this meeting: %s", (", ".join(members_present)))

    random.shuffle(members_present)
    presenter_order = members_present
    logging.info("\nPresenter order: %s", (", ".join(presenter_order)))

    shuffled_members_deque = deque(members_present)

    note_taker_order = copy(shuffled_members_deque)
    note_taker_order.rotate(2)
    logging.info("Note taker order: %s", (", ".join(note_taker_order)))

    time_keeper_order = copy(shuffled_members_deque)
    time_keeper_order.rotate(3)
    logging.info("Time keeper order: %s\n", (", ".join(time_keeper_order)))

    for i in range(0, len(presenter_order)):
        logging.info(
            "Presenter: '%s'.  Note-taker: '%s'.  Time keeper: '%s'.",
            presenter_order[i], note_taker_order[i], time_keeper_order[i]
        )
    #     presentation_tuples.append(presentation_tuple)
    #
    # for presentation_tuple in presentation_tuples:
    #     logging.info(", ".join(presentation_tuple))


if __name__ == '__main__':
    args = parser.parse_args()
    members_present = args.members_present

    main(members_present)
