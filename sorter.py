import json
import os
import csv


def overall_score(score_file):
    with open(score_file, "r", encoding="utf-8") as f:
        score_dict = json.load(f)
    
    check_none = lambda x: False if x is None else True
    
    scores_list = ["related_skills", "similar_previous_jobs", "matching_education",
                    "seniority_level_match", "related_projects", "related_publication"]
    
    weights_list = [0.177, 0.216, 0.132, 0.160, 0.196, 0.119]
    
    final_score = 0
    evaluation_completeness = 0
    complete_evolutions = 0
   
    for i, v in enumerate(scores_list):
        if check_none(score_dict.get(v)):
            final_score += weights_list[i] * score_dict.get(v)/100
            complete_evolutions += 1
    
    if complete_evolutions == 0:
        final_score = None
    
    evaluation_completeness = (complete_evolutions / len(scores_list)) * 100
    
    location_bool = score_dict.get("location")
    
    return final_score, evaluation_completeness, location_bool


def sorter_func(scores_dir, sorted_result_dir, sorted_candidates):

    score_files = [f for f in os.listdir(scores_dir) if os.path.isfile(os.path.join(scores_dir, f))]

    for s_file in score_files:
        final_score, evaluation_completeness, location_bool = overall_score(os.path.join(scores_dir, s_file))
        candidate_name = os.path.basename(os.path.join(scores_dir, s_file))
        sorted_candidates.append((candidate_name, final_score, evaluation_completeness, location_bool))


    sorted_candidates.sort(key=lambda x:x[1], reverse=True)

    with open(os.path.join(sorted_result_dir, "sorted_result.csv"), "w", encoding="utf-8") as csv_out:
        csv_writer = csv.writer(csv_out)
        csv_writer.writerow(["candidate_name", "final_score", "evaluation_completeness", "location_bool"])
        csv_writer.writerows(sorted_candidates)

    for item in sorted_candidates:
        if item[3] == True:
            print(f"Final score for {item[0]} is: {item[1]:.3f} and evaluation_completeness is: {item[2]:.3f}")
        elif item[3] == False:
            print(f"Final score for {item[0]} is: {item[1]:.3f} and evaluation_completeness is: {item[2]:.3f}. Location does not match.")
        else:
            print(f"Final score for {item[0]} is: {item[1]:.3f} and evaluation_completeness is: {item[2]:.3f}. Location is not defined.")