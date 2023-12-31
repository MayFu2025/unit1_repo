# Make a Combini!
# Possible improvements:
# -Key interruptions
# -Timed scrolling
# -Split change in correct notes
# -Delete items
# -Calculate change
# -Add photo
# -User colors
# -Indicate Qty from user input
# -Read from file the inventory
# -Password protection
# -Saving the sales to check profit
# -Employee discount

def frame_maker(msg:str, symbol:str, spaces:int)->str:
    height = 5
    width = 2+2*spaces+len(msg)
    cyan = "\33[0;36m"
    end_code = "\33[0m"

    top_line = symbol*width
    middle_line = symbol + (" "*(width-2)) + symbol
    msg_line = symbol + " "*spaces + msg.title() + " "*spaces + symbol
    banner = f"{top_line}\n{middle_line}\n{msg_line}{end_code}\n{middle_line}\n{top_line}"

    return banner

title = 'Welcome to Combini!'
items = ['onigiri', 'bread', 'chips', 'coffee', 'ice cream']
prices = [500, 200, 150, 100, 150]
total = 0
logo = """
         _.-.
       ,'/ //\.
      /// // /)
     /// // //|
    /// // ///
   /// // ///
  (`: // ///
   `;`: ///
   / /:`:/
  / /  `'
 / /
(_/  Combini
"""

print(logo)

#                  Menu
#1. Onigiri........................500yen
#2. Bread..........................200yen


print(f"{frame_maker(msg=title, symbol='*', spaces=19)}\n") #Make frame

print("Menu".center(50,' ')) #Print Menu
for it in range(len(items)):
    print(f"{it+1}. {items[it].title().ljust(50, '.')}{prices[it]}yen")

order = [] #Empty list for user order
ordering = True

while ordering:
    selection = (input(f"\nPlease enter a item number (1-{len(items)}): "))
    available = "" #Empty string
    for i in range(len(items)): #For loop to append the numbers user can input
        available += str(i+1)
    while not (selection.isdigit() and selection in available): #Don't trust the user.
        selection = (input(f"Error. Please enter a item number (1-{len(items)}): "))

    order.append(int(selection)-1) #Append order to cart
    total += prices[int(selection)-1]

    for it in range(len(items)):
        count = 0
        for o in order:
            if o == it:
                count += 1
        if count > 0:
            total_price = prices[it]*count
            print(f'{items[it].title().ljust(20)} x {count} = {total_price}yen')

    answer = input("\nWould you like to check out? (Y/N:)  ")
    while not answer in "yYnN":
        answer = input("\nError. Check out? (Y/N):  ")

    if answer in "yY":
        ordering = False


print(frame_maker(msg=f"Your total is {(total*1.1):.2f} yen.", symbol='*', spaces=19))

