class ResearchReportFormatter:

    def print_report(self, report):

        print()
        print("===================================")
        print("   Universal Research Report (URR)")
        print("===================================")

        print(f"Topic            : {report.topic}")
        print(f"Content Type     : {report.content_type}")
        print(f"Target Audience  : {report.target_audience}")
        print(f"Goal             : {report.goal}")
        print(f"Tone             : {report.tone}")

        print()
        print("Research Content")
        print("-----------------------------------")
        print(report.content)

        print("===================================")