from google.genai.errors import ClientError, ServerError


class RetryManager:

    @staticmethod
    def should_retry(error):

        return isinstance(error, (ClientError, ServerError))