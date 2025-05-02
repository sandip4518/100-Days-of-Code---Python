# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
import art

print(art.logo)
blind_auction={}

stopAuction=False
while not stopAuction:
    name = input("Enter Your Name : ").lower()
    bid = int(input("Enter Your Bid: $"))
    blind_auction[name] = bid
    OtherBidders=input("\nAre there any other bidders? Type 'yes or 'no': ").lower()

    if OtherBidders=="yes":
      continue
    else:
        highbidder=max(blind_auction,key=blind_auction.get)
        maxbid=blind_auction[highbidder]
        print(f"\nThe winner is {highbidder} with a bid of ${maxbid}.")
        stopAuction=True


