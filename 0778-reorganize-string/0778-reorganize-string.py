class Solution:
    def reorganizeString(self, s: str) -> str:
        ans = []
        pq = [(-freq, char) for char, freq in Counter(s).items()]
        heapq.heapify(pq)

        while len(pq) >= 2:
            freq1, char1 = heappop(pq)
            freq2, char2 = heappop(pq)

            ans.extend([char1, char2])
            if freq1 + 1 < 0:
                heapq.heappush(pq, (freq1 + 1, char1))
            if freq2 + 1 < 0:
                heapq.heappush(pq, (freq2+1, char2))
        if pq:
            freq, char = heapq.heappop(pq)
            if -freq > 1:
                return ""
            ans.append(char)

        return ''.join(ans)