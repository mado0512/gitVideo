import time


def reportPer(waitTime: int) -> None:
	for i in range(5):
		print(time.time())
		time.sleep(5)


if __name__ == '__main__':
	reportPer(0.25)
	seconds: int = 1
	print(f"Then report per {seconds} seconds")
	reportPer(seconds)
