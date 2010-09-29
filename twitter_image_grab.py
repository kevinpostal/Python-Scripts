import twitter
import sys
import time

twitter_list = [
"whiterabbittruk",
"greatballsot",
"tropshaveice",
"nomnomtruck",
"sprinklesmobile",
"kogibbq",
"grlldcheesetruk",
"COOLHAUS",
"Green_Truck",
"donchowtacos",
"CalbiBBQ",
"TheBurgerBus",
"mattieskitchen",
"CartForACause",
"labbqguy",
"weliketospoon",
"Fressers",
"unclelaubbq",
"bullkogi",
"SKEWERSONWHEELS",
"Qzillabbq",
"TapaBoyLA",
"PaniniOnWheels",
"GrillMastersLA",
"pupusamobile",
"tacos_sinaloa",
"lagueratamalera",
"GermanFoodTruck",
"TheSweetsTruck",
"BorderGrill",
"Frysmith",
"GrillEmAllTruck",
"ButtermilkTruck",
"SliceTruck",
"FlyingPigTruck",
"IndiaJonesCT",
"worldfare",
"BabysBBs",
"fishlips_sushi",
"southphillyexp",
"dosatruck",
"komodofood",
"lomoarigato",
"Marked5",
"manilamachine",
"BarbiesQ",
"CrepesBonaparte",
"letsbefrank",
"CantersTruck",
"thegastrobus",
"MandolineGrill",
"LouksToGo",
"BoolBBQ",
"umamiburger",
"DumplingStation",
"ItsBentoBaby",
"KingKoneLA",
"TheFrankenStand",
"VesuvioLA",
"LA_FuXion",

]

def grabTwitterImg():
    api = twitter.Api()

    for account in twitter_list:

        twitter_url = "http://twitter.com/%s" % (account)
        name = api.GetUser(account).name
        url = api.GetUser(account).url
        try:
            img = api.GetUser(account).profile_image_url
        except:
            pass
        try:
            description = api.GetUser(account).description.encode("utf-8")
        except:
            pass #POS encoding
        print twitter_url
        print "-----"
        print "name: %s" % ( name)
        print "url: %s" % ( url)
        print "img: <img src='%s'>" % ( img)
        print "description: %s" % ( description)
        print "<br /> <br />"
        #time.sleep(0.3)

def main(argv=sys.argv):
    grabTwitterImg()
    
    
if __name__ == "__main__":
    main()
