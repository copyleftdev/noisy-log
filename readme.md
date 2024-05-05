# Noisy Log

## Overview
Noisy Log is a Python library inspired by STOK's "Weaponizing Plain Text: ANSI Escape Sequences as a Forensic Nightmare". Tailored for developers who value the craft of code and the intricacies of cybersecurity, this tool enables sophisticated manipulation of log files and telemetry data through ANSI escape sequences.

## Features
- **Advanced Data Obfuscation:** Injects ANSI escape sequences into data streams, obscuring log readability and complicating forensic analysis.
- **Seamless Integration:** Easily integrates into any software service, allowing for strategic deployment and immediate impact.
- **Comprehensive Command Set:** Provides a robust selection of ANSI commands and styles, empowering users to customize their obfuscation techniques.

## Implications
Using Noisy Log introduces:
- **Complex Log Analysis:** Transforms straightforward logs into intricate puzzles, challenging conventional forensic techniques.
- **Increased Analytical Demands:** Necessitates advanced analytical methods to decode the altered data.
- **Evasion Capabilities:** Offers a refined method to mask potentially malicious activities within obscured logs.

## Ideal Use Cases
- **Enhanced Security Testing:** Assess the resilience of log analysis tools against complex obfuscation.
- **Red Team Operations:** Equip red teams with advanced tools for simulating threats that manipulate log outputs.
- **Cybersecurity Research:** Investigate the impact of log manipulation in various security scenarios.

## Getting Started
### Prerequisites
- Python 3.6 or newer



### Usage
Deploy obfuscation with the `EscapeFuzzer` class from `libs\escape_fuzz.py`:
```python
from libs.escape_fuzz import EscapeFuzzer

fuzzer = EscapeFuzzer()

# Example obfuscation commands
print(fuzzer.set_window_title("My Custom Terminal"))
print(fuzzer.send_notification("Notification: Task Completed!"))
print(fuzzer.set_hyperlink("https://www.example.com", "Visit our website"))
print(fuzzer.set_256_color_fg(125))
print(fuzzer.set_true_color_fg(255, 100, 100))
print(fuzzer.display_unicode('ℜ'))
print(fuzzer.fuzz(5))
```

## Contributing
Contribute to Noisy Log:
- Fork the Project
- Create your Feature Branch (`git checkout -b feature/YourNewFeature`)
- Commit your Changes (`git commit -m 'Add some YourNewFeature'`)
- Push to the Branch (`git push origin feature/YourNewFeature`)
- Open a Pull Request

## Credits
This project was inspired by the research of [STOK Fredrik](https://github.com/stokfredrik). His innovative insights into ANSI escape sequences have significantly influenced the development of Noisy Log.

## Contact
**copyleftdev** - [@copyleftdev](https://github.com/copyleftdev)