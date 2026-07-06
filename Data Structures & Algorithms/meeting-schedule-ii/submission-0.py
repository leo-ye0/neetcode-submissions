"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
            
        # Step 1: Extract and sort start times and end times into separate timelines
        start_times = sorted([meeting.start for meeting in intervals])
        end_times = sorted([meeting.end for meeting in intervals])
        
        s = 0  # Pointer for start times
        e = 0  # Pointer for end times
        
        rooms_in_use = 0
        max_rooms_needed = 0
        
        # Step 2: Sweep through the start events
        while s < len(intervals):
            if start_times[s] < end_times[e]:
                rooms_in_use += 1
                s += 1  # Handled the arrival, advance start pointer
            else:
                # A room opened up! Clear it out.
                # On the next iteration, 's' will consume this free slot.
                rooms_in_use -= 1
                e += 1  # Handled the departure, advance end pointer
                
            # Track the peak high-water mark of rooms needed
            max_rooms_needed = max(max_rooms_needed, rooms_in_use)
            
        return max_rooms_needed