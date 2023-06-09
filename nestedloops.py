
iterations = ["first", "second", "third"]

print("Starting the outer loop!")

for outer_number in iterations:
    print("Starting the inner loop!")

    for inner_number in iterations:
        print(f"The outer loop is on its {outer_number} iteration, while the inner loop is on its {inner_number} iteration")
    
    print("Inner loop complete!")
print("Outer loop complete")