"""
문자열이 주어지며, 금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력해라.
대소문자 구분하지 않으며 , 구두점(마침표 , 쉼표 등) 또한 무시

입력
paragrapy(str) = "Bob hit a ball, the hit BALL flew far after it was hit."
banned(list) = ["hit"]

출력
"ball"
"""

import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        sum_dict = {}
        p = re.compile("[\W]")
        para_list= p.sub(" ",paragraph).lower().split()

        for para in para_list:
            if para in sum_dict.keys():
                sum_dict[para] += 1
            else : 
                sum_dict[para] = 1

        for ban in banned:
            if ban in sum_dict.keys():
                del sum_dict[ban]

        common_word = [k for k, v in sum_dict.items() if v == max(sum_dict.values())]
        return common_word[0]
    
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

s = Solution()
print(s.mostCommonWord(paragraph, banned))

'''
내 문제 풀이 방식
- 정규식을 통해 문자만 남김(".", "," 등 삭제 ) => \W (문자열 아닌 것을 뽑아냄)
- 모두 소문자로 만들고 리스트로 변경(para_list)
- 리스트를 돌며 딕셔너리(sum_dict)에 넣어서 반복 수 세기
- ban할 단어를 딕셔너리에서 삭제해주기
- sum_dict에 있는 값들 중 max값을 찾아서 뽑아내기 
'''