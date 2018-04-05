# Python 3
# Example for how to build a command-line application

import cmd
# You can add other imports here if you want

class AppShell(cmd.Cmd):
    intro = "\nWelcome to the My App!\nType `help` or `?` to list commands.\n"
    prompt = '> '
    event = None

    def do_quit(self, arg):
      """Quit"""
      return True

    def do_buy(self, args):
      """Buy a Ticket"""
      print("TO DO: Implement buying a ticket")

    def do_refund(self, args):
      """Refund a Ticket"""
      print("TO DO: Implement refunding a ticket")


if __name__ == '__main__':
    AppShell().cmdloop()
