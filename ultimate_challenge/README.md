# The Ultimate Challenge

This was a three part challenge aimed at predicting rider retention for a taxi service. The goal was to identify the most significant factors contributing to rider retention. 

## Part 1 - Exploratory data analysis

This part was seperate from the prediction phase and was meant to explore login trends for users over a given time period. The time stamp was aggregated by logins over 15 minute intervals and examined for intermediate trends. The timeseries plots reveal weekday surges around 12pm and 12am, and weekend surges around 4am (Friday and Saturday night).

## Part 2 ‑ Experiment and metrics design

Problem prompt:

"The neighboring cities of Gotham and Metropolis have complementary circadian rhythms: on
weekdays, Ultimate Gotham is most active at night, and Ultimate Metropolis is most active
during the day. On weekends, there is reasonable activity in both cities.
However, a toll bridge, with a two­way toll, between the two cities causes driver partners to tend
to be exclusive to each city. The Ultimate managers of city operations for the two cities have
proposed an experiment to encourage driver partners to be available in both cities, by
reimbursing all toll costs.

1. What would you choose as the key measure of success of this experiment in encouraging driver partners to serve both cities, and why would you choose this metric?
2. Describe a practical experiment you would design to compare the effectiveness of the proposed change in relation to the key measure of success. 

    Please provide details on:

        a. how you will implement the experiment
        b. what statistical test(s) you will conduct to verify the significance of the observation
        c. how you would interpret the results and provide recommendations to the city operations team along with any caveats."

Response:

Assuming each driver is registered in either Matropolis or Gotham, we could measure the effectiveness of a bridge toll reimbursement experiment by tallying the number of rides each driver takes outside of their registered city. Our key measure of success would then be the average number of riders picked up outside of a drivers registered location. Assuming there is a significant bias towards ones own city, the average number would be low for drivers in both cities. The hope then would be that this statistic increases after the incentive is provided, thus deeming the experiment a success. 

This can be done by testing the incentive with a randomly selected group of drivers and comparing the results to a control group who was not given the incentive. If the results indicate an increase, this can be tested by comparing means for each group and determining if the change is deemed significant. 

Significance here can be determined using the two sample t-test, which will determine if the difference in means of randomly sampled groups from two populations is significant enough to rule out the null hypothesis. Our null hypothesis here would be that the incentive has no influence on whether a driver will leave his city to pick up a rider. Our alternative hypothesis would be that it does. 

The results would be interpreted based on the 5% conventional threshold for significance. If the difference in means is considered significant it can be concluded that the incentive does motivate drivers to navigate outside of the their registered city limits to pick up a fare. However, the difference must also be significant enough to justify the cost of implementing the incentive. The outcome would need to be cross examined by the finance team to determine if the incentive is feasible for the entire population for both cities. 

## Part 3 ‑ Predictive modeling

### Results

The best results came from the catboost classifier which was able to determine if a rider will be retained with about an 80% accuracy. The AUROC was about an 86% which is also promising. The top 3 most influential indicators of rider retention according to this model are weekday percentage of rides, location and the type of phone a rider has. The most significant indicator here is the weekday percentage of rides for users, so I will specifically focus on how Ultimate can leverage this to their advantage. 

The question here is how the significant features can be interpreted, from the exploratory analysis performed it was evident that retained riders are balanced in their use of the Ultimate service, the percentage gradually varied from primarily weekend users to primarily weekday users, with very few polarized to either one. Riders who were not retained used the service almost exclusively on the weekends or during the weekday with over 60% of them split between the two. 

Ultimate can use this to their advantage by advertising the service to riders who need it for work and play. This would be riders who live an inner city lifestyle and do not have a car, or are paying the cost of having to park. These customers would need the service not just as a convenience, but as a necessity. By increasing the number of riders who are using the service on weekdays and weekends, presumably for work and weekend outings, the percentage of retained riders should increase.