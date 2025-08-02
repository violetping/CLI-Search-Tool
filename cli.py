import argparse
from cli_tool import googlesearch, location, weather

def main():
    parser = argparse.ArgumentParser(
        description="CLI Search Tool - Perform Google Search, Location Info, and Weather Lookup"
    )

    subparsers = parser.add_subparsers(dest="command", help="Available Commands")

    # Google Search command
    search_parser = subparsers.add_parser("googlesearch", help="Search Google and get top results")
    search_parser.add_argument("query", nargs='+', help="Search query (multiple words allowed without quotes)")
    search_parser.add_argument(
        "-n", "--num",
        type=int,
        default=5,
        help="Number of results to return (1 to 10, default=5)"
    )

    # Location command
    location_parser = subparsers.add_parser("location", help="Get location information")
    location_parser.add_argument("location_name", help="Name of the location")

    # Weather command
    weather_parser = subparsers.add_parser("weather", help="Get weather information")
    weather_parser.add_argument("api_key", help="Your weather API key")
    weather_parser.add_argument("city", help="City name or ID")

    args = parser.parse_args()

    if args.command == "googlesearch":
        query = ' '.join(args.query)
        num = min(max(args.num, 1), 20)  # Clamp between 1 and 20
        googlesearch.run(query, num=num)

    elif args.command == "location":
        location.run(args.location_name)

    elif args.command == "weather":
        weather.run(args.api_key, args.city)

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
