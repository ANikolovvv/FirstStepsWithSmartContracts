whole_number=int(input());
bonus_score=0;

if whole_number%2==0:
    bonus_score+=1;
if whole_number%10==5:
    bonus_score+=2;

if whole_number <=100:
    bonus_score+=5;
elif whole_number>100 and whole_number<=1000:
    bonus_score+=whole_number*0.2;
else:
    bonus_score+=whole_number*0.1;

print(bonus_score);
print(whole_number+bonus_score);
