# Box Office Agent

The application uses "cmd" module to imitate a command line style interaction.

Start the app by `./agent.py`

Help on operation
---
Type `?` or `help` for an overview of all possible commands.

Specific instruction of an operation can be viewed by `help <command>` or `?buy`

### buy:
Buy a ticket. e.g.`buy 20180412 n 3`

    Input: buy <date> <showtime> <auditorium>
    <date> format: yyyymmdd
    <showtime>: m for matinee, n for night
    <auditorium>: 1 - 5

### refund
Refund with specific serial number. (given by "buy" command) e.g. `refund`
    
    Input: refund <serial_number>
    <serial_number> is provided when you buy the ticket.
    
### r_day
Report of a certain day. e.g. `r_day 20180412`

    Generate a report of the total number of tickets sold on any given date
    Input: <date>
    Print: ticket sale for the day.
    <date> format: yyyymmdd
    
### r_event
Report of an event. e.g. `r_event 20180412 n 3`

    Generate a report of the number of tickets sold and number of vacant seats
    for any given showtime, past or future
    Input: r_event <date> <showtime> <auditorium>
    Print: ticket sale for the specific event, if exists.
    <date> format: yyyymmdd
    <showtime>: m for matinee, n for night
    <auditorium>: 1 - 5
