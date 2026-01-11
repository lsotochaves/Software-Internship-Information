class MergeIntervals:
    def __init__(self, intervals):
        self.intervals = intervals

    def sort_intervals(self):
        # Sorts the intervals by analizing first element of each interval
        self.intervals.sort(key=lambda x: x[0])
        return self.intervals

    def build_intervals(self):
        self.sort_intervals()
        resulting_intervals = []

        for interval in self.intervals:
            if not resulting_intervals:
                resulting_intervals.append(interval)

            # Checks latest value in resulting_intervals, compares to first and accomodates the interval accordingly
            elif resulting_intervals[-1][1] >= interval[0]:
                resulting_intervals[-1][1] = max(
                    resulting_intervals[-1][1], interval[1]
                )
            else:
                resulting_intervals.append(interval)

        return resulting_intervals

    def print_statement(self):
        result = self.build_intervals()

        if result:
            print(f"Resulting intervals: {result}")

        else:
            print("There is no intervals to analyze")


def main():
    intervals = [[5, 7], [8, 10], [2, 34], [67, 100]]

    test_instance = MergeIntervals(intervals)
    test_instance.print_statement()


if __name__ == "__main__":
    main()
