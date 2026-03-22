import pandas as pd
df = pd.read_csv("student_data.csv")

# features and target 
x = df[['hours_studied', 'sleep_hours', 'phone_usage', 'attendance']]
y = df['marks']

# train and test split
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
 
#  training
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)

# Accuracy
score = model.score( X_test, y_test)
print("Accuracy:", score)

# prediction making 

sample = pd.DataFrame({
    'hours_studied': [5],
    'sleep_hours': [7],
    'phone_usage': [3],
    'attendance': [80]
})

prediction = model.predict(sample)
print("Predicted Marks:", prediction[0])

# suuggestion system
def give_suggestions(hours, sleep, phone, attendance):
    suggestions = []

    if hours < 6:
        suggestions.append(" Increase study time by 1-2 hours daily")

    if sleep < 6:
        suggestions.append(" Improve sleep (at least 6-8 hours needed)")

    if phone > 4:
        suggestions.append(" Reduce phone usage to focus better")

    if attendance < 75:
        suggestions.append(" Improve attendance for better understanding")

    if not suggestions:
        suggestions.append(" Great job! Keep it up")

    return suggestions


# With prediction
hours = 5
sleep = 7
phone = 3
attendance = 80

pred = model.predict(pd.DataFrame({
    'hours_studied': [hours],
    'sleep_hours': [sleep],
    'phone_usage': [phone],
    'attendance': [attendance]
}))

print("Predicted Marks:", pred[0])

suggestions = give_suggestions(hours, sleep, phone, attendance)

print("\nSuggestions:")
for s in suggestions:
    print("-", s)
    
    
