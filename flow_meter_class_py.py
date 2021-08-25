import minimalmodbus
import time
from random import randint
#import matplotlib.pyplot as plt
from collections import deque
import datetime
from  random import randint
class owen:
    def __init__(self, port=0, slave_id_modbus=0, baundrate=9600, stopbit=1, bytesize=8,
                 timeout=1, debug = False):
        self.port = port
        self.slave_id_modbus = slave_id_modbus
        self.baundrate = baundrate
        self.stopbit = stopbit
        self.bytesize = bytesize
        self.timeout = timeout

        self.debug = debug

        self.ready_q =[0,0,0,0,0]
        self.close_or = []
        self.open_or = []

        self.time = 3000

        self.register_time = 2
        self.register_start_q =[0]
        self.register_dir_q = [1]
        self.register_ready_q = [3]

        if self.debug == False:
            self.instr = minimalmodbus.Instrument(self.port, self.slave_id_modbus, minimalmodbus.MODE_RTU)
            self.instr.serial.baudrate = self.baundrate  # Baud
            self.instr.serial.bytesize = self.bytesize
            self.instr.serial.stopbits = self.stopbit
            self.instr.serial.timeout = self.timeout
            self.instr.mode = minimalmodbus.MODE_RTU
            self.instr.clear_buffers_before_each_transaction = True
        else:
            print("debug start")

    def read_register(self,addr_reg):
        check = 0
        while check == 0:
            check = 1
            try:
                data = self.instr.read_register(addr_reg)
            except:
                check = 0
        return data

    def write_register(self, adrr, valume):
        check = 0
        while check == 0:
            check = 1
            try:
                self.instr.write_register(adrr, valume)
            except:
                check = 0

    def open_q(self, num_q, time):
        if self.debug == False:
            self.write_register(self.register_time, time)
            self.write_register(self.register_dir_q[num_q-1],1)
            self.write_register(self.register_start_q[num_q-1],1)
            self.ready_q[num_q-1] = 0
        else:
            self.ready_q[num_q - 1] = 0

    def close_q(self, num_q, time):
        if self.debug == False:
            self.write_register(self.register_time, time)
            self.write_register(self.register_dir_q[num_q - 1], 3)
            self.write_register(self.register_start_q[num_q - 1], 1)
            self.ready_q[num_q - 1] = 0
        else:
            self.ready_q[num_q - 1] = 0

    def open_all_q(self, num_q):
        if self.debug == False:
            self.write_register(self.register_dir_q[num_q - 1], 2)
            self.write_register(self.register_start_q[num_q - 1], 1)
            self.ready_q[num_q - 1] = 0
        else:
            self.ready_q[num_q - 1] = 0

    def close_all_q(self, num_q):
        if self.debug == False:
            self.write_register(self.register_dir_q[num_q - 1], 4)
            self.write_register(self.register_start_q[num_q - 1], 1)
            self.ready_q[num_q - 1] = 0
        else:
            self.ready_q[num_q - 1] = 0

    def read_ready(self):
        if self.debug == False:
            self.ready_q[0] = self.read_register(self.register_ready_q[0])
            self.ready_q[1] = self.read_register(self.register_ready_q[1])
            self.ready_q[2] = self.read_register(self.register_ready_q[2])
            self.ready_q[3] = self.read_register(self.register_ready_q[3])
            self.ready_q[4] = self.read_register(self.register_ready_q[4])
            return self.ready_q
        else:
            return[1,1,1,1,1]


class flow_meter_class:
    def __init__(self, port = 0, slave_id_modbus = 0, baundrate = 9600, stopbit = 1, bytesize = 8,
                 timeout = 1, register_flow = 0, register_temp = 0, debug = False, default_valume = 4):
        self.port = port
        self.slave_id_modbus = slave_id_modbus
        self.baundrate = baundrate
        self.stopbit = stopbit
        self.bytesize = bytesize
        self.timeout = timeout
        self.register_flow = register_flow
        self.register_temp = register_temp

        self.debug = debug
        self.counter_one = 0
        self.counter_zero = 0
        self.default_valume = default_valume

        if self.debug == False:
            self.instr = minimalmodbus.Instrument(self.port,self.slave_id_modbus,minimalmodbus.MODE_RTU)
            self.instr.serial.baudrate = self.baundrate  # Baud
            self.instr.serial.bytesize = self.bytesize
            self.instr.serial.stopbits = self.stopbit
            self.instr.serial.timeout = self.timeout
            self.instr.mode = minimalmodbus.MODE_RTU
            self.instr.clear_buffers_before_each_transaction = True
        else:
            print("debug init")


        self.flow = 0
        self.temp = 0

    def read_temp_and_flow(self):
        if self.debug == False:
            try:
                self.flow = self.instr.read_float(self.register_flow, 4, 2)
            except:
                self.flow = -1

            try:
                self.temp = self.instr.read_float(self.register_temp, 4, 2)
            except:
                self.temp = -1
        else:
            if self.counter_one < 30:
                self.flow = self.default_valume + randint((-1) * self.default_valume, self.default_valume)/10
                self.counter_one += 1
            else:
                if self.counter_zero < 4:
                    self.flow = 0
                    self.counter_zero += 1
                else:
                    self.counter_zero = 0
                    self.counter_one = 0


        return [self.flow, self.temp]


class mx110_read_data:
    def __init__(self, port = 0, slave_id_modbus = 0, baundrate = 9600, stopbit = 1, bytesize = 8,
                 timeout = 1, debug = False, default_valume = 4):
        self.port = port
        self.slave_id_modbus = slave_id_modbus
        self.baundrate = baundrate
        self.stopbit = stopbit
        self.bytesize = bytesize
        self.timeout = timeout

        self.debug = debug
        self.default_valume = default_valume

        self.data_1 = 0
        self.data_2 = 0
        self.data_3 = 0
        self.data_4 = 0
        self.data_5 = 0
        self.data_6 = 0
        self.data_7 = 0
        self.data_8 = 0

        self.register_1 = 4
        self.register_2 = 10
        self.register_3 = 16
        self.register_4 = 22
        self.register_5 = 28
        self.register_6 = 34
        self.register_7 = 40
        self.register_8 = 46

        if self.debug == False:
            self.instr = minimalmodbus.Instrument(self.port,self.slave_id_modbus,minimalmodbus.MODE_RTU)
            self.instr.serial.baudrate = self.baundrate  # Baud
            self.instr.serial.bytesize = self.bytesize
            self.instr.serial.stopbits = self.stopbit
            self.instr.serial.timeout = self.timeout
            self.instr.mode = minimalmodbus.MODE_RTU
            self.instr.clear_buffers_before_each_transaction = True
        else:
            print("debug init")

    def read_data(self):#new function
        if self.debug == False:
            try:
                self.data_1 = self.instr.read_float(self.register_1, 3, 2)
            except:
                self.data_1 = -1
            try:
                self.data_2 = self.instr.read_float(self.register_2, 3, 2)
            except:
                self.data_2 = -1
            try:
                self.data_3 = self.instr.read_float(self.register_3, 3, 2)
            except:
                self.data_3 = -1
            try:
                self.data_4 = self.instr.read_float(self.register_4, 3, 2)
            except:
                self.data_4 = -1
            try:
                self.data_5 = self.instr.read_float(self.register_5, 3, 2)
            except:
                self.data_5 = -1
            try:
                self.data_6 = self.instr.read_float(self.register_6, 3, 2)
            except:
                self.data_6 = -1
            try:
                self.data_7 = self.instr.read_float(self.register_7, 3, 2)
            except:
                self.data_7 = -1
            try:
                self.data_8 = self.instr.read_float(self.register_8, 3, 2)
            except:
                self.data_8 = -1

        else:
            self.data_1 = self.default_valume + randint((-1) * self.default_valume, self.default_valume)/10
            self.data_2 = self.default_valume + randint((-1) * self.default_valume, self.default_valume) / 10
            self.data_3 = self.default_valume + randint((-1) * self.default_valume, self.default_valume) / 10
            self.data_4 = self.default_valume + randint((-1) * self.default_valume, self.default_valume) / 10
            self.data_5 = self.default_valume + randint((-1) * self.default_valume, self.default_valume) / 10
            self.data_6 = self.default_valume + randint((-1) * self.default_valume, self.default_valume) / 10
            self.data_7 = self.default_valume + randint((-1) * self.default_valume, self.default_valume) / 10
            self.data_8 = self.default_valume + randint((-1) * self.default_valume, self.default_valume) / 10

        return [self.data_1, self.data_2, self.data_3, self.data_4, self.data_5, self.data_6, self.data_7, self.data_8]



class filter_data: # memory!!!!!!
    def __init__(self, N):
        self.N = N
        self.y1 = 0
        self.list_data = []
        for i in range(self.N):
            self.list_data.append(0.001)

    def sum_n(self):
        self.y1 = 0
        for i in range(1,self.N + 1):
            self.y1 += self.list_data[-i]
            print("info",i,"fff", self.list_data[-i])
        return self.y1

    def filter(self, data):
        self.list_data.append(data)
        self.y = self.sum_n()/(self.N)
        return self.y


class class_telling_owen:
    def __init__(self, port = 0, slave_id_modbus = 0, baundrate = 9600, stopbit = 1, bytesize = 8,
                 timeout = 1, debug = False, default_valume = 4):
        self.port = port
        self.slave_id_modbus = slave_id_modbus
        self.baundrate = baundrate
        self.stopbit = stopbit
        self.bytesize = bytesize
        self.timeout = timeout

        self.debug = debug
        self.default_valume = default_valume

        #q1
        self.open_or_q1 = False
        self.close_or_q1 = False

        # q2
        self.open_or_q2 = False
        self.close_or_q2 = False

        # q3
        self.open_or_q3 = False
        self.close_or_q3 = False

        # q4
        self.open_or_q4 = False
        self.close_or_q5 = False

        # q5
        self.open_or_q5 = False
        self.close_or_q5 = False



        if self.debug == False:
            self.instr = minimalmodbus.Instrument(self.port,self.slave_id_modbus,minimalmodbus.MODE_RTU)
            self.instr.serial.baudrate = self.baundrate  # Baud
            self.instr.serial.bytesize = self.bytesize
            self.instr.serial.stopbits = self.stopbit
            self.instr.serial.timeout = self.timeout
            self.instr.mode = minimalmodbus.MODE_RTU
            self.instr.clear_buffers_before_each_transaction = True
        else:
            print("debug init")
        pass

    def move_flow_meter(self, dir = 0, sec = 0, device = 0):
        # dir = +1,0,-1
        # sec if(0) none
        # device 1,2,3,4,5
        pass

    def check_correct_task(self):
        return

    def close(self, device = 0):
        pass

    def open(self, device = 0):
        pass
    def status_busy(self):
        return False




class hard_loop_class:
    def __init__(self):
        self.current_rate_q1 = 0
        self.current_rate_q2 = 0
        self.current_rate_q3 = 0
        self.current_rate_q4 = 0
        self.current_rate_q5 = 0

        self.current_Temp1 = 0
        self.current_Temp2 = 0
        self.current_Temp3 = 0
        self.current_Temp4 = 0
        self.current_Temp5 = 0
        self.current_Temp6 = 0
        self.current_Temp7 = 0
        self.current_Temp8 = 0

        self.current_Temp_q1 = 0
        self.current_Temp_q2 = 0
        self.current_Temp_q3 = 0
        self.current_Temp_q4 = 0
        self.current_Temp_q5 = 0

        self.current_P1 = 0
        self.current_P2 = 0
        self.current_P3 = 0
        self.current_P4 = 0
        self.current_P5 = 0
        self.current_P6 = 0
        self.current_P7 = 0
        self.current_P8 = 0

        self.input_cmd_deque = deque()
        self.busy_cmd = False
        self.current_numeric_cmd = 0
        self.cmd_q1 = 0
        self.cmd_q2 = 0
        self.cmd_q3 = 0
        self.cmd_q4 = 0
        self.cmd_q5 = 0

        self.meter_q1 = flow_meter_class()
        self.meter_q2 = flow_meter_class()
        self.meter_q3 = flow_meter_class()
        self.meter_q4 = flow_meter_class()
        self.meter_q5 = flow_meter_class()

        self.mx110_temp = mx110_read_data()
        self.mx110_pres = mx110_read_data()
        self.owen_device = class_telling_owen()


        list_delete =[]

    def read_all_data(self):
        list_delete = self.meter_q1.read_temp_and_flow()
        self.current_rate_q1 = list_delete[0]
        self.current_Temp_q1 = list_delete[1]

        list_delete = self.meter_q2.read_temp_and_flow()
        self.current_rate_q2 = list_delete[0]
        self.current_Temp_q2 = list_delete[1]

        list_delete = self.meter_q3.read_temp_and_flow()
        self.current_rate_q3 = list_delete[0]
        self.current_Temp_q3 = list_delete[1]

        list_delete = self.mx110_temp()
        self.current_Temp1 = list_delete[0]
        self.current_Temp2 = list_delete[1]
        self.current_Temp3 = list_delete[2]
        self.current_Temp4 = list_delete[3]
        self.current_Temp5 = list_delete[4]
        self.current_Temp6 = list_delete[5]
        self.current_Temp7 = list_delete[6]
        self.current_Temp8 = list_delete[7]

        list_delete = self.mx110_pres()
        self.current_P1 = list_delete[0]
        self.current_P2 = list_delete[1]
        self.current_P3 = list_delete[2]
        self.current_P4 = list_delete[3]
        self.current_P5 = list_delete[4]
        self.current_P6 = list_delete[5]
        self.current_P7 = list_delete[6]
        self.current_P8 = list_delete[7]


    def loop_main(self):
        self.read_all_data()
        if self.owen_device.status_busy() == False:
            pass

    def get_data(self):
        pass








if __name__ == '__main__':
    '''
    q = flow_meter_class(debug = True, default_valume = 5)
    mx110 = mx110_read_data(debug= True, default_valume= 5)
    filter = filter_data(10)
    list1 = []
    list2 =[]
    for i in range(1000):
        print(mx110.read_data())
        flow = q.read_temp_and_flow()
        list1.append(flow[0])
        list2.append(filter.filter(flow[0]))
    plt.plot(list1)
    plt.plot(list2)
    plt.show()
    '''
    q1 = flow_meter_class("COM5",1,9600,1,8,1,167,171)
    T1 = mx110_read_data("COM5", 16, 9600, 1, 8, 1, default_valume=4)
    while 1 == 1:
        #data = q1.read_temp_and_flow()
        #print(data)
        data = T1.read_data()
        print(data)
        time.sleep(1)
'''
from ui_20_08_2021 import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

if __name__ == "__main__":
    import sys
    app =QtWidgets.QApplication(sys.argv)
    main_wind = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(main_wind)
    main_wind.show()
    sys.exit(app.exec_())
    '''