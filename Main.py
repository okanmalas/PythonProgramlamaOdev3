kucuk_alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"
buyuk_alfabe = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"
alfabe_uzunlugu = 29

class String:
    @staticmethod
    def getText():
        print("Lütfen Mesajı Giriniz -> ")
        text = input()
        if text.replace(" ", "").isalpha(): #bu satırı yapay zeka yazdı
            return text
        else:
            print("Sadece metin giriniz")
            return String.getText()
    @staticmethod
    def reverseText(text):
        return text[::-1] #bu satırı yapay zeka yazdı

class Sezar:
    @staticmethod
    def encode(text,count):
        result = ""
        for key in text:
            if key in kucuk_alfabe:
                currentIndex = kucuk_alfabe.index(key)
                result += kucuk_alfabe[(currentIndex + count) % alfabe_uzunlugu]
            elif key in buyuk_alfabe:
                currentIndex = buyuk_alfabe.index(key)
                result += buyuk_alfabe[(currentIndex + count) % alfabe_uzunlugu]
            else:
                result += key
        return result

class Resolver:
    @staticmethod
    def decode(text):
        print("Ele Geçirilen Metin -> " + text)
        print(" ")
        print("      Ters Metin         Düz Metin")
        print("-----------------------------------------")
        for keyCount in range(alfabe_uzunlugu):
            result = ""
            for key in text:
                if key in kucuk_alfabe:
                    currentIndex = kucuk_alfabe.index(key)
                    result += kucuk_alfabe[(currentIndex - keyCount) % alfabe_uzunlugu]
                elif key in buyuk_alfabe:
                    currentIndex = buyuk_alfabe.index(key)
                    result += buyuk_alfabe[(currentIndex - keyCount) % alfabe_uzunlugu]
                else:
                    result += key
            print (f"Key " + str(keyCount) + " -> " + result + "  --  " + String.reverseText(result))

def run():
    text = String.getText()
    print("Öteleme miktarını giriniz -> ")
    count = int(input())
    print("---------------------------------------------")
    print("Girilen Metin -> " + text)
    text = String.reverseText(text)
    print("Ters Çevirilmiş Metin -> " + text)
    text = Sezar.encode(text, count)
    print("Şifrelenmiş Metin -> " + text)
    print("----------------------------------------------")
    Resolver.decode(text)

if __name__ == "__main__":
    run()