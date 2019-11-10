content = "honesty integrity boldness trust trust trust trust trust moral moral moral"

company_values = ["integrity", "boldness","honesty","trust"]
integrity_words = "honesty integrity".split()
boldness_words = "challenge encourage feedback openness".split()
honesty_words = "truth moral ethical".split()
trust_words = "confidence trusted trust".split()
counter = [0]*len(company_values)

for word in content.split():
    if word in integrity_words:
        counter[0] += 1
    elif word in boldness_words:
        counter[1] += 1
    elif word in honesty_words:
        counter[2] += 1
    elif word in trust_words:
        counter[3] += 1
x = counter.copy()
x.sort(reverse=True)
ranking1 = company_values[counter.index(x[0])]
ranking2 = company_values[counter.index(x[1])]
ranking3 = company_values[counter.index(x[2])]

print("Top Three Values:")
print(ranking1)
print(ranking2)
print(ranking3)
