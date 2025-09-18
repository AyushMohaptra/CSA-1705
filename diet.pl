% A simple knowledge base for a dieting system based on diseases.

% Facts about foods to avoid for specific diseases.
avoids(diabetes, high_sugar).
avoids(diabetes, refined_carbs).
avoids(hypertension, high_salt).
avoids(hypertension, saturated_fats).
avoids(celiac_disease, gluten).
avoids(kidney_disease, high_potassium).

% Facts about foods to recommend for specific diseases.
recommends(diabetes, vegetables).
recommends(diabetes, lean_protein).
recommends(hypertension, fruits).
recommends(hypertension, whole_grains).
recommends(celiac_disease, gluten_free_grains).
recommends(kidney_disease, low_sodium_foods).

% A rule to find what foods to avoid for a disease.
diet_to_avoid(Disease, Food) :-
    avoids(Disease, Food).

% A rule to find what foods to recommend for a disease.
diet_to_recommend(Disease, Food) :-
    recommends(Disease, Food).

% Example queries:
% To find what to avoid for diabetes:
% ?- diet_to_avoid(diabetes, Food).

% To find what is recommended for hypertension:
% ?- diet_to_recommend(hypertension, Food).
