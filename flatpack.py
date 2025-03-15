import serial
import csv
import sys
import io
import os
import random
import pygame

pygame.mixer.init()

ser = serial.Serial('/dev/cu.usbmodem14101', 9600)

try:
    while True:
        if ser.in_waiting > 0:
            data = ser.readline().decode('utf-8').strip()
            if data == "1":
                folder_path = '1'
                mp3_files = [file for file in os.listdir(folder_path) if file.endswith('.mp3')]
                random_mp3 = random.choice(mp3_files)
                file_path = os.path.join(folder_path, random_mp3)
                pygame.mixer.music.load(file_path)
                pygame.mixer.music.play()
                
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick(10)
                ser.write(b'5')
                
            if data == "2":
                folder_path = '2'
                mp3_files = [file for file in os.listdir(folder_path) if file.endswith('.mp3')]
                random_mp3 = random.choice(mp3_files)
                file_path = os.path.join(folder_path, random_mp3)
                pygame.mixer.music.load(file_path)
                pygame.mixer.music.play()
                
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick(10)
                ser.write(b'5')
                
            if data == "3":
                folder_path = '3'
                mp3_files = [file for file in os.listdir(folder_path) if file.endswith('.mp3')]
                random_mp3 = random.choice(mp3_files)
                file_path = os.path.join(folder_path, random_mp3)
                pygame.mixer.music.load(file_path)
                pygame.mixer.music.play()
                
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick(10)
                    
                ser.write(b'5')
            if data == "4":
                folder_path = '4'
                mp3_files = [file for file in os.listdir(folder_path) if file.endswith('.mp3')]
                random_mp3 = random.choice(mp3_files)
                file_path = os.path.join(folder_path, random_mp3)
                pygame.mixer.music.load(file_path)
                pygame.mixer.music.play()
                
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick(10)
                    
                ser.write(b'5')


except KeyboardInterrupt:
    ser.close()
    print("Serial port closed")
except serial.SerialException as e:
    print(f"Error: {e}")
finally:
    if ser.is_open:
        ser.close()