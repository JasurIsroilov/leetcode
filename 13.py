roman_dict = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}


class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        for i in range(len(s) - 1):
            if roman_dict.get(s[i]) >= roman_dict.get(s[i+1]):
                res += roman_dict.get(s[i])
            else:
                res -= roman_dict.get(s[i])
        res += roman_dict.get(s[len(s) - 1])
        return res


sol = Solution()
print(sol.romanToInt('MCMXCIV'))
