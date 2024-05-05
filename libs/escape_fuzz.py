import random
import urllib.parse
import base64
import platform
import logging

class EscapeFuzzer:
    def __init__(self):
        self.escape = '\033['
        self.os = platform.system()
        self.commands = {
            'cursor_up': 'A',
            'cursor_down': 'B',
            'cursor_forward': 'C',
            'cursor_back': 'D',
            'cursor_next_line': 'E',
            'cursor_previous_line': 'F',
            'cursor_horizontal_absolute': 'G',
            'cursor_position': 'H',
            'erase_display': 'J',
            'erase_line': 'K',
            'scroll_up': 'S',
            'scroll_down': 'T',
            'save_cursor_position': 's',
            'restore_cursor_position': 'u',
            'hide_cursor': '?25l',
            'show_cursor': '?25h',
            'set_scroll_region': 'r',
            'set_tab': 'H',
            'clear_tab': 'g',
            'reset_device': 'c',
            'enable_line_wrap': '?7h',
            'disable_line_wrap': '?7l',
            'text_formatting_reset': '0m',
            'set_window_title': '2;',  # OSC command to set window title
            'notification': '9;'       # OSC command for notification
        }
        self.styles = {
            'reset': '0m',
            'bold': '1m',
            'underline': '4m',
            'blink': '5m',
            'reverse': '7m'
        }
        self.color_fg = range(30, 38)  # Standard colors
        self.color_bg = range(40, 48)  # Standard colors
        self.control_characters = {
            0x00: "NUL", 0x01: "SOH", 0x02: "STX", 0x03: "ETX",
            0x04: "EOT", 0x05: "ENQ", 0x06: "ACK", 0x07: "BEL",
            0x08: "BS",  0x09: "HT",  0x0A: "LF",  0x0B: "VT",
            0x0C: "FF",  0x0D: "CR",  0x0E: "SO",  0x0F: "SI",
            0x10: "DLE", 0x11: "DC1", 0x12: "DC2", 0x13: "DC3",
            0x14: "DC4", 0x15: "NAK", 0x16: "SYN", 0x17: "ETB",
            0x18: "CAN", 0x19: "EM",  0x1A: "SUB", 0x1B: "ESC",
            0x1C: "FS",  0x1D: "GS",  0x1E: "RS",  0x1F: "US",
            0x7F: "DEL"
        }
        logging.basicConfig(level=logging.DEBUG)
        self.adjust_for_platform()

    def set_hyperlink(self, url, text):
        start_osc = f'\033]8;;{url}\033\\'
        end_osc = '\033]8;;\033\\'
        return f'{start_osc}{text}{end_osc}'

    def set_clipboard(self, text, clipboard='c'):
        encoded_text = base64.b64encode(text.encode()).decode()
        return f"{self.escape}]52;{clipboard};{encoded_text}\033\\"

    def command_builder(self, *commands):
        result = f"{self.escape}"
        for command in commands:
            result += self.commands.get(command, '') + ';'
        return result.strip(';') + 'm'

    def set_256_color_fg(self, color_index):
        return f"{self.escape}38;5;{color_index}m"

    def set_true_color_fg(self, r, g, b):
        return f"{self.escape}38;2;{r};{g};{b}m"

    def set_window_title(self, title):
        return f"\033]0;{title}\007"

    def send_notification(self, message):
        return f"\033]{self.commands['notification']}{message}\007"

    def display_unicode(self, unicode_char):
        return unicode_char

    def adjust_for_platform(self):
        if self.os == "Windows":
            self.escape = '\033['
            logging.info("Adjusted escape sequences for Windows.")
        else:
            logging.info("Using standard UNIX/Linux escape sequences.")

    def random_command(self):
        command = random.choice(list(self.commands.values()))
        return f"{self.escape}{random.randint(1, 100)}{command}"

    def random_style(self):
        style = random.choice(list(self.styles.values()))
        return f"{self.escape}{style}"

    def random_color(self):
        fg = random.choice(list(self.color_fg))
        bg = random.choice(list(self.color_bg))
        return f"{self.escape}{fg}m{self.escape}{bg}m"

    def random_control_char(self):
        char_code = random.choice(list(self.control_characters.keys()))
        return chr(char_code)

    def url_encode(self, text):
        return urllib.parse.quote_plus(text)

    def fuzz(self, count=10, url_encode=False):
        results = []
        for _ in range(count):
            choice = random.choice([
                self.random_command, 
                self.random_style, 
                self.random_color, 
                self.random_control_char,
                lambda: self.set_hyperlink("http://example.com", "Example Link")
            ])
            results.append(choice())
        result = ''.join(results)
        if url_encode:
            return self.url_encode(result)
        return result

