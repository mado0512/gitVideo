import time


def runPer(waitTime: int, fn, iter=5) -> None:
	for i in range(iter):
		fn()
		time.sleep(waitTime)


if __name__ == '__main__':
	reportTime = lambda : print(time.time())
	
	wts: [int] = [0.25, 1, 2, 3]	
	for wt in wts:
		print(f'Report time per {wt} seconds')
		runPer(wt, reportTime,iter=10)
