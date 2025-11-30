import inspect, pyperclip
import src.sparkSession
code  = inspect.getsource(src.sparkSession)
pyperclip.copy(code)
