def single_root_words(root_worlds, *other_worlds):
    same_words = []
    for i in other_worlds:
        if root_worlds.upper() in i.upper() or i.upper() in root_worlds.upper():
            same_words.append(i)

    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)