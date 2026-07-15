# ==========================================================
# Imports
# ==========================================================

import time


# ==========================================================
# Performance Profiler
# ==========================================================

class PerformanceProfiler:

    def __init__(self):

        self.timings = {}

    # ------------------------------------------------------
    # Start Timer
    # ------------------------------------------------------

    def start(self, name):

        self.timings[name] = {
            "start": time.perf_counter(),
            "end": None,
        }

    # ------------------------------------------------------
    # Stop Timer
    # ------------------------------------------------------

    def stop(self, name):

        if name not in self.timings:
            return

        self.timings[name]["end"] = time.perf_counter()

    # ------------------------------------------------------
    # Reset
    # ------------------------------------------------------

    def reset(self):

        self.timings.clear()

    # ------------------------------------------------------
    # Report
    # ------------------------------------------------------

    def report(self):

        print("\n===================================")
        print("Performance Report")
        print("===================================\n")

        completed = []

        total_time = 0.0

        for name, value in self.timings.items():

            start = value.get("start")
            end = value.get("end")

            if start is None or end is None:
                continue

            elapsed = end - start

            completed.append((name, elapsed))

            total_time += elapsed

        if not completed:

            print("No performance data available.")
            return

        fastest = min(
            completed,
            key=lambda item: item[1]
        )

        slowest = max(
            completed,
            key=lambda item: item[1]
        )

        average = total_time / len(completed)

        for name, elapsed in completed:

            percent = (
                elapsed / total_time * 100
                if total_time
                else 0
            )

            print(
                f"{name:<30}"
                f"{elapsed:>8.2f} sec"
                f"   ({percent:>5.1f}%)"
            )

        print("\n-----------------------------------")

        print(
            f"{'Total':<30}"
            f"{total_time:>8.2f} sec"
        )

        print(
            f"{'Steps':<30}"
            f"{len(completed)}"
        )

        print(
            f"{'Average':<30}"
            f"{average:>8.2f} sec"
        )

        print(
            f"{'Fastest':<30}"
            f"{fastest[0]} "
            f"({fastest[1]:.2f} sec)"
        )

        print(
            f"{'Slowest':<30}"
            f"{slowest[0]} "
            f"({slowest[1]:.2f} sec)"
        )

        print("-----------------------------------")