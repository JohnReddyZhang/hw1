#! /usr/bin/env python3
# Python 3
# Example for how to build a command-line application

import cmd
from function import BOffice


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