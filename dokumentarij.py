# Dokumentarij je aplikacija za ispis i unos novih studenata 
# na kolegiju Razvoj poslovnih aplikacija
# za brisanje: https://note.nkmk.me/en/python-list-clear-pop-remove-del/
class DokumentarijModel:
    def __init__(self):
        self.names = [] 

        @property
        def names(self):
            return self._names 

        @names.setter
        def names(self, new_name):
            self._names = new_name 



class DokumentarijView:
    def display_title_bar(self):    
        print("\t****************************************************")
        print("\t***  Dokumentarij - Razvoj poslovnih aplikacija  ***")
        print("\t****************************************************")
        
    def get_user_choice(self):
        print("\n[1] Pogledaj listu studenata.")
        print("[2] Dodaj novog studenta.")
        print("[x] Izlaz.")
        return input("Što želite napraviti u dokumentariju?")
    def get_new_name(self):
        new_name = input("\nUnesite ime studenta: ")
        return new_name 
    def show_names(self,name):
        print(name.title())

class DokumentarijControler:   
    def __init__(self, model, view):
        self.model = model
        self.view = view
    def get_names(self):
        print("\nOvo je popis studenata na kolegiju Razvoj poslovnih aplikacija 2019/2020:\n")
        for name in self.model.names:
            print(self.view.show_names(name))
    def input_new_name(self):
        new_name = self.view.get_new_name()
        if new_name in self.model.names:
            print("{} je već upisan/a u dokumentariju!".format(new_name.title()))
        else:
            self.model.names.append(new_name)
            print("Dobrodošao/la {}!\n".format(new_name.title()))
    ### MAIN PROGRAM ###
    # Set up a loop where users can choose what they'd like to do.
    def play(self):
        choice = ''
        self.view.display_title_bar()
        while choice != 'x':    
            choice = self.view.get_user_choice()
            # Respond to the user's choice.
            self.view.display_title_bar()
            if choice == '1':
                self.get_names()
            elif choice == '2':
                self.input_new_name()
            elif choice == 'x':
                print("\nHvala na pregledu/uređivanju dokumentarija. Pozdrav.")
            else:
                print("\nGreška - napravite hvatanje izuzetaka sami za vježbu.\n")
                
if __name__ == "__main__":
    game = DokumentarijControler(DokumentarijModel(), DokumentarijView())
    game.play()