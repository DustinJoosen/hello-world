import pyautogui
import time
import os
import moviepy.video.io.ImageSequenceClip


class Recorder:
	def __init__(self, seconds_recording, frame_rate=24, output_file="recording.mp4", image_folder="screenshots"):
		self.seconds_recording = seconds_recording
		self.frame_rate = frame_rate
		self.output_file = output_file
		self.image_folder = image_folder

		self.amount_frames = self.frame_rate * self.seconds_recording

		self.image_files = []
		self.screenshots = []

	def Record(self):
		print("Recording")
		frame_duration = 1 / self.frame_rate

		for _ in range(self.amount_frames):
			start_time = time.time()
			self.screenshots.append(pyautogui.screenshot())

			time.sleep(int(frame_duration - (time.time() - start_time)))

	def Save(self):
		print("Saving")
		for i, screenshot in enumerate(self.screenshots):
			screenshot.save(f"{self.image_folder}/{i + 1}.png")

		self.Convert()

	def Convert(self):
		print("Converting")
		for i in range(self.amount_frames):
			self.image_files.append(f"{self.image_folder}/{str(i + 1)}.png")

		clip = moviepy.video.io.ImageSequenceClip(self.image_files, fps=self.frame_rate)
		clip.write_videofile(self.output_file)
