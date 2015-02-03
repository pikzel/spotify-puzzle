# Small python hack for Spotify Puzzle 'reversebinary', by Pontus Palmenäs
# Who needs readability anyway? ;)
print int(str(bin(int(raw_input())))[2:][::-1], 2)