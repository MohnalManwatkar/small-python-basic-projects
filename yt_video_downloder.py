from pytube import YouTube

link = "https://www.youtube.com/watch?v=TpKcAmaaBts"

youtube_1 = YouTube(link)

# print(youtube_1.title)
# print(youtube_1.thumbnail_url)

# Creating a variable for streaming quality
# videos = youtube_1.streams.all()

videos = youtube_1.streams.filter(only_audio=False)

vid = list(enumerate(videos))  #creatin a list of streaming quality for choose for download

for i in vid:
    print(i)

strm = int(input('enter :  '))
videos[strm].download()
print('Successfully downloaded')


