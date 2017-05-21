import tflearn
import numpy as np

x = [];
y = [];
class regTest:
    def __init__(self, _x, _y):
        x = np.array(_x, dtype=float);
        y = np.array(_y, dtype=float);

def anaData(_x,_y):
    x = np.array(_x, dtype=float);
    y = np.array(_y, dtype=float);
    input_ = tflearn.input_data(shape=[None,2])
    #linear = tflearn.single_unit(input_)
    linear = tflearn.fully_connected(input_,1)
    #linear = tflearn.fully_connected(linear,1)


    regression = tflearn.regression(linear, optimizer='sgd', loss='mean_square',
                                    metric='R2', learning_rate=0.01)
    m = tflearn.DNN(regression)
    m.fit(x, y, n_epoch=500, show_metric=True, snapshot_epoch=False)

    print("\nRegression result:")
    print("Y = " + str(m.get_weights(linear.W)) + "*X + " + str(m.get_weights(linear.b)))
