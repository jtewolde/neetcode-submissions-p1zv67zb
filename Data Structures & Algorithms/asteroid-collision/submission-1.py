class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # Logic: You have an array of asteroids where sign of an asteroid represents directiond
        # And the value represents its mass
        # When collisions occurs, the smaller asteroid is destroyed(popped from stack)
        # If both are same size, both are destroyed
        # Use stack to simulate collison process

        # Initialize stack to append asteroids that don't collide
        stack = []

        # Iterate through every asteroid
        for ast in asteroids:

            # Check if there are asteroids in stack and the current asteroid is negative
            # and the last asteroid in stack is positive:
            # Meaning that a collision is going to occur
            while stack and ast < 0 < stack[-1]:
                # If the current asteroid has bigger magntitude than last asteroid,
                # Then, pop out last asteroid as it is destroyed
                if -ast > stack[-1]:
                    stack.pop()
                    continue

                # If both asteroids are the same size, destory both
                elif -ast == stack[-1]:
                    stack.pop()
                break

            # Otherwise, if neither conditions are met, append asteroid to stack
            else:
                stack.append(ast)

        return stack


