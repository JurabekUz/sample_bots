"""
 Bu wikipedia moduli test qilindi
 Izlash va malumot topish funksiyalari ishlashi tekshirildi
"""
import wikipedia

wikipedia.set_lang('uz') #Til o'zbek tiliga o'zgartirildi

# izlash funksiyasi test qilinishi
izlash=wikipedia.search('xorazm')

natijalar=list(izlash)
print(natijalar)

# malumot topish funksiyasining testi

malumot=wikipedia.summary('xorazm')

print(malumot)
