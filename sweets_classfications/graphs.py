import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
import seaborn as sns


true_labels = ['gulab jamun','jalebi','kajja','Kaju katli']
predicted_labels = ['gulab jamun','jalebi','kajja','Kaju katli']

# Generate confusion matrix
cm = confusion_matrix(true_labels, predicted_labels)

# Plot confusion matrix
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, cmap='Blues', fmt='g')
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('Confusion Matrix')
plt.show()


import matplotlib.pyplot as plt
from sklearn.metrics import precision_score, recall_score, f1_score

# Calculate precision, recall, and F1 score
precision = precision_score(true_labels, predicted_labels)
recall = recall_score(true_labels, predicted_labels)
f1 = f1_score(true_labels, predicted_labels)

# Plot bar chart
metrics = ['Precision', 'Recall', 'F1 Score']
values = [precision, recall, f1]
plt.bar(metrics, values)
plt.ylabel('Score')
plt.title('Model Evaluation Metrics')
plt.show()
