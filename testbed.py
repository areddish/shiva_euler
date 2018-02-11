import shiva
import faster
from harness import average_run
   
if __name__ == "__main__":
   print("Running tests:")
   print("Shiva average: ", average_run(shiva.pythagorean_triplet)*1000, "ms")
   print("faster average: ", average_run(faster.pythagorean_triplet)*1000, "ms")
