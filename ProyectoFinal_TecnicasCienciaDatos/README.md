# Final Project Data Science Techniques

## Description:
In this project, we will be working with a dataset provided by company "A" (dataInformation.csv). This company focuses on rehabilitating individuals with mental illnesses through brain-training games. The information available in the dataset includes:

* Patient ID
* Date of the score record
* The score obtained by the user after playing the game

Additionally, the company has [tasked](/ProyectoFinal_TecnicasCienciaDatos/EnunciadoTrabajo.pdf) us with completing specific objectives to present the information in an organized manner and creating a model for classifying the improvement of patients according to a designated class. The tasks include:

1. Display the performance time series $x_i(t)$ for each user $i$. Note that the number of data points in each series varies.

2. Construct and visualize new time series $p_i(t)$, where at each time point, the $p_x$ percentile of the performance value $x$ computed over the entire sample is shown. **HELP:** You may assume that the distribution of values remains constant over time. Is this approximation valid?

3. Define three classes as follows:

- $$C_1 = \{x : x \in p_x \leq 20\}$$
- $$C_2 = \{x : 20 < p_x \leq 80\}$$
- $$C_3 = \{x : x \in p_x > 80\}$$

Compute, as a function of $\bar{x}$ (where $\bar{x}$ is the mean of $x$ in the first 15 days), the membership of each class after 6 months from the first recorded measurement. **HELP:** Perform supervised or multiclass classification or 1 class vs. the rest. Define training, validation, and testing cohorts.


The programming process and project development can be found in [Trabajo_Final_Tecnicas.ipynb](/ProyectoFinal_TecnicasCienciaDatos//Trabajo_Final_Tecnicas.ipynb)
