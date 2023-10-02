import math

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        h = {}
        b = {
            'b': 1,
            'a': 1,
            'l': 2,
            'o': 2,
            'n': 1
        }
        for char in text:
            if char not in h:
                h[char] = 1
            else:
                h[char] += 1

        max_number = []
        for key, value in b.items():
            if key in h and value > 0:
                max_number.append(h[key])
        result = 0
        if len(max_number) == 5:
            while max_number[0] >= 0 and max_number[2] >= 0 and max_number[3] >= 0 and max_number[4] >= 0:
                result += 1
                max_number[0] -= 1
                max_number[1] -= 1
                max_number[2] -= 2
                max_number[3] -= 2
                max_number[4] -= 1
            result -= 1
        return result

if __name__ == '__main__':
    text = "krhizmmgmcrecekgyljqkldocicziihtgpqwbticmvuyznragqoyrukzopfmjhjjxemsxmrsxuqmnkrzhgvtgdgtykhcglurvppvcwhrhrjoislonvvglhdciilduvuiebmffaagxerjeewmtcwmhmtwlxtvlbocczlrppmpjbpnifqtlninyzjtmazxdbzwxthpvrfulvrspycqcghuopjirzoeuqhetnbrcdakilzmklxwudxxhwilasbjjhhfgghogqoofsufysmcqeilaivtmfziumjloewbkjvaahsaaggteppqyuoylgpbdwqubaalfwcqrjeycjbbpifjbpigjdnnswocusuprydgrtxuaojeriigwumlovafxnpibjopjfqzrwemoinmptxddgcszmfprdrichjeqcvikynzigleaajcysusqasqadjemgnyvmzmbcfrttrzonwafrnedglhpudovigwvpimttiketopkvqw"
    solution = Solution()
    print(solution.maxNumberOfBalloons(text))
