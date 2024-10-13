from translate import Translator # type: ignore
translator_de = Translator(to_lang="es")
greet = translator_de.translate("hello, I <3 u")
print(greet)
