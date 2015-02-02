# Small python hack for Spotify Puzzle 'zipfsong', by Pontus Palmenäs
n, m = map(int, raw_input().split())
songs = []
for i in xrange(1, n + 1):
    f, s = raw_input().split()
    q = float(f) * i
    songs.append((i, q, s))
songs.sort(key=lambda x: x[1], reverse=True)
for i in xrange(m):
    print(songs[i][2])