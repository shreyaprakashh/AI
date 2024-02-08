a=int(input("Enter the quantity of jug a:"));
b=int(input("Enter the quantity of jug b:"));
ai=int(input("Enter the initial value of a:"));
bi=int(input("Enter the initial value of b:"));
af=int(input("Enter the final value of a:"));
bf=int(input("Enter the final value of b:"));
print("List of options")
print("1.Fill jug a completely\n");
print("2.Fill jug b completely\n");
print("3.Empty a completely\n");
print("4.Empty b completely\n");
print("5.Pour from jug a till jug b filled completely or a becomes empty\n");
print("6.Pour from jug b till jug a filled completely or b becomes empty\n");
print("7.Pour all from jug b to jug a\n");
print("8.Pour all from jug a to jug b\n");

while(ai!=af or bi!=bf):
 opt=int(input("Enter the option:"));
 if(opt==1):
    ai=a;
 elif(opt==2):
    bi=b;
 elif(opt==3):
    ai=0;
 elif(opt==4):
    bi=0;
 elif(opt==5):
    if(b-bi>ai):
      bi=ai+bi;
      ai=0;
    else:
      ai=ai-(b-bi);
      bi=b;
 elif(opt==6):
    if(a-ai>bi):
      ai=ai+bi;
      bi=0;
    else:
      bi=bi-(a-ai);
      ai=a;
 elif(opt==7):
      ai=ai+bi;
      bi=0;
 elif(opt==8):
      bi=bi+ai;
      ai=0;
 print(ai,bi);
