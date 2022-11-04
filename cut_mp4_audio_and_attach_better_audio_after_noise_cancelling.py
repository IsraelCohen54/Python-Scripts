import ffmpeg

"""First, follow that tutorial until 13:40:
            https://www.youtube.com/watch?v=jSxQY50HXsI
After that, you can continue use her solution only once... hence my program:"""

# Todo change each time!!! so it won't delete existing one with that name ~~~
OUTPUT_PATH = "C:/Users/hartk/Desktop/slam/lectures/Lect03_noise_reduction.mp4"

# Todo change path to current needed video:
video_without_audio = ffmpeg.input("C:/Users/hartk/Desktop/slam/lectures"
                                   "/Lect03 67604 CV Based Navigation-012.mp4").video  # get only video channel

# Todo change path to current processed noise reduction audio of the above video:
audio_after_noise_reduction = ffmpeg.input("C:/Users/hartk/OneDrive/Documents/Audacity"
                                           "/Lect03 audio noise reduced.mp3").audio  # get only audio channel

output = ffmpeg.output(video_without_audio, audio_after_noise_reduction
                       , OUTPUT_PATH, vcodec='copy', acodec='aac', strict='experimental')
ffmpeg.run(output)
