import random
import sys


#arriveCustomer(int id, int t, int numb)
arrive_function = "arriveCustomer"

# customerState(int id, int t)
# griddleState(int t)
# griddleWait(int t)
common_functions = ["customerState", "griddleState", "griddleWait"]

# customerWaitTime(int id)
# avgWaitTime()
final_functions = ["customerWaitTime", "avgWaitTime"]

block = """try{{
    {};
}}
catch(IllegalNumberException e){{
    System.out.println("Exception");
}}"""


total_customers = int(sys.argv[1])
k = sys.argv[2]
m = sys.argv[3]
test_case = sys.argv[4]

f = open('TestCase'+test_case+'.java', 'w')


start_code = '''import java.io.*;  
public class TestCase{} {{ 
public static void main(String[] args){{


try{{
    PrintStream o = new PrintStream(new File("StudentAnswer{}.txt"));
    PrintStream console = System.out;

    // Assign o to output stream
    System.setOut(o);
}}
catch (FileNotFoundException ex){{
        // insert code to run when exception occurs
}}

MMBurgersInterface mm = new MMBurgers();
System.out.println("--Started simulation--");
try{{
    mm.setK({});
    mm.setM({});
}}
catch(IllegalNumberException e){{
    System.out.println("Exception");
}}'''.format(test_case, test_case, k, m)

f.write(start_code)

#customer id
customer = 1
time = 0
max_cust_at_once = int(0.1*total_customers)
turn = 1
max_burgers = 100

while customer<=total_customers :
    
    if(turn == 1):
        #call arrive customers only
        for cust in range(min(total_customers-customer+1, random.randint(1, max_cust_at_once))):
            f.write(block.format("mm.arriveCustomer("+str(customer)+", "+str(time)+", "+str(random.randint(1, max_burgers))+")"))
            customer += 1
            time += random.randint(0, 10)

    else :
        #call common functions
        # customerState(int id, int t)
        # griddleState(int t)
        # griddleWait(int t)
        for i in range(random.randint(1, max(5, int(max_cust_at_once*0.5)))):
            function = random.choice(common_functions)
            if function == "customerState":
                f.write(block.format("System.out.println("+function+"("+str(random.randint(1, total_customers))+", "+str(time)+"))"))
            elif function == "griddleState":
                f.write(block.format("System.out.println("+function+"("+str(time)+"))"))
            else:
                f.write(block.format("System.out.println("+function+"("+str(time)+"))"))
            
            time += random.randint(1, 10)

    turn = 1 - turn




for i in range(min(total_customers, 100)):
    function = random.choice(common_functions)
    if function == "customerState":
        f.write(block.format("System.out.println("+function+"("+str(random.randint(1, total_customers))+", "+str(time)+"))"))
    elif function == "griddleState":
        f.write(block.format("System.out.println("+function+"("+str(time)+"))"))
    else:
        f.write(block.format("System.out.println("+function+"("+str(time)+"))"))
    
    time += random.randint(1, 10)


for i in range(max(total_customers, 100)):
    function = final_functions[0]
    f.write(block.format("System.out.println("+function+"("+str(random.randint(1, total_customers))+"))"))
  

f.write(block.format("System.out.println("+final_functions[1]+"())"))
f.write('\n}\n}')
f.close()