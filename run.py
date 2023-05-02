from eBay.eBay import ebay



with ebay() as bot:
    bot.load_first_page()
    bot.autologin_first_page()
    bot.go_to_ad_setings()
    bot.ad_all_informations_()