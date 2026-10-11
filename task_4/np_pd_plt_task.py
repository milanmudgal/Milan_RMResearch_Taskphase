import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(67)
# i

a = np.random.randint(1,100, size=(5,5))

print("original matrix is\n",a)

t = a.T
print("transpose of matrix is\n", t)

rowsum= a.sum(axis=0)
colsum=a.sum(axis=1)

print("sums of columns are\n", colsum)
print("sums of rows are\n", rowsum)


max_val= a.max()
print("max value is\n",max_val)


max_pos = np.unravel_index(np.argmax(a), a.shape)
print("position of max value is\n row:",max_pos[0]+1,"\n","column:",max_pos[1]+1)

# ii

names = ["Aarav", "Priya", "Rohan", "Ishita", "Kabir",
         "Meera", "Yusuf", "Ananya", "Devika"]

subjects = ["Math", "Science", "English", "Math", "Science",
            "English", "Math", "Science", "English"]

marks = [78, 65, np.nan, 92, 55, 60, 42, 67, 69]
attendance = [92, 70, 85, 95, 60, 78, 55, 90, 65]

df = pd.DataFrame({
    "name": names,
    "subject": subjects,
    "marks": marks,
    "attendance": attendance
})
print("Raw Data\n",df)
df["marks"] = df["marks"].fillna(df["marks"].mean())


avg_marks_per_subject = df.groupby("subject")["marks"].mean()
print("\avg marks per subject:\n", avg_marks_per_subject)


low_attendance = df[df["attendance"] < 75]
print("\nstudents with attendance below 75:\n", low_attendance)


df["result"] = np.where(df["marks"] >= 40, "Pass", "Fail")
print("\n with pass/fail column ")
print(df)


top5 = df.sort_values("marks", ascending=False).head(5)
print("\ntop 5 by marks:\n", top5)

# iii

plt.figure(figsize=(8, 5))
plt.plot(df["name"], df["marks"], color="green")
plt.xticks(rotation=45, ha="right")
plt.title("marks trend")
plt.xlabel("student")
plt.ylabel("marks")
plt.savefig("linePlot.png")
plt.close()

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].bar(avg_marks_per_subject.index, avg_marks_per_subject.values)
axes[0].set_title("avg marks per subject")
axes[0].set_ylabel("avg marks")

axes[1].hist(df["marks"], bins=6)
axes[1].set_title("mraks distribution")
axes[1].set_xlabel("marks")
axes[1].set_ylabel("number of students")


plt.savefig("bar_and_Histogram.png")
plt.close()

print("\nSaved: linePlot.png and bar_and_Histogram.png")