# student_performance_analysis.py

import pandas as pd
import numpy as np

# -----------------------------
# STEP 1: Create data manually
# -----------------------------
data = {
    'Name': ['Aman', 'Riya', 'Karan', 'Tanvi', 'Daksh'],
    'Maths': [85, 78, 90, 85, 88],
    'Science': [92, 81, 85, 100, 91],
    'English': [88, 74, 89, 90, 93]
}

# Create DataFrame
df = pd.DataFrame(data)

# -----------------------------
# STEP 2: Calculate total and average marks
# -----------------------------
df['Total'] = df[['Maths', 'Science', 'English']].sum(axis=1)
df['Average'] = np.round(df['Total'] / 3, 2)

# -----------------------------
# STEP 3: Assign grades
# -----------------------------
def get_grade(avg):
    if avg >= 90:
        return 'A+'
    elif avg >= 80:
        return 'A'
    elif avg >= 70:
        return 'B'
    elif avg >= 60:
        return 'C'
    else:
        return 'D'

df['Grade'] = df['Average'].apply(get_grade)

# -----------------------------
# STEP 4: Find toppers and subject analysis
# -----------------------------
overall_topper = df.loc[df['Total'].idxmax(), 'Name']
maths_topper = df.loc[df['Maths'].idxmax(), 'Name']
science_topper = df.loc[df['Science'].idxmax(), 'Name']
english_topper = df.loc[df['English'].idxmax(), 'Name']

# -----------------------------
# STEP 5: Display analysis
# -----------------------------
print("\n📊 STUDENT PERFORMANCE DATA ANALYSIS 📊\n")
print(df)
print("\nOverall Topper:", overall_topper)
print("Maths Topper:", maths_topper)
print("Science Topper:", science_topper)
print("English Topper:", english_topper)

# -----------------------------
# STEP 6: Subject-wise statistics
# -----------------------------
print("\n📈 SUBJECT-WISE AVERAGES 📈")
for subject in ['Maths', 'Science', 'English']:
    print(f"{subject}: {df[subject].mean():.2f}")

# -----------------------------
# STEP 7: Grade distribution
# -----------------------------
print("\n🎓 GRADE DISTRIBUTION 🎓")
print(df['Grade'].value_counts())