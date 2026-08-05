from datetime import datetime, timedelta


class DateUtils:

    @staticmethod
    def today():

        return datetime.today().strftime("%Y-%m-%d")

    @staticmethod
    def days_before(days):

        return (
            datetime.today()
            - timedelta(days=days)
        ).strftime("%Y-%m-%d")