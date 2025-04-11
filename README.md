# Auto-Battle Script (Educational Purposes Only)


This Python script automates gameplay in a web-based Pokémon game by simulating keyboard inputs and mouse clicks to battle common mobs across two game accounts.

--- 

## 🚀 Features

- Switches between two game accounts and automates battle sequences
- Uses `pydirectinput`'s image recognition  to detect battle start screens and specific Pokémon
- Avoids attacking valuable Pokémon by identifying them through screenshots
- Users can customize which mobs are considered "common" by adding their own screenshots to the `common_pokemon` list in the script
- Terminates safely when encountering unexpected events or failing to identify battles
- Simulates movement with `pydirectinput` to initiate wild encounters

---

## 🧠 How It Works

1. The script starts with a short delay (2 seconds) to give you time to focus the game window.
2. It begins on the **top account tab** and alternates between the two accounts.
3. For each account, the script:
   - Scans a specified region of the screen for the battle start screen using image recognition.
   - If no battle is found, it simulates movement to trigger an encounter.
   - If a battle is found, it checks if the encountered Pokémon is in a list of **common mobs** using additional image detection.
   - If a common Pokémon is detected, it performs a series of clicks to initiate an attack.
   - If no known Pokémon is identified after a few attempts, the script exits safely using `sys.exit`.
4. After a successful battle or a failed detection, the script switches to the other account tab by clicking predefined coordinates.
5. This cycle continues indefinitely unless terminated by an unexpected event or a manual stop.

## 📸 Screenshots Template Tips

- Keep image resolution consistent with the game window and your screen settings  
- Use tightly cropped, unique parts of the sprite or UI to improve detection accuracy  
- Test and adjust `confidence` levels in `pyautogui.locateOnScreen()` between `0.90` and `0.95` for optimal results  
- Save all `.png` files in the same directory as the script, or you can create a folder for them

