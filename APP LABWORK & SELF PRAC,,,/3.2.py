for i in range(5):
    a=int(input("enter first number :"))
    b=int(input("enter secont number:"))
    c=int(input("enter third number :"))
    if a==b:
        print("a and b are equal")
        if c>a :
            print("a and b are smallest")
        else:
            print("c is smallest")    
    elif a==c:
        print("a and c are equal")
        if b>a :
            print("a and c is smallest")
        else:
            print("b is smallest")    
    elif b==c:
        print("c and b are equal")
        if a>b :
            print("c and b are smallest")
        else:
            print("a is smallest")    
    elif a<b:
        if a<c:
            print("a is smallest")
        else:
            print("c is smallest")
    elif b<a:
        if b<c:
            print("b is smallest")
        else:
            print("c is smallest")
    elif a<c:
        if a<b:
            print("a is smallest")
        else:
            print("b is smallest")  
    else:
        print("all are equal") 


##########################################################

for i in range(5):
    a=int(input("enter first number :"))
    b=int(input("enter secont number:"))
    c=int(input("enter third number :"))
    if a==b:
        print("a and b are equal")
        if c>a :
            print("c is greatest")
    elif a==c:                          
        print("a and c are equal")
        if b>a :
            print("c is greatest")
    elif b==c:
        print("c and b are equal")
        if a>b :
            print("c is greatest")
    elif a>b:
        if a>c:
            print("a is greatest")
        else:
            print("c is greatest")
    elif b>a:
        if b>c:
            print("b is greatest")
        else:
            print("c is greatest")
    elif a>c:
        if a>b:
            print("a is greatest")
        else:
            print("b is greatest")  
    else:
        print("all are equal")                  

#####################################################



num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

match operator:
    case "+":
        print("Result:", num1 + num2)
    case "-":
        print("Result:", num1 - num2)
    case "*":
        print("Result:", num1 * num2)
    case "/":
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Error: Division by zero")
    case _:
        print("Error: Invalid operator")

######################################################
order=int(input("enter what do you want to oder 1.sandwhich 2.pizza 3.burger  :"))
match order:
    case 1:
        a=int(input("which sandwhich do you want to order 1.grilled 2.potato 3.dry "))
        match a:
            case 1:
                print("ordered grilled sandwhich")
            case 2:
                print("ordered potato sandwhich")
            case 3:
                print("ordered dry sandwhich")    
    case 2:
        b=int(input("which pizza do you want to order 1.crust 2.brust 3.dough "))
        match b:
            case 1:
                print("ordered crust pizza")
            case 2:
                print("ordered brust pizza")
            case 3:
                print("ordered dough pizza")
    case 3:
        c=int(input("which burger do you want to order 1.cheese 2.extra garlic 3.restro special ")) 
        match c:
            case 1:
                print("ordered cheese burger")
            case 2:
                print("ordered extra garlic burger")
            case 3:
                print("ordered restro special burger")    
    case _:
        print("invalid order")        

################################################################

def telecom_system():
    print("--- Telecom Calling System ---")
    print("1. English")
    print("2. Hindi")
    print("3. Gujarati")
    
    choice = input("Please select your language (1/2/3): ")

    match choice:
        case '1':
            print("\nYou selected English.")
            print("1. Account Balance")
            print("2. Talk to Customer Care")
            sub_choice = input("Select an option (1/2): ")
            
            match sub_choice:
                case '1': print("Your balance is $50.00.")
                case '2': print("Connecting you to English support...")
                case _: print("Invalid selection.")

        case '2':
            print("\nआपने हिंदी चुनी है।")
            print("1. खाता शेष")
            print("2. ग्राहक सेवा से बात करें")
            sub_choice = input("विकल्प चुनें (1/2): ")
            
            match sub_choice:
                case '1': print("आपका बैलेंस 50 रुपये है।")
                case '2': print("हिंदी सहायता से जोड़ा जा रहा है...")
                case _: print("अमान्य चयन।")

        case '3':
            print("\nતમે ગુજરાતી પસંદ કર્યું છે.")
            print("1. એકાઉન્ટ બેલેન્સ")
            print("2. કસ્ટમર કેર સાથે વાત કરો")
            sub_choice = input("વિકલ્પ પસંદ કરો (1/2): ")
            
            match sub_choice:
                case '1': print("તમારું બેલેન્સ 50 રૂપિયા છે.")
                case '2': print("ગુજરાતી સપોર્ટ સાથે જોડી રહ્યા છીએ...")
                case _: print("અમાન્ય પસંદગી.")

        case _:
            print("\nInvalid language selection.")
telecom_system()