from libs.escape_fuzz import EscapeFuzzer

term = EscapeFuzzer()
print(term.set_window_title("My Custom Terminal"))
print(term.send_notification("Notification: Task Completed!"))
print(term.set_hyperlink("https://www.example.com", "Visit our website"))
print(term.set_256_color_fg(125))
print(term.set_true_color_fg(255, 100, 100))
print(term.display_unicode('ℜ'))
print(term.fuzz(5, False))