# https://leetcode-cn.com/problems/positions-of-large-groups/
# Date: 2021-01-05 20:29:27

class Solution:
    def largeGroupPositions(self, s: str):
        cnt = 1
        pre = s[0]
        res = []
        for idx, i in enumerate(s[1:]):
            print(idx, i, pre, cnt)
            if i == pre:
                cnt += 1
            if i != pre:
                pre = i
                if cnt >= 3:
                    res.append([idx - cnt + 1, idx])
                cnt = 1
            if idx + 2 == len(s) and cnt >= 3:
                res.append([idx - cnt + 2, idx + 1])

                

        return res

if __name__ == "__main__":
    import datetime
    sample = "abbxxxxzzy"
    so = Solution()
    res = so.largeGroupPositions(sample)
    print(res)
    now_time = datetime.datetime.now()
    print(now_time.strftime('%Y-%m-%d %H:%M:%S'))

