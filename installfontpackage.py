import os
import shutil
import winreg

def install_font(font_file_path):
    font_dir = os.path.join(os.environ['WINDIR'], 'Fonts')
    
    try:
        shutil.copy(font_file_path, font_dir)
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Fonts", 0, winreg.KEY_SET_VALUE)
        font_name = os.path.splitext(os.path.basename(font_file_path))[0]

        winreg.SetValueEx(key, font_name, 0, winreg.REG_SZ, font_file_path)
        winreg.CloseKey(key)
        
        print(f'Die Schriftart "{font_name}" wurde erfolgreich hinzugefügt.')

    except Exception as e:
        print(f'Fehler beim Hinzufügen der Schriftart: {str(e)}')

if __name__ == "__main__":
    font_file_path = "C:\\Users\\eduard.wagner\\Desktop\\Space_Grotesk\\SpaceGrotesk-VariableFont_wght.ttf"
    install_font(font_file_path)
