% Knowledge base of diseases and their symptoms.
% Format: disease(DiseaseName, [symptom1, symptom2, ...]).
disease(flu, [fever, cough, aches, fatigue]).
disease(cold, [sore_throat, runny_nose, sneezing]).
disease(migraine, [headache, light_sensitivity, nausea]).
disease(food_poisoning, [nausea, vomiting, diarrhea, stomach_cramps]).

% The user must add facts about their symptoms.
% Example:
% has_symptom(fever).
% has_symptom(cough).
% has_symptom(aches).

% A rule to find a diagnosis. A disease is a possible diagnosis if
% all of its symptoms are present.
possible_diagnosis(Disease) :-
    disease(Disease, Symptoms),
    forall(member(Symptom, Symptoms), has_symptom(Symptom)).

% Example Queries:
% To find a diagnosis for someone with a cold:
% ?- has_symptom(sore_throat), has_symptom(runny_nose), possible_diagnosis(Disease).
% To find all possible diagnoses for a user:
% ?- possible_diagnosis(Disease).
