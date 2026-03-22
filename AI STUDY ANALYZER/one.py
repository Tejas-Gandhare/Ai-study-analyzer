import pandas as pd
import numpy as np

np.random.seed(42)

data = {
    "hours_studied": np.random.randint(1, 10, 200),
    "sleep_hours": np.random.randint(4, 9, 200),
    "phone_usage": np.random.randint(1, 8, 200),
    "attendance": np.random.randint(50, 100, 200),
}

df = pd.DataFrame(data)

# Create marks (logic-based)
df["marks"] = (
    df["hours_studied"] * 5 +
    df["sleep_hours"] * 2 -
    df["phone_usage"] * 3 +
    df["attendance"] * 0.5 +
    np.random.randint(-10, 10, 200)
)

print(df.head())

# Save dataset
df.to_csv("student_data.csv", index=False)

df.info()
df.describe()
import seaborn as sns
import matplotlib.pyplot as plt

sns.pairplot(df)
plt.show()
