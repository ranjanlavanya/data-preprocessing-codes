# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 14:39:35 2024

@author: Lavanya Ranjan
"""
# converts all videos with (.mp4) extension in a folder to (.mts) extension for ethovision analysis.

import os
import subprocess

# Ensure the working directory is correct (optional)
os.chdir("D:\\Setups\\python\\ffmpeg")
print(os.getcwd())

def convert_mp4_to_mts(input_file, output_file):
    # Check if the input file exists
    if not os.path.isfile(input_file):
        print(f"Error: The file {input_file} does not exist.")
        return

    # Run the ffmpeg command to convert the file with stream copy to preserve settings
    try:
        subprocess.run(['ffmpeg', '-i', input_file, '-codec', 'copy', output_file], check=True)
        print(f"Successfully converted {input_file} to {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error: Conversion failed with message {e}")

def batch_convert_mp4_to_mts(input_folder, output_folder):
    # Check if the input folder exists
    if not os.path.isdir(input_folder):
        print(f"Error: The folder {input_folder} does not exist.")
        return

    # Ensure output folder exists, if not, create it
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Iterate over all .mp4 files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith('.mp4'):
            input_file = os.path.join(input_folder, filename)
            print(f"Converting: {input_file}")
            output_file = os.path.join(output_folder, filename.replace('.mp4', '.MTS'))
            convert_mp4_to_mts(input_file, output_file)
        else:
            print(f"{filename} is not an .mp4 file, skipping.")

# Example usage
input_folder = r'D:\Setups\python\ffmpeg\codes\ELS_EPM'
output_folder = r'D:\Setups\python\ffmpeg\codes\ELS_EPM\output_mts'
batch_convert_mp4_to_mts(input_folder, output_folder)
