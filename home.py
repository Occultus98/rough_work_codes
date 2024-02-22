
#DECLARATIONS
math_marks = int(input("\nMath Score: "))
art_marks = int(input("Art Score: "))
science_marks = int(input("Science Score: "))
english_marks = int(input("English Score: "))
SUBJECTS_COUNT = 4

#COMPUTATIONS
total = math_marks + art_marks + science_marks + english_marks
average = total/SUBJECTS_COUNT

#OUTPUT
print(f"\nTOTAL: {total}\nAVERAGE: {average}\n")

