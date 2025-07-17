from model import gemini, simtom_detection, direct_detection
import time

example_prompt_injection = ""
print("simtom:", simtom_detection(example_prompt_injection))
print("\n------------\n\n\n----------\n")
start_time = time.time()

print(f"direct: ```{direct_detection(example_prompt_injection)}```")
end_time = time.time()

print(end_time-start_time)
