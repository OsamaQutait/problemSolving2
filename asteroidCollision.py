from typing import *

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            while stack and asteroid < 0 < stack[-1]:
                if abs(asteroid) > abs(stack[-1]):
                    stack.pop()
                    continue
                elif abs(asteroid) == abs(stack[-1]):
                    stack.pop()
                break
            else:
                stack.append(asteroid)
        return stack

if __name__ == '__main__':
    asteroids = [10, 2, -5]
    solution = Solution()
    print(solution.asteroidCollision(asteroids))