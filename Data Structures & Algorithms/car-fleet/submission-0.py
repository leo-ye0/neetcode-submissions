class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        stack = []
        for p, s in cars:
            # 2. Calculate time to target for the current car
            time = (target - p) / s
            
            # 3. If the stack is empty, or this car takes LONGER than the 
            # fleet in front of it, it forms a new fleet.
            if not stack or time > stack[-1]:
                stack.append(time)
                
            # If time <= stack[-1], the car catches up and joins the 
            # existing fleet. We don't add it to the stack.
        return len(stack)