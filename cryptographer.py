# Окно с кнопкой

from tkinter import *



# Шифровка введенного текста
text = input ('Enter ur text: ')
keys = { 'A':'$', 'B':'@', 'C':'*',
         'a':'^', 'b':'2', 'c':'№',
         'D':'%', 'E':'j', 'F':'&',
         'd':'#', 'e':'!', 'f':'4',
         'G':'в', 'H':'/', 'I':'q',
         'g':'w', 'h':'-', 'i':'+',
         'J':'?', 'K':'|', 'L':'Щ',
         'j':'m', 'k':'o', 'l':'l',
         'M':'й', 'N':':', 'O':'r',
         'm':'р', 'n':'d', 'o':'s',
         'P':'8', 'Q':']', 'R':'3',
         'p':'_', 'q':'=', 'r':'z',
         'S':'x', 'T':'ц', 'U':'ж',
         's':'м', 't':'ю', 'u':'7',
         'V':'с', 'W':'ф', 'X':'5',
         'v':'g', 'w':'.', 'x':';',
         'Y':'<', 'Z':',',
         'y':'>', 'z':'}',' ':'ь'  }
crypt = ""
for i in text:
    if i in keys:
        crypt+=keys[i]
print ("crypted: "+crypt)
keys.clear()


# Расшифровка зашифрованного текста
password = False
pas = input ("Password: ")
if pas == "010101":
    password = True
    def click_button():
            global crypt
            unkeys = {
         '$':'A', '@':'B', '*':'C',
         '^':'a', '2':'b', '№':'c',
         '%':'D', 'j':'E', '&':'F',
         '#':'d', '!':'e', '4':'f',
         'в':'G', '/':'H', 'q':'I',
         'w':'g', '-':'h', '+':'i',
         '?':'J', '|':'K', 'Щ':'L',
         'm':'j', 'o':'k', 'l':'l',
         'й':'M', ':':'N', 'r':'O',
         'р':'m', 'd':'n', 's':'o',
         '8':'P', ']':'Q', '3':'R',
         '_':'p', '=':'q', 'z':'r',
         'x':'S', 'ц':'T', 'ж':'U',
         'м':'s', 'ю':'t', '7':'u',
         'с':'V', 'ф':'W', '5':'X',
         'g':'v', '.':'w', ';':'x',
         '<':'Y', ',':'Z', '>':'y',
         '}':'z', 'ь':' '}
            decrypt = ''
            for i in crypt:
                if i in unkeys:
                    decrypt += unkeys [i]
                    print ('-----------------------------------------------------------------')
                    print ("Decrypted text: "+decrypt)


root = Tk()
root.title("GUI на Python")
root.geometry("50x50")
btn = Button(text="Decrypt", background="#444", foreground="#0f3", padx="15", pady="8", font="12", command=click_button)
btn.pack()
canvas = Canvas (root, bg = '#444')
root.mainloop()

'''
if date == "010101":
    txt = crypt
    print (txt)
    unkeys = {
         '$':'A', '@':'B', '*':'C',
         '^':'a', '2':'b', '№':'c',
         '%':'D', 'j':'E', '&':'F',
         '#':'d', '!':'e', '4':'f',
         'в':'G', '/':'H', 'q':'I',
         'w':'g', '-':'h', '+':'i',
         '?':'J', '|':'K', 'Щ':'L',
         'm':'j', 'o':'k', 'l':'l',
         'й':'M', ':':'N', 'r':'O',
         'р':'m', 'd':'n', 's':'o',
         '8':'P', ']':'Q', '3':'R',
         '_':'p', '=':'q', 'z':'r',
         'x':'S', 'ц':'T', 'ж':'U',
         'м':'s', 'ю':'t', '7':'u',
         'с':'V', 'ф':'W', '5':'X',
         'g':'v', '.':'w', ';':'x',
         '<':'Y', ',':'Z', '>':'y',
         '}':'z'}
    decrypt = ''
    for i in txt:
        if i in unkeys:
            decrypt += unkeys [i]
print ("Decrypt:\n"+decrypt+"\n")

'''
