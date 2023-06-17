def is_lucky_ticket(ticket_number):
    ticket_str = str(ticket_number)

    if len(ticket_str) != 6:
        return False

    first_half_sum = sum(int(digit) for digit in ticket_str[:3])
    second_half_sum = sum(int(digit) for digit in ticket_str[3:])

    if first_half_sum == second_half_sum:
        return True
    else:
        return False



ticket1 = 385916
ticket2 = 123456

if is_lucky_ticket(ticket1):
    print(f"Билет {ticket1} - счастливый")
else:
    print(f"Билет {ticket1} - несчастливый")

if is_lucky_ticket(ticket2):
    print(f"Билет {ticket2} - счастливый")
else:
    print(f"Билет {ticket2} - несчастливый")
