
import matplotlib
import matplotlib.pyplot as plt

#조사 수동 제거
sentence = u"""진동벨 좀 만들었으면 좋겠다 2층 매장이라 결국 손님 어딨는지는 몰라서 그저 열심히 목터져가며 소리지르는게 전부임 넘 안쓰럽다 그리고 픽업 장소 옆은 시장통임 북적북적
옆 동네 스타벅스 왔다,,, 무려 노트북 들고,,,,!
스타벅스 있다가 나오면 머리카락 커피향기 배는데 안에 있을 땐 모르겠다가 밖에 나와서 머리카락 흔들릴 때마다 느껴지는 거 너무 좋아
저도...마싯는 커피 마시고 싶어여...훌젹 ㅋㅋㅋ 막 요즘 로스팅 전문 하는 데 가서 마시구 싶고 그러네요 근데 어떤데 있는질 몰라서... 합정 상수 부근 쪽 찾아볼가여?
예전에는 스타벅스 비싸다는 인식 있었는데 카페 가격 다 똑같은듯
저도 그렇게 섬세한 입맛 아니라서 ㅋㅋ 가격 맛 찾아낼 수 있을지는 의문이네요...ㅋㅋㅋ 평범한  곳 가도 갠찬아여! 엄청 맛 없는 것만 아니라면야 ㅋㅋㅋ"""

def do():
    #단어추출
    words = sentence.split() 
    
    #빈도수 측정
    wordsDict = dict() 
    for c in words:
        if c not in wordsDict:
            wordsDict[c] = 1
        else:
            wordsDict[c] = wordsDict[c] + 1
    # wordsDict.items()
    
    #유의미한 빈도 추출
    _wordsDict = dict() 
    # _wordsDict = {k: v for k,v in wordsDict.items() if v > 1}
    for key, values in wordsDict.items():
        if values > 1:
            _wordsDict[key] = values
            # print(key,values)
    #시각화
    plt.rcParams['font.family'] = 'NanumGothic'
    plt.bar(range(len(_wordsDict)), _wordsDict.values(), align = 'center')
    plt.xticks(range(len(_wordsDict)), list(_wordsDict.keys()))
    plt.show()

def main():
    do()

if __name__ == "__main__":
    main()
