import json
import os
import numpy as np
import csv

sorted_candiates = []

scores_dir = os.path.join(os.getcwd(), "candidate_score")
sorted_result_dir = os.makedirs("sorted_candidates", exist_ok=True)

score_files = [f for f in os.listdir(scores_dir) if os.path.isfile(os.path.join(scores_dir, f))]

def overall_score(score_file):
    with open(score_file, "r", encoding="utf-8") as f:
        score_dict = json.load(f)
    
    check_null = lambda x: 0 if x==None
    
    skill_score = check_null(score_dict.get("related_skills"))
    job_score = check_null(score_dict.get("similar_previous_jobs"))
    education_score = check_null(score_dict.get("matching_education"))
    location_bool = check_null(score_dict.get("location"))
    seniority_score = check_null(score_dict.get("seniority_level_match"))
    project_score = check_null(score_dict.get("related_projects"))
    publication_score = check_null(score_dict.get("related_publication"))
    
    final_score = (0.177 * skill_score/100 + 
                   0.216 * job_score/100 + 
                   0.132 * education_score/100 +  
                   0.160 * seniority_score/100 + 
                   0.196 * project_score/100 +
                   0.119 * publication_score/100)
    
    return final_score, location_bool


for s_file in score_files:
    final_score, location_bool = overall_score(os.path.join(scores_dir, s_file))
    candidate_name = os.path.basename(os.path.join(scores_dir, s_file))
    sorted_candiates.append((candidate_name, final_score, location_bool))


sorted_candidates.sort(key=lambda x:x[1], reverse=True)

with open("sorted_result.csv", "w") as csv_out:
    csv_writer = csv.writer(csv_out)
    csv_writer.writerows(sorted_candidates)

for item in sorted_candiates:
    if item[2] == True:
        print(f"Final score for {item[0]} is: {item[1]}")
    elif item[2] == False:
        print(f"Final score for {item[0]} is: {item[1]}. Location does not match.")
    else:
        print(f"Final score for {item[0]} is: {item[1]}. Location is not defined.")