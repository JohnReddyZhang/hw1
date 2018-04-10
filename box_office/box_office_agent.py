#! /usr/bin/env python3
# Python 3
# Example for how to build a command-line application

import cmd
from sys import exit
from datetime import datetime, timedelta


class BOffice(object):
    """
    Box Office class that do the operations.
    """
    def __init__(self):
        self.now = None
        self.tickets = {}
        self.avail_t = timedelta(days=7)
        self.price = ['tier1', 'tier2', 'tier3', 'tier4']

    def buy(self, show_d, show_t, screen):
        self.now = datetime.now()

        info = (show_d, show_t, screen)
        # (date, showtime, auditorium)
        showtime = datetime.strptime(show_d + '1400' if show_t == 'm'
                                     else show_d + '2000',
                                     '%Y%m%d%H%M')

        if showtime - self.now > self.avail_t or showtime < self.now:
            print('Cannot buy tickets for this day.')
            return False
        else:
            price = 'unallocated'
            if showtime.weekday() <= 3:
                if show_t == 'm':
                    price = self.price[0]
                elif show_t == 'n':
                    price = self.price[1]
            else:
                if show_t == 'm':
                    price = self.price[2]
                elif show_t == 'n':
                    price = self.price[3]
        if info in self.tickets.keys():
            if self.tickets[info]['tickets'] == 0:
                print('Ticket for this event is sold out.')
            else:
                serial = ''.join(info) + self.tickets[info]['tickets'].pop()
                self.tickets[info]['serial'].append(serial)
                print('Success! Your serial number: {}\nPrice tier: {}'.format(self.tickets[info]['serial'][-1], price))
        else:
            self.tickets[info] = {'tickets': ['{:0<3}'.format(str(i)) for i in range(0, 200)],
                                  'price': price,
                                  'serial': []}
            serial = ''.join(info) + self.tickets[info]['tickets'].pop()
            self.tickets[info]['serial'].append(serial)
            print('Success! Your serial number: {}\nPrice tier: {}'.format(self.tickets[info]['serial'][-1], price))

    def refund(self, serial):
        self.now = datetime.now()

        info = (serial[0: 8], serial[8], serial[9])
        show_d, show_t, screen = info
        # (date, showtime, auditorium)
        showtime = datetime.strptime(show_d+'1400' if show_t == 'm'
                                     else show_d + '2000',
                                     '%Y%m%d%H%M')
        if info in self.tickets.keys() and serial in self.tickets[info]['serial']:
            # If the ticket exists, check whether the time has past.
            if showtime < self.now:
                print('Cannot refund. Time has past.')
            else:
                print('Refund value: {}'.format(self.tickets[info]['price']))
                self.tickets[info]['serial'].remove(serial)
                self.tickets[info]['tickets'].append(serial[10:])
        else:
            print('Did not find ticket record for this event.')

    def r_event(self, show_d, show_t, screen):
        info = (show_d, show_t, screen)
        # print(info)
        if info in self.tickets.keys():
            print('Current event on {} {} in Auditorium {}\n'
                  'has sold {} tickets, has {} vacant seats'
                  .format(show_d, 'Matinee' if show_t == 'm' else 'Night', screen,
                          200 - self.tickets[info]['tickets'], self.tickets[info]['tickets']))
        else:
            print('Did not find event.')

    def r_day(self, day):
        sold = 0
        if self.tickets == {}:
            print('No data found.')
        else:
            for info, value in self.tickets.items():
                if info[0] == day:
                    sold += (200 - len(value['tickets']))
            print('{} tickets sold on day {}'.format(sold, day))


class AppShell(cmd.Cmd):
    intro = "\nWelcome to the Box Office!\nType `help` or `?` to list commands.\nType `quit` to exit app."
    prompt = '> '

    def __init__(self):
        super().__init__()
        self.b_office = BOffice()

    @staticmethod
    def do_quit(args=''):
        """
        Quit by typing 'quit' command.
        """
        print('Goodbye. {}'.format(args))
        exit()

    def do_buy(self, args):
        """
        Buy a Ticket
        Input: buy <date> <showtime> <auditorium>
        <date> format: yyyymmdd
        <showtime>: m for matinee, n for night
        <auditorium>: 1 - 5
        """
        self.b_office.buy(*args.split(' '))

    def do_refund(self, args):
        """
        Refund a Ticket
        Input: refund <serial_number>
        <serial_number> is provided when you buy the ticket.
        """
        # print("TO DO: Implement refunding a ticket")
        self.b_office.refund(*args.split(' '))

    def do_r_event(self, args):
        """
        Generate a report of the number of tickets sold and number of vacant seats
        for any given showtime, past or future
        Input: r_event <date> <showtime> <auditorium>
        Print: ticket sale for the specific event, if exists.
        <date> format: yyyymmdd
        <showtime>: m for matinee, n for night
        <auditorium>: 1 - 5
        """
        self.b_office.r_event(*args.split(' '))

    def do_r_day(self, args):
        """
        Generate a report of the total number of tickets sold on any given date
        Input: <date>
        Print: ticket sale for the day.
        <date> format: yyyymmdd
        """
        self.b_office.r_day(*args.split(' '))

    def emptyline(self):
        print('Did not receive entry.{}'.format(self.intro))

    # def precmd(self, line):
    #     line = line.lower()
    #     return line


if __name__ == '__main__':
    AppShell().cmdloop()