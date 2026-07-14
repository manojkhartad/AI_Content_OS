import time


class UsageTracker:

    def __init__(self):
        self.total_requests = 0
        self.successful_requests = 0
        self.failed_requests = 0
        self.current_model = None
        self.response_time = 0.0

    def start_request(self, model):

        self.total_requests += 1
        self.current_model = model

        return time.time()

    def end_request(self, start_time, success):

        self.response_time = round(time.time() - start_time, 2)

        if success:
            self.successful_requests += 1
        else:
            self.failed_requests += 1

    def get_stats(self):

        return {
            "total_requests": self.total_requests,
            "successful_requests": self.successful_requests,
            "failed_requests": self.failed_requests,
            "current_model": self.current_model,
            "response_time": self.response_time,
        }