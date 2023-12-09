import sys
sample_input1 = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
sample_input2 = "bvwbjplbgvbhsrlpgdmjqwftvncz"
sample_input3 = "nppdvjthqldpwncqszvftbrmjlhg"
sample_input4 = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
sample_input5 = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"

def start_of_sequence(line: str):
    for i in range(13, len(line)):
        testString = line[i-13:i+1]
        if len(set(testString)) == 14:
            return i + 1
    print("Error")
    return -1

if __name__ == "__main__":
    print(start_of_sequence(sample_input1))
    print(start_of_sequence(sample_input2))
    print(start_of_sequence(sample_input3))
    print(start_of_sequence(sample_input4))
    print(start_of_sequence(sample_input5))    

    with open('input') as inputfile:
        line = inputfile.readline()
    print(start_of_sequence(line))
