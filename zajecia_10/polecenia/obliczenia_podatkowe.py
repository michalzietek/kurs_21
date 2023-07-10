def oblicz_moj_podatek(kwota):
    if kwota < 32000:
        return 0
    if 120000 > kwota > 32000:
        return (kwota-32000) * 0.12
    else:
        return (kwota-32000) * 0.12 + (kwota-120000) * 0.32


def oblicz_moj_vat(kwota_netto, podatek_vat):
    return kwota_netto * podatek_vat

def znajdz_kwote_brutto(kwota_netto, podatek_vat):
    return kwota_netto + (1+podatek_vat)