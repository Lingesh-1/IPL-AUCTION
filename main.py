#IPL Auction Program
import random as r
def auction(n,bid):
    for i in range(len(aucbid)):
        if aucbid[i]['bid']>bid:
            bid=aucbid[i]['bid']

    aucbi={'name':n,'bid':bid}
    aucbid.append(aucbi)

    # for i in range(len(aucbid)):
    #     if aucbid[i]['bid']>bid:
    #         bid=aucbid[i]['bid']
    # return bid
def highestbidder(aucbid,h,highest):
    
    for i in range(len(aucbid)):
        if aucbid[i]['bid']>h:
            h=aucbid[i]['bid']
# print(h)
    for j in range(len(aucbid)):
        if aucbid[j]['bid']==h:
            highest.append(aucbid[j])
    

print("Welcome TO Screte IPL Auction Program!!!")
print("""'
     ___________
     \         /
      )_______(
      |"""""""|_.-._,.---------.,_.-._
      |       | | |               | | ''-.
      |       |_| |_             _| |_..-'
      |_______| '-' `'---------'` '-'
      )'''''''(
     |_________|
     `'-------'`
    .-------------.
    /_______________\'""")


#how=int(input("How many of you are here to Bid:"))
circ=['Hardik Pandya', ' Rohit Sharma', ' Dewald Brevis', ' Suryakumar Yadav', ' Ishan Kishan', ' N. Tilak Varma', ' Tim David', ' Harvik Desai', ' Arjun Tendulkar', ' Shams Mulani', ' Nehal Wadhera', ' Jasprit Bumrah', ' Kumar Kartikeya', ' Piyush Chawla', ' Akash Madhwal', ' Luke Wood', ' Romario Shepherd', ' Gerald Coetzee',
 ' Shreyas Gopal', ' Nuwan Thushara', ' Naman Dhir', ' Anshul Kamboj', ' Mohammad Nabi', ' Shivalik Sharma', 'Faf du Plessis', ' Glenn Maxwell', ' Virat Kohli', ' Rajat Patidar', ' Anuj Rawat', ' Dinesh Karthik', ' Suyash Prabhudessai', ' Will Jacks', ' Mahipal Lomror', ' Karn Sharma', ' Manoj Bhandage', ' Mayank Dagar', ' Vijaykumar Vyshak', ' Akash Deep', 
 ' Mohammed Siraj', ' Reece Topley', ' Himanshu Sharma', ' Rajan Kumar', ' Cameron Green', 
 ' Alzarri Joseph', ' Yash Dayal', ' Tom Curran', ' Lockie Ferguson', ' Swapnil Singh', ' Saurav Chauhan', '\nShreyas Iyer', ' Nitish Rana', ' Rinku Singh', ' Rahmanullah Gurbaz', ' Phil Salt', ' Sunil Narine', ' Suyash Sharma', ' Anukul Roy', ' Andre Russell', ' Venkatesh Iyer', ' Harshit Rana', ' Vaibhav Arora', ' Varun Chakaravarthy', ' KS Bharat', ' Chetan Sakariya', ' Mitchell Starc', ' Angkrish Raghuvanshi',
  ' Ramandeep Singh', ' Sherfane Rutherford', ' Manish Pandey', ' Allah Ghazanfar', ' Dushmantha Chameera', ' Sakib Hussain', ' Shubman Gill ', ' David Miller', ' Matthew Wade', ' Wriddhiman Saha', ' Kane Williamson', ' Abhinav Manohar', ' B. Sai Sudharsan', ' Darshan Nalkande', ' Vijay Shankar', ' Jayant Yadav', ' Rahul Tewatia', ' Noor Ahmad', ' Sai Kishore', ' Rashid Khan', ' Joshua Little', ' Mohit Sharma', 
  ' Azmatullah Omarzai', ' Umesh Yadav', ' Shahrukh Khan', ' Sushant Mishra', ' Kartik Tyagi', ' Manav Suthar', ' Spencer Johnson', ' Sandeep Warrier', ' BR Sharath', '\nPat Cummins', ' Abdul Samad', ' Abhishek Sharma', ' Aiden Markram', ' Marco Jansen', ' Rahul Tripathi', ' Washington Sundar', ' Glenn Phillips', ' Sanvir Singh', ' Heinrich Klaasen', ' Bhuvneshwar Kumar', ' Mayank Agarwal', ' T. Natarajan', ' Anmolpreet Singh',
   ' Mayank Markande', ' Upendra Singh Yadav', ' Umran Malik',
   ' Nitish Kumar Reddy', ' Fazalhaq Farooqi', ' Shahbaz Ahmed ', ' Travis Head', ' Vijayakanth Viyaskanth', ' Jaydev Unadkat', ' Akash Singh', ' Jhathavedh Subramanyan', 'Sanju Samson ', ' Jos Buttler', ' Shimron Hetmyer', ' Yashasvi Jaiswal', ' Dhruv Jurel', ' Riyan Parag', ' Donovan Ferreira', ' Kunal Rathore', ' Ravichandran Ashwin', ' Kuldeep Sen', ' Navdeep Saini', ' Sandeep Sharma', ' Trent Boult', ' Yuzvendra Chahal', 
   ' Avesh Khan', ' Rovman Powell', ' Shubham Dubey', ' Tom Kohler-Cadmore', ' Abid Mushtaq', ' Nandre Burger', ' Tanush Kotian', ' Keshav Maharaj','Ms Dhoni', 'Devon Conway', 'Ruturaj Gaikwad', 'Ajinkya Rahane', 'Shaik Rasheed', 'Sameer Rizvi', 'Avanish Rao Aravelly', 'Ravindra Jadeja', 'Mitchell Santner', 'Moeen Ali', 'Shivam Dube', 'Nishant Sindhu', 'Ajay Mandal', 'Rachin Ravindra', 'Shardul Thakur', 'Daryl Mitchell', 'Rajvardhan Hangargekar', 'Deepak Chahar', 'Maheesh Theekshana', 'Mukesh Choudhary', 
   'Mustafizur Rahman', 'Prashant Solanki', 'Simarjeet Singh', 'Tushar Deshpande', 'Matheesha Pathirana']
player= r.choice(circ)
# print(f"Player Released is {player}")
csk=[]
psk=[]
i='yes'
aucbid=[]
while i=='yes' or i=='y':
    print(f"\nPlayer Name {player}\n")
    n=input("Enter Your  Franchies Name:")
    bid=float(input("What's your bid in Crores:₹"))
    auction(n,bid)
    i=input("Are there any other Bidders?y/n:")
    print("\n\n\n\n\n\n\n\n\n\n")
    print(f"Bid is going on {bid}C and enter your Bid more than {bid}C!!!")
# print(aucbid)


h=0
highest=[]
l=0
# for i in range(len(aucbid)):
#     if aucbid[i]['bid']>h:
#         h=aucbid[i]['bid']
# # print(h)
# for j in range(len(aucbid)):
#     if aucbid[j]['bid']==h:
#         highest.append(aucbid[j])
highestbidder(aucbid=aucbid,h=h,highest=highest)
print("\nThe Auction Ends...\n")
# print(f"\ {highest[0]['name'].upper()}\n")
print(f"\n{player} is Packed by {highest[0]['name'].upper()} for the amount ₹{highest[0]['bid']}C ")

print("Bidding Result\n")
print("Franchies\tBid Ammount")
for i in range(len(aucbid)):
    print(f"{aucbid[i]['name']}\t\t{aucbid[i]['bid']}")
