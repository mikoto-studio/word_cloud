from wordcloud import WordCloud
 
# テキストファイル読み込み
text = open("MyExamples_JD1.txt", encoding="utf8").read()
 
# 画像作成
wordcloud = WordCloud(max_font_size=40).generate(text)
 
# 画像保存
wordcloud.to_file("MyExamples_JD1.png")
