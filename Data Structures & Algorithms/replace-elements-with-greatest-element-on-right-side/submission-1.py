class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        largest = -1
        for num in range(len(arr) -1, -1, -1):
            temp = arr[num]
            arr[num] = largest
            if (temp > largest):
                largest = temp
        return arr