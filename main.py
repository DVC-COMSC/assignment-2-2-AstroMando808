def main():
    """
    ##################################################
    # Comlete your code here
    Use the same variables: celcius fahrenheit 
    ##################################################
    """
    temp = int(input("Please enter the celcius temperature to convert to fahrenheit: "))

    temp = round((9 * temp) / 5 + 32, 1)

    print("The temperature in Fahrenheit is: ",  (temp))
    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return celcius, fahrenheit


if __name__ == '__main__':
    main()
