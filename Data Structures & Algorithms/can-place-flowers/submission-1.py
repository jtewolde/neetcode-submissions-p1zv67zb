class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # Approach: Use iteration through flowerbed to keep track of prev and curr elements
        # Pad flowerbed with zeros on both ends to prevent out of bounds error
        # Compare previous, current, and next elements in array to see if a flower can be bedded

        # Create new flower array that pads flowerbed array with zeros on both ends
        flower = [0] + flowerbed + [0]

        # Iterate through flower, starting from index 1 to avoid padded zeros
        for i in range(1, len(flower) - 1):
            # Compare current element with next and previous elements to see if flower can be planted
            if flower[i] == 0 and flower[i - 1] != 1 and flower[i + 1] != 1:
                flower[i] = 1
                n -= 1

        return n <= 0