songs = ["ROCKSTAR", "Do It", "For The Night"]
print(songs[1:3])
songs[2] = "She Said She Said"
print(songs)
songs.extend(["Starman", "While My Guitar Gently Weeps", "Diddy Bop"])
print(songs)
del songs[0]
print(songs)
for song in songs:
    print(song)
for i in range(len(songs)):
    print(songs[i])

animals = ["Cat", "Dog", "Bird"]
animals.append("Elephant")
print(animals[2])
del animals[0]
for animal in animals:
    print(animal)

