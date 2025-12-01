import os
import sys

def get_size_readable(size_in_bytes):
    """Converts raw bytes to KB, MB, GB so humans can read it."""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size_in_bytes < 1024.0:
            return f"{size_in_bytes:.2f} {unit}"
        size_in_bytes /= 1024.0
    return f"{size_in_bytes:.2f} PB"

def get_directory_size(path):
    """
    Calculates the total size of a directory by summing up
    every file inside it (and inside its sub-folders).
    """
    total_size = 0
    try:
        # os.scandir is faster than os.listdir for system tools
        with os.scandir(path) as it:
            for entry in it:
                if entry.is_file():
                    total_size += entry.stat().st_size
                elif entry.is_dir(follow_symlinks=False):
                    # RECURSION: The function calls itself!
                    total_size += get_directory_size(entry.path)
    except PermissionError:
        # This happens if we try to read a System folder (like "System Volume Information")
        return 0 
    except Exception as e:
        return 0
    return total_size

def print_tree(path, level=0, max_depth=2):
    """
    Prints the folder structure like a tree with sizes.
    max_depth prevents it from printing 1,000,000 lines.
    """
    if level > max_depth:
        return

    try:
        # Get all items in the current folder
        items = list(os.scandir(path))
        
        # Sort them: Folders first, then Files
        items.sort(key=lambda x: (not x.is_dir(), x.name.lower()))

        for entry in items:
            indent = "    " * level + "|-- "
            
            if entry.is_dir(follow_symlinks=False):
                # It's a folder: Calculate its size and print
                size = get_directory_size(entry.path)
                readable_size = get_size_readable(size)
                print(f"{indent}[DIR]  {entry.name}  ({readable_size})")
                
                # Go deeper into the tree (Recursion)
                print_tree(entry.path, level + 1, max_depth)
                
            else:
                # It's a file: Just print size (Optional: comment this out to see folders only)
                size = entry.stat().st_size
                readable_size = get_size_readable(size)
                # Only show files if they are large (e.g., > 100MB) to keep output clean
                if size > 100 * 1024 * 1024: 
                    print(f"{indent}[FILE] {entry.name}  ({readable_size})")
                    
    except PermissionError:
        print("    " * level + "|-- [ACCESS DENIED]")

if __name__ == "__main__":
    # 1. Ask the user for the drive (e.g., D:\ or C:\Users\Name)
    target_path = input("Enter drive path (e.g., D:\\ or /home/user): ").strip()
    
    if os.path.exists(target_path):
        print(f"\nScanning {target_path}... This might take a moment.\n")
        print(f"ROOT: {target_path}")
        print("-" * 40)
        
        # We limit depth to 2 levels so your screen doesn't explode with text
        print_tree(target_path, max_depth=1) 
        
        print("-" * 40)
        print("Scan Complete.")
    else:
        print("Error: That path does not exist.")
