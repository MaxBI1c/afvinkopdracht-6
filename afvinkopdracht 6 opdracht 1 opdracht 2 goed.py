def main():
    i = 1
    l =[]
    for i in range(0,20):
        x = float(input('Voer een getal in'))
        i = i + 1
        l.append(x)
        laagste_score = min(l)
        hoogste_score = max(l)
        totaal_score = sum(l)           
        gemiddelde_score = totaal_score / len(l)
        y = print( laagste_score ,hoogste_score, totaal_score, gemiddelde_score )
main()