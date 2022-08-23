import random
import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))


class NeuralNetwork:
    def __init__(self):
        self.input_layer_weight = (np.random.random((2, 6)) - 0.7) * 4
        self.hidden_layer_weight = (np.random.random((6, 1)) - 0.7) * 4

    def feed_forward(self, x):
        z1 = x.dot(self.input_layer_weight)
        output_layer_input = sigmoid(z1)

        if len(output_layer_input.shape) == 1:
            output_layer_input = np.reshape(output_layer_input, (1,6))

        z2 = output_layer_input.dot(self.hidden_layer_weight)
        output = sigmoid(z2)
        return output

class AI:
    def __init__(self):
        self.nn = [NeuralNetwork() for i in range(50)]
        self.ev = [0] * 50
        self.current_ai = 0
        self.generation = 1

    def jump(self, h_dist, v_dist):
        return self.nn[self.current_ai].feed_forward(np.array([h_dist, v_dist]))[0] > 0.5

    def game_over(self, evaluate):
        self.ev[self.current_ai] = evaluate
        self.current_ai += 1
        if self.current_ai == 50:
            self.current_ai = 0
            self.generation += 1
            top4 = []
            top4ev = []
            mx, mxi = 0, 0
            for i in range(50):
                if mx < self.ev[i]:
                    mx = self.ev[i]
                    mxi = i

            if mx != 0:
                top4.append(mxi)
                top4ev.append(mx)
                for i in range(50):
                    if max([x for x in self.ev if x not in top4ev] + [0]) == self.ev[i]:
                        mx = self.ev[i]
                        if mx == 0:
                            break
                        mxi = i
                        top4ev.append(mx)
                        top4.append(mxi)
                        break
                for i in range(50):
                    if max([x for x in self.ev if x not in top4ev] + [0]) == self.ev[i]:
                        mx = self.ev[i]
                        if mx == 0:
                            break
                        mxi = i
                        top4ev.append(mx)
                        top4.append(mxi)
                        break
                for i in range(50):
                    if max([x for x in self.ev if x not in top4ev] + [0]) == self.ev[i]:
                        mx = self.ev[i]
                        if mx == 0:
                            break
                        mxi = i
                        top4ev.append(mx)
                        top4.append(mxi)
                        break

            if len(top4) != 0:
                print(len(top4), self.ev[top4[0]])
            for i in range(50):
                ran = np.random.choice(3, 1, p=[0.8, 0.15, 0.05])

                if i in top4:
                    continue

                if ran[0] == 0:
                    # top4중에서 선택(selection)
                    if len(top4) == 0:
                        self.nn[i].input_layer_weight = (np.random.random((2, 6)) - 0.5) * 4
                        self.nn[i].hidden_layer_weight = (np.random.random((6, 1)) - 0.5) * 4
                        continue
                    self.nn[i] = self.nn[random.choice(top4)]
                elif ran[0] == 1:
                    if len(top4) < 2:
                        if len(top4) == 0:
                            self.nn[i].input_layer_weight = (np.random.random((2, 6)) - 0.5) * 4
                            self.nn[i].hidden_layer_weight = (np.random.random((6, 1)) - 0.5) * 4
                        else:
                            ran = np.random.randint(0, 2)
                            if ran == 0:
                                self.nn[i] = self.nn[random.choice(top4)]
                            else:
                                self.nn[i].input_layer_weight = (np.random.random((2, 6)) - 0.5) * 4
                                self.nn[i].hidden_layer_weight = (np.random.random((6, 1)) - 0.5) * 4
                        continue

                    # top4 중에서 둘을 뽑아서 교차 -> (crossover)
                    selected = np.random.choice(top4, 2, False)
                    for j in range(2):
                        for k in range(6):
                            self.nn[i].input_layer_weight[j][k] =\
                                random.choice([self.nn[selected[0]].input_layer_weight[j][k],
                                               self.nn[selected[1]].input_layer_weight[j][k]])
                    for j in range(6):
                        k = 0
                        self.nn[i].hidden_layer_weight[j][k] =\
                            random.choice([self.nn[selected[0]].hidden_layer_weight[j][k],
                                           self.nn[selected[1]].hidden_layer_weight[j][k]])
                else:
                    # 돌연변이(mutation)
                    if len(top4) == 0:
                        self.nn[i].input_layer_weight = (np.random.random((2, 6)) - 0.5) * 4
                        self.nn[i].hidden_layer_weight = (np.random.random((6, 1)) - 0.5) * 4
                    else:
                        for j in range(2):
                            for k in range(6):
                                self.nn[i].input_layer_weight[j][k] = \
                                    np.random.choice([self.nn[top4[0]].input_layer_weight[j][k],
                                                   (np.random.random_sample() - 0.5) * 4], p=[0.7, 0.3])
                        for j in range(6):
                            k = 0
                            self.nn[i].hidden_layer_weight[j][k] = \
                                np.random.choice([self.nn[top4[0]].hidden_layer_weight[j][k],
                                               (np.random.random_sample() - 0.5) * 4], p=[0.7, 0.3])
