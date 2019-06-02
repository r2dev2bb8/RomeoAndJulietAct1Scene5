import vlc

effect_objects = []
song_names = ["knuckles.mp3", "Cantina.mp3", "Huliet.mp3"]

counter = 1
for i in song_names:
    effect_objects.append(vlc.MediaPlayer(i))
    print(str(counter) + " " + i[:-4])
    counter += 1

success = False
while not success:
    effect = effect_objects[int(input("effect number ")) - 1]
    effect.play()
    stop = input("close effect(press enter) ")
    effect.stop()
    if stop == "quit":
        success = True
