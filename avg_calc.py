from typing import List


def total_nums(nums: List[int]):
    """Calculates a list of numbers"""
    result = 0

    for n in nums:
        result += n

    return result


def main():
    numbers: List[int] = []

    while True:
        cmd = input('Either input a number or use "help": ')

        # calculates the average number
        if cmd == 'avg':
            total = total_nums(numbers)
            return total / len(numbers)
        # shows the available commands
        elif cmd == 'help':
            print('* edit [index] [new number] -- To modify a value')
            print('* avg -- To calculate the average amount')
            print('* show -- To show the existing numbers')
            continue
        # shows the list of numbers that is added
        elif cmd == 'show':
            if not numbers:
                print('No numbers were inputted yet!')
                continue

            print(' ')
            for i, n in enumerate(numbers):
                print(f'[{i}] {n}')

            print(f'Total : {total_nums(numbers)}')
            print(f'Count : {len(numbers)}')
            
            continue
        # allows u to edit/modify a number that was added
        elif cmd.startswith('edit'):
            args = cmd.split(' ')
            args.pop(0)

            try:
                index = int(args[0])
                new_num = int(args[1])

                numbers[index] = new_num

                print(' ')
                print(f'Changes is made on index of {index} and replaced with {new_num}!')
                print(f'Total : {total_nums(numbers)}')
            except:
                print('Invalid command :/')

            continue

        try:
            number = int(cmd)
        except:
            print('Invalid number or command!')
            continue

        numbers.append(number)

        print(' ')
        print(f'Added  : {number}')
        print(f'Total  : {total_nums(numbers)}')
        print(f'Count  : {len(numbers)}')


if __name__ == "__main__":
    average = main()
    print(f'The average is {average}')
