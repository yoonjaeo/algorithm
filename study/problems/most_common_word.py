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
import collections 

class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        sum_dict = {}
        p = re.compile("[\W]")
        para_list= p.sub(" ",paragraph).lower().split()


        sum_dict = collections.defaultdict(int)
        for para in para_list:
            if para not in banned:
                sum_dict[para] += 1
                
        common_word = [k for k, v in sum_dict.items() if v == max(sum_dict.values())]
        return common_word[0]
    

    def mostCommonWord_book(self, paragraph: str, banned: list[str]) -> str:
        words = [word for word in re.sub(r'[^\w]',' ', paragraph).lower().split() if word not in banned]
        counts = collections.Counter(words)
        return counts.most_common(1)[0][0]



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

''''
책 문제 풀이 방식과 내 방식과 다른점
- 각 단어의 리스트를 반들 때 제외 단어를 넣어줌 
- 딕셔너리로 만드는 방식을 모듈을 통해 만듬(collections 모듈)
    - defaultdict(int) : 키 존재 유무를 확인할 필요 없이 즉시 +1 수행가능
        counts = collections.defaultdict(int)
        for word in words:
            counts[word] += 1
    - Counter : 개수 처리 -> most_common 
        counts = collections.Counter(words)
        counts.most_common(1)[0][0]
'''


