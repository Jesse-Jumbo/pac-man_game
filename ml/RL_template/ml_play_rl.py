import numpy as np
from .Qtable import QLearningTable


class MLPlay:
    def __init__(self):
        self.car_pos_x = 20
        self.p_car_pos_x = 20

        self.car_pos_y = 160
        self.reward = 0
        self.action = 0
        # 可自行定義有種action
        self.action_space = ["SPEED", "BRAKE", "MOVE_LEFT", "MOVE_RIGHT", "NONE"]
        # self.action_space = ["SPEED", "BRAKE", "NONE"]
        self.n_actions = len(self.action_space)
        self.RL = QLearningTable(actions=list(range(self.n_actions)))
        self.observation = 0
        self.status = "ALIVE"
        # 可自行定義state
        self.state = ""
        self.state_ = ""
        self.distance = 0
        self.prev_distance = 0
        print("Initial ml script")

    def update(self, scene_info: dict):
        """
        Generate the command according to the received scene information
        """
        '''
        if scene_info["status"] == "GAME_OVER":
            return "RESET"
        '''

        self.car_pos_x = scene_info["x"]
        self.car_pos_y = scene_info["y"]
        self.distance = scene_info["distance"]

        def check_grid():
            # 狀態為蘇老師說的，直線速度與左右車道的結合
            self.observation = 0

            # 走到最上貨是最下車到是要避免的，因此給不同的狀態
            if self.car_pos_y <= 140:  # lane 1
                self.observation = 1
                self.state_ = '撞到上面'
                return

            if self.car_pos_y >= 490:  # lane 9
                self.observation = 1
                self.state_ = '撞到下面'
                return

                # 檢查前後是否有車以及距離

            for car in scene_info["all_cars_pos"]:
                # 與我在近乎同一個車道 abs(car[1]-self.car_pos_y) < 30
                # 在我前方 car[0] > self.car_pos_x
                # 與我的距離小於180  car[0] - self.car_pos_x < 180
                if abs(car[1] - self.car_pos_y) < 30 and car[0] > self.car_pos_x and car[0] - self.car_pos_x < 180:
                    self.observation = 1
                    self.state_ = "該減速"
                    return
                # 與我在近乎同一個車道 abs(car[1]-self.car_pos_y) < 30
                # 在我後方 car[0] < self.car_pos_x
                # 與我的距離小於120  car[0] - self.car_pos_x > -120
                elif abs(car[1] - self.car_pos_y) < 30 and car[0] < self.car_pos_x and car[0] - self.car_pos_x > -120:
                    self.observation = 1
                    self.state_ = "該加速"
                    return
                else:
                    pass

            # 不是上述條件則狀態維持在不動
            self.observation = 1
            self.state_ = "不動"
            return

        def check_nearby(state):
            result_state = state
            # print("a")

            for car in scene_info["all_cars_pos"]:
                bias = 20
                if (self.car_pos_x - bias - 60 > car[0] > self.car_pos_x + bias + 60):
                    if (car[1] > self.car_pos_y - 30 - bias):
                        result_state += "左邊有車;"
                    if (car[1] < self.car_pos_y + 30 + bias):
                        result_state += "右邊有車;"

            return result_state + ";"

        def step(self, state):
            # reward function
            self.reward = 0
            if self.observation != 0:
                # 以下各個狀態的reward就是需要各為自己調整了!
                if state == '撞到上面' or state == '撞到下面':
                    self.reward = -4000

                if state == "該減速":
                    self.reward = -250

                if state == "該加速":
                    self.reward = -500

                if state == "不動":
                    self.reward = 5000
                    # 鼓勵往前走
                    if self.distance > self.prev_distance:
                        self.reward += 35000
                        # elif self.prev_distance > self.distance:
                    #     self.reward -= 100 + (self.prev_distance - self.distance) * 100

                if state.find("左") > -1:
                    self.reward -= 500

                if state.find("右") > -1:
                    self.reward -= 500

            if scene_info["status"] == "GAME_OVER":
                self.reward = -5000
            if scene_info["status"] == "GAME_PASS":
                self.reward = 5000

            # print(state + " reward:" + str(self.reward), end=' ' )
            return self.reward

        check_grid()
        self.state_ = check_nearby(self.state_)

        self.reward = step(self, self.state_)
        action = self.RL.choose_action(str(self.state_))
        # Disable following line if dont want to update model, just use it
        self.RL.learn(str(self.state), self.action, self.reward, str(self.state_))
        self.action = action
        self.state = self.state_

        self.prev_distance = self.distance
        self.p_car_pos_x = self.p_car_pos_x

        if scene_info["status"] != "GAME_ALIVE" and scene_info["status"] != "ALIVE":
            return "RESET"
        return self.action_space[action]

    def reset(self):
        """
        Reset the status
        """
        print(self.RL.q_table)
        # Disable following line if don't save model
        self.RL.q_table.to_pickle('games/racing_car/log/qlearning.pickle')
        # self.RL.plot_cost()
        print("reset ml script")

        pass
#
# class MLPlay:
#     def __init__(self):
#         self.car_pos = (20, 160)
#         self.cars_pos = []
#         self.car_lane = self.car_pos[1] // 50  # lanes 1 ~ 9
#         self.step = 0
#         self.reward = 0
#         self.action = 0
#         # 可自行定義有種action
#         self.action_space = ["SPEED", "BRAKE"]
#         self.n_actions = len(self.action_space)
#         self.n_features = 2
#         self.RL = QLearningTable(actions=list(range(self.n_actions)))
#         self.observation = 0
#         self.status = "ALIVE"
#         # 可自行定義state
#         self.state = [self.observation, ]
#         self.state_ = [self.observation, ]
#
#         print("Initial ml script")
#
#
#     # 16 grid relative position  // 此16宮格可作為賽車相對位置之參考
#
# #      |    |    |    |    |    |
# #      |  1 |  2 |  3 |  4 |  5 |
# #      |    |    |    |    |    |
# #      |  6 |  c |  8 |  9 | 10 |
# #      |    |    |    |    |    |
# #      | 11 | 12 | 13 | 14 | 15 |
# #      |    |    |    |    |    |
#
#
#     def update(self, scene_info: dict):
#         """
#         Generate the command according to the received scene information
#         """
#         if scene_info["status"] == "GAME_OVER":
#             return "RESET"
#
#
#         def check_grid():
#             self.observation = 0
#
#             '''
#             observation可以用來記錄車子狀態, 如下
#
#             # car position
#             x = scene_info["x"]
#             y = scene_info["y"]
#
#             if y <= 140: # lane 1
#                 self.observation = 1
#             if y >= 490: # lane 9
#                 self.observation = 2
#             '''
#
#
#         def step(self, state):
#             # reward function
#             self.reward = 0
#
#             '''
#             you can design your reward function here !
#             '''
#
#             return self.reward
#
#
#         check_grid()
#
#         self.reward = step(self, self.state_)
#         action = self.RL.choose_action(str(self.state))
#         self.RL.learn(str(self.state), self.action, self.reward, str(self.state_))
#         self.action = action
#         self.state = self.state_
#
#         if scene_info["status"] != "GAME_ALIVE" and scene_info["status"] != "ALIVE":
#             return "RESET"
#
#         if scene_info.__contains__("coin"):
#             self.coin_pos = scene_info["coin"]
#
#         return self.action_space[action]
#
#
#     def reset(self):
#         """
#         Reset the status
#         """
#         print(self.RL.q_table)
#         self.RL.q_table.to_pickle('games/RacingCar/log/qlearning.pickle')
#     #    self.RL.plot_cost()
#         print("reset ml script")
#
#         pass
