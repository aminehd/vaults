import bisect

class MyCalendarThree:

    def __init__(self):
        # We store (timestamp, delta) where delta is the change in overlap count.
        # We will keep this list sorted by timestamp to allow sweep line in O(N).
        self.timeline = []
        self.max_k = 0

    def book(self, startTime: int, endTime: int) -> int:
        """
        Adds a new booking [startTime, endTime).
        Returns the maximum k-booking.
        """
        # Sweep line approach: 
        # For each booking, increment at startTime and decrement at endTime.
        # Then calculate the prefix sum to find the max overlap.

        # Binary search for the insertion point for startTime
        self._update(startTime, 1)
        # Binary search for the insertion point for endTime
        self._update(endTime, -1)

        # Sweep through to find the max prefix sum
        curr_k = 0
        self.max_k = 0
        for _, delta in self.timeline:
            curr_k += delta
            if curr_k > self.max_k:
                self.max_k = curr_k
        
        return self.max_k

    def _update(self, timestamp: int, delta: int):
        """
        Helper to update the timeline. 
        If timestamp exists, update its delta. Otherwise, insert it.
        """
        idx = bisect.bisect_left(self.timeline, (timestamp, -float('inf')))
        
        if idx < len(self.timeline) and self.timeline[idx][0] == timestamp:
            # Timestamp exists, update existing delta
            new_delta = self.timeline[idx][1] + delta
            self.timeline[idx] = (timestamp, new_delta)
        else:
            # Timestamp doesn't exist, insert new one
            bisect.insort(self.timeline, (timestamp, delta))


def test_my_calendar_three():
    obj = MyCalendarThree()
    
    # Example 1
    # [10, 20] -> 1
    assert obj.book(10, 20) == 1
    # [50, 60] -> 1
    assert obj.book(50, 60) == 1
    # [10, 40] -> 2 ([10, 20] and [10, 40] overlap)
    assert obj.book(10, 40) == 2
    # [5, 15] -> 3 ([10, 20], [10, 40], and [5, 15] overlap at [10, 15])
    assert obj.book(5, 15) == 3
    # [5, 10] -> 3
    assert obj.book(5, 10) == 3
    # [25, 55] -> 3
    assert obj.book(25, 55) == 3
    
    print("Test passed!")

if __name__ == "__main__":
    test_my_calendar_three()
