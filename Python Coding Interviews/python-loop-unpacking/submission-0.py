from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:
    #unpack then sort then return highest value 
    highest_student = ("Hi", 0)
    highest_name, highest_score = highest_student
    for student,score in scores:
        if score > highest_score:
            highest_name = student
            highest_score = score
    
    return highest_name
            
            
        



# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
