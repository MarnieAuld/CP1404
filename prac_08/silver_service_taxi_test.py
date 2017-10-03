"""
CP1404 Practical 8 - Silver Service Taxi Test
"""

from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    """Test SilverServiceTaxi class."""
    fancy_taxi = SilverServiceTaxi("Silver Service Taxi", 100, 2)
    hummer = SilverServiceTaxi("Hummer", 200, 4)
    fancy_taxi.start_fare()
    fancy_taxi.drive(18)
    print(fancy_taxi.get_fare())
    print(fancy_taxi)
    print(hummer)
    
main()
