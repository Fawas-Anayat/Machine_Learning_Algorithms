from pytube import YouTube

# Step 1: Paste your YouTube video URL
url = "https://youtu.be/wkxZFLkVBvI?si=3RThMRsjkx4f2d2v"

# Step 2: Create a YouTube object
yt = YouTube(url)

# Step 3: Choose the highest resolution stream
stream = yt.streams.get_highest_resolution()

# Step 4: Download the video
stream.download()  # Downloads to current working directory

print("✅ Download completed successfully!")
