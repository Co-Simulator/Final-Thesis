import os
import warnings
import pandas as pd
import pandapipes as pipe


class Notification():
    
    def initial_step(self):
        print("To start with Grid Process please choose one of below interfaces:")
        user_ask = input("1_Create your network manually\n2_Import and convert PICKLE file\n3_Import and convert JSON file\n4_Import and convert EXCEL file\nType your answer: ")
        return user_ask

    #~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#
    
    def net_name(self):
        net_name = input("Choose the name of your network? ")
        return net_name

    def net_creation_confirm(self):
        print("The empty network has been created successfully")

    #~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#
    
    def user_junction_interface(self):
        junc_ask = input("Do you want to create 'JUNCTION' for your network?\n1_Yes\n2_No\nType your answer: ")
        return junc_ask

    def user_junction_number(self):
        junc_number = int(input("How many 'Junctions' you want to create for your network? "))
        return junc_number
    
    def user_junction_detail(self, i):
        junc_name = input(f"What is the name of bus number {i}: ")
        pnbar = float(input(f"Enter the pn_bar for junction {junc_name}: "))
        tfluidk = float(input(f"Enter the tfluid_k for junction {junc_name}: "))
        height = float(input(f"Enter the height for junction {junc_name}: "))        
        return junc_name, pnbar, tfluidk, height

    def user_junction_creation_confirm(self, net, junc_name):
        print(f"JUNCTION {junc_name} HAS BEEN CREATED")
        print(net)
            
    #~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#
        
    def user_pipe_interface(self):
        pipe = input("Do you want to create 'Pipe' for your network?\n1_Yes\n2_No\nType your answer: ")
        return pipe

    def user_pipe_number(self):
        pipe_number = int(input("How many Pipes you want to create for your network? "))
        return pipe_number
    
    def user_pipe_detail(self, number):
        pipe_name = input(f"Enter a name for VALVE number {number}: ")
        f_junc = input(f"What is the source junction of '{pipe_name}'? ")
        t_junc = input(f"What is the destination junction of '{pipe_name}'? ")        
        pipe_std = input("A standard-types file has been created in the root foolder.\nChoose one of the standard types for pipe '{pipe_name}'.\nType the chosen standard: ")
        pipe_len = float(input("What is the length of pipe '{pipe_name}' in KM? "))      
        return pipe_name, f_junc, t_junc, pipe_std, pipe_len
    
    def user_pipe_confirm(self, net):
        print("PIPE HAS BEEN CREATED")
        print(net)

    #~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#                   
        
    def user_valve_interface(self):
        valve = input("Do you want to create 'VALVE' for your network?\n1_Yes\n2_No\nType your answer: ")
        return valve

    def user_valve_number(self):
        valve_number = int(input("How many VALVES you want to create for your network? "))
        return valve_number
    
    def user_valve_detail(self, number):
        valve_name = input(f"Enter a name for VALVE number {number}: ")
        f_junc = input(f"What is the source junction of '{valve_name}'? ")
        t_junc = input(f"What is the destination junction of '{valve_name}'? ")          
        return valve_name, f_junc, t_junc
    
    def user_valve_creation_confirm(self, net):
        print("VALVE HAS BEEN CREATED")
        print(net)        

    #~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#          
        
    def user_sink_interface(self):
        sink = input("Do you want to create 'SINK' for your network?\n1_Yes\n2_No\nType your answer: ")
        return sink

    def user_sink_number(self):
        sink_number = int(input("How many 'SINKS' you want to create? "))
        return sink_number
    
    def user_sink_detail(self, number):
        sink_name = input(f"Enter a name for SINK number {number}: ")
        junc = input(f"What is the junction that '{sink_name}' is connected to? ")
        m_dot = float(input(f"Enter the mdot_kg_per_s for junction {sink_name}: "))        
        return sink_name, junc, m_dot

    def user_sink_creation_confirm(self, net):
        print("SINK HAS BEEN CREATED")
        print(net)        

    #~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#          

    def user_source_interface(self):
        source = input("Do you want to create 'SOURCE' for your network?\n1_Yes\n2_No\nType your answer: ")
        return source

    def user_source_number(self):
        source_number = int(input("How many 'SOURCES' you want to create? "))
        return source_number
    
    def user_source_detail(self, number):
        source_name = input(f"Enter a name for SOURCE number {number}: ")
        junc = input(f"What is the junction that '{source_name}' is connected to? ")
        m_dot = float(input(f"Enter the mdot_kg_per_s for junction {source_name}: "))        
        return sink_name, junc, m_dot

    def user_source_creation_confirm(self, net):
        print("SOURCE HAS BEEN CREATED")
        print(net)        

    #~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~# 

    def user_ext_grid_interface(self):
        ext_grid = input("Do you want to create 'Ext_Grid' for your network?\n1_Yes\n2_No\nType your answer: ")
        return ext_grid

    def user_ext_grid_number(self):
        ext_grid_number = int(input("How many 'Ext_Grids' you want to create? "))
        return ext_grid_number
    
    def user_ext_grid_detail(self, number):
        ext_grid_name = input(f"Enter a name for Ext_Grid number {number}: ")
        junc = input(f"What is the junction that '{ext_grid_name}' is connected to? ")
        pbar = float(input(f"What is the p_bar of {ext_grid_name}: "))
        tk = float(input(f"What is the t_k of {ext_grid_name}: "))   
        return ext_grid_name, junc, pbar, tk

    def user_ext_grid_creation_confirm(self, net):
        print("EXT_GRID HAS BEEN CREATED")
        print(net)        

    #~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#
        
    def case_file_import_confirm(self, net):
        print("The Case File has been imported")
        print(net)
        
    def file_edit(self):
        ask_edit = input("Do you want to edit the imported casefile?\n1_YES\n2_NO\nType your answer: ")
        return ask_edit
    
    def element_edit_select(self, network_elements):
        print(f"Available elements in the converted network are: \n{network_elements}")
        print("      ")
        elem_number = int(input("How many elements you want to edit? "))
        return elem_number
    
    def element_ask(self, elem):
        elem_name = input(f"Type the {elem}st element that you want to edit: ").lower()
        return elem_name
    
    def edit_interface(self):
        print("Select one of the available interfaces to edit the selected element.")
        print("   ")
        edit_method = input("1_Using Excel file\n2_Using CSV file\nType your answer: ")
        return edit_method        
        
    def Excel_export(self):
        process = input("The 'Excel' file has been created.\nNow you can open the file and edit its data\nWhen the edit is done, press '1' to import the file\nType your answer: ")
        return process
         
    def CSV_export(self):
        process = input("The 'CSV' file has been created.\nNow you can open the file and edit its data\nWhen the edit is done, press '1' to import the file\nType your answer: ")
        return process
 
    def case_file_error(self):
        print("WRONG INPUT")        
        
        
        
        
#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#
#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~# 
#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#         




class CaseFileReader():


    def Pickle_reader(self):
        for file_name in os.listdir("G:\Project - OOP\Fluid Network\Case Files\Pickle files"):
            if file_name.endswith(".pkl"):
                Pickle = file_name
        input_directory = os.path.dirname(os.path.realpath('__file__'))
        net = pipe.from_pickl(os.path.join(input_directory, 'Case Files/Pickle files/' + Pickle))
        warnings.filterwarnings('ignore')
        return net

    def JSON_reader(self):
        for file_name in os.listdir("G:\Project - OOP\Fluid Network\Case Files\Json files"):
            if file_name.endswith(".json"):
                Json = file_name
        input_directory = os.path.dirname(os.path.realpath('__file__'))
        net = pipe.from_json(os.path.join(input_directory, 'Case Files/Json files/' + Json))
        warnings.filterwarnings('ignore')
        return net
    
    def Excel_reader(self):
       for file_name in os.listdir("G:\Project - OOP\Fluid Network\Case Files\Excel files"):
           if file_name.endswith(".xlsx"):
               Excel = file_name
       input_directory = os.path.dirname(os.path.realpath('__file__'))
       File = os.path.join(input_directory, 'Case Files/Excel files/' + Excel)
       Excel_file = pd.ExcelFile(File)
       warnings.filterwarnings('ignore')
       return Excel_file   



#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#
#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~# 
#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#  



class CaseFileEditor():
    
    def __init__(self, net):

        self.net = net
        self.network_elements = []
        self.junctions = self.net.junction
        self.pipes = self.net.pipe
        self.valves = self.net.valve
        self.sinks = self.net.sink
        self.sources = self.net.source
        self.ext_grids = self.net.ext_grid
        self.Excel_file = None


    def network_element_detector(self):
        if self.junctions.empty:
            pass
        else:
            self.network_elements.append("junctions")

        if self.pipes.empty:
            pass
        else:
            self.network_elements.append("pipes")
            
        if self.valves.empty:
            pass
        else:
            self.network_elements.append("valves")
            
        if self.sinks.empty:
            pass
        else:
            self.network_elements.append("sinks")
            
        if self.sources.empty:
            pass
        else:
            self.network_elements.append("sources")
        
        if self.ext_grids.empty:
            pass
        else:
            self.network_elements.append("ext_grids")
        return self.network_elements
    
    
    def network_elements_analyzer_editor(self, net, elem_name):
        if elem_name == "junctions":
            edit_method = Notification.edit_interface(self)
            if edit_method == "1":
                with pd.ExcelWriter("Exports/Excel/junctions.xlsx") as excel_junctions:
                    self.junctions.to_excel(excel_junctions)
                process = Notification.Excel_export(self)
                if process == "1":
                    updated_junctions_values = pd.read_excel("Exports/Excel/junctions.xlsx", index_col=0)
                    for i in range(len(self.junctions)):
                        self.junctions.loc[i] = updated_junctions_values.loc[i].values
            elif edit_method == "2":
                self.junctions.to_csv('Exports/CSV/junctions.csv')
                process = Notification.CSV_export(self)
                    if process == "1":
                        updated_junctions_values = pd.read_csv("Exports/CSV/junctions.csv", index_col=0)
                        for i in range(len(self.junctions)):
                            self.junctions.loc[i] = updated_junctions_values.loc[i].values
                            self.net.junction = self.junctions


        if elem_name == "pipes":
            edit_method = Notification.edit_interface(self)
            if edit_method == "1":
                with pd.ExcelWriter("Exports/Excel/pipes.xlsx") as excel_pipes:
                    self.pipes.to_excel(excel_pipes)
                process = Notification.Excel_export(self)
                if process == "1":
                    updated_pipes_values = pd.read_excel("Exports/Excel/pipes.xlsx", index_col=0)
                    for i in range(len(self.pipes)):
                        self.pipes.loc[i] = updated_pipes_values.loc[i].values
            elif edit_method == "2":
                self.pipes.to_csv('Exports/CSV/pipes.csv')
                process = Notification.CSV_export(self)
                    if process == "1":
                        updated_pipes_values = pd.read_csv("Exports/CSV/pipes.csv", index_col=0)
                        for i in range(len(self.pipes)):
                            self.pipes.loc[i] = updated_pipes_values.loc[i].values
                            self.net.pipe = self.pipes


        if elem_name == "valves":
            edit_method = Notification.edit_interface(self)
            if edit_method == "1":
                with pd.ExcelWriter("Exports/Excel/valves.xlsx") as excel_valves:
                    self.valves.to_excel(excel_valves)
                process = Notification.Excel_export(self)
                if process == "1":
                    updated_valves_values = pd.read_excel("Exports/Excel/valves.xlsx", index_col=0)
                    for i in range(len(self.valves)):
                        self.valves.loc[i] = updated_valves_values.loc[i].values
            elif edit_method == "2":
                self.valves.to_csv('Exports/CSV/valves.csv')
                process = Notification.CSV_export(self)
                    if process == "1":
                        updated_valves_values = pd.read_csv("Exports/CSV/valves.csv", index_col=0)
                        for i in range(len(self.valves)):
                            self.valves.loc[i] = updated_valves_values.loc[i].values
                            self.net.valve = self.valves


        if elem_name == "sinks":
            edit_method = Notification.edit_interface(self)
            if edit_method == "1":
                with pd.ExcelWriter("Exports/Excel/sinks.xlsx") as excel_sinks:
                    self.sinks.to_excel(excel_sinks)
                process = Notification.Excel_export(self)
                if process == "1":
                    updated_sinks_values = pd.read_excel("Exports/Excel/sinks.xlsx", index_col=0)
                    for i in range(len(self.sinks)):
                        self.sinks.loc[i] = updated_sinks_values.loc[i].values
            elif edit_method == "2":
                self.sinks.to_csv('Exports/CSV/sinks.csv')
                process = Notification.CSV_export(self)
                    if process == "1":
                        updated_sinks_values = pd.read_csv("Exports/CSV/sinks.csv", index_col=0)
                        for i in range(len(self.sinks)):
                            self.sinks.loc[i] = updated_sinks_values.loc[i].values
                            self.net.sink = self.sinks


        if elem_name == "sources":
            edit_method = Notification.edit_interface(self)
            if edit_method == "1":
                with pd.ExcelWriter("Exports/Excel/sources.xlsx") as excel_sources:
                    self.sources.to_excel(excel_sources)
                process = Notification.Excel_export(self)
                if process == "1":
                    updated_sources_values = pd.read_excel("Exports/Excel/sources.xlsx", index_col=0)
                    for i in range(len(self.sources)):
                        self.lines.loc[i] = updated_sources_values.loc[i].values
            elif edit_method == "2":
                self.sources.to_csv('Exports/CSV/sources.csv')
                process = Notification.CSV_export(self)
                    if process == "1":
                        updated_sources_values = pd.read_csv("Exports/CSV/sources.csv", index_col=0)
                        for i in range(len(self.sources)):
                            self.sources.loc[i] = updated_sources_values.loc[i].values
                            self.net.source = self.sources


        if elem_name == "ext_grids":
            edit_method = Notification.edit_interface(self)
            if edit_method == "1":
                with pd.ExcelWriter("Exports/Excel/ext_grids.xlsx") as excel_ext_grids:
                    self.ext_grids.to_excel(excel_ext_grids)
                process = Notification.Excel_export(self)
                if process == "1":
                    updated_ext_grids_values = pd.read_excel("Exports/Excel/ext_grids.xlsx", index_col=0)
                    for i in range(len(self.ext_grids)):
                        self.ext_grids.loc[i] = updated_ext_grids_values.loc[i].values
            elif edit_method == "2":
                self.ext_grids.to_csv('Exports/CSV/ext_grids.csv')
                process = Notification.CSV_export(self)
                    if process == "1":
                        updated_ext_grids_values = pd.read_csv("Exports/CSV/ext_grids.csv", index_col=0)
                        for i in range(len(self.trafos)):
                            self.ext_grids.loc[i] = updated_ext_grids_values.loc[i].values
                            self.net.ext_grid = self.ext_grids
        print(self.net)  



#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#
#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~# 
#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#  



class Excel_grid_creator():
    
    def __init__(self, net):
        self.Excel_file = CaseFileReader.Excel_reader(self)
        self.sheets = file.sheet_names
        self.grid_elem = {"junctions" : []}
        self.net = net
        
    def Excel_file_analyzer(self):
        for i in range(len(self.sheets)):
            if "junction" in self.sheets:
                sheet_junction = self.sheets.pop(i)
                excel = pd.read_excel(self.Excel_file, sheet_name = sheet_junction, index_col = 0)
                for junc in excel.index:
                   junc_name = excel.at[junc, "name"]
                   pnbar = excel.at[junc, "pn_bar"]
                   tfluidk = excel.at[junc, "tfluid_k"]  
                   height = excel.at[junc, "height_m"]     
                   globals()["junction" + str(number)] = pipe.create_junction(self.net, pn_bar = pnbar,
                                                        tfluid_k = tfluidk, height_m = height, name = junc_name)
                   self.grid_elem["junction"].append(excel.at[junction, "name"])



            if "pipe" in self.sheets:
                sheet_pipe = self.sheets.pop(i)
                excel = pd.read_excel(self.Excel_file, sheet_name = sheet_pipe, index_col = 0) 
                for pipe in excel.index:
                    for f in excel.index:
                        f_j = excel.at[pipe, "from_junction"]
                        if f_j in self.grid_elem["junctions"]:
                            from_junc = globals()["junction" + str(f)]  
                        else:
                            pass
                    for t in excel.index:
                        t_j = excel.at[pipe, "to_junction"]
                        if t_j in self.grid_elem["junctions"]:
                            to_junc = globals()["junction" + str(t)]  
                        else:
                            pass    
                    pipe_std = excel.at[pipe, "std_type"]
                    pipe_name = excel.at[pipe, "name"]
                    pipe_leng = excel.at[pipe, "length_km"]
                    
                    globals()["pipe" + str(pipe)] = pipe.create_pipe(self.net, from_junction = from_junc, to_junction = to_junc,
                                                                     std_type = pipe_std, length_km = pipe_leng, name = pipe_name)



            if "valve" in self.sheets:
                sheet_valve = self.sheets.pop(i)
                excel = pd.read_excel(self.Excel_file, sheet_name = sheet_valve, index_col = 0) 
                for valve in excel.index:
                    for f in excel.index:
                        f_j = excel.at[valve, "from_junction"]
                        if f_j in self.grid_elem["junctions"]:
                            from_junc = globals()["junction" + str(f)]  
                        else:
                            pass
                    for t in excel.index:
                        t_j = excel.at[valve, "to_junction"]
                        if t_j in self.grid_elem["junctions"]:
                            to_junc = globals()["junction" + str(t)]  
                        else:
                            pass    
                    valve_name = excel.at[pipe, "name"]
                    
                    globals()["valve" + str(valve)] = pipe.create_valve(self.net, from_junction = from_junc, to_junction = to_junc,
                                                                                                                 name = valve_name)



            if "sink" in self.sheets:
                sheet_sink = self.sheets.pop(i)
                excel = pd.read_excel(self.Excel_file, sheet_name = sheet_sink, index_col = 0)
                for sink in excel.index:
                    s_j = excel.at[sink, "junction"]
                    if s_j in self.grid_elem["junctions"]:
                        sink_junct = globals()["junction" + str(s_j)]
                        mdotkg_pers = excel.at[sink, "mdot_kg_per_s"]
                        sink_name = excel.at[sink, "name"]
                        globals()["sink" + str(g)] = pipe.create_sink(self.net, junction = sink_junct,
                                                                     mdot_kg_per_s = mdotkg_pers, name = sink_name)  



            if "source" in self.sheets:
                sheet_source = self.sheets.pop(i)
                excel = pd.read_excel(self.Excel_file, sheet_name = sheet_source, index_col = 0)
                for source in excel.index:
                    s_j = excel.at[source, "junction"]
                    if s_j in self.grid_elem["junctions"]:
                        source_junct = globals()["junction" + str(s_j)]
                        mdotkg_pers = excel.at[source, "mdot_kg_per_s"]
                        source_name = excel.at[source, "name"]
                        globals()["source" + str(source)] = pipe.create_source(self.net, junction = source_junct,
                                                                     mdot_kg_per_s = mdotkg_pers, name = source_name)  



            if "ext_grid" in self.sheets:
                sheet_ext_grid = self.sheets.pop(i)
                excel = pd.read_excel(self.Excel_file, sheet_name = sheet_ext_grid, index_col = 0)
                for ext_grid in excel.index:
                    e_j = excel.at[ext_grid, "junction"]
                    if e_j in self.grid_elem["junctions"]:
                        ext_junct = globals()["junction" + str(e_j)]
                        ext_name = excel.at[ext_grid, "name"]
                        ext_pbar = excel.at[ext_grid, "p_bar"]
                        ext_tk = excel.at[ext_grid, "t_k"]  
                        globals()["ext_grid" + str(ext_grid)] = pipe.create_ext_grid(self.net, junction = ext_junct,
                                                                                     p_bar = ext_pbar, t_k = ext_tk, name = ext_name) 
 