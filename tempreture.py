def main():
    while True:
        temp_type = input("wich tempeture type you want to convert(fahreneit, celcius or kelvin):  ").lower()
        if temp_type == "kelvin":
            break
        elif temp_type == "celcius":
            break
        elif temp_type == "fahreneit":
            break
    while True:
        conv_type = input("wich tempreture type you want to convert to(fahreneit, celcius or kelvin):  ").lower()
        if conv_type == "kelvin":
            break
        elif conv_type == "celcius":
            break
        elif conv_type == "fahreneit":
            break
    while True:
        try:
            temp = float(input("enter the tempreture:  "))
            if int(temp) == temp:
                temp = int(temp)
            else:
                pass
            if temp_type == "kelvin" and temp < 0:
                print("It is not a valid tempreture")
                continue
            elif temp_type == "celcius" and temp < -273:
                print("It is not a valid tempreture")
                continue
            elif temp_type == "fahreneit" and temp < -459.4:
                print("It is not a valid tempreture")
                continue
            break
        except ValueError:
            pass

    def translation_c_to_f(celcius):
        fahreneit = (celcius*18 + 320) / 10
        if int(fahreneit) == fahreneit:
            fahreneit = int(fahreneit)
        print(f"{celcius} Celcius correspond to {fahreneit} Fahreneit.")

    def translation_f_to_c(fahreneit):
        celcius = ((fahreneit - 32) * 10) / 18
        if int(celcius) == celcius:
            celcius = int(celcius)
        print(f"{fahreneit} Fahreneit correspond to {celcius} Celcius.")

    def translation_c_to_k(celcius):
        kelvin = celcius + 273
        if int(kelvin) == kelvin:
            kelvin = int(kelvin)
        print(f"{celcius} Celcius correspond to {kelvin} Kelvin.")

    def translation_k_to_c(kelvin):
        celcius = kelvin - 273
        if int(celcius) == celcius:
            celcius = int(celcius)
        print(f"{kelvin} Kelvin correspond to {celcius} Celcius.")

    def translation_k_to_f(kelvin):
        fahreneit = ((kelvin - 273) * 18) / 10
        if int(fahreneit) == fahreneit:
            fahreneit = int(fahreneit)
        print(f"{kelvin} Kelvin correspond to {fahreneit} Fahreneit.")

    def translation_f_to_k(fahreneit):
        kelvin = (((fahreneit-32)*10) / 18) + 273
        if int(kelvin) == kelvin:
            kelvin = int(kelvin)
        print(f"{fahreneit} Fahreneit correspond to {kelvin} Kelvin.")

    if temp_type == "fahreneit":
        if conv_type == "celcius":
            translation_f_to_c(temp)
        elif conv_type == "kelvin":
            translation_f_to_k(temp)
        else:
            pass

    if temp_type == "celcius":
        if conv_type == "fahreneit":
            translation_c_to_f(temp)
        elif conv_type == "kelvin":
            translation_c_to_k(temp)
        else:
            pass

    if temp_type == "kelvin":
        if conv_type == "fahreneit":
            translation_k_to_f(temp)
        elif conv_type == "celcius":
            translation_k_to_c(temp) 
        else:
            pass


main()
