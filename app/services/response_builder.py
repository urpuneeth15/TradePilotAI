from datetime import datetime


class ResponseBuilder:

    @staticmethod
    def success(data):

        return {
            "success": True,
            "timestamp": datetime.now().isoformat(),
            "data": data,
            "message": "OK"
        }

    @staticmethod
    def error(message):

        return {
            "success": False,
            "timestamp": datetime.now().isoformat(),
            "data": None,
            "message": message
        }


response_builder = ResponseBuilder()