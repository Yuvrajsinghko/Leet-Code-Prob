#Logest-Common-Prefix

"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        final_str = strs[0]
        if not strs:
            final_str = ""
        else:
            for word in strs[1:]:
                i = 0
                while i < len(final_str) and i < len(word) and final_str[i] == word[i]:
                    i += 1
                final_str = final_str[:i]
        return final_str












