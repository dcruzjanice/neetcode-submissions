class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            if num not in count:
                count[num] = 1
            count[num] += 1

        pairs = list(count.items())

        pairs.sort(key=lambda pair: pair[1], reverse=True)

        answer = []

        for i in range(k):
            number = pairs[i][0]
            answer.append(number)

        return answer
