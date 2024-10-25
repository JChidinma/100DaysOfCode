class FlightData:

    def __init__(self, price, origin_airport, destination_airport, out_date, return_date, stops):
        """
        Constructor for initializing a new flight data instance with specific travel details.
        Parameters:
        - price: The cost of the flight in CAD.
        - origin_airport: The IATA code for the flight's origin airport.
        - destination_airport: The IATA code for the flight's destination airport.
        - out_date: The departure date for the flight.
        - return_date: The return date for the flight.
        - stops: 0 for direct flights. 1 or more for indirect flights.
        """
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date
        se
        f.stops = stops


def find_cheapest_flight(data):
    # Handle empty data if no flight or Amadeus rate limit exceeded
    if data is None or not data['data']:
        print("No flight data")
        return FlightData(
            price="N/A",
            origin_airport="N/A",
            destination_airport="N/A",
            out_date="N/A",
            return_date="N/A",
            stops="N/A")

    # Data from the first flight in the json
    try:
        first_flight = data['data'][0]
        lowest_price = float(first_flight["price"]["grandTotal"])
        nr_stops = len(first_flight["itineraries"][0]["segments"]) - 1
        origin = first_flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
        destination = first_flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
        out_date = first_flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[
            0]
        return_date = first_flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[
            0]
    except (KeyError, IndexError) as e:
        print(f"Error parsing flight data: {e}")
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A", "N/A")

    # Initialize FlightData with the first flight for comparison
    cheapest_flight = FlightData(
        lowest_price, origin, destination, out_date, return_date, nr_stops)

    for flight in data["data"]:
        price = float(flight["price"]["grandTotal"])
        if price < lowest_price:
            lowest_price = price
            origin = flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
            destination = flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
            out_date = flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[
                0]
            return_date = flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[
                0]
            cheapest_flight = FlightData(
                lowest_price, origin, destination, out_date, return_date, nr_stops)
            print(f"Lowest price to {destination} is CAD{lowest_price}")

    return cheapest_flight
