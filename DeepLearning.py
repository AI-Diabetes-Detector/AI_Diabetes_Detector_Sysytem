import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_recall_fscore_support, roc_auc_score

# 1. Custom Dataset Class for Tabular Health Data
class DiabetesDataset(Dataset):
    def __init__(self, X, y):
        self.X = torch.tensor(X, dtype=torch.float32)
        self.y = torch.tensor(y, dtype=torch.float32).unsqueeze(1)
        
    def __len__(self):
        return len(self.X)
    
    def __getitem__(self, idx):
        return self.X[idx], self.y[idx]

# 2. Deep Neural Network (MLP) for Diabetes Detection
class DiabetesDetectorNN(nn.Module):
    def __init__(self, input_dim):
        super(DiabetesDetectorNN, self).__init__()
        self.network = nn.Sequential(
            nn.Linear(input_dim, 64),
            nn.BatchNorm1d(64),
            nn.ReLU(),
            nn.Dropout(0.3),
            
            nn.Linear(64, 32),
            nn.BatchNorm1d(32),
            nn.ReLU(),
            nn.Dropout(0.3),
            
            nn.Linear(32, 16),
            nn.ReLU(),
            
            nn.Linear(16, 1),
            nn.Sigmoid()  # Outputs probability between 0 and 1
        )
        
    def forward(self, x):
        return self.network(x)

# 3. Data Preparation Pipeline
def prepare_data(filepath=None):
    # If no file is provided, generate synthetic sample data for demonstration
    if filepath is None:
        np.random.seed(42)
        X = np.random.randn(768, 8)  # 8 clinical features (e.g., glucose, BMI, age, etc.)
        y = np.random.randint(0, 2, size=(768, 1))
    else:
        df = pd.read_csv(filepath)
        X = df.iloc[:, :-1].values
        y = df.iloc[:, -1].values

    # Train/Test Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    # Standardization (Crucial for Neural Networks)
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    return X_train, X_test, y_train, y_test

# 4. Training Function
def train_model():
    X_train, X_test, y_train, y_test = prepare_data()
    
    train_dataset = DiabetesDataset(X_train, y_train)
    test_dataset = DiabetesDataset(X_test, y_test)
    
    train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=32, shuffle=False)
    
    model = DiabetesDetectorNN(input_dim=X_train.shape[1])
    criterion = nn.BCELoss()  # Binary Cross-Entropy Loss
    optimizer = optim.Adam(model.parameters(), lr=0.001, weight_decay=1e-4)
    
    epochs = 50
    print(f"--- Starting Training for {epochs} Epochs ---")
    
    for epoch in range(epochs):
        model.train()
        running_loss = 0.0
        for inputs, targets in train_loader:
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, targets)
            loss.backward()
            optimizer.step()
            running_loss += loss.item() * inputs.size(0)
            
        epoch_loss = running_loss / len(train_loader.dataset)
        if (epoch + 1) % 10 == 0:
            print(f"Epoch [{epoch+1}/{epochs}], Loss: {epoch_loss:.4f}")
            
    # Evaluation
    model.eval()
    all_preds = []
    all_targets = []
    all_probs = []
    
    with torch.no_grad():
        for inputs, targets in test_loader:
            outputs = model(inputs)
            preds = (outputs >= 0.5).float()
            all_preds.extend(preds.numpy())
            all_targets.extend(targets.numpy())
            all_probs.extend(outputs.numpy())
            
    acc = accuracy_score(all_targets, all_preds)
    precision, recall, f1, _ = precision_recall_fscore_support(all_targets, all_preds, average='binary')
    roc_auc = roc_auc_score(all_targets, all_probs)
    
    print("\n--- Model Evaluation Results ---")
    print(f"Accuracy:  {acc:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall:    {recall:.4f}")
    print(f"F1-Score:  {f1:.4f}")
    print(f"ROC-AUC:   {roc_auc:.4f}")
    
    # Save Model Weights
    torch.save(model.state_dict(), "diabetes_nn_model.pth")
    print("\nModel saved successfully as 'diabetes_nn_model.pth'")

if __name__ == "__main__":
    train_model()

