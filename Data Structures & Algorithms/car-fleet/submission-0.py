class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)

        fleets = []
        for position, speed in cars:
            time = (target - position) / speed
            if not fleets or time > fleets[-1]:
                fleets.append(time)

        return len(fleets)

# GOAL
# ========
# Return the number of car fleets that will arrive at
# the destination.

# BRUTE FORCE
# ========
# While all cars are not at target -- O(T):
#   For each car not at target -- O(N),
#       Move the car up according to their speed. Do not let them pass car ahead -- O(N).
# TC: O(N^2 * T)
# SC: O(1)

# IDEA
# ========
# Sort cars + their speed by position in descending order to ensure cars cannot pass one ahead of it -- O(N log N).
# Have a list to track diff fleets.
# For each car in descending list, O(N)
#   Calulate time it takes to reach destination.
#       time = (target - position) / speed
#   If time <= time of car before it (car's time is faster than car ahead of it),
#       They are in the same fleet.
#   Otherwise (car's time is slower than car ahead of it),
#       Add it fleet.
# Return size of fleet.
# TC: O(N log N)
# SC: O(N)