class TrafficModel:
    def __init__(self, start_hour=11):
        """
        start_hour: simulation start time (24h format)
        """
        self.start_hour = start_hour

    def get_time(self, tick):
        """
        Convert simulation tick → hour of day.

        Assumption:
        1 tick = 1 minute
        """
        minutes = tick
        hour = self.start_hour + (minutes // 60)
        return hour % 24

    def get_profile(self, tick):
        """
        Returns:
        (traffic_level, expected_waiting_customers)
        """
        hour = self.get_time(tick)

        # Staff only (system running, restaurant not open yet)
        if 11 <= hour < 12:
            return "quiet", 1

        # Lunch peak
        elif 12 <= hour < 14:
            return "busy", 20

        # Midday lull
        elif 14 <= hour < 18:
            return "normal", 7

        # Dinner peak
        elif 18 <= hour < 21:
            return "busy", 22

        # Closing / staff only
        elif 21 <= hour <= 22:
            return "quiet", 1

        # Outside operating hours
        else:
            return "closed", 0