import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager, rc
from matplotlib import style
import seaborn as sns

# styling setting
style.use('seaborn')
sns.set(style='darkgrid')
matplotlib.font_manager._rebuild()
font_name = font_manager.FontProperties(fname='C:/Windows/Fonts/gulim.ttc').get_name()
rc('font', family=font_name)


# data reading sorting by year

total_data = pd.read_csv("total_data.csv")

Genre_data = list(total_data["Genre"])

Genre_list = []
for i in range(len(Genre_data)):
    Genre_list.append(Genre_data[i].split('/'))

Genreconcat = sum(Genre_list,[])
for i in range(len(Genreconcat)):
    Genreconcat[i] = Genreconcat[i].strip()

Genreconcat = pd.Series(Genreconcat).value_counts()
del Genreconcat["전체"]
del Genreconcat["가요"]

Genreconcat = pd.DataFrame(Genreconcat, columns= ["Freq"],index = Genreconcat.index)
Genre_plot=sns.barplot(data = Genreconcat, x = Genreconcat.axes[0], y="Freq")
plt.title("Total Genre")
Genre_plot.set_xticklabels(Genre_plot.get_xticklabels(),rotation=45)
Genre_plot.figure.savefig("Total Genre.jpg")
plt.close()

#1970

data1970 = total_data[(total_data["Year"] >= 1970) & (total_data["Year"]<1980)]
Genre_1970 = list(data1970["Genre"])

Genre_1970list = []
for i in range(len(Genre_1970)):
    Genre_1970list.append(Genre_1970[i].split('/'))

Genreconcat1970 = sum(Genre_1970list,[])
for i in range(len(Genreconcat1970)):
    Genreconcat1970[i] = Genreconcat1970[i].strip()

Genreconcat1970 = pd.Series(Genreconcat1970).value_counts()
del Genreconcat1970["전체"]
del Genreconcat1970["가요"]

Genreconcat1970 = pd.DataFrame(Genreconcat1970, columns= ["Freq"],index = Genreconcat1970.index)
Genre_1970plot=sns.barplot(data = Genreconcat1970, x = Genreconcat1970.axes[0], y="Freq")
plt.title("1970 Genre")
Genre_1970plot.set_xticklabels(Genre_1970plot.get_xticklabels(),rotation=45)
Genre_1970plot.figure.savefig("1970 Genre.jpg")
plt.close()

#1980

data1980 = total_data[(total_data["Year"] >= 1980) & (total_data["Year"]<1990)]

Genre_1980 = list(data1980["Genre"])

Genre_1980list = []
for i in range(len(Genre_1980)):
    Genre_1980list.append(Genre_1980[i].split('/'))

Genreconcat1980 = sum(Genre_1980list,[])
for i in range(len(Genreconcat1980)):
    Genreconcat1980[i] = Genreconcat1980[i].strip()

Genreconcat1980 = pd.Series(Genreconcat1980).value_counts()
del Genreconcat1980["전체"]
del Genreconcat1980["가요"]

Genreconcat1980 = pd.DataFrame(Genreconcat1980, columns= ["Freq"],index = Genreconcat1980.index)
Genre_1980plot=sns.barplot(data = Genreconcat1980, x = Genreconcat1980.axes[0], y="Freq")
plt.title("1980 Genre")
Genre_1980plot.set_xticklabels(Genre_1980plot.get_xticklabels(),rotation=45)
Genre_1980plot.figure.savefig("1980 Genre.jpg")
plt.close()

#1990

data1990 = total_data[(total_data["Year"] >= 1990) & (total_data["Year"]<2000)]

Genre_1990 = list(data1990["Genre"])

Genre_1990list = []
for i in range(len(Genre_1990)):
    Genre_1990list.append(Genre_1990[i].split('/'))

Genreconcat1990 = sum(Genre_1990list,[])
for i in range(len(Genreconcat1990)):
    Genreconcat1990[i] = Genreconcat1990[i].strip()

Genreconcat1990 = pd.Series(Genreconcat1990).value_counts()
del Genreconcat1990["전체"]
del Genreconcat1990["가요"]

Genreconcat1990 = pd.DataFrame(Genreconcat1990, columns= ["Freq"],index = Genreconcat1990.index)
Genre_1990plot=sns.barplot(data = Genreconcat1990, x = Genreconcat1990.axes[0], y="Freq")
plt.title("1990 Genre")
Genre_1990plot.set_xticklabels(Genre_1990plot.get_xticklabels(),rotation=45)
Genre_1990plot.figure.savefig("1990 Genre.jpg")
plt.close()

#2000

data2000 = total_data[(total_data["Year"] >= 2000) & (total_data["Year"]<2010)]

Genre_2000 = list(data2000["Genre"])

Genre_2000list = []
for i in range(len(Genre_2000)):
    Genre_2000list.append(Genre_2000[i].split('/'))

Genreconcat2000 = sum(Genre_2000list,[])
for i in range(len(Genreconcat2000)):
    Genreconcat2000[i] = Genreconcat2000[i].strip()

Genreconcat2000 = pd.Series(Genreconcat2000).value_counts()
del Genreconcat2000["전체"]
del Genreconcat2000["가요"]

Genreconcat2000 = pd.DataFrame(Genreconcat2000, columns= ["Freq"],index = Genreconcat2000.index)
Genre_2000plot=sns.barplot(data = Genreconcat2000, x = Genreconcat2000.axes[0], y="Freq")
plt.title("2000 Genre")
Genre_2000plot.set_xticklabels(Genre_2000plot.get_xticklabels(),rotation=45)
Genre_2000plot.figure.savefig("2000 Genre.jpg")
plt.close()

#2010

data2010 = total_data[(total_data["Year"] >= 2010) & (total_data["Year"]<2020)]

Genre_2010 = list(data2010["Genre"])

Genre_2010list = []
for i in range(len(Genre_2010)):
    Genre_2010list.append(Genre_2010[i].split('/'))

Genreconcat2010 = sum(Genre_2010list,[])
for i in range(len(Genreconcat2010)):
    Genreconcat2010[i] = Genreconcat2010[i].strip()

Genreconcat2010 = pd.Series(Genreconcat2010).value_counts()
del Genreconcat2010["전체"]
del Genreconcat2010["가요"]

Genreconcat2010 = pd.DataFrame(Genreconcat2010, columns= ["Freq"],index = Genreconcat2010.index)
Genre_2010plot=sns.barplot(data = Genreconcat2010, x = Genreconcat2010.axes[0], y="Freq")
plt.title("2010 Genre")
Genre_2010plot.set_xticklabels(Genre_2010plot.get_xticklabels(),rotation=45)
Genre_2010plot.figure.savefig("2010 Genre.jpg")
plt.close()

#2020

data2020 = total_data[(total_data["Year"] == 2020)]

Genre_2020 = list(data2020["Genre"])

Genre_2020list = []
for i in range(len(Genre_2020)):
    Genre_2020list.append(Genre_2020[i].split('/'))

Genreconcat2020 = sum(Genre_2020list,[])
for i in range(len(Genreconcat2020)):
    Genreconcat2020[i] = Genreconcat2020[i].strip()

Genreconcat2020 = pd.Series(Genreconcat2020).value_counts()

Genreconcat2020 = pd.DataFrame(Genreconcat2020, columns= ["Freq"],index = Genreconcat2020.index)
Genre_2020plot=sns.barplot(data = Genreconcat2020, x = Genreconcat2020.axes[0], y="Freq")
plt.title("2020 Genre")
Genre_2020plot.set_xticklabels(Genre_2020plot.get_xticklabels(),rotation=45)
Genre_2020plot.figure.savefig("2020 Genre.jpg")
plt.close()



# recently data reading
data = pd.read_csv("2020_data.csv")

one_to_ten = data[data["Rangking"]<=10]

one_to_ten_title = pd.DataFrame(one_to_ten["Title"].value_counts())
one_to_ten_artist = pd.DataFrame(one_to_ten["Artist"].value_counts())

top_title = one_to_ten_title[one_to_ten_title["Title"]>=21]
top_artist = one_to_ten_artist[one_to_ten_artist["Artist"]>=19]

target_title = top_title.index
target_artist = top_artist.index

plot_date = data.sort_values(by='Date')

# plot on top rangking title on Youtube Music
x1=list(data[(data["Title"]==target_title[0]) & (data["Artist"]=="조정석") & (data["Source Site"]=="Youtube Music")]["Rangking"])
x2=list(data[(data["Title"]==target_title[1]) & (data["Source Site"]=="Youtube Music")]["Rangking"])
x3=list(data[(data["Title"]==target_title[2]) & (data["Artist"]=="전미도") & (data["Source Site"]=="Youtube Music")]["Rangking"])
x4=list(data[(data["Title"]==target_title[3]) & (data["Source Site"]=="Youtube Music")]["Rangking"])
x5=list(data[(data["Title"]==target_title[4]) & (data["Source Site"]=="Youtube Music")]["Rangking"])
x6=list(data[(data["Title"]==target_title[5]) & (data["Source Site"]=="Youtube Music")]["Rangking"])
x7=list(data[(data["Title"]==target_title[6]) & (data["Source Site"]=="Youtube Music")]["Rangking"])
x8=list(data[(data["Title"]==target_title[7]) & (data["Source Site"]=="Youtube Music")]["Rangking"])
x9=list(data[(data["Title"]==target_title[8]) & (data["Source Site"]=="Youtube Music")]["Rangking"])
x10=list(data[(data["Title"]==target_title[9]) & (data["Source Site"]=="Youtube Music")]["Rangking"])
x11=list(data[(data["Title"]==target_title[10]) & (data["Source Site"]=="Youtube Music")]["Rangking"])

y1=list(data[(data["Title"]==target_title[0]) & (data["Artist"]=="조정석")& (data["Source Site"]=="Youtube Music")]["Date"])
y2=list(data[(data["Title"]==target_title[1]) & (data["Source Site"]=="Youtube Music")]["Date"])
y3=list(data[(data["Title"]==target_title[2]) & (data["Artist"]=="전미도")& (data["Source Site"]=="Youtube Music")]["Date"])
y4=list(data[(data["Title"]==target_title[3]) & (data["Source Site"]=="Youtube Music")]["Date"])
y5=list(data[(data["Title"]==target_title[4]) & (data["Source Site"]=="Youtube Music")]["Date"])
y6=list(data[(data["Title"]==target_title[5]) & (data["Source Site"]=="Youtube Music")]["Date"])
y7=list(data[(data["Title"]==target_title[6]) & (data["Source Site"]=="Youtube Music")]["Date"])
y8=list(data[(data["Title"]==target_title[7]) & (data["Source Site"]=="Youtube Music")]["Date"])
y9=list(data[(data["Title"]==target_title[8]) & (data["Source Site"]=="Youtube Music")]["Date"])
y10=list(data[(data["Title"]==target_title[9]) & (data["Source Site"]=="Youtube Music")]["Date"])
y11=list(data[(data["Title"]==target_title[10]) & (data["Source Site"]=="Youtube Music")]["Date"])


plt.title("Top Ranking of Title on Youtube Music")
plt.grid()
plt.ylim((-1,100))
plt.xticks(rotation=45)
plt.plot(y1,x1,label = target_title[0])
plt.plot(y2,x2,label = target_title[1])
plt.plot(y3,x3,label = target_title[2])
plt.plot(y4,x4,label = target_title[3])
plt.plot(y5,x5,label = target_title[4])
plt.plot(y6,x6,label = target_title[5])
plt.plot(y7,x7,label = target_title[6])
plt.plot(y8,x8,label = target_title[7])
plt.plot(y9,x9,label = target_title[8])
plt.plot(y10,x10,label = target_title[9])
plt.plot(y11,x11,label = target_title[10])
plt.legend(prop = {'size' : 6})
plt.gca().invert_yaxis()
plt.savefig("Top Ranking of Title on Youtube Music.jpg")
plt.close()

# plot on top rangking title on Naver Vibe
paris_x=list(data[(data["Title"]=="Paris In The Rain") & (data["Source Site"]=="Naver Vibe")]["Rangking"])
nowtrustme_x=list(data[(data["Title"]=="이제 나만 믿어요") & (data["Source Site"]=="Naver Vibe")]["Rangking"])
nightletter_x=list(data[(data["Title"]=="밤편지") & (data["Source Site"]=="Naver Vibe")]["Rangking"])
meteor_x=list(data[(data["Title"]=="METEOR") & (data["Source Site"]=="Naver Vibe")]["Rangking"])
rockstone_x=list(data[(data["Title"]=="돌덩이") & (data["Source Site"]=="Naver Vibe")]["Rangking"])

paris_y=list(data[(data["Title"]=="Paris In The Rain") & (data["Source Site"]=="Naver Vibe")]["Date"])
nowtrustme_y=list(data[(data["Title"]=="이제 나만 믿어요") & (data["Source Site"]=="Naver Vibe")]["Date"])
nightletter_y=list(data[(data["Title"]=="밤편지") & (data["Source Site"]=="Naver Vibe")]["Date"])
meteor_y=list(data[(data["Title"]=="METEOR") & (data["Source Site"]=="Naver Vibe")]["Date"])
rockstone_y=list(data[(data["Title"]=="돌덩이") & (data["Source Site"]=="Naver Vibe")]["Date"])


plt.title("Top Ranking of Title on Naver Vibe")
plt.grid()
plt.ylim((-1,100))
plt.xticks(rotation=45)
plt.plot(paris_y,paris_x,label = "Paris In The Rain")
plt.plot(nowtrustme_y,nowtrustme_x,label = "이제 나만 믿어요")
plt.plot(nightletter_y,nightletter_x,label = "밤편지")
plt.plot(meteor_y,meteor_x,label = "METEOR")
plt.plot(rockstone_y,rockstone_x,label = "돌덩이")
plt.legend(prop = {'size' : 6})
plt.gca().invert_yaxis()
plt.savefig("Middle Ranking of Title on Naver Vibe.jpg")
plt.close()

# plot on each sites by 아로하
aroha_x1=list(data[(data["Title"]==target_title[0]) & (data["Artist"]=="조정석") & (data["Source Site"]=="Melon Music")]["Rangking"])
aroha_y1=list(data[(data["Title"]==target_title[0]) & (data["Artist"]=="조정석")& (data["Source Site"]=="Melon Music")]["Date"])

aroha_x2=list(data[(data["Title"]==target_title[0]) & (data["Artist"]=="조정석") & (data["Source Site"]=="Youtube Music")]["Rangking"])
aroha_y2=list(data[(data["Title"]==target_title[0]) & (data["Artist"]=="조정석")& (data["Source Site"]=="Youtube Music")]["Date"])

aroha_x3=list(data[(data["Title"]==target_title[0]) & (data["Artist"]=="조정석") & (data["Source Site"]=="Bugs Music")]["Rangking"])
aroha_y3=list(data[(data["Title"]==target_title[0]) & (data["Artist"]=="조정석")& (data["Source Site"]=="Bugs Music")]["Date"])

aroha_x4=list(data[(data["Title"]==target_title[0]) & (data["Artist"]=="조정석") & (data["Source Site"]=="Apple Music")]["Rangking"])
aroha_y4=list(data[(data["Title"]==target_title[0]) & (data["Artist"]=="조정석")& (data["Source Site"]=="Apple Music")]["Date"])

aroha_x5=list(data[(data["Title"]==target_title[0]) & (data["Artist"]=="조정석") & (data["Source Site"]=="Genie Music")]["Rangking"])
aroha_y5=list(data[(data["Title"]==target_title[0]) & (data["Artist"]=="조정석")& (data["Source Site"]=="Genie Music")]["Date"])

aroha_x6=list(data[(data["Title"]==target_title[0]) & (data["Artist"]=="조정석") & (data["Source Site"]=="Naver Vibe")]["Rangking"])
aroha_y6=list(data[(data["Title"]==target_title[0]) & (data["Artist"]=="조정석")& (data["Source Site"]=="Naver Vibe")]["Date"])

plt.title("아로하 on each Music Sites")
plt.grid()
plt.ylim((-1,100))
plt.xticks(rotation=45)
plt.plot(aroha_y1,aroha_x1,label = "Melon")
plt.plot(aroha_y2,aroha_x2,label = "Youtube")
plt.plot(aroha_y3,aroha_x3,label = "Bugs")
plt.plot(aroha_y4,aroha_x4,label = "Apple")
plt.plot(aroha_y5,aroha_x5,label = "Genie")
plt.plot(aroha_y6,aroha_x6,label = "Naver")
plt.legend()
plt.gca().invert_yaxis()
plt.savefig("아로하 차트 비교.jpg")
plt.close()

# plot on each sites by 사랑하게 될 줄 알았어
becominglove_x1=list(data[(data["Title"]==target_title[2]) & (data["Artist"]=="전미도") & (data["Source Site"]=="Melon Music")]["Rangking"])
becominglove_y1=list(data[(data["Title"]==target_title[2]) & (data["Artist"]=="전미도")& (data["Source Site"]=="Melon Music")]["Date"])

becominglove_x2=list(data[(data["Title"]==target_title[2]) & (data["Artist"]=="전미도") & (data["Source Site"]=="Youtube Music")]["Rangking"])
becominglove_y2=list(data[(data["Title"]==target_title[2]) & (data["Artist"]=="전미도")& (data["Source Site"]=="Youtube Music")]["Date"])

becominglove_x3=list(data[(data["Title"]==target_title[2]) & (data["Artist"]=="전미도") & (data["Source Site"]=="Bugs Music")]["Rangking"])
becominglove_y3=list(data[(data["Title"]==target_title[2]) & (data["Artist"]=="전미도")& (data["Source Site"]=="Bugs Music")]["Date"])

becominglove_x4=list(data[(data["Title"]==target_title[2]) & (data["Artist"]=="전미도") & (data["Source Site"]=="Apple Music")]["Rangking"])
becominglove_y4=list(data[(data["Title"]==target_title[2]) & (data["Artist"]=="전미도")& (data["Source Site"]=="Apple Music")]["Date"])

becominglove_x5=list(data[(data["Title"]==target_title[2]) & (data["Artist"]=="전미도") & (data["Source Site"]=="Genie Music")]["Rangking"])
becominglove_y5=list(data[(data["Title"]==target_title[2]) & (data["Artist"]=="전미도")& (data["Source Site"]=="Genie Music")]["Date"])

becominglove_x6=list(data[(data["Title"]==target_title[2]) & (data["Artist"]=="전미도") & (data["Source Site"]=="Naver Vibe")]["Rangking"])
becominglove_y6=list(data[(data["Title"]==target_title[2]) & (data["Artist"]=="전미도")& (data["Source Site"]=="Naver Vibe")]["Date"])

plt.title("사랑하게 될 줄 알았어 on each Music Sites")
plt.grid()
plt.ylim((-1,100))
plt.xticks(rotation=45)
plt.plot(becominglove_y1,becominglove_x1,label = "Melon")
plt.plot(becominglove_y2,becominglove_x2,label = "Youtube")
plt.plot(becominglove_y3,becominglove_x3,label = "Bugs")
plt.plot(becominglove_y4,becominglove_x4,label = "Apple")
plt.plot(becominglove_y5,becominglove_x5,label = "Genie")
plt.plot(becominglove_y6,becominglove_x6,label = "Naver")
plt.legend()
plt.gca().invert_yaxis()
plt.savefig("사랑하게 될 줄 알았어 차트 비교.jpg")
plt.close()

# plot on each sites by Dolphin
Dolphin_x1=list(data[(data["Title"]==target_title[5]) & (data["Source Site"]=="Melon Music")]["Rangking"])
Dolphin_y1=list(data[(data["Title"]==target_title[5]) & (data["Source Site"]=="Melon Music")]["Date"])

Dolphin_x2=list(data[(data["Title"]==target_title[5]) & (data["Source Site"]=="Youtube Music")]["Rangking"])
Dolphin_y2=list(data[(data["Title"]==target_title[5]) & (data["Source Site"]=="Youtube Music")]["Date"])

Dolphin_x3=list(data[(data["Title"]==target_title[5]) & (data["Source Site"]=="Bugs Music")]["Rangking"])
Dolphin_y3=list(data[(data["Title"]==target_title[5]) & (data["Source Site"]=="Bugs Music")]["Date"])

Dolphin_x4=list(data[(data["Title"]==target_title[5]) & (data["Source Site"]=="Apple Music")]["Rangking"])
Dolphin_y4=list(data[(data["Title"]==target_title[5]) & (data["Source Site"]=="Apple Music")]["Date"])

Dolphin_x5=list(data[(data["Title"]==target_title[5]) & (data["Source Site"]=="Genie Music")]["Rangking"])
Dolphin_y5=list(data[(data["Title"]==target_title[5]) & (data["Source Site"]=="Genie Music")]["Date"])

Dolphin_x6=list(data[(data["Title"]==target_title[5]) & (data["Source Site"]=="Naver Vibe")]["Rangking"])
Dolphin_y6=list(data[(data["Title"]==target_title[5]) & (data["Source Site"]=="Naver Vibe")]["Date"])

plt.title("Dolphin on each Music Sites")
plt.grid()
plt.ylim((-1,100))
plt.xticks(rotation=45)
plt.plot(Dolphin_y1,Dolphin_x1,label = "Melon")
plt.plot(Dolphin_y2,Dolphin_x2,label = "Youtube")
plt.plot(Dolphin_y3,Dolphin_x3,label = "Bugs")
plt.plot(Dolphin_y4,Dolphin_x4,label = "Apple")
plt.plot(Dolphin_y5,Dolphin_x5,label = "Genie")
plt.plot(Dolphin_y6,Dolphin_x6,label = "Naver")
plt.legend()
plt.gca().invert_yaxis()
plt.savefig("Dolphin 차트 비교.jpg")
plt.close()

# plot on each sites by 시작
Start_x1=list(data[(data["Title"]==target_title[7]) & (data["Source Site"]=="Melon Music")]["Rangking"])
Start_y1=list(data[(data["Title"]==target_title[7]) & (data["Source Site"]=="Melon Music")]["Date"])

Start_x2=list(data[(data["Title"]==target_title[7]) & (data["Source Site"]=="Youtube Music")]["Rangking"])
Start_y2=list(data[(data["Title"]==target_title[7]) & (data["Source Site"]=="Youtube Music")]["Date"])

Start_x3=list(data[(data["Title"]==target_title[7]) & (data["Source Site"]=="Bugs Music")]["Rangking"])
Start_y3=list(data[(data["Title"]==target_title[7]) & (data["Source Site"]=="Bugs Music")]["Date"])

Start_x4=list(data[(data["Title"]==target_title[7]) & (data["Source Site"]=="Apple Music")]["Rangking"])
Start_y4=list(data[(data["Title"]==target_title[7]) & (data["Source Site"]=="Apple Music")]["Date"])

Start_x5=list(data[(data["Title"]==target_title[7]) & (data["Source Site"]=="Genie Music")]["Rangking"])
Start_y5=list(data[(data["Title"]==target_title[7]) & (data["Source Site"]=="Genie Music")]["Date"])

Start_x6=list(data[(data["Title"]==target_title[7]) & (data["Source Site"]=="Naver Vibe")]["Rangking"])
Start_y6=list(data[(data["Title"]==target_title[7]) & (data["Source Site"]=="Naver Vibe")]["Date"])

plt.title("시작 on each Music Sites")
plt.grid()
plt.ylim((-1,100))
plt.xticks(rotation=45)
plt.plot(Start_y1,Start_x1,label = "Melon")
plt.plot(Start_y2,Start_x2,label = "Youtube")
plt.plot(Start_y3,Start_x3,label = "Bugs")
plt.plot(Start_y4,Start_x4,label = "Apple")
plt.plot(Start_y5,Start_x5,label = "Genie")
plt.plot(Start_y6,Start_x6,label = "Naver")
plt.legend()
plt.gca().invert_yaxis()
plt.savefig("시작 차트 비교.jpg")
plt.close()

# plot on each sites by 화려하지 않은 고백
notgorgeous_x1=list(data[(data["Title"]==target_title[9]) & (data["Source Site"]=="Melon Music")]["Rangking"])
notgorgeous_y1=list(data[(data["Title"]==target_title[9]) & (data["Source Site"]=="Melon Music")]["Date"])

notgorgeous_x2=list(data[(data["Title"]==target_title[9]) & (data["Source Site"]=="Youtube Music")]["Rangking"])
notgorgeous_y2=list(data[(data["Title"]==target_title[9]) & (data["Source Site"]=="Youtube Music")]["Date"])

notgorgeous_x3=list(data[(data["Title"]==target_title[9]) & (data["Source Site"]=="Bugs Music")]["Rangking"])
notgorgeous_y3=list(data[(data["Title"]==target_title[9]) & (data["Source Site"]=="Bugs Music")]["Date"])

notgorgeous_x4=list(data[(data["Title"]==target_title[9]) & (data["Source Site"]=="Apple Music")]["Rangking"])
notgorgeous_y4=list(data[(data["Title"]==target_title[9]) & (data["Source Site"]=="Apple Music")]["Date"])

notgorgeous_x5=list(data[(data["Title"]==target_title[9]) & (data["Source Site"]=="Genie Music")]["Rangking"])
notgorgeous_y5=list(data[(data["Title"]==target_title[9]) & (data["Source Site"]=="Genie Music")]["Date"])

notgorgeous_x6=list(data[(data["Title"]==target_title[9]) & (data["Source Site"]=="Naver Vibe")]["Rangking"])
notgorgeous_y6=list(data[(data["Title"]==target_title[9]) & (data["Source Site"]=="Naver Vibe")]["Date"])

plt.title("화려하지 않은 고백 on each Music Sites")
plt.grid()
plt.ylim((-1,100))
plt.xticks(rotation=45)
plt.xticks(rotation=45)
plt.plot(notgorgeous_y1,notgorgeous_x1,label = "Melon")
plt.plot(notgorgeous_y2,notgorgeous_x2,label = "Youtube")
plt.plot(notgorgeous_y3,notgorgeous_x3,label = "Bugs")
plt.plot(notgorgeous_y4,notgorgeous_x4,label = "Apple")
plt.plot(notgorgeous_y5,notgorgeous_x5,label = "Genie")
plt.plot(notgorgeous_y6,notgorgeous_x6,label = "Naver")
plt.legend()
plt.gca().invert_yaxis()
plt.savefig("화려하지 않은 고백 차트 비교.jpg")
plt.close()

# plot on each sites by 흔꽃네샴
notgorgeous_x1=list(data[(data["Title"]=="흔들리는 꽃들 속에서 네 샴푸향이 느껴진거야") & (data["Source Site"]=="Melon Music")]["Rangking"])
notgorgeous_y1=list(data[(data["Title"]=="흔들리는 꽃들 속에서 네 샴푸향이 느껴진거야") & (data["Source Site"]=="Melon Music")]["Date"])

notgorgeous_x2=list(data[(data["Title"]=="흔들리는 꽃들 속에서 네 샴푸향이 느껴진거야") & (data["Source Site"]=="Youtube Music")]["Rangking"])
notgorgeous_y2=list(data[(data["Title"]=="흔들리는 꽃들 속에서 네 샴푸향이 느껴진거야") & (data["Source Site"]=="Youtube Music")]["Date"])

notgorgeous_x3=list(data[(data["Title"]=="흔들리는 꽃들 속에서 네 샴푸향이 느껴진거야") & (data["Source Site"]=="Bugs Music")]["Rangking"])
notgorgeous_y3=list(data[(data["Title"]=="흔들리는 꽃들 속에서 네 샴푸향이 느껴진거야") & (data["Source Site"]=="Bugs Music")]["Date"])

notgorgeous_x4=list(data[(data["Title"]=="흔들리는 꽃들 속에서 네 샴푸향이 느껴진거야") & (data["Source Site"]=="Apple Music")]["Rangking"])
notgorgeous_y4=list(data[(data["Title"]=="흔들리는 꽃들 속에서 네 샴푸향이 느껴진거야") & (data["Source Site"]=="Apple Music")]["Date"])

notgorgeous_x5=list(data[(data["Title"]=="흔들리는 꽃들 속에서 네 샴푸향이 느껴진거야") & (data["Source Site"]=="Genie Music")]["Rangking"])
notgorgeous_y5=list(data[(data["Title"]=="흔들리는 꽃들 속에서 네 샴푸향이 느껴진거야") & (data["Source Site"]=="Genie Music")]["Date"])

notgorgeous_x6=list(data[(data["Title"]=="흔들리는 꽃들 속에서 네 샴푸향이 느껴진거야") & (data["Source Site"]=="Naver Vibe")]["Rangking"])
notgorgeous_y6=list(data[(data["Title"]=="흔들리는 꽃들 속에서 네 샴푸향이 느껴진거야") & (data["Source Site"]=="Naver Vibe")]["Date"])

plt.title("흔꽃네샴 느껴진거야 on each Music Sites")
plt.grid()
plt.ylim((-1,100))
plt.xticks(rotation=45)
plt.xticks(rotation=45)
plt.plot(notgorgeous_y1,notgorgeous_x1,label = "Melon")
plt.plot(notgorgeous_y2,notgorgeous_x2,label = "Youtube")
plt.plot(notgorgeous_y3,notgorgeous_x3,label = "Bugs")
plt.plot(notgorgeous_y4,notgorgeous_x4,label = "Apple")
plt.plot(notgorgeous_y5,notgorgeous_x5,label = "Genie")
plt.plot(notgorgeous_y6,notgorgeous_x6,label = "Naver")
plt.legend()
plt.gca().invert_yaxis()
plt.savefig("흔꽃네샴 차트 비교.jpg")
plt.close()

# plot on each sites by 돌덩이
rockstone_x1=list(data[(data["Title"]=="돌덩이") & (data["Source Site"]=="Melon Music")]["Rangking"])
rockstone_y1=list(data[(data["Title"]=="돌덩이") & (data["Source Site"]=="Melon Music")]["Date"])

rockstone_x2=list(data[(data["Title"]=="돌덩이") & (data["Source Site"]=="Youtube Music")]["Rangking"])
rockstone_y2=list(data[(data["Title"]=="돌덩이") & (data["Source Site"]=="Youtube Music")]["Date"])

rockstone_x3=list(data[(data["Title"]=="돌덩이") & (data["Source Site"]=="Bugs Music")]["Rangking"])
rockstone_y3=list(data[(data["Title"]=="돌덩이") & (data["Source Site"]=="Bugs Music")]["Date"])

rockstone_x4=list(data[(data["Title"]=="돌덩이") & (data["Source Site"]=="Apple Music")]["Rangking"])
rockstone_y4=list(data[(data["Title"]=="돌덩이") & (data["Source Site"]=="Apple Music")]["Date"])

rockstone_x5=list(data[(data["Title"]=="돌덩이") & (data["Source Site"]=="Genie Music")]["Rangking"])
rockstone_y5=list(data[(data["Title"]=="돌덩이") & (data["Source Site"]=="Genie Music")]["Date"])

rockstone_x6=list(data[(data["Title"]=="돌덩이") & (data["Source Site"]=="Naver Vibe")]["Rangking"])
rockstone_y6=list(data[(data["Title"]=="돌덩이") & (data["Source Site"]=="Naver Vibe")]["Date"])

plt.title("돌덩이 on each Music Sites")
plt.grid()
plt.ylim((-1,100))
plt.xticks(rotation=45)
plt.xticks(rotation=45)
plt.plot(rockstone_y1,rockstone_x1,label = "Melon")
plt.plot(rockstone_y2,rockstone_x2,label = "Youtube")
plt.plot(rockstone_y3,rockstone_x3,label = "Bugs")
plt.plot(rockstone_y4,rockstone_x4,label = "Apple")
plt.plot(rockstone_y5,rockstone_x5,label = "Genie")
plt.plot(rockstone_y6,rockstone_x6,label = "Naver")
plt.legend()
plt.gca().invert_yaxis()
plt.savefig("돌덩이 차트 비교.jpg")
plt.close()

# plot on each sites by 밤편지
nightletter_x1=list(data[(data["Title"]=="밤편지") & (data["Source Site"]=="Melon Music")]["Rangking"])
nightletter_y1=list(data[(data["Title"]=="밤편지") & (data["Source Site"]=="Melon Music")]["Date"])

nightletter_x2=list(data[(data["Title"]=="밤편지") & (data["Source Site"]=="Youtube Music")]["Rangking"])
nightletter_y2=list(data[(data["Title"]=="밤편지") & (data["Source Site"]=="Youtube Music")]["Date"])

nightletter_x3=list(data[(data["Title"]=="밤편지") & (data["Source Site"]=="Bugs Music")]["Rangking"])
nightletter_y3=list(data[(data["Title"]=="밤편지") & (data["Source Site"]=="Bugs Music")]["Date"])

nightletter_x4=list(data[(data["Title"]=="밤편지") & (data["Source Site"]=="Apple Music")]["Rangking"])
nightletter_y4=list(data[(data["Title"]=="밤편지") & (data["Source Site"]=="Apple Music")]["Date"])

nightletter_x5=list(data[(data["Title"]=="밤편지") & (data["Source Site"]=="Genie Music")]["Rangking"])
nightletter_y5=list(data[(data["Title"]=="밤편지") & (data["Source Site"]=="Genie Music")]["Date"])

nightletter_x6=list(data[(data["Title"]=="밤편지") & (data["Source Site"]=="Naver Vibe")]["Rangking"])
nightletter_y6=list(data[(data["Title"]=="밤편지") & (data["Source Site"]=="Naver Vibe")]["Date"])

plt.title("밤편지 on each Music Sites")
plt.grid()
plt.ylim((-1,100))
plt.xticks(rotation=45)
plt.xticks(rotation=45)
plt.plot(nightletter_y1,nightletter_x1,label = "Melon")
plt.plot(nightletter_y2,nightletter_x2,label = "Youtube")
plt.plot(nightletter_y3,nightletter_x3,label = "Bugs")
plt.plot(nightletter_y4,nightletter_x4,label = "Apple")
plt.plot(nightletter_y5,nightletter_x5,label = "Genie")
plt.plot(nightletter_y6,nightletter_x6,label = "Naver")
plt.legend()
plt.gca().invert_yaxis()
plt.savefig("밤편지 차트 비교.jpg")
plt.close()

# plot on each sites by Paris In The Rain
parisintherain_x1=list(data[(data["Title"]=="Paris In The Rain") & (data["Source Site"]=="Melon Music")]["Rangking"])
parisintherain_y1=list(data[(data["Title"]=="Paris In The Rain") & (data["Source Site"]=="Melon Music")]["Date"])

parisintherain_x2=list(data[(data["Title"]=="Paris In The Rain") & (data["Source Site"]=="Youtube Music")]["Rangking"])
parisintherain_y2=list(data[(data["Title"]=="Paris In The Rain") & (data["Source Site"]=="Youtube Music")]["Date"])

parisintherain_x3=list(data[(data["Title"]=="Paris In The Rain") & (data["Source Site"]=="Bugs Music")]["Rangking"])
parisintherain_y3=list(data[(data["Title"]=="Paris In The Rain") & (data["Source Site"]=="Bugs Music")]["Date"])

parisintherain_x4=list(data[(data["Title"]=="Paris In The Rain") & (data["Source Site"]=="Apple Music")]["Rangking"])
parisintherain_y4=list(data[(data["Title"]=="Paris In The Rain") & (data["Source Site"]=="Apple Music")]["Date"])

parisintherain_x5=list(data[(data["Title"]=="Paris In The Rain") & (data["Source Site"]=="Genie Music")]["Rangking"])
parisintherain_y5=list(data[(data["Title"]=="Paris In The Rain") & (data["Source Site"]=="Genie Music")]["Date"])

parisintherain_x6=list(data[(data["Title"]=="Paris In The Rain") & (data["Source Site"]=="Naver Vibe")]["Rangking"])
parisintherain_y6=list(data[(data["Title"]=="Paris In The Rain") & (data["Source Site"]=="Naver Vibe")]["Date"])

plt.title("Paris In The Rain on each Music Sites")
plt.grid()
plt.ylim((-1,100))
plt.xticks(rotation=45)
plt.xticks(rotation=45)
plt.plot(parisintherain_y1,parisintherain_x1,label = "Melon")
plt.plot(parisintherain_y2,parisintherain_x2,label = "Youtube")
plt.plot(parisintherain_y3,parisintherain_x3,label = "Bugs")
plt.plot(parisintherain_y4,parisintherain_x4,label = "Apple")
plt.plot(parisintherain_y5,parisintherain_x5,label = "Genie")
plt.plot(parisintherain_y6,parisintherain_x6,label = "Naver")
plt.legend()
plt.gca().invert_yaxis()
plt.savefig("Paris In The Rain 차트 비교.jpg")
plt.close()