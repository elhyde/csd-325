#Emmy Hyde
#10/26/25
#Module 1.3

def main():
    try:
        #Enter number of bottles
        beer = float(int(input('Enter the number of bottles: ')))
            # invalid number
    except ValueError:
        print('Invalid input. Please enter a number.')
        return
    while beer > 0:
        if beer > 1:
            print(f'{beer} bottles of beer on the wall, {beer} bottles of beer. '
                  f'You take one down and pass it around, {beer - 1} bottles of beer on the wall')
            beer -= 1
        else:
            #All out, time to make a beer run...
            print(f'Time to buy more bottles of beer.')
            break
main()
