import numpy as np

#This dataset is the current status at the beginning of each game for the  rst 4 games in a season.
#toes = current number of toes
#wlrec = current games won (percent) nfans = fan count (in millions)
toes = np.array([8.5, 9.5, 9.9, 9.0])
wlrec = np.array([0.65, 0.8, 0.8, 0.9])
nfans = np.array([1.2, 1.3, 0.5, 1.0])

#toes %win #fans
ih_wgt = np.array([[0.1, 0.2, -0.1], #hid[0]
                  [-0.1, 0.1, 0.9], #hid[1]
                  [0.1, 0.4, 0.1]]).T #hid[2]

# hid[0] hid[1] hid[2]
hp_wgt = np.array([[0.3, 1.1, -0.3], #hurt?
                  [0.1, 0.2, 0.0], #win?
                  [0.0, 1.3, 0.1]]).T #sad?

input = np.array([toes[0], wlrec[0], nfans[0]])
weights = [ih_wgt, hp_wgt]

def neural_network(input, weights):
    hid = input.dot(weights[0])
    pred = hid.dot(weights[1])
    return pred

pred = neural_network(input, weights)
print(pred)
