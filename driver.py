from solution import Solution

def main():
    # Create an instance of the Solution class
    solver = Solution()

    solver.hello_world()

    # Testing solution to problem 2678. Number of Senior Citizens
    details = ["7868190130M7522", "5303914400F9211", "9273338290F4010"]

    result = solver.countSeniors(details)
    print(f"Solution to problem 2678: {result}")

if __name__ == "__main__":
    main()
