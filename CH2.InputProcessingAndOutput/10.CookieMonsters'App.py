sugarPerCookie = 1.5/48
butterPerCokie = 1/48
flourPerCookie = 2.75/48

cookieCount=int (input("How many cookies does the monster require "))

sugarForThisBatch = sugarPerCookie*cookieCount
butterForThisBatch = butterPerCokie*cookieCount
flourForThisBatch = flourPerCookie*cookieCount

print("You will need: \n",
      format(sugarForThisBatch,".2f"),"cups of sugar\n",
      format(butterForThisBatch,".2f"),"cups of butter\n",
      "Aaaand",format(flourForThisBatch,".2f"),"cups of flour\n",
      "Now go make those cookies the monster is waiting!!!")