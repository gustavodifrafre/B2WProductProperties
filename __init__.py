from b2w import B2W


codes = B2W.Get_Prod_Codes_By_Cat("https://www.americanas.com.br/categoria/tv-e-home-theater/tv", 10)
prods = B2W.Get_Properties_By_Cods(codes)
print(prods)
