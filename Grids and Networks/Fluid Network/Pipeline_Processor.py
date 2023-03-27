import os
import json
import geojson
import warnings
import pandas as pd
import pandapipes as pipe
from Helper import Notification, CaseFileReader, CaseFileEditor, Excel_pipeline_creator

class UserPipelineCreator():
    def __init__(self, net, Network_Elements):
        self.net = net
        self.junction_number = None
        self.Network_Elements = Network_Elements

    def junction(self):
        ask_junc = Notification.user_junction_interface(self)     
        if ask_junc == "1":
            self.junction_number = Notification.user_junction_number(self)
            for number in range(self.junction_number):
                junc_name, pnbar, tfluidk, height = Notification.user_junction_detail(self, number)
                globals()["junction" + str(number)] = pipe.create_junction(self.net, pn_bar = pnbar, tfluid_k = tfluidk, height_m = height, name = junc_name)
                self.Network_Elements["junctions"].append(junc_name)
                Notification.user_junction_creation_confirm(self, self.net, junc_name)
        else:
            pass

    def pipe(self):
        ask_pipe = Notification.user_pipe_interface(self)
        if ask_pipe == "1":
            pipe_numbers = Notification.user_pipe_number(self)
            for number in range(pipe_numbers):
                pipe_name, f_junc, t_junc, pipe_std, pipe_len = Notification.user_pipe_detail(self, self.net, number)               
                for f in range(len(self.Network_Elements["junctions"])):
                    if f_junc in self.Network_Elements["junctions"][f]:
                        from_junc = globals()["junction" + str(f)]   
                for t in range(len(self.Network_Elements["junctions"])):
                    if t_junc in self.Network_Elements["junctions"][t]:
                        to_junc = globals()["junction" + str(t)]             
                        
                globals()["pipe" + str(number)] = pipe.create_pipe(self.net, from_junction = from_junc, to_junction = to_junc, std_type = pipe_std, length_km = pipe_len, name = pipe_name)
                Notification.user_pipe_confirm(self, self.net)     
        else:
            pass

    def valve(self):
        ask_valve = Notification.user_valve_interface(self)
        if ask_valve == "1":
            valve_numbers = Notification.user_valve_number(self)
            for number in range(valve_numbers):
                valve_name, f_junc, t_junc = Notification.user_valve_detail(self, self.net, number)                
                for f in range(len(self.Network_Elements["junctions"])):
                    if f_junc in self.Network_Elements["junctions"][f]:
                        from_junc = globals()["junction" + str(f)]   
                for t in range(len(self.Network_Elements["junctions"])):
                    if t_junc in self.Network_Elements["junctions"][t]:
                        to_junc = globals()["junction" + str(t)]                                    
                globals()["valve" + str(number)] = pipe.create_valve(self.net, from_junction = from_junc, to_junction = to_junc, name = valve_name)
                Notification.user_valve_creation_confirm(self, self.net)     
        else:
            pass
     
    def sink(self):
        ask_sink= Notification.user_sink_interface(self)
        if ask_sink == "1":
            sink_number = Notification.user_sink_number(self)
            for number in range(sink_number):
                sink_name, junc, m_dot = Notification.user_sink_detail(self, number)
                for number in range(len(self.Network_Elements["junctions"])):
                    if junc in self.Network_Elements["junctions"][number]:
                        globals()["sink" + str(number)] = pipe.create_sink(self.net, junction = junc, mdot_kg_per_s = m_dot, name = sink_name)  
                        Notification.user_sink_creation_confirm(self, self.net)
        else:
            pass

    def source(self):
        ask_source = Notification.user_source_interface(self)
        if ask_source == "1":
            source_number = Notification.user_source_number(self)
            for number in range(source_number):
                source_name, junc, m_dot = Notification.user_source_detail(self, number)
                for number in range(len(self.Network_Elements["junctions"])):
                    if junc in self.Network_Elements["junctions"][number]:
                        globals()["source" + str(number)] = pipe.create_source(self.net, junction = junc, mdot_kg_per_s = m_dot, name = source_name)  
                        Notification.user_sink_creation_confirm(self, self.net)
        else:
            pass

    def ext_grid(self):
        ext_grid = Notification.user_ext_grid_interface(self)
        if ext_grid == "1":
            ext_grid_number = Notification.user_ext_grid_number(self)
            for number in range(ext_grid_number):
                ext_grid_name, junc, pbar, tk = Notification.user_ext_grid_detail(self, number)
                for number in range(len(self.Network_Elements["junctions"])):
                    if junc in self.Network_Elements["junctions"][number]:
                        globals()["ext_grid" + str(number)] = pipe.create_ext_grid(self.net, junction = junc, p_bar = pbar, t_k = tk, name = ext_grid_name)  
                        Notification.user_ext_grid_creation_confirm(self, self.net)
        else:
            pass

#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#
#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~# 
#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#      

class ElementAssigner():
    def __init__(self, net):
        self.buildings = None
        self.pipeline = net

    def junction_assigner(self):
        for file_name in os.listdir("G:\Final-Project\GeoProcessing\Files\D_Teaser Profile"):
            if file_name.endswith(".geojson"):
                Geo_file = file_name
        with open(os.path.join('G:/Final-Project/GeoProcessing/Files/D_Teaser Profile/' + Geo_file)) as File:
            self.buildings = geojson.load(File)

        if len(self.buildings) == len(self.pipeline.junction):
            for i in range(len(self.pipeline.junction)):
                junc = self.pipeline.junction.iloc[i]
                junc = junc.to_dict()
                self.buildings[i]["tags"]["junction"] = junc
                
        elif len(self.buildings) > len(self.pipeline.junction):
            for i in range(len(self.pipeline.junction)):
                junc = self.pipeline.junction.iloc[i]
                junc = junc.to_dict()
                self.buildings[i]["tags"]["junction"] = junc
                
        elif len(self.buildings) < len(self.pipeline.junction):
            for i in range(len(self.buildings)):
                junc = self.pipeline.junction.iloc[i]
                junc = junc.to_dict()
                self.buildings[i]["tags"]["bus"] = junc

        with open('G:/Final-Project/GeoProcessing/Files/D_Teaser Profile/Teaser.geojson', 'w') as f:
                              json.dump(self.buildings, f)

#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#
#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~# 
#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#        

if __name__ == "__main__":
    
    Network_Elements = {"junctions" : []}    
    interface = Notification.initial_step(Notification)
    if interface == "1":
        net_name = Notification.net_name(Notification)
        net = pipe.create_empty_network(name = net_name, fluid = "water", add_stdtypes = True)
        Notification.net_creation_confirm(Notification)
        Main_network = UserPipelineCreator(net, Network_Elements)
        Main_network.junction()
        Main_network.pipe()
        Main_network.valve()
        Main_network.sink()        
        Main_network.source()
        Main_network.ext_grid()
        
    elif interface == "2":
        net = CaseFileReader.Pickle_reader(CaseFileReader)
        Notification.case_file_import_confirm(Notification)
        answer = Notification.file_edit(Notification)
        if answer == "1":
            Main = ElementAssigner(net)
            Main.junction_assigner()
        elif answer == "2":
            Edit = CaseFileEditor(net)
            elements = Edit.network_element_detector()
            Edit.network_elements_analyzer_editor(elements)
            Main = ElementAssigner(net)
            Main.junction_assigner()

    elif interface == "3":
        net = CaseFileReader.JSON_reader(CaseFileReader)
        Notification.case_file_import_confirm(Notification)
        answer = Notification.file_edit(Notification)
        if answer == "1":
            Main = ElementAssigner(net)
            Main.junction_assigner()
        elif answer == "2":
            Edit = CaseFileEditor(net)
            elements = Edit.network_element_detector()
            Edit.network_elements_analyzer_editor(elements)
            Main = ElementAssigner(net)
            Main.junction_assigner()     

    elif interface == "4":
        net = pipe.create_empty_network(name = "Network", fluid = "water", add_stdtypes = True)
        Notification.case_file_import_confirm(Notification)
        Excel_Process = Excel_pipeline_creator(net)
        net = Excel_Process.Excel_file_analyzer() 
        answer = Notification.file_edit(Notification)
        if answer == "1":
            Main = ElementAssigner(net)
            Main.junction_assigner()
        elif answer == "2":
            Edit = CaseFileEditor(net)
            elements = Edit.network_element_detector()
            Edit.network_elements_analyzer_editor(elements)
            Main = ElementAssigner(net)
            Main.junction_assigner()