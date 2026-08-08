import datetime
import time
import pygame

def set_alarm(alarm_time):
    print(f"Alarm is set for: {alarm_time}")
    sound_file = "audio.mp3"
    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%I:%M:%S %p")
        print(current_time)

        if current_time == alarm_time:
            print("WAKE UP! ⏰⏰")
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)

                is_running = False

        time.sleep(1)


if __name__ == "__main__":
    alarm_time = input("Enter the alarm time (HH:MM:SS  AM/PM): ")
    set_alarm(alarm_time)




