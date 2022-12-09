from pygame import mixer

# Sounds to play:
mixer.init()
sound_enemyHit = mixer.Sound("materials/sounds/enemyHit.wav")
sound_baseHit = mixer.Sound("materials/sounds/baseHit.wav")
sound_selection = mixer.Sound("materials/sounds/selection.wav")
sound_build = mixer.Sound("materials/sounds/build.wav")
sound_upgrade = mixer.Sound("materials/sounds/upgrade.wav")
sound_shot = mixer.Sound("materials/sounds/shot.wav")
sound_bgMusic = mixer.Sound("materials/sounds/bgMusic.mp3")


# Class for binding audiofiles to methods:
class AudioController:

    #Set volume
    def __init__(self):
        sound_selection.set_volume(0.25)
        sound_shot.set_volume(0.5)
        sound_build.set_volume(0.6)
        sound_upgrade.set_volume(0.6)
        sound_bgMusic.set_volume(0.2)
        pass

    #play
    def playEnemyHit(self):
        sound_enemyHit.play()

    def playBaseHit(self):
        sound_baseHit.play()

    def playShot(self):
        sound_shot.play()

    def playBuild(self):
        sound_build.play()

    def playUpgrade(self):
        sound_upgrade.play()

    def playSelection(self):
        sound_selection.play()

    def playBg(self):
        sound_bgMusic.play(100)
