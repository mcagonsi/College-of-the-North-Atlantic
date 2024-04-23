from datetime import datetime
import locale


def get_arrival_date():
    while True:
        date_str = input("Enter arrival date (YYYY-MM-DD): ")
        try:
            arrival_date = datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            print("Invalid date entered. Please try again\n")
            continue

        now = datetime.now()
        today = datetime(now.year, now.month, now.day)
        if arrival_date < today:
            print("Enter the correct arrival date, it should be today or later. Try again\n")
        else:
            return arrival_date


def get_departure_date(arrival_date):
    while True:
        date_str = input("Enter departure date (YYYY-MM-DD): ")
        try:
            departure_date = datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            print("Invalid date entered. Please try again\n")
            continue

        if departure_date <= arrival_date:
            print("Enter the correct arrival date, it should be today or later. Try again\n")
        else:
            return departure_date


def main():
    print("The Hotel Reservation Program\n")

    do_again = 'y'
    while do_again.lower() == 'y':
        # Get the datetime from user
        arrival_date = get_arrival_date()
        departure_date = get_departure_date(arrival_date)
        print()

        # Calculate costs
        rate = 85.0
        rate_message = ''
        if arrival_date.month == 8:
            rate = 105
            rate_message = "(High Season)"
        total_nights = (departure_date - arrival_date).days
        total_cost = rate * total_nights

        # Formatting
        date_format = '%B %d, %Y'
        locale.setlocale(locale.LC_ALL, 'en_CA')
        print(f"Arrival Date:   {arrival_date:{date_format}}")
        print(f"Departure Date: {departure_date:{date_format}}")
        print(f"Nightly rate:   {locale.currency(rate)} {rate_message}")
        print(f"Total nights:   {total_nights}")
        print(f"Total price:    {locale.currency(total_cost)}\n")

        # Update do_again
        do_again = input("Continue? (y/n): ")
        print()

    print("Bye!")


if __name__ == '__main__':
    main()
