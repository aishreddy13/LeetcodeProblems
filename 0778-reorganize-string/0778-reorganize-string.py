class Solution:
    def reorganizeString(self, s: str) -> str:
        ans = []
        queueP = [(-count, char) for char, count in Counter(s).items()]
        heapify(queueP)

        while queueP:
            count_first, char_first = heappop(queueP)
            if not ans or char_first != ans[-1]:
                ans.append(char_first)
                if count_first + 1 != 0:
                    heappush(queueP, (count_first + 1, char_first))
            else:
                if not queueP: return ''
                count_second, char_second = heappop(queueP)
                ans.append(char_second)
                if count_second + 1 != 0:
                    heappush(queueP, (count_second + 1, char_second))
                heappush(queueP, (count_first, char_first))
        return ''.join(ans)
        