# ==========================================================
# Imports
# ==========================================================

import time

from utils.logger import Logger


# ==========================================================
# Usage Tracker
# ==========================================================

class UsageTracker:

    def __init__(self):

        self.logger = Logger.get_logger()

        self.total_requests = 0

        self.successful_requests = 0

        self.failed_requests = 0

        self.current_model = None

        self.last_response_time = 0.0

        self.total_response_time = 0.0

        self.fastest_response = None

        self.slowest_response = 0.0

        self.model_stats = {}

    # ------------------------------------------------------
    # Start Request
    # ------------------------------------------------------

    def start_request(

        self,

        model: str,

    ):

        self.total_requests += 1

        self.current_model = model

        if model not in self.model_stats:

            self.model_stats[model] = {

                "requests": 0,

                "success": 0,

                "failed": 0,

                "total_time": 0.0,

                "average_time": 0.0,

                "fastest": None,

                "slowest": 0.0,

            }

        self.model_stats[model]["requests"] += 1

        return time.perf_counter()

    # ------------------------------------------------------
    # End Request
    # ------------------------------------------------------

    def end_request(

        self,

        start_time,

        success: bool,

    ):

        elapsed = round(

            time.perf_counter() - start_time,

            2,

        )

        self.last_response_time = elapsed

        self.total_response_time += elapsed

        stats = self.model_stats[self.current_model]

        stats["total_time"] += elapsed

        stats["average_time"] = round(

            stats["total_time"] / stats["requests"],

            2,

        )

        if (

            stats["fastest"] is None

            or elapsed < stats["fastest"]

        ):

            stats["fastest"] = elapsed

        if elapsed > stats["slowest"]:

            stats["slowest"] = elapsed

        if (

            self.fastest_response is None

            or elapsed < self.fastest_response

        ):

            self.fastest_response = elapsed

        if elapsed > self.slowest_response:

            self.slowest_response = elapsed

        if success:

            self.successful_requests += 1

            stats["success"] += 1

        else:

            self.failed_requests += 1

            stats["failed"] += 1

        self.logger.info(

            f"{self.current_model} | "

            f"{elapsed:.2f}s | "

            f"{'SUCCESS' if success else 'FAILED'}"

        )

    # ------------------------------------------------------
    # Get Stats
    # ------------------------------------------------------

    def get_stats(self):

        average = 0.0

        if self.total_requests:

            average = round(

                self.total_response_time

                / self.total_requests,

                2,

            )

        return {

            "total_requests": self.total_requests,

            "successful_requests": self.successful_requests,

            "failed_requests": self.failed_requests,

            "current_model": self.current_model,

            "last_response_time": self.last_response_time,

            "average_response_time": average,

            "fastest_response": self.fastest_response,

            "slowest_response": self.slowest_response,

            "total_response_time": round(

                self.total_response_time,

                2,

            ),

            "models": self.model_stats,

        }

    # ------------------------------------------------------
    # Print Report
    # ------------------------------------------------------

    def report(self):

        stats = self.get_stats()

        print("\n===================================")

        print("LLM Usage Report")

        print("===================================")

        print(

            f"Total Requests      : {stats['total_requests']}"

        )

        print(

            f"Successful Requests : {stats['successful_requests']}"

        )

        print(

            f"Failed Requests     : {stats['failed_requests']}"

        )

        print(

            f"Average Time        : {stats['average_response_time']} sec"

        )

        print(

            f"Fastest Response    : {stats['fastest_response']} sec"

        )

        print(

            f"Slowest Response    : {stats['slowest_response']} sec"

        )

        print(

            f"Total Time          : {stats['total_response_time']} sec"

        )

        print("\nPer Model")

        print("-----------------------------------")

        for model, data in stats["models"].items():

            print(f"\n{model}")

            print(

                f"Requests : {data['requests']}"

            )

            print(

                f"Success  : {data['success']}"

            )

            print(

                f"Failed   : {data['failed']}"

            )

            print(

                f"Average  : {data['average_time']} sec"

            )

            print(

                f"Fastest  : {data['fastest']} sec"

            )

            print(

                f"Slowest  : {data['slowest']} sec"

            )

        print("===================================")

    # ------------------------------------------------------
    # Reset
    # ------------------------------------------------------

    def reset(self):

        self.__init__()