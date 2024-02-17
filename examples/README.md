# Examples 👨🏼‍💻

Here are some examples to get you started.

**Covered topics:** 
- **Branching** (Conditional Statements)

## Example 1: Temperature Feedback Messages
**Problem:** Write a program where the user enters a temperature value, and if this value is less than or equal to `0` degrees Celsius, you need to display the message "A cold, isn’t it?". If the temperature is more than `0` and less than `10` degrees Celsius, the message will be "Cool.". In other cases, "Nice weather we’re having.".

| No. | Inputs | Outputs                         |
| --- | ------ | ------------------------------- |
| 1   | 12.5   | Nice weather we're having.      |
| 2   | -5     | A cold, isn't it?               |
| 3   | 9      | Cool.                           |

## Example 2: Football Match Scoring
**Problem:** In a football championship, a team is given `3` points for a win, `0` for a loss, and `1` for a draw. The number of points received by the team for the game is known. Display the result of the game in the form of corresponding words: "win", "loss", or "draw".

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 3      | win     |
| 2   | 1      | draw    |
| 3   | 0      | lose    |

## Example 3: Positive, Negative, or Zero Determination
**Problem:** Determine whether an entered number is positive, negative, or zero.

| No. | Inputs | Outputs                |
| --- | ------ | ---------------------- |
| 1   | 7      | It is a positive number|
| 2   | -5.6   | It is a negative number|
| 3   | 0      | It is Zero             |

## Example 4: Spacecraft Trajectory
**Problem:** Write a program that determines the behavior of a spacecraft launching at the equator, depending on its initial speed `v`, given in km/s (real numbers). There are four possible cases: 
- if `v < 7.8` km/s, the device will fall to the Earth's surface; 
- if `7.8 ≤ v < 11.2` km/s, the device will become a satellite of the Earth; 
- if `11.2 ≤ v < 16.4` km/s, the device will become a satellite of the Sun; 
- if `v ≥ 16.4` km/s, the spacecraft will leave the Solar System.

| No. | Inputs | Outputs                               |
| --- | ------ | ------------------------------------- |
| 1   | 12.5   | The device will become a satellite of the Sun. |
| 2   | 8.3    | The device will become a satellite of the Earth. |
| 3   | 0      | The device will fall to the Earth's surface. |
| 4   | 20     | The device will leave the Solar System. |

## Example 5: Grading System Interpretation
**Problem:** The university uses the following scale to interpret student test results: 
- `90` points and above (A), 
- `80-89` (B), 
- `70-79` (C), 
- `60-69` (D), 
- below `60` (F). 

Write a program that allows the student to enter the test score, and then display the grade for this score.

| No. | Inputs | Outputs             |
| --- | ------ | ------------------- |
| 1   | 95     | Your grade is A.    |
| 2   | 74     | Your grade is C.    |
| 3   | 60     | Your grade is D.    |

## Example 6: Day of the Week Determination
**Problem:** Determine the day of the week based on a number entered by the user.

| No. | Inputs | Outputs                      |
| --- | ------ | ---------------------------- |
| 1   | 5      | Friday                       |
| 2   | 2      | Tuesday                      |
| 3   | 7      | Sunday                       |

## Example 7: Magic date

**Problem:** We will call the date October 2, 2020, "magic" because when it is written in the format `02.10.20`, the product of the day and month values equals the year value. Write a program that asks the user to enter the day, month, and year (only the last two digits) in numerical form. The program should output a message that the entered date is "magic". Otherwise, there should be a message that it is a regular date.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 2<br>10<br>20 | The date is magic! |
| 2   | 3<br>11<br>21 | The date is not magic. |
| 3   | 1<br>1<br>21  | The date is not magic. |


## Example 8: Roman Numeral Conversion
**Problem:** Convert a decimal number within 1 to 10 into its Roman numeral equivalent.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 8      | VIII    |
| 2   | 10     | X       |
| 3   | 4      | IV      |

## Example 9: Software Package Discount Calculation
**Problem:** A software manufacturer in the field of information security sells one set of programs for £2700. If multiple units of goods are purchased, a discount system works: 
- `10-19` units of goods - `10%`, 
- `20-49` - `20%`, 
- `50-99` - `30%`, 
- `100` or more - `40%`. 

Write a program that receives from the user an integer - the number of purchased software sets and outputs a message about the amount of the discount (if any) and the total amount of the purchase with the discount.

| No. | Inputs | Outputs                                                   |
| --- | ------ | --------------------------------------------------------- |
| 1   | 26     | The amount of discount is 20%, total amount of the purchase after the discount is £56160.00 |
| 2 | 3 | The amount of discount is 0%, total amount of the purchase after the discount is £8100.00 |
| 3 | 110 | The amount of discount is 40%, total amount of the purchase after the discount is £178200.00 |


## Example 10: Days in a Month
**Problem:** Output the number of days in a given month.

| No. | Inputs   | Outputs                     |
| --- | -------- | --------------------------- |
| 1   | February | February has 28 or 29 days in it. |
| 2   | April    | April has 30 days in it.    |
| 3   | December | December has 31 days in it. |

## Example 11: Tax Calculation Based on Brackets
**Problem:** Depending on the size of the amount, the tax from it is calculated according to the following scheme: 
- if the amount does not exceed a certain value `a`, then the tax is not calculated; 
- if the amount is greater than `a` but does not exceed `b`, then the tax is `10%`; 
- if the amount is greater than `b` but does not exceed `c`, then the tax is `25%`; 
- if the amount is greater than `c`, then the tax is `50%`. 

Determine what tax (real number) will be calculated from the amount of size `s`. The data (integers) are entered in the following order: `a`, `b`, `c`, `s`.

| No. | Inputs | Outputs                        |
| --- | ------ | ------------------------------ |
| 1   | 1000<br>10000<br>100000<br>15000 | 1500.0 |
| 2   | 1000<br>10000<br>100000<br>5000  | 500.0  |
| 3   | 1000<br>10000<br>100000<br>500000 | 250000.0 |


## Example 12: Ending with 5 Determination
**Problem:** Determine if a given number ends with the digit 5.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 12395  | True    |
| 2   | 123    | False   |
| 3   | 0      | False   |

## Example 13: Roulette Color Prediction
**Problem:** Given a two-digit number. Determine which of its digits is larger: 
- the first (output `1`) 
- or the second (output `2`), 
- or the digits are equal (output `=`).
- If the number is less than `10` or greater than `99`, output `0`.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 23     | 2       |
| 2   | 37     | 2       |
| 3   | 22     | =       |
| 4   | 10     | 1       |
| 5   | -1    | 0       |

## Example 14: Overtime Pay Calculation
**Problem:** Several workers work at the car repair station. If any worker works more than `40` hours a week, he receives `1.5` times more than the usual hourly pay. Develop a program that calculates the employee's salary, including payment for extra hours. The program receives two integers - the number of working hours and the hourly rate.

| No. | Inputs | Outputs     |
| --- | ------ | ----------- |
| 1   | 45     | 712.5       |
| 2   | 35     | 560.0       |
| 3   | 50     | 875.0       |

## Example 15: Circle Belonging Determination
**Problem:** The coordinates `(x, y)` of point `A` and the radius of the circle `(r)` are entered. Determine whether the given point belongs to the circle if its center is at the origin.

| No. | Inputs | Outputs                         |
| --- | ------ | ------------------------------- |
| 1   | 3<br>4   | The point belongs to the circle |
| 2   | -2<br>5  | The point is outside the circle |

## Example 16: Coordinate Quarter Determination
**Problem:** Determine the quarter of the coordinate plane a point belongs to.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 2<br>-4  | IV      |
| 2   | -4<br>3  | II      |
| 3   | 0<br>0   | The point is at the origin |

## Example 17: Body Mass Index and Categorization
**Problem:** Write a program to calculate the body mass index, which is calculated by the formula: `index = mass / (height * height)`. The user enters the values of height (in meters) and mass (in kilograms), and the program calculates the body mass index and outputs the corresponding message: 
- `underweight` (low mass, index less than `18.5`), 
- `normal weight` (normal mass, index `18.5-24.9`), 
- `overweight` (excessive mass, index more than `24.9`).

| No. | Inputs      | Outputs                                       |
| --- | ----------- | --------------------------------------------- |
| 1   | 1.79<br>88    | Your body mass index is: 27.46, that is overweight. |
| 2   | 1.90<br>85    | Your body mass index is: 23.55, that is normal weight. |
| 3   | 1.60<br>50    | Your body mass index is: 19.53, that is normal weight. |

## Example 18: Chessboard Cell Color Matching
**Problem:** Two cells of a chessboard are given. If they are painted in one color, then print the word `Yes`, and if in different colors - `No`. The program receives four numbers from `1` to `8` each, which set the column number and the row number first for the first cell, then for the second cell.

| No. | Inputs    | Outputs |
| --- | --------- | ------- |
| 1   | 1<br>1<br>2<br>2 | No  |
| 2   | 1<br>1<br>1<br>2 | Yes |
| 3   | 1<br>1<br>2<br>1 | Yes |

## Example 19: Triangle Type Determination
**Problem:** Given three sides of a triangle `a`, `b`, `c`. Determine the type of triangle with the given sides. Print one of four words: 
- `rectangular` for a right triangle, 
- `acute` for an acute triangle, 
- `obtuse` for an obtuse triangle, 
- or `impossible` if there is no triangle with such sides.Determine the type of a triangle based on its angles.

| No. | Inputs | Outputs   |
| --- | ------ | --------- |
| 1   | 3<br>4<br>5 | rectangular |
| 2   | 3<br>4<br>6 | obtuse      |
| 3   | 3<br>4<br>7 | impossible  |
| 4   | 3<br>4<br>4 | acute       |

## Example 20: Identical Digits Counting
**Problem:** Given a three-digit integer. Determine the number of identical digits in the number record and output the value of this quantity.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 123    | 0       |
| 2   | 111    | 3       |
| 3   | 121    | 2       |
| 4   | 100    | 1       |

## Example 21: Next Day Date Validation
**Problem:** Write a program in which the user enters the value of the current date: day, month, and year (integer numbers), and the program outputs tomorrow's date in the format: `dd.mm.yyyy`.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 1<br>1<br>2020 | 02.01.2020 |
| 2   | 28<br>2<br>2020 | 29.02.2020 |
| 3   | 31<br>12<br>2020 | 01.01.2021 |


**Notes:** All the examples above are solved using Python. You can find the solutions in the [examples](./examples) folder. Covered with explanations and comments, these examples will help you understand the practical implementation of the concepts covered in this module. Python tests are also included to verify the correctness of the solutions.