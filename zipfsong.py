n, m = map(int, raw_input().split())
songs = []
for i in range(1,n+1):
	f, s = raw_input().split()
	z = 1/float(i)
	q = int(f)/float(z)
	songs.append((i,q,s))
songs.sort(key=lambda x: x[1], reverse=True)
for i in range(m):
	print(songs[i][2])
