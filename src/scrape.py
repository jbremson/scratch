import argparse
from src.loader import Cities, Trips


parser = argparse.ArgumentParser(description="Run the scraper that collects drive time data.")
parser.add_argument("-n", "--no-write", help="Do not write to the database, i.e. test run." )
parser.add_argument("-c", "--load-cities", help="Load new cities")
parser.add_argument("-x", "--no-scrape", help="Do not run the scraper", action="store_true")
args = parser.parse_args()

if args.load_cities:
    Cities.load_cities()
if not args.no_scrape:
    Trips.process_trips(no_write=args.no_write);
print("Done")