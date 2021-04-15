def verif_num(var):
    for i in var:
        if i < "0" or i > "9":
            print("entree invalide, non numerique !")
            return False
    return True

# test de la fonction
if __name__ == "__main__":
    ret=verif_num("123456")
    print ("ret: ", ret)
