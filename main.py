from moviepy.editor import VideoFileClip
from moviepy.editor import CompositeVideoClip
from moviepy.editor import ImageClip
import os

# constants
input_folder_path = os.path.join(os.getcwd(), "input")
output_folder_path = os.path.join(os.getcwd(), "output")

logo_image_clip = ImageClip("python_logo.png").set_position(("left", "top"))

# go through all videos in input folder
for f in os.listdir("input"):
    filename, ext = os.path.splitext(f)
    if ext in [".mp4", ".mkv", ".mov", ".avi"]:
        vc = VideoFileClip(os.path.join(input_folder_path, f))
        logo_image_clip = logo_image_clip.set_duration(vc.duration)

        composite_video = CompositeVideoClip([vc, logo_image_clip])
        composite_video.write_videofile(os.path.join(output_folder_path, f),
                                        threads=os.cpu_count(),
                                        audio_codec="aac")