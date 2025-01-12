minutes_of_control=float(input());
seconds_of_control=float(input());
disange_of_competition=float(input());
seconds_of_100m_distance=int(input());

total_time_of_control=(minutes_of_control*60)+seconds_of_control;
reduced_time_of_control=disange_of_competition/120;

total_reduced_time=reduced_time_of_control *2.5;
time_of_marvin=(disange_of_competition/100 *seconds_of_100m_distance) - total_reduced_time;
control_time= time_of_marvin <=total_time_of_control;

if control_time:
    print("Marin Bangiev won an Olympic quota!");
    print(f"His time is {time_of_marvin:.3f}.")
else:
    print(f"No, Marin failed! He was {time_of_marvin-total_time_of_control:.3f} second slower.")
