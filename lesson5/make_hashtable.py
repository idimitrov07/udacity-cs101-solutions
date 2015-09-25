def make_hashtable(nbuckets):
    table = []
    for b in range(0, nbuckets):
        table.append([])
    return table

print make_hashtable(13)
