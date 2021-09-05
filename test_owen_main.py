import time

import minimalmodbus
from flow_meter_class_py import owen, mx110_read_data, flow_meter_class
from threading import Thread

class driver_hard:
    def __init__(self):
        self.task_q = [{"mode": "none", "time": 1000, "dir": 1, "q": 0.54},
                       {"mode": "none", "time": 1000, "dir": 1, "q": 0.54},
                       {"mode": "none", "time": 1000, "dir": 1, "q": 0.54},
                       {"mode": "none", "time": 1000, "dir": 1, "q": 0.54},
                       {"mode": "none", "time": 1000, "dir": 1, "q": 0.54}
                       ]

        self.current_q   = [0, 0, 0, 0, 0]
        self.current_T_q = [0, 0, 0, 0, 0]
        self.current_T_mx = [0, 0, 0, 0, 0, 0, 0, 0]
        self.current_P   = [0, 0, 0, 0, 0, 0, 0, 0]
        self.error       = [0.02, 0.02, 0.01, 0.3, 0.3]
        self.ready_task  = [0, 0, 0, 0, 0]
        self.ready_owen  = [0, 0, 0, 0, 0]
        self.ready_pid   = [0, 0, 0, 0, 0]
        self.task_is_new = [0, 0, 0, 0, 0]

        self.mx_T = mx110_read_data(debug=True)
        self.mx_P = mx110_read_data("COM7",16)
        self.ow = owen("COM7",1)
        self.q1 = flow_meter_class("COM7",2,register_flow=167,register_temp=171)
        self.q2 = flow_meter_class("COM7",3,register_flow=167,register_temp=171)
        self.q3 = flow_meter_class("COM7",4,register_flow=167,register_temp=171)
        self.q4 = flow_meter_class("COM7",5,register_flow=0,register_temp=171,is_no_air= True, debug=False)
        self.q5 = flow_meter_class(debug=True)


    def _read_all_data_dev(self):

        x1 = self.q1.read_temp_and_flow()
        x2 = self.q2.read_temp_and_flow()
        x3 = self.q3.read_temp_and_flow()
        x4 = self.q4.read_temp_and_flow()
        x5 = self.q5.read_temp_and_flow()
        self.current_q = [x1[0], x2[0], x3[0], x4[0], x5[0]]
        self.current_T_q = [x1[1], x2[1], x3[1], x4[1], x5[1]]
        self.current_T_mx = self.mx_T.read_data()
        self.current_P = self.mx_P.read_data()
        self.ready_owen = self.ow.read_ready()



    def loop_hard(self):
        while 1 == 1:
            self._rule_device()
            self._read_all_data_dev()
            self._is_ready_task()
            print("i here")
            #time.sleep(0.5)

    def _rule_device(self):
        for i in range(1,4):
            if self.task_is_new[i-1] == 1:
                if self.task_q[i-1]["mode"] == "time":
                    if self.task_q[i-1]["dir"] == 1:
                        self.ow.open_q(i, self.task_q[i-1]["time"])
                    if self.task_q[i-1]["dir"] == 2:
                        self.ow.open_all_q(i)
                    if self.task_q[i-1]["dir"] == 3:
                        self.ow.close_q(i, self.task_q[0]["time"])
                    if self.task_q[i-1]["dir"] == 4:
                        self.ow.close_all_q(i)
                    self.task_is_new[i - 1] = 0
                    self.ready_task[i - 1] = 0
            if self.task_q[i-1]["mode"] == "q":
                self._my_pid(i,self.task_q[i-1]["q"])
                self.ready_task[i-1] = 0

    def _is_ready_task(self):
        self.ready_owen = self.ow.read_ready()
        for i in range(1,5):
            if self.task_q[i-1]["mode"] == "time":
                if self.ready_owen[i-1] == 1:
                    self.ready_task[i-1] = 1
            if self.task_q[i - 1]["mode"] == "q":
                if self.ready_pid[i-1] == 1:
                    self.ready_task[i-1] = 1



    def _my_pid(self, num_q, task):
        self.ready_owen = self.ow.read_ready()

        if self.ready_owen[num_q-1] == 1:
            self.ready_pid[num_q - 1] = 0
            if self.current_q[num_q-1] > task + self.error[num_q-1]:
                self.ow.close_q(num_q, 500)
            elif self.current_q[num_q-1] < task - self.error[num_q-1]:
                self.ow.open_q(num_q, 500)
            else:
                self.ready_pid[num_q - 1] = 1


    def get_all_data_to_ui(self):
        return [self.current_q, self.current_T_q,
                self.current_P, self.current_T_mx,
                self.task_q, self.ready_task]

    def set_new_task(self, mode ='none' , time = 500, q = 0, dir = 0, num_q = 0):
        if self.task_q[num_q - 1]["mode"] == mode:
            if self.task_q[num_q - 1]["q"] == q:
                if self.task_q[num_q - 1]["dir"] == dir:
                    if self.task_q[num_q - 1]["time"] == time:
                        self.task_is_new[num_q-1] = 0
                        return
        self.task_is_new[num_q-1] = 1

        if mode == 'time':
            self.task_q[num_q-1] = {"mode": "time", "time": time, "dir": dir, "q": q}
        if mode == 'q':
            self.task_q[num_q - 1] = {"mode": "q", "time": time, "dir": dir, "q": q}
    def set_new_err(self,num,err):
        self.error[num-1] = err
if __name__ == '__main__':
    '''
    ow = owen("COM11",1)
    ow.open_q(1, 2000  )
    #time.sleep(5)
    ow.close_q(1,2000)
    '''
    x = driver_hard()
    tr = Thread(target=x.loop_hard)
    tr.start()
    while 1==1:
        print(x.get_all_data_to_ui())
        time.sleep(2)