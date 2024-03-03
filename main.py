import winsound
from rich.console import Console
from rich.theme import Theme
import random, time

from rich.progress import track

# custom theme ->
custom_theme = Theme({
    "error": "bold red",
    "success": "bold green",
    "prompt": "cyan",
    "input": "green",
})
# using console ->
console = Console(theme=custom_theme)
# start
console.print("Welcome to bpg by [cyan]@oopshnik[clear]")
inp = console.input("""[yellow](s)[clear]tart [magenta](h)[clear]elp [red](e)[clear]xit   ->""")
if "h" in inp:
    console.print("""
frequency(hz) hz played (minimal 37)
duration(ms) - duration how long is beep played (1000ms - 1s)            
""")
elif "e" in inp:
    console.print("Exiting...", style="error")
    exit()
else:
    console.clear()


ads_list = ["(random ad)", "github.com/oopshnik", "gitlab.com/oopshnik", "your advertisement could be here"]

random_index = random.randint(0, 3)
console.print("Welcome to bpg by [cyan]@oopshnik[clear]")

console.print(f"[bold]ad: [blink][red]{ads_list[random_index]}")

def beep():
    while True:
        try:

            frequency = int(console.input("[prompt]frequency [input](hz):[/input] "))
            if frequency <= 36:
                console.print("Frequency must be more than 36", style="error")
                continue  # restart
            
            duration = int(console.input("[prompt]duration [input](ms):[/input] "))
            console.print(f"Beeping at {frequency} Hz for {duration} ms ✅", style="success") 
            
            # Beep
            winsound.Beep(frequency, duration)

        except ValueError: # if value error:
            console.print("Error: Please enter a valid integer", style="error")
        except KeyboardInterrupt: # if ctrl+c error
            console.print("Exiting...", style="error")
            break
        except Exception as e: # other errors
            console.print(f"Error: {e}", style="error")

beep()
