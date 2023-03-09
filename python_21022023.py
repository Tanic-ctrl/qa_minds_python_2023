# Para abordar vuelo a destino internacional se necesita:
# Boletos de avion
# Pasaporte
# COVID (una de estas dos opciones):
# VACCINE_BOOSTER_COVID
# PRC_TEST

plane_ticket = True
passport = True
vaccine_booster_covid = False
pcr_test = True

if plane_ticket and passport and (vaccine_booster_covid or pcr_test):
    print("Board plane")
else:
    print("Don't board plane")
