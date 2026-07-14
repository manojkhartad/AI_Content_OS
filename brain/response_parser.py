class ResponseParser:

    @staticmethod
    def parse(response):

        if response is None:
            return ""

        if hasattr(response, "text"):
            return response.text

        return str(response)