import os
import warnings
import pandas as pd
import pandapower as pp
from Helper import Notification, CaseFileReader, CaseFileEditor


class UserGridCreator():
    def __init__(self, net, Grid_Elements):
        self.net = net
        self.bus_number = None
        self.Grid_Elements = Grid_Elements


    def bus(self):
        ask_bus = Notification.user_bus_interface(self)     
        if ask_bus == "1":
            self.bus_number = Notification.user_bus_number(self)
            for number in range(self.bus_number):
                bus_name, vnkv = Notification.user_bus_detail(self, number)
                globals()["bus" + str(number)] = pp.create_bus(self.net, vn_kv = vnkv, name = bus_name )
                self.Grid_Elements["buses"].append(bus_name)
                Notification.user_bus_creation_confirm(self, self.net, bus_name)
        else:
            pass


    def ext_grid(self):
        ask_ext_grid = Notification.user_ext_grid_interface(self)
        if ask_ext_grid == "1":
            ext_grid_numbers = Notification.user_ext_grid_number(self)
            for grid in range(ext_grid_numbers):
                ext_grid_name, ext_grid_vmpu = Notification.user_ext_grid_detail(self, grid)
                ext_grid_bus = Notification.user_ext_grid_bus(self, self.net, ext_grid_name)
                for counter in range(len(self.Grid_Elements["buses"])):
                    if ext_grid_bus in self.Grid_Elements["buses"][counter]:
                        globals()["ext_grid" + str(grid)] = pp.create_ext_grid(self.net, bus = globals()["bus" + str(counter)] , vm_pu = ext_grid_vmpu, name = ext_grid_name)
                        Notification.user_ext_grid_creation_confirm(self, self.net)

                    else:
                        pass
        else:
            pass
        
        
    def load(self):
        ask_load = Notification.user_load_interface(self)
        if ask_load == "1":
            load_number = Notification.user_load_number(self)
            for number in range(load_number):
                load_name, load_pmw, load_qkvar = Notification.user_load_detail(self, number)
                load_bus = Notification.user_load_bus(self, self.net, load_name) 
                for counter in range(len(self.Grid_Elements["buses"])):
                    if load_bus in self.Grid_Elements["buses"][counter]:
                        globals()["Load" + str(number)] = pp.create_load(self.net, bus = globals()["bus" + str(counter)], q_kvar = load_qkvar, p_mw = load_pmw, name = load_name)  
                        Notification.user_load_creation_confirm(self, self.net)
        else:
            pass
    

    def trasformer(self):
        ask_transformer = Notification.user_transform_interface(self)
        if ask_transformer == "1":
            trafo_number = Notification.user_transformer_number(self)
            for number in range(trafo_number):
                trafo_name, trafo_hvbus, trafo_lvbus, trafo_std = Notification.user_trafo_detail(self, self.net, number)
                for hv in range(len(self.Grid_Elements["buses"])):
                    if trafo_hvbus in self.Grid_Elements["buses"][hv]:
                        h_bus = globals()["bus" + str(hv)]   
                for lv in range(len(self.Grid_Elements["buses"])):
                    if trafo_lvbus in self.Grid_Elements["buses"][lv]:
                        l_bus = globals()["bus" + str(lv)]                    
                globals()["trafo" + str(number)] = pp.create_transformer(self.net, hv_bus = h_bus, lv_bus = l_bus, std_type = trafo_std, name = trafo_name)
                Notification.user_trafo_creation_confirm(self, self.net)     
        else:
            pass

        
    def line(self):
        ask_line = Notification.user_line_interface(self)
        if ask_line == "1":
            line_number = Notification.user_line_number(self)
            for number in range(line_number):
                line_name, source_bus, destination_bus, line_std, line_length = Notification.user_line_detail(self, self.net, number)
                for source in range(len(self.Grid_Elements["buses"])):
                    if source_bus in self.Grid_Elements["buses"][source]:
                        s_bus = globals()["bus" + str(source)]
                for destination in range(len(self.Grid_Elements["buses"])):
                    if destination_bus in self.Grid_Elements["buses"][destination]:
                        d_bus = globals()["bus" + str(destination)]                    
                globals()["line" + str(number)] = pp.create_line(self.net, from_bus = s_bus, to_bus = d_bus, length_km = line_length, std_type = line_std, name = line_name)
                Notification.user_line_creation_confirm(self, self.net)     
        else:
            pass  


    def switch(self):
        ask_switch = Notification.user_switch_interface(self)
        if ask_switch == "1":
            switch_number = Notification.user_switch_number(self)
            for number in range(switch_number):
                switch_name, switch_bus, elem_number, elem_type, switch_status = Notification.user_line_detail(self, self.net, number)
                for counter in range(len(self.Grid_Elements["buses"])):
                    if switch_bus in self.Grid_Elements["buses"][counter]:
                        s_bus = globals()["bus" + str(counter)]
                if switch_status == 1:
                    switch_closed = True
                else:
                    switch_closed = False
                globals()["switch" + str(number)] = pp.create_switch(self.net ,bus = s_bus, element = elem_number, et = elem_type, closed = switch_closed, name = switch_name)
                Notification.user_switch_creation_confirm(self, self.net)     
        else:
            pass  


    def storage(self):
        ask_storage = Notification.user_storage_interface(self)
        if ask_storage == "1":
            storage_number = Notification.user_storage_number(self)
            for number in range(storage_number):
                storage_name, storage_bus, pkw, max_ekw = Notification.user_storage_detail(self, self.net, number)
                for counter in range(len(self.Grid_Elements["buses"])):
                    if storage_bus in self.Grid_Elements["buses"][counter]:
                        s_bus = globals()["bus" + str(counter)]
                globals()["storage" + str(number)] = pp.create_storage(self.net, bus = s_bus, p_kw = pkw, max_e_kwh = max_ekw, name = storage_name) 
                Notification.user_storage_creation_confirm(self, self.net)     
        else:
            pass  




#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#
#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~# 
#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~# 




class CaseFileProcessor():
    
    def __init__(self, net):
        self.net = net


    def MATPower_processor(self):
        ask_edit = Notification.file_edit(self)
        if ask_edit == "1":
            pp.runpp(self.net)
            print(self.net)   
        elif ask_edit == "2":
            CaseFileEditor(self.net)
            grid_elements = CaseFileEditor.grid_element_detector(self)
            elem_number = Notification.element_edit_select(self, grid_elements)
            for elem in range(elem_number):
                elem_name = Notification.element_ask(self, elem)
                self.net = CaseFileEditor.grid_elements_analyzer_editor(self, self.net, elem_name)
                pp.runpp(self.net)
                print(self.net)  
        else:
            Notification.case_file_error(self)


    def PyPower_processor(self):
        ask_edit = Notification.file_edit(self)
        if ask_edit == "1":
            pp.runpp(self.net)
            print(self.net)   
        elif ask_edit == "2":
            CaseFileEditor(self.net)
            grid_elements = CaseFileEditor.grid_element_detector(self)
            elem_number = Notification.element_edit_select(self, grid_elements)
            for elem in range(elem_number):
                elem_name = Notification.element_ask(self, elem)
                self.net = CaseFileEditor.grid_elements_analyzer_editor(self, self.net, elem_name)                
                pp.runpp(self.net)
                print(self.net)              
        else:
            Notification.case_file_error(self)


    def Pickle_processor(self):
        ask_edit = Notification.file_edit(self)
        if ask_edit == "1":
            pp.runpp(self.net)
            print(self.net)   
        elif ask_edit == "2":
            CaseFileEditor(self.net)
            grid_elements = CaseFileEditor.grid_element_detector(self)
            elem_number = Notification.element_edit_select(self, grid_elements)
            for elem in range(elem_number):
                elem_name = Notification.element_ask(self, elem)
                self.net = CaseFileEditor.grid_elements_analyzer_editor(self, self.net, elem_name)                
                pp.runpp(self.net)
                print(self.net)              
        else:
            Notification.case_file_error(self)

            
    def JSON_processor(self):
        ask_edit = Notification.file_edit(self)
        if ask_edit == "1":
            pp.runpp(self.net)
            print(self.net)   
        elif ask_edit == "2":
            CaseFileEditor(self.net)
            grid_elements = CaseFileEditor.grid_element_detector(self)
            elem_number = Notification.element_edit_select(self, grid_elements)
            for elem in range(elem_number):
                elem_name = Notification.element_ask(self, elem)
                self.net = CaseFileEditor.grid_elements_analyzer_editor(self, self.net, elem_name)                
                pp.runpp(self.net)
                print(self.net)              
        else:
            Notification.case_file_error(self)
       


#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#
#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~# 
#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#        



if __name__ == "__main__":
    Grid_Elements = {"buses" : []}
    
    interface = Notification.initial_step(Notification)
    if interface == "1":
        net_name = Notification.net_name(Notification)
        net = pp.create_empty_network(name = net_name)
        Notification.grid_creation_confirm(Notification, net)
        Main_Grid = UserGridCreator(net, Grid_Elements)
        Main_Grid.bus()
        Main_Grid.ext_grid()
        Main_Grid.load()
        Main_Grid.trasformer()        
        Main_Grid.line()
        Main_Grid.switch()
        Main_Grid.storage()

    elif interface == "2":
        net = CaseFileReader.MATPower_reader(CaseFileReader)
        Notification.case_file_import_confirm(Notification)
        Main_Process = CaseFileProcessor(net)
        Main_Process.MATPower_processor()
        
    elif interface == "3":
        net = CaseFileReader.PyPower_reader(CaseFileReader)
        Notification.case_file_import_confirm(Notification)
        Main_Process = CaseFileProcessor(net)
        Main_Process.PyPower_processor()
        
    elif interface == "4":
        net = CaseFileReader.Pickle_reader(CaseFileReader)
        Notification.case_file_import_confirm(Notification)
        Main_Process = CaseFileProcessor(net)
        Main_Process.Pickle_processor()       

    elif interface == "5":
        net = CaseFileReader.JSON_reader(CaseFileReader)
        Notification.case_file_import_confirm(Notification)
        Main_Process = CaseFileProcessor(net)
        Main_Process.JSON_processor()       

    elif interface == "6":
        net = pp.create_empty_network(name = "Excel Grid")
        Excel_Process = Excel_grid_creator(net)
        Excel_Process.Excel_file_analyzer()  