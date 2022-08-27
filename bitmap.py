import sys
# (!)Try changing this multiline string to any image you lie:
#There are 68 periods along the top and bottom of this string:
bitmap = """
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
...................................................................."""
print('bitmap message')
print('Enter the message to display with bitmap')
message = input('> ')
if message == ' ':
    sys.exit()

# Loop over each line in the bitmap:
for line in bitmap.splitlines():
    # loop over each character in the line:
    for i, bit in enumerate(line):
        if bit == ' ':
            #print an empty space since there is a space in the bitmap:
            print(' ', end =' ')
        else:
                # print a character from the message:
            print(message [i % len(message)], end = ' ')
print()