class Solution:
    def __init__(self):
        pass

    def hello_world(self):
        print(f'Hi, World!')

    # Solution to 2678 Number of Senior Citizens
    def countSeniors(self, details) -> int:
        count = 0
        for record in details:
            if int(record[11:13]) > 60:
                count += 1
        return count



