"""
We know that a person allergic to eggs can not eat a recipe that has egg. In the same way when we saw the ingredients of a recipe we look for
the words related to our allergy, but what happens when you search for "egg" and find "eggplant", there are terms that aren't related to an 
allergy, but can be confused. In this script we create a dataset that for each allergy search items that are related to that allergy and items
that aren't related but can confuse the computer for their similarity in words.
"""

import pandas as pd

def string_terms_to_reduced_list(string):
    terms = []
    for element in string.lower().split(", "):
        add = True
        remove = []
        for term in terms:
            if term in element:
                add=False #We don't add this element
                break
            elif element in term:
                remove.append(term)
        if add:
            terms.append(element)
        for r in remove:
            terms.remove(r)
    return terms

data = pd.DataFrame(columns=["Allergy","trueAllergy","falseAllergy"])

def addData(name,trueAllergy,falseAllergy):
    trueAllergy = string_terms_to_reduced_list(trueAllergy)
    falseAllergy = string_terms_to_reduced_list(falseAllergy)
    data.loc[data.shape[0]]=[name,trueAllergy,falseAllergy]


dairy = 'milk, cream, butter, cheese, yogurt, sour cream, evaporated milk, condensed milk, ricotta cheese, cottage cheese, cream cheese, ice cream, whipped cream, half-and-half, ghee, milk powder, whey, casein, curds, milk solids, buttermilk, milk chocolate, crème fraîche, mascarpone, kefir, custard, béchamel sauce, ranch dressing, Alfredo sauce, buttercream frosting'
nodairy = "almond milk, soy milk, coconut milk, rice milk, oat milk, cashew milk, hemp milk, lactose-free milk, lactose-free yogurt, lactose-free cheese, vegan cheese, nondairy creamers, silken tofu, coconut cream, nut-based cream"
addData("Dairy",dairy,nodairy)

gluten = "wheat, barley, rye, spelt, durum wheat, semolina, farro, bulgur, couscous, kamut, einkorn, wheat bran, wheat germ, graham flour, malt, malt extract, malt syrup, malt vinegar, brewer's yeast, triticale, seitan, wheat starch, matzo, panko breadcrumbs, bread, pasta, flour tortillas, cakes, cookies, crackers, beer, soy sauce, gravies, soups, cereals, pizza dough"
nogluten = "gluten-free, gluten-free bread, gluten-free pasta, gluten-free soy sauce, gluten-free beer, gluten-free pizza dough, gluten-free flour, gluten-free crackers, gluten-free cakes, gluten-free cookies, gluten-free cereals, gluten-free breadcrumbs, gluten-free malt extract, rice couscous, corn couscous, gluten-free graham crackers, gluten-free soups, gluten-free gravies"
addData("Gluten",gluten,nogluten)

egg = "egg, egg yolk, egg white, whole egg, powdered egg, egg wash, liquid egg, dried egg, egg substitute (may contain egg), albumin, meringue powder, egg protein"
noegg = "eggplant, eggless mayonnaise, eggless pasta, eggless cake mix, egg-free egg substitute, egg-free"
addData("Egg",egg,noegg)

fish = "fish, cod, haddock, salmon, tuna, sardines, mackerel, herring, trout, bass, sole, flounder, grouper, snapper, tilapia, swordfish, halibut, eel, fish sauce, fish stock, anchovy, anchovy paste, shark, pollock, bonito flakes, caviar, roe, surimi"
nofish = "crayfish, shellfish, starfish, jellyfish, cuttlefish, fish pepper"
addData("Fish",fish,nofish)

shellfish = "shrimp, prawns, lobster, crab, crayfish, krill, langoustine, mantis shrimp, barnacles"
noshellfish=""
addData("Shellfish",shellfish,noshellfish)

treenut = "almonds, walnuts, cashews, hazelnuts, pecans, pistachios, macadamia nuts, brazil nuts, pine nuts, chestnuts, marzipan, nut butter, almond butter, cashew butter, walnut butter, hazelnut butter, pecan butter, pistachio butter, macadamia nut butter, brazil nut butter, pine nut butter, chestnut butter, nut oils, walnut oil, almond oil, cashew oil, hazelnut oil, pecan oil, pistachio oil, macadamia nut oil, brazil nut oil, pine nut oil, chestnut oil, praline, nut pastes"
notreenut = "nutmeg, water chestnuts, shea nut butter, butternut squash, coconut, nut grass"
addData("Treenut",treenut,notreenut)

peanut = "peanut, peanut butter, peanut oil, peanut flour, peanut protein, roasted peanuts, ground peanuts, peanut paste"
nopeanut = "peanut butter fruit, groundnut, peanut pumpkin"
addData("Peanut", peanut, nopeanut)

soy = "soy, soybeans, soy protein, soy milk, soy flour, soy sauce, tofu, tempeh, edamame, miso, natto, soy lecithin, soy oil, soy protein isolate, soy protein concentrate, textured soy protein, hydrolyzed soy protein, soy nuts"
nosoy = "gluten-free, soya wax, soy candles"
addData("Soy", soy, nosoy)

sesame = "sesame seeds, sesame oil, sesame paste, tahini, toasted sesame seeds, black sesame seeds, white sesame seeds, sesame flour, sesame butter"
nosesame = "sesame grass"
addData("Sesame", sesame, nosesame)

mustard = "mustard"
nomustard = ""
nomustard = addData("Mustard", mustard, nomustard)

data.to_csv("../datasets/Allergies.csv")
