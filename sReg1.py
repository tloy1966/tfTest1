import tflearn
import numpy as np

# Regression data
X = np.array([[3.3, 1.7],[4.4, 2.76],[5.5, 2.09],[6.71, 3.19],[6.93, 1.694]
,[4.168,1.573],[9.779,3.366],[6.182,2.596],[7.59,2.53],[2.167,1.221]
,[7.042,2.827],[10.791,3.465],[5.313,1.65],[7.997,2.904],[5.654,2.42]
,[9.27,2.94],[3.1,1.3]], dtype=float)
Y = np.array([[1.7], [2.76], [2.09], [3.19], [1.694]
,[1.573],[3.366],[2.596],[2.53] ,[1.221]
,[2.827],[3.465],[1.65] ,[2.904],[2.42]
,[2.94],[1.3]],dtype=float)
print(X)
print(Y)
# Linear Regression graph
input_ = tflearn.input_data(shape=[None,2])
#linear = tflearn.single_unit(input_)
linear = tflearn.fully_connected(input_,1)
#linear = tflearn.fully_connected(linear,1)


regression = tflearn.regression(linear, optimizer='sgd', loss='mean_square',
                                metric='R2', learning_rate=0.01)
m = tflearn.DNN(regression)
m.fit(X, Y, n_epoch=500, show_metric=True, snapshot_epoch=False)

print("\nRegression result:")
print("Y = " + str(m.get_weights(linear.W)) + "*X + " + str(m.get_weights(linear.b)))

print("\nTest prediction for x = [3.2,1], [3.3,2], [3.4,3]:")
print(m.predict([[3.2,1], [3.3,2], [3.4,3]]))

#Y = [[ 0.0404694 ] [ 0.81263494]]*X + [ 0.19824818]
#Test prediction for x = [3.2,1], [3.3,2], [3.4,3]:
#[[1.1403851509094238], [1.9570670127868652], [2.7737488746643066]]
#