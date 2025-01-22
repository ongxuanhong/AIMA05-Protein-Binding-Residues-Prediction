model = Sequential()

# 1D convolution layer (Conv1D)  with 32 filters, kernel size of 3, ReLU activation function
model.add(Conv1D(32, kernel_size=3, activation='relu', input_shape=(X_train.shape[1], 1)))

# Max pooling layer with pool size of 2
model.add(MaxPooling1D(pool_size=2))

# Flatten the multi-dimensional data
model.add(Flatten())

# Fully connected layer with 64 neurons and ReLU activation function
model.add(Dense(64, activation='relu'))

# Fully connected layer with 3 neurons and softmax activation function
# 3 classes: mometal, nuclear acid, small molecules
model.add(Dense(3, activation='softmax'))