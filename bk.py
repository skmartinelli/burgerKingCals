# data from https://burger-king-menu.net/burger-king-nutrition#:~:text=%20%20%20%20%20%20%20,%20%20161%20%202%20more%20rows%20
# - if not present above then found in app (ie impossible whopper)
# - im not counting drinks bc the only soda i drink is diet coke.
# - all burgers are assumed with cheese if available.


largeFries = 386
largeOnionRings = 450
whopper = 703
chickenSandwich = 344
EightPcNuggets = 343
doubleWhopper = 941
smallFries = 219
impossibleWhopper = 652
baconKing = 1051
whopperJr = 353
NinePcChickenFries = 326
doubleCheeseburger = 416
mediumFries = 282
originalChickenSandwich = 684
cheeseburger = 282

offersCalsPrice = {}

offersCalsPrice["$1.49 Large Fries"] = [largeFries, 1.49]
offersCalsPrice["$1.49 Large Onion Rings"] = [largeOnionRings, 1.49]
offersCalsPrice["$22 Ultimate Bundle"] = [
    2 * whopper + 2 * chickenSandwich + 2 * EightPcNuggets, 22]
offersCalsPrice["$7 Double Whopper and Small Fries"] = [
    doubleWhopper + smallFries, 7]
offersCalsPrice["$7 Small Whopper Meal"] = [whopper + smallFries, 7]
offersCalsPrice["$8 Small Impossible Whopper Meal"] = [
    impossibleWhopper + smallFries, 8]
offersCalsPrice["$10 Medium Bacon King Meal"] = [baconKing + mediumFries, 10]
offersCalsPrice["$11.99 Small Whopper Meal for Two"] = [
    2 * whopper + 2 * smallFries,11.99]
offersCalsPrice["$6.99 Two Whopper Jr. Sandwiches and Two Small Fries"] = [2* whopperJr + 2*smallFries, 6.99]
offersCalsPrice["$7.99 Two Original Chicken Sandwiches and Two Small Fries"] = [2*originalChickenSandwich + 2*smallFries, 7.99]
offersCalsPrice["$4.49 Large Fries and  9 Pc Chicken Fries / 8 Pc Nuggets"] = [EightPcNuggets + largeFries,4.49]
offersCalsPrice["Bogo Whopper"] = [2*whopper, 7.29]
offersCalsPrice["$3 Whopper Wednesday (Wednesdays only)"] = [whopper, 3]
offersCalsPrice["$5.50 Double Cheeseburger, Small Fries, Small Soft Drink"] = [doubleCheeseburger + smallFries, 5.50]
offersCalsPrice["$6.99 Snack box"] = [cheeseburger + EightPcNuggets + smallFries, 6.99]


for item in offersCalsPrice:
    padding = len(item)
    currentCalsAndPrice = offersCalsPrice[item]
    cals = currentCalsAndPrice[0]
    price = currentCalsAndPrice[1]
    #print(item[0])
    print(item, " "* (60-padding), "cals:", cals ,"      price: $", price, "  cals per dollar: ", int(cals/price) )




#print(offersCalsPrice)
