# OCR.py
import numpy as np
import cv2
import pytesseract
from selenium import webdriver
from selenium.webdriver.common.by import By
import re

# Path to tesseract (adjust if needed)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# --- Method 1: From Screenshot (classic OCR) ---
def extract_puzzle_from_image(img_path, grid_size=3):
    img = cv2.imread(img_path)
    if img is None:
        return None
    h, w = img.shape[:2]
    cell_h, cell_w = h // grid_size, w // grid_size
    board = np.zeros((grid_size, grid_size), dtype=int)

    for i in range(grid_size):
        for j in range(grid_size):
            y1, y2 = i * cell_h, (i + 1) * cell_h
            x1, x2 = j * cell_w, (j + 1) * cell_w
            cell = img[y1:y2, x1:x2]
            gray = cv2.cvtColor(cell, cv2.COLOR_BGR2GRAY)
            th = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                       cv2.THRESH_BINARY, 31, 9)
            th = cv2.bitwise_not(th)
            th = cv2.resize(th, None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC)
            config = "--psm 10 -c tessedit_char_whitelist=0123456789"
            text = pytesseract.image_to_string(th, config=config).strip()
            board[i, j] = int(text) if text.isdigit() else 0
    return board

# --- Method 2: Manual Input (hand the array) ---
def extract_puzzle_from_input():
    print("Enter 9 numbers row by row (use 0 for blank):")
    nums = list(map(int, input().split()))
    if len(nums) != 9:
        raise ValueError("You must enter exactly 9 numbers.")
    return np.array(nums).reshape(3,3)

# --- Method 3: Live Browser (via Selenium) ---
def open_puzzle():
    driver = webdriver.Edge()  # or webdriver.Chrome()
    driver.get("https://www.bing.com/spotlight/imagepuzzle")
    return driver
def extract_puzzle_from_site(driver):
    tiles = driver.find_elements(By.CSS_SELECTOR, "div.tile")
    nums = []
    for el in tiles:
        txt = el.text.strip()
        if txt.isdigit():
            val = int(txt)
        else:
            classes = (el.get_attribute("class") or "").split()
            token = classes[0] if classes else ""
            if token.isdigit() and 0 <= int(token) <= 7:
                # If it's a numbered tile but text didn't show, map class id+1
                val = int(token) + 1
            else:
                # Random id tile = blank
                val = 0
        nums.append(val)

    print("Scraped numbers (with blank as 0):", nums)

    if len(nums) != 9:
        raise ValueError(f"Expected 9 tiles, got {len(nums)}: {nums}")

    return np.array(nums).reshape(3,3)

