# Ask user for width snf loop until they
# Enter a number that is more than zero
def int_check(question, low):

        error = f"Please enter a number that is more than or equal to {low}\n"
        while True:


            try:
                # ask the user for a number
                    response = int(input(question))

                # check that the number is more than zero

                    if response >=low:
                       return response
                    else:
                        print(error)


            except ValueError :
                print(error)


# Calculate how many bits are needed to represent an integer
def image_calc():
    width = int_check("width: ", 1)
    height = int_check("height: ", 1)
    print(height)

    # Calculate the number of pixels and multiply by 24 to get the number of bits
    num_pixels = width * height
    num_bits = num_pixels * 24

    # Set-up answer and return it
    answer = (f"\nNumber of pixels: {width} * {height} = {num_pixels}"
              f" \nNumber of bits: {num_pixels} * 24 ={num_bits}")

    return answer

# Main routine goes here
image_ans = image_calc()
print(image_ans)

