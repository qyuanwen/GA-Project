<img src="http://imgur.com/1ZcRyrc.png" style="float: left; margin: 20px; height: 55px">

#  Capstone Project: Train Delays Predictor
---

### Problem Statement and Solution Approach:

**Problem:**<br>
Despite ongoing efforts to improve the MRT system, train delays and faults persist, causing frustration and inconvenience for passengers.

**Proposed Solution:**<br>As a daily commuter of Singapore MRT, I aim to develop a train delays predictor that can identify stations and timings that are more likely to experience breakdowns or delays. 

By analyzing historical data on time of day, type of day, station name, commuter volume, and breakdown/non-breakdown indicators, I hope to create a model that can accurately predict future breakdowns and help commuters avoid stations and times with potential delays.

---

### Data used:
Data used in the analysis consists of SMRT information from the Land Transport Authorithy and SMRT tweets about train faults scrapped from SMRT Twitter profile page. Please rerefer to the data dictionary for more information on the columns extracted.

---

### Data dictionary

<a id="trainFault_df"></a>
**Dataset name: `trainFault_df`**<br>This dataset contains the cleaned information from twitter on the train's delays/faults.


| Feature | Type | Description |
| ------- | ---- | ----------- |
| year_month | string | The year and month of the record. |
| day_type | string | The type of day (weekday/weekend) |
| time_per_hour | integer | The hour of the day in which the record was recorded. |
| pt_code | string | The unique identifier for the train station. |
| station_name | string | The name of the train station.|
| train_line | string | Train line code |
| fault_type | string | A description of the type of fault that occurred, if any. |




<a id="passenger_df"></a>
**Dataset name: `passenger_df`**<br>This dataset contains the cleaned information from LTA on the train's passenger tap-ins and tap-outs.<br> **(Note: Only information from Dec-2022 to Feb-2023 is extracted from LTA using API, the rest of the period data are imputed using scikit Learn)**

| **Feature** | **Type** | **Description** |
|-------------|----------|-----------------|
| year_month | string | The year and month of the record. |
| day_type | string | The type of day (weekday/weekend) |
| time_per_hour | string | The hour of the day in which the record was recorded. |
| pt_code | string | The unique identifier for the train station. |
| station_name | string | The name of the train station. |
| total_tap_in_volume | int | The total number of passengers who tapped in at the station during the recorded hour.|
| total_tap_out_volume | int | The total number of passengers who tapped out at the station during the recorded hour. |


<a id="combinedSmrt_df"></a>
**Dataset name: `combinedSmrt_df`**<br>This dataset contains the combined information from the above dataset and additional calculated features for modelling.<br>

| Feature | Type | Description |
| :--- | :--- | :--- |
| year_month | string | The year and month of the record. |
| day_type | string | The type of day (weekday/weekend) |
| time_per_hour | int | The hour of the day in which the record was recorded. |
| pt_code | string | The unique identifier for the train station. |
| station_name | string | The name of the train station. |
| total_tap_in_volume | int | The total number of passengers who tapped in at the station during the recorded hour. |
| total_tap_out_volume | int | The total number of passengers who tapped out at the station during the recorded hour. |
| fault | bool | A binary indicator of whether a fault occurred at the station during the recorded hour. |
| fault_type | string | A description of the type of fault that occurred, if any. |



---

### Data Collection
Refer to **1. Data Collection** notebook.

---

### Data Cleaning and Data Analysis
Refer to **2. Data Cleaning and Data Analysis** notebook.

---

### Data Modelling

Refer to **Data Modelling** notebook.

---

### Key Takeaways

1. The Train delays predictor uses Logistic regression as it achieved a 72.4% accuracy.

2. The time of day and station name were found to be important predictors of train breakdowns, suggesting that improvements in infrastructure and maintenance should be prioritized for these high-risk areas.

3. With further research and data collection, the predictor model can be improved to more accurately predict train breakdowns and enable proactive maintenance and repairs, ultimately improving the commuting experience for passengers.

---

### Limitations and Future Enhancements

1. Limited data availability due to most of the 5 years of passenger tap-in and out data being imputed and only 3 months of latest data being provided by LTA.

2. The predictor model only considers data from SMRT and does not include train lines from SBS transit. This can be improved in the future after scraping data from SBS transit twitter profile.

3. There is potential to improve accuracy and gain new insights by including additional features like weather and maintenance schedule in the predictor model.
