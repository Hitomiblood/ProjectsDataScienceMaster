# Final Project Data Science Techniques

## Description:
- In this project we are going to work with a DataSet provided by company "A" ([dataInformation.csv](/ProyectoFinal_TecnicasCienciaDatos/dataInformation.csv)). This company works to rehabilitate people from mental illnesses with games that train their brain. The information we have in the DataSet is:
    - Id of the patient.
    - Date of the score record.
    - The score obtained by the user after playing the game.

    On the other hand, the company asks us to complete some [tasks](/ProyectoFinal_TecnicasCienciaDatos/EnunciadoTrabajo.docx) to show them the information they give us in an organized way and create a model to make a classification of the improvement of the patients in relation to a class they design. The tasks are:

- Display the performance time series x_i (t) for each user i. Note that the number of points in each series is different.
- Construct and visualize new time series of p_i (t), where at each point in time the p_x percentile of the performance value x computed over the entire sample is shown. 
HELP: You may consider that the moments of the distribution of values do not change over time. Is this approximation valid?
- If we define three classes as follows.

    C_1={x∶ x ∈〖 p〗_x≤20} C_2={x∶ x ∈〖 20< p〗_x≤80} C_3={x∶ x∈〖 p〗_x>80}
    
    computes as a function of ▁x (where ▁x is the mean of x in the first 15 days) the membership of each class after 6 months from the first recorded measurement. 
    
    HELP: Perform supervised or multiclass classification or 1 class vs. the rest. Define training, validation and testing cohorts.
    
The programming process and the develop of the project is in [Trabajo_Final_Tecnicas.ipynb](/ProyectoFinal_TecnicasCienciaDatos//Trabajo_Final_Tecnicas.ipynb)
