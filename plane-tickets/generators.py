"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    Parameters:
        number (int): Total number of seat letters to be generated.

    Returns:
        generator: A generator that yields seat letters.

    Note:
        Seat letters are generated from A to D.
        After D the sequence starts again with A.
        For example: A, B, C, D, A, B

    """

    list_seatletters = ['A', 'B', 'C', 'D']
    
    count = 0
    while count <= number:
        for seat in list_seatletters:
            count += 1
            if count <= number:
                yield seat 
            else:
                break

        

def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    Parameters:
        number (int): The total number of seats to be generated.

    Returns:
        generator: A generator that yields seat numbers.

    Note:
        A seat number consists of the row number and the seat letter.
        There is no row 13, and each row has 4 seats.

        Seats should be sorted from low to high.
        For example: 3C, 3D, 4A, 4B

    """

    list_seatletters = ['A', 'B', 'C', 'D']
    
    if (number // 4) % 4 == 0 and number not in (1,2,3):
        floor_seatnum = number // 4
    else:
        floor_seatnum = (number // 4) + 1
    
    count = 0
    for seat_number in range(1, floor_seatnum+1):
        if seat_number == 13:
            continue
        
        for seat in list_seatletters:
            count += 1
            if count <= number:
                yield str(seat_number) + seat
            else:
                return


def assign_seats(passengers):
    """Assign seats to passengers.

    Parameters:
        passengers (list[str]): A list of strings containing names of passengers.

    Returns:
        dict: With passenger names as keys and seat numbers as values.
        Example output: {"Adele": "1A", "Björk": "1B"}

    """

    number_passangers = len(passengers)
    dict_pass = {}
    
    for index, seat in enumerate(generate_seats(number_passangers)):
        dict_pass[passengers[index]] = seat
    return dict_pass


def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    Parameters:
        seat_numbers (list[str]): A list of seat numbers.
        flight_id (str): A string containing the flight identifier.

    Returns:
        generator: A generator that yields 12 character long ticket codes.

    """

    for num in seat_numbers:
        code_str = num + flight_id
        num_zeros = 12 - len(code_str)
        yield code_str + str(0) * num_zeros
