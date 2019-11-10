content = #insert string datatype


company_values = ["integrity", "Boldness","Honesty", "Trust", "Accountability","Passion", "Fun", "Humility", "Learning", "Ownership","Growth","Leadership","Diversity", "Innovation", "Teamwork"]
integrity_words = "integrity high-mindedness honor incorruptibility irreproachability right-mindedness scrupulosity scrupulousness appropriateness correctness decorousness decorum etiquette fitness ethics morals character decency goodness honesty morality probity rectitude righteousness rightness uprightness virtue virtuousness ".split()
boldness_words = "boldness adventuresome adventurous audacious daring dashing emboldened enterprising free-swinging wild brave courageous dauntless fearless gallant greathearted heroic intrepid lionhearted stalwart stout stouthearted swashbuckling unafraid undaunted valiant valorous".split()
honesty_words = "honesty probity truthfulness veracity verity honor honorableness incorruptibility rectitude righteousness right-mindedness scrupulosity scrupulousness uprightness artlessness candidness candor good faith sincerity  dependability reliability trustability trustiness trustworthiness accuracy authenticity correctness genuineness truth credibility".split()
trust_words = "trust confidence credence faith stock acceptance assurance assuredness certainty certitude conviction positiveness sureness surety credit dependence hope reliance".split()
acc_words = "accountability answerability liability responsibility reliable".split()
passion_words = "passion affection attachment devotedness devotion love ardor eagerness enthusiasm fervor zeal appreciation esteem estimation regard respect adoration adulation deification idolatry idolization worship allegiance faithfulness fealty fidelity loyalty steadfastness".split()
fun_words = "fun joke jolly josh kid quip wisecrack yuk jeer mock caricature lampoon parody amuse divert entertain".split()
humility_words = "Humility demureness down-to-earthness humbleness lowliness meekness modesty acquiescence compliance deference directness".split()
learning_words = "learning education erudition knowledge learnedness literacy scholarship culture edification enlightenment reading bookishness pedantry".split()
ownership_words = "ownership control enjoyment hands keeping possession authority command dominion mastery power".split()
growth_words = "growth development elaboration evolution expansion progress progression advancement betterment improvement perfection refinement enhancement evolvement".split()
leadership_words = "leadership mentor mentorship direction generalship governance lead management guidance".split()
diversity_words = "diversity inclusivity access inclusive diverse".split()
innovation_words = "innovation picture vision conception imagining origination creative".split()
teamwork_words = "teamwork collaboration cooperation coordination community mutualism reciprocity solidarity".split()

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
    elif word in acc_words:
        counter[4] += 1
    elif word in passion_words:
        counter[5] += 1
    elif word in fun_words:
        counter[6] += 1
    elif word in humility_words:
        counter[7] += 1
    elif word in learning_words:
        counter[8] += 1
    elif word in ownership_words:
        counter[9] += 1
    elif word in growth_words:
        counter[10] += 1
    elif word in leadership_words:
        counter[11] += 1
    elif word in diversity_words:
        counter[12] += 1
    elif word in innovation_words:
        counter[13] += 1
    elif word in teamwork_words:
        counter[14 +=1]

x = counter.copy()
x.sort(reverse=True)
ranking1 = company_values[counter.index(x[0])]
ranking2 = company_values[counter.index(x[1])]
ranking3 = company_values[counter.index(x[2])]

print("Top Three Values:")
print(ranking1)
print(ranking2)
print(ranking3)
