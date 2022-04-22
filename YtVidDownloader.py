from pytube import YouTube

link = input("Enter the link of the video: ")

yt = YouTube(link)

print("Title: ", yt.title)

print("Number of views: ", yt.views)

print("Length of the video: ", yt.length,'seconds')

print("Description of the video ", yt.description)

print("Ratings: ", yt.rating)

print(yt.streams)

print(yt.streams.filter(only_audio=True))
print(yt.streams.filter(only_video=True))
print(yt.streams.filter(progressive=True))
yd = yt.streams.get_highest_resolution()
yd = yt.streams.get_by_itag("22")
yd.download()
yd.download("location")
