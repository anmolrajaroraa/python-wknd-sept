Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(0,10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(0,10,1))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(0,10,-1))
[]
>>> list(range(10,0,-1))
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
>>> list(reversed(range(0,10,1)))
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
>>> 
>>> '''
*
**
***
****
*****
'''
'\n*\n**\n***\n****\n*****\n'
>>> counter = 1
>>> for i in range(10):
	for j in range(counter):
		print('*')

		
*
*
*
*
*
*
*
*
*
*
>>> for i in range(10):
	print('j loop started')
	for j in range(counter):
		print('*')
	print('j loop ended')
	counter += 1

	
j loop started
*
j loop ended
j loop started
*
*
j loop ended
j loop started
*
*
*
j loop ended
j loop started
*
*
*
*
j loop ended
j loop started
*
*
*
*
*
j loop ended
j loop started
*
*
*
*
*
*
j loop ended
j loop started
*
*
*
*
*
*
*
j loop ended
j loop started
*
*
*
*
*
*
*
*
j loop ended
j loop started
*
*
*
*
*
*
*
*
*
j loop ended
j loop started
*
*
*
*
*
*
*
*
*
*
j loop ended
>>> for i in range(10):
	print('j loop started')
	for j in range(counter):
		print('*',end='')
	print('j loop ended')
	counter += 1

	
j loop started
***********j loop ended
j loop started
************j loop ended
j loop started
*************j loop ended
j loop started
**************j loop ended
j loop started
***************j loop ended
j loop started
****************j loop ended
j loop started
*****************j loop ended
j loop started
******************j loop ended
j loop started
*******************j loop ended
j loop started
********************j loop ended
>>> counter = 1
>>> for i in range(10):
	print('j loop started')
	for j in range(counter):
		print('*',end='')
	print('j loop ended')
	counter += 1

	
j loop started
*j loop ended
j loop started
**j loop ended
j loop started
***j loop ended
j loop started
****j loop ended
j loop started
*****j loop ended
j loop started
******j loop ended
j loop started
*******j loop ended
j loop started
********j loop ended
j loop started
*********j loop ended
j loop started
**********j loop ended
>>> for i in range(10):
	for j in range(counter):
		print('*',end='')
	counter += 1

	
***********************************************************************************************************************************************************
>>> counter = 1
>>> for i in range(10):
	for j in range(counter):
		print('*',end='')
	print('\n')
	counter += 1

	
*

**

***

****

*****

******

*******

********

*********

**********

>>> counter = 1
>>> for i in range(10):
	for j in range(counter):
		print('*',end='')
	print()
	counter += 1

	
*
**
***
****
*****
******
*******
********
*********
**********
>>> for i in range(10):
	for j in range(i + 1):
		print('*',end='')
	print()

	
*
**
***
****
*****
******
*******
********
*********
**********
>>> for i in range(10):
	for j in range(i + 1):
		print('*',end='')
	print()

	
*
**
***
****
*****
******
*******
********
*********
**********
>>> '''
    *
   **
  ***
 ****
*****
'''
'\n    *\n   **\n  ***\n ****\n*****\n'
>>> for i in range(10):
	for j in range(i + 1):
		print(' ',end='*')
	print()

	
 *
 * *
 * * *
 * * * *
 * * * * *
 * * * * * *
 * * * * * * *
 * * * * * * * *
 * * * * * * * * *
 * * * * * * * * * *
>>> 
>>> '''
i = [0,1,2,3,4]   4 - i
$$$$*
$$$**
$$***
$****
*****
'''
'\ni = [0,1,2,3,4]   4 - i\n$$$$*\n$$$**\n$$***\n$****\n*****\n'
>>> for i in range(10):
	for j in range(9 - i):
		print('$', end='')
	print()

	
$$$$$$$$$
$$$$$$$$
$$$$$$$
$$$$$$
$$$$$
$$$$
$$$
$$
$

>>> for i in range(10):
	for j in range(9 - i):
		print('$', end='')
	for k in range(i + 1):
		print(' ',end='*')
	print()

	
$$$$$$$$$ *
$$$$$$$$ * *
$$$$$$$ * * *
$$$$$$ * * * *
$$$$$ * * * * *
$$$$ * * * * * *
$$$ * * * * * * *
$$ * * * * * * * *
$ * * * * * * * * *
 * * * * * * * * * *
>>> for i in range(10):
	for j in range(9 - i):
		print('$', end='')
	for k in range(i + 1):
		print('*',end='')
	print()

	
$$$$$$$$$*
$$$$$$$$**
$$$$$$$***
$$$$$$****
$$$$$*****
$$$$******
$$$*******
$$********
$*********
**********
>>> for i in range(10):
	for j in range(9 - i):
		print(' ', end='')
	for k in range(i + 1):
		print('*',end='')
	print()

	
         *
        **
       ***
      ****
     *****
    ******
   *******
  ********
 *********
**********
>>> for i in range(10):
	for j in range(9 - i):
		print(' ', end='')
	for k in range(i + 1):
		print(' *',end='')
	print()

	
          *
         * *
        * * *
       * * * *
      * * * * *
     * * * * * *
    * * * * * * *
   * * * * * * * *
  * * * * * * * * *
 * * * * * * * * * *
>>> '''
$$$$*
$$$***
$$*****
$*******
*********
'''
'\n$$$$*\n$$$***\n$$*****\n$*******\n*********\n'
>>> for i in range(10):
	for j in range(10 - i):
		print('$', end='')
	print()

	
$$$$$$$$$$
$$$$$$$$$
$$$$$$$$
$$$$$$$
$$$$$$
$$$$$
$$$$
$$$
$$
$
>>> for i in range(10):
	for j in range(10 - i):
		print('$', end='')
	for k in range(i + 2)
	print()

	
SyntaxError: invalid syntax
>>> for i in range(10):
	for j in range(10 - i):
		print('$', end='')
	for k in range(i + 2):
		print('*',end='')
	print()

	
$$$$$$$$$$**
$$$$$$$$$***
$$$$$$$$****
$$$$$$$*****
$$$$$$******
$$$$$*******
$$$$********
$$$*********
$$**********
$***********
>>> for i in range(10):
	for j in range(10 - i):
		print('$', end='')
	for k in range(i * 2):
		print('*',end='')
	print()

	
$$$$$$$$$$
$$$$$$$$$**
$$$$$$$$****
$$$$$$$******
$$$$$$********
$$$$$**********
$$$$************
$$$**************
$$****************
$******************
>>> for i in range(10):
	for j in range(10 - i):
		print('$', end='')
	for k in range((i * 2) + 1 ):
		print('*',end='')
	print()

	
$$$$$$$$$$*
$$$$$$$$$***
$$$$$$$$*****
$$$$$$$*******
$$$$$$*********
$$$$$***********
$$$$*************
$$$***************
$$*****************
$*******************
>>> for i in range(10):
	for j in range(10 - i):
		print(' ', end='')
	for k in range((i * 2) + 1 ):
		print('*',end='')
	print()

	
          *
         ***
        *****
       *******
      *********
     ***********
    *************
   ***************
  *****************
 *******************
>>> '''
$$$$*
$$$***
$$*****
$*******
*********
$*******
$$*****
$$$***
$$$$*
'''
'\n$$$$*\n$$$***\n$$*****\n$*******\n*********\n$*******\n$$*****\n$$$***\n$$$$*\n'
>>> for i in range(20):
	if i <= 10:
		for j in range(10 - i):
			print('$',end='')

			
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
>>> for i in range(20):
	if i <= 10:
		for j in range(10 - i):
			print('$',end='')
		print()

		
$$$$$$$$$$
$$$$$$$$$
$$$$$$$$
$$$$$$$
$$$$$$
$$$$$
$$$$
$$$
$$
$

>>> for i in range(20):
	if i <= 10:
		for j in range(10 - i):
			print('$',end='')
		print()
	else:
		for j2 in range(i - 10)
		
SyntaxError: invalid syntax
>>> for i in range(20):
	if i <= 10:
		for j in range(10 - i):
			print('$',end='')
		print()
	else:
		for j2 in range(i - 10):
			print('$',end='')
		print()

		
$$$$$$$$$$
$$$$$$$$$
$$$$$$$$
$$$$$$$
$$$$$$
$$$$$
$$$$
$$$
$$
$

$
$$
$$$
$$$$
$$$$$
$$$$$$
$$$$$$$
$$$$$$$$
$$$$$$$$$
>>> for i in range(20):
	if i <= 10:
		for j in range(10 - i):
			print('$',end='')
		for k in range((i * 2) + 1 ):
			print('*',end='')
		print()
	else:
		for j2 in range(i - 10):
			print('$',end='')
		print()

		
$$$$$$$$$$*
$$$$$$$$$***
$$$$$$$$*****
$$$$$$$*******
$$$$$$*********
$$$$$***********
$$$$*************
$$$***************
$$*****************
$*******************
*********************
$
$$
$$$
$$$$
$$$$$
$$$$$$
$$$$$$$
$$$$$$$$
$$$$$$$$$
>>> #11 -> 19
>>> #12 -> 17
>>> #13 -> 15
>>> #14 -> 13
>>> #15 -> 11
>>> #16 -> 9
>>> #17 -> 7
>>> #18 -> 5
>>> #19 -> 3
>>> #20 -> 1for i in range(20):
	if i <= 10:
		for j in range(10 - i):
			print('$',end='')
		for k in range((i * 2) + 1 ):
			print('*',end='')
		print()
	else:
		for j2 in range(i - 10):
			print('$',end='')
		for k2 in range((20 - i) * 2):
			print('*',end='')
		print()
		
SyntaxError: unexpected indent
#20 -> 1for i in range(20):
	if i <= 10:
		for j in range(10 - i):
			print('$',end='')
		for k in range((i * 2) + 1 ):
			print('*',end='')
		print()
	else:
		for j2 in range(i - 10):
			print('$',end='')
		for k2 in range((20 - i) * 2):
			print('*',end='')
		print()
>>> if i <= 10:
	for j in range(10 - i):
		print('$',end='')
	for k in range((i * 2) + 1 ):
		print('*',end='')
	print()
    else:
	for j2 in range(i - 10):
		print('$',end='')
	for k2 in range((20 - i) * 2):
		print('*',end='')
	print()
	
SyntaxError: unindent does not match any outer indentation level
>>> 
>>> for i in range(21):
	if i <= 10:
		for j in range(10 - i):
			print('$',end='')
		for k in range((i * 2) + 1 ):
			print('*',end='')
		print()
	else:
		for j2 in range(i - 10):
			print('$',end='')
		for k2 in range((20 - i) * 2):
			print('*',end='')
		print()

		
$$$$$$$$$$*
$$$$$$$$$***
$$$$$$$$*****
$$$$$$$*******
$$$$$$*********
$$$$$***********
$$$$*************
$$$***************
$$*****************
$*******************
*********************
$******************
$$****************
$$$**************
$$$$************
$$$$$**********
$$$$$$********
$$$$$$$******
$$$$$$$$****
$$$$$$$$$**
$$$$$$$$$$
>>> for i in range(21):
	if i <= 10:
		for j in range(10 - i):
			print(' ',end='')
		for k in range((i * 2) + 1 ):
			print('*',end='')
		print()
	else:
		for j2 in range(i - 10):
			print(' ',end='')
		for k2 in range(((20 - i) * 2 ) + 1):
			print('*',end='')
		print()

		
          *
         ***
        *****
       *******
      *********
     ***********
    *************
   ***************
  *****************
 *******************
*********************
 *******************
  *****************
   ***************
    *************
     ***********
      *********
       *******
        *****
         ***
          *
>>> 
