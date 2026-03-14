# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 14:39:35 2024

@author: Lavanya Ranjan
"""
# converts videos with (.mts) extension to (.mp4) extension for DLC analysis.

import os
import subprocess

# Ensure the working directory is correct (optional)
os.chdir("D:\\Setups\\python\\ffmpeg")
print(os.getcwd())

def convert_mts_to_mp4(input_file, output_file):
    # Check if the input file exists
    if not os.path.isfile(input_file):
        print(f"Error: The file {input_file} does not exist.")
        return
      
    # Run the ffmpeg command to convert the file
    try:
        subprocess.run(['ffmpeg', '-i', input_file, '-codec', 'copy', output_file], check=True)
        print(f"Successfully converted {input_file} to {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error: Conversion failed with message {e}")

def batch_convert_mts_to_mp4(input_folder, output_folder):
    # Check if the input folder exists
    if not os.path.isdir(input_folder):
        print(f"Error: The folder {input_folder} does not exist.")
        return
    
    # Iterate over all .mts files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith('.MTS'):
            input_file = os.path.join(input_folder, filename)
            print(input_file)
            output_file = os.path.join(output_folder, filename.replace('.MTS', '.mp4'))
            convert_mts_to_mp4(input_file, output_file)
        else: print(".mts not found!!!!!")

# Example usage
input_folder = r'D:\Setups\python\ffmpeg\codes\representative_vids'
output_folder = r'D:\Setups\python\ffmpeg\codes\representative_vids\output_mp4'
batch_convert_mts_to_mp4(input_folder, output_folder)


