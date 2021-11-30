import wordcloud
import matplotlib.pyplot as plt

keyword={'안녕':2, '하세요':1, '빅데이터':5, '웹크롤링':3}

wc = wordcloud.WordCloud(font_path='c:/Windows/fonts/Hancom Gothic Bold.ttf')
cloud = wc.generate_from_frequencies(keyword)

figure = plt.figure()
plt.imshow(cloud)
plt.show()
figure.savefig('word.png') # 처리결과를 이미지로 저장