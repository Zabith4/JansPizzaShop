import run_sim as sim
import run_sim2 as sim2
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

'''
generates the graph that plots average number of houses
per trip vs the amount of minutes that the shop is open.
gap_time = 10 minutes
'''
def avg_houses(gap):

    avg_houses = []

    for minutes in range(60, 721, 30):
        total_houses = 0
        total_trips = 0
        for sims in range(0, 15):
            stats = sim.run_sim(gap, minutes)
            total_trips += stats.total_trips
            total_houses += stats.total_houses
        avg = total_houses / total_trips
        avg_houses.append(avg)

    return avg_houses

''' The new  function will plot the average number of houses
per trip vs the amount of mintes that the shop is open
gap_time increases from 1 to 5'''
    
def gap_time_house_distance_graph():
    
    avg_house_gap_1 = []
    avg_house_gap_2 = []
    avg_house_gap_3 = []
    avg_house_gap_4 = []
    avg_house_gap_5 = []
    
    avg_house_gap_1 = avg_houses(1)
    avg_house_gap_2 = avg_houses(2)
    avg_house_gap_3 = avg_houses(3)
    avg_house_gap_4 = avg_houses(4)
    avg_house_gap_5 = avg_houses(5)
    
    plt.scatter(range(60, 721, 30), avg_house_gap_1,color = 'b')
    plt.scatter(range(60, 721, 30), avg_house_gap_2,color = 'r')
    plt.scatter(range(60, 721, 30), avg_house_gap_3,color = 'y')
    plt.scatter(range(60, 721, 30), avg_house_gap_4,color = 'k')
    plt.scatter(range(60, 721, 30), avg_house_gap_5,color = 'g')
    blue_patch = mpatches.Patch(color='blue', label='Gap Time 1')
    red_patch = mpatches.Patch(color='red', label='Gap Time 2')
    yellow_patch = mpatches.Patch(color='yellow', label='Gap Time 3')
    black_patch = mpatches.Patch(color='black', label='Gap Time 4')
    magenta_patch = mpatches.Patch(color='green', label='Gap Time 5')
    plt.legend(handles=[blue_patch,red_patch,yellow_patch,black_patch,magenta_patch],loc=4)
    plt.title("Average Delivery Route Size vs Length Shop is Open")
    plt.xlabel("Minutes Shop is Open")
    plt.ylabel("Average Number of Houses on Delivery Route")
    plt.savefig("Average_Number_of_Houses_on_Delivery_Route_with_gap_time")
    
    print(len(avg_house_gap_1))

def avg_travle_time(gap):
    
    avg_travel = []
    
    for minutes in range(60, 721, 30):
        total_travle_time = 0
        for sims in range(0, 100):
            stats = sim.run_sim(gap, minutes)
            total_travle_time += stats.avg_travel_time
        avg = total_travle_time / 100
        avg_travel.append(avg)
    return avg_travel

def gap_time_travle_time_graph():
    
    avg_trav_dist_gap_1 = []
    
    avg_trav_dist_gap_1 = avg_travle_time(5)    
    
    plt.scatter(range(60, 721, 30), avg_trav_dist_gap_1,color = 'b')
    plt.title("Average Travle Distance vs Length Shop is Open")
    plt.xlabel("Minutes Shop is Open")
    plt.ylabel("Average Travle Time on Delivery Route")
    plt.savefig("Average_Number_of_Houses_on_Avg_Travle_time_Route_with_gap_time")

def avg_revenue_busy_time():

    avg_revenue = []

    for busy in range(5, 120, 15):
        total_renvue = 0
        for sims in range(0, 50):
            stats = sim2.run_sim(10, 240, busy,  720)
            total_renvue += stats.total_revenue
        avg_revenue.append(total_renvue/50)

    plt.scatter(range(5, 120, 15), avg_revenue)
    plt.title("Average Revenue vs Length of Busy Time")
    plt.xlabel("Length of Busy Time")
    plt.ylabel("Average Revenue")
    plt.show()

def avg_revenue_houses_busy_time():
    avg_revenue = []
    avg_house = []

    for busy in range(0, 125, 25):
        total_renvue = 0
        total_houses = 0
        for sims in range(0, 1):
            stats = sim2.run_sim(5, 240, busy,  720)
            total_renvue += stats.total_revenue
            total_houses += stats.total_houses
        avg_revenue.append(total_renvue/1)
        avg_house.append(total_houses/1)

    plt.scatter(range(0, 100, 25), avg_revenue, 'bo')
    plt.scatter(range(0, 100, 25), avg_house, 'ro')
    plt.title("Average Revenue vs Length of Busy Time")
    plt.xlabel("Length of Busy Time")
    plt.ylabel("Average Revenue")
    plt.show()

    
    
def main():
    #gap_time_house_distance_graph()
    #gap_time_travle_time_graph()
    avg_revenue_busy_time()

if __name__ == '__main__':
    main()


