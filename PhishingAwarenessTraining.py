print("=====================================")
print("   PHISHING AWARENESS TRAINING")
print("=====================================")

print("\nWhat is Phishing?")
print("Phishing is a cyber attack where attackers try to steal sensitive information")
print("like passwords, credit card numbers or personal data by pretending to be")
print("a trusted organization.")

print("\n-------------------------------------")
print("HOW TO RECOGNIZE PHISHING EMAILS")
print("-------------------------------------")

print("1. Suspicious sender email address")
print("2. Urgent messages like 'Your account will be closed!'")
print("3. Spelling and grammar mistakes")
print("4. Fake links that look like real websites")
print("5. Requests for personal information")

print("\n-------------------------------------")
print("SOCIAL ENGINEERING TACTICS")
print("-------------------------------------")

print("Attackers may:")
print("- Pretend to be bank officials")
print("- Send fake job offers")
print("- Ask for OTP or passwords")
print("- Create fear or urgency")

print("\n-------------------------------------")
print("BEST PRACTICES TO STAY SAFE")
print("-------------------------------------")

print("1. Never click suspicious links")
print("2. Always check the sender email")
print("3. Do not share passwords or OTP")
print("4. Use two-factor authentication")
print("5. Verify websites before logging in")

print("\n=====================================")
print("           QUIZ TIME")
print("=====================================")

score = 0

# Question 1
print("\nQ1: Phishing attacks are mainly used to:")
print("A. Improve website speed")
print("B. Steal sensitive information")
print("C. Update software")

ans = input("Enter answer: ")

if ans.upper() == "B":
    print("Correct!")
    score += 1
else:
    print("Wrong! Correct answer: B")

# Question 2
print("\nQ2: Which of these is a sign of phishing?")
print("A. Official domain email")
print("B. Secure website")
print("C. Urgent message asking for password")

ans = input("Enter answer: ")

if ans.upper() == "C":
    print("Correct!")
    score += 1
else:
    print("Wrong! Correct answer: C")

# Question 3
print("\nQ3: What should you do if you receive a suspicious email?")
print("A. Click the link immediately")
print("B. Ignore or report it")
print("C. Send your password")

ans = input("Enter answer: ")

if ans.upper() == "B":
    print("Correct!")
    score += 1
else:
    print("Wrong! Correct answer: B")

print("\n=====================================")
print("Your Score:", score, "/ 3")
print("=====================================")

print("\nThank you for completing Phishing Awareness Training!")