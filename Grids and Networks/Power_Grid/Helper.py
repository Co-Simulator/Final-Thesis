import os
import geojson
import warnings
import pandas as pd
import pandapower as pp

class Notification():
    
    def initial_step(self):
        print("To start with Grid Process please choose one of below interfaces:")
        user_ask = input("1_Create your grid manually\n2_Import and convert MATPOWER file\n3_Import and convert PYPOWER file\n4_Import and convert PICKLE file\n5_Import and convert JSON file\n6_Import and convert EXCEL file\nType your answer: ")
        return user_ask

    #~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#
    
    def net_name(self):
        net_name = input("Choose the name of your network? ")
        return net_name

    def grid_creation_confirm(self):
        print("The empty network has been created successfully")

    #~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#
    
    def user_bus_interface(self):
        bus_ask = input("Do you want to create 'BUS' for your network?\n1_Yes\n2_No\nType your answer: ")
        return bus_ask

    def user_bus_number(self):
        bus_number = int(input("How many 'Buses' you want to create for your network? "))
        return bus_number
    
    def user_bus_detail(self, i):
        bus_name = input(f"What is the name of bus number {i}: ")
        vnkv = float(input(f"Enter the vn_kv for bus {bus_name}: "))
        return bus_name, vnkv

    def user_bus_creation_confirm(self, net, bus_name):
        print(f"BUS {bus_name} HAS BEEN CREATED")
        print(net.bus)
        print(net)
            
    #~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#
        
    def user_ext_grid_interface(self):
        ext_grid = input("Do you want to create 'Ext_Grid' for your network?\n1_Yes\n2_No\nType your answer: ")
        return ext_grid

    def user_ext_grid_number(self):
        ext_grid_number = int(input("How many Ext_Grids you want to create for your network? "))
        return ext_grid_number
    
    def user_ext_grid_detail(self, grid_counter):
        ext_grid_name = input(f"Enter a name for Ext_Grid number {grid_counter}: ")
        ext_grid_vmpu = float(input(f"What is the vm_pu of grid '{ext_grid_name}'? "))
        return ext_grid_name, ext_grid_vmpu
    
    def user_ext_grid_bus(self, net, ext_grid_name):
        print(net.bus)
        ext_grid_bus = input(f"What is the bus that grid '{ext_grid_name}' is conected to? ")
        return ext_grid_bus
    
    def user_ext_grid_creation_confirm(self, net):
        print("EXTERNAL GRID HAS BEEN CREATED")
        pp.runpp(net)
        print(net)

    #~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#                   
        
    def user_load_interface(self):
        load = input("Do you want to create 'LOAD' for your network?\n1_Yes\n2_No\nType your answer: ")
        return load

    def user_load_number(self):
        load_number = int(input("How many LOADS you want to create for your network? "))
        return load_number
    
    def user_load_detail(self, number):
        load_name = input(f"Enter a name for LOAD number {number}: ")
        load_pmw = float(input(f"What is the p_mw of '{load_name}'? "))
        load_qkvar = input(f"What is the q_kvar of '{load_name}'? ")
        return load_name, load_pmw, load_qkvar
    
    def user_load_bus(self, net, load_name):
        print(net.bus)
        load_bus = input(f"What is the bus that '{load_name}' is conected to? ") 
        return load_bus
    
    def user_load_creation_confirm(self, net):
        print("LOAD HAS BEEN CREATED")
        pp.runpp(net)
        print(net)        

    #~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#          
        
    def user_transform_interface(self):
        ask_transformer = input("Do you want to create 'TRANSFORMER' for your network?\n1_Yes\n2_No\nType your answer: ")
        return ask_transformer

    def user_transformer_number(self):
        trafo_number = int(input("How many 'TRANSFORMERS' you want to create? "))
        return trafo_number
    
    def user_trafo_detail(self, net, number):
        trafo_name = input(f"Enter a name for 'TRANSFORMER' number {number}: ")
        print(net.bus)
        trafo_hvbus = input(f"What is the hv_bus that '{trafo_name}' is conected to? ")
        trafo_lvbus = input(f"What is the lv_bus that '{trafo_name}' is conected to? ") 
        print(pp.available_std_types(net, element='trafo'))
        trafo_std = input(f"Choose one of the above standard types for '{trafo_name}'? ") 
        return trafo_name, trafo_hvbus, trafo_lvbus, trafo_std

    def user_trafo_creation_confirm(self, net):
        print("TRAFO HAS BEEN CREATED")
        pp.runpp(net)
        print(net)        

    #~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#          

    def user_line_interface(self):
        ask_line = input("Do you want to create 'LINES' for your network?\n1_Yes\n2_No\nType your answer: ")
        return ask_line

    def user_line_number(self):
        line_number = int(input("How many 'LINES' you want to create? "))
        return line_number
    
    def user_line_detail(self, net, number):
        line_name = input(f"Enter a name for 'LINE' number {number}: ")
        print(net.bus)
        source_bus = input(f"What is the source bus that '{line_name}' is conected to? ")
        destination_bus = input(f"What is the destination bus that '{line_name}' is conected to? ") 
        print(pp.available_std_types(net, element='line'))
        line_std = input(f"Choose one of the above standard types for '{line_name}'? ") 
        line_length = float(input(f"What is the length of line between buses {source_bus} and {destination_bus} in KM? "))
        return line_name, source_bus, destination_bus, line_std, line_length

    def user_line_creation_confirm(self, net):
        print("LINE HAS BEEN CREATED")
        pp.runpp(net)
        print(net)        

    #~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~# 

    def user_switch_interface(self):
        ask_switch = input("Do you want to create 'SWITCH' for your network?\n1_Yes\n2_No\nType your answer: ")
        return ask_switch

    def user_switch_number(self):
        switch_number = int(input("How many 'SWITCHES' you want to create? "))
        return switch_number
    
    def user_switch_detail(self, net, number):
        switch_name = input(f"Enter a name for 'SWITCH' number {number}: ")
        print(net.bus)
        switch_bus = input(f"What is the bus that '{switch_name}' is conected to? ")
        elem_number = int(input(f"Type the element number for '{switch_name}'? "))
        elem_type = input(f"Type the element type for '{switch_name}'\nAvailable options are 'b', 'l', 't':  ")
        switch_status = int(input(f"Switch '{switch_name}' is closed or open?\n1_CLOSED\n2_OPEN\nType your answer:  "))
        return switch_name, switch_bus, elem_number, elem_type, switch_status

    def user_switch_creation_confirm(self, net):
        print("SWITCH HAS BEEN CREATED")
        pp.runpp(net)
        print(net)        

    #~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~# 

    def user_storage_interface(self):
        ask_storage = input("Do you want to create 'STORAGE' for your network?\n1_Yes\n2_No\nType your answer: ")
        return ask_storage

    def user_storage_number(self):
        storage_number = int(input("How many 'STORAGES' you want to create? "))
        return storage_number
    
    def user_storage_detail(self, net, number):
        storage_name = input(f"Enter a name for 'STORAGE' number {number}: ")
        print(net.bus)
        storage_bus = input(f"What is the bus that '{storage_name}' is conected to? ")
        pkw = float(input(f"What is the p_kw of '{storage_name}'? "))
        max_ekw = float(input(f"What is the max_e_kwh of '{storage_name}'? "))
        return storage_name, storage_bus, pkw, max_ekw

    def user_storage_creation_confirm(self, net):
        print("STORAGE HAS BEEN CREATED")
        pp.runpp(net)
        print(net)        

    #~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#
        
    def case_file_import_confirm(self, net):
        print("The Case File has been imported")
        # pp.runpp(net)
        
    def file_edit(self):
        ask_edit = input("Do you want to edit the values in the case file?.\n1_No\n2_Yes\nType your answer: ")
        return ask_edit
    
    def element_edit_select(self, grid_elements):
        print(f"Available elements in the network are: \n{grid_elements}")
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
        print("*** WRONG INPUT ***")        

#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#
#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~# 
#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#         

# Read case files in different formats from the determined folder
class CaseFileReader():
    
    def MATPower_reader(self):
        for file_name in os.listdir("G:\Final-Project\Grids and Networks\Power_Grid\Case Files\MatPower files"):
            if file_name.endswith(".mat"):
                MAT_File = file_name
        MAT_name = os.path.splitext(MAT_File)[0]
        input_directory = os.path.dirname(os.path.realpath('__file__'))
        net = pp.converter.from_mpc(os.path.join(input_directory, 'Case Files/MatPower files/' + MAT_File), casename_mpc_file = MAT_name)
        warnings.filterwarnings('ignore')
        return net

    def PyPower_reader(self):
        for file_name in os.listdir("G:\Project\Power_Grid\Case Files\PyPower files"):
            if file_name.endswith(".py"):
                PyFile = file_name
        input_directory = os.path.dirname(os.path.realpath('__file__'))
        net = pp.converter.from_ppc(os.path.join(input_directory, 'Case Files/PyPower files/' + PyFile))
        warnings.filterwarnings('ignore')
        return net

    def Pickle_reader(self):
        for file_name in os.listdir("G:\Project\Power_Grid\Case Files\Pickle files"):
            if file_name.endswith(".py"):
                Pickle = file_name
        input_directory = os.path.dirname(os.path.realpath('__file__'))
        net = pp.from_pickle(os.path.join(input_directory, 'Case Files/Pickle files/' + Pickle))
        warnings.filterwarnings('ignore')
        return net

    def JSON_reader(self):
        for file_name in os.listdir("G:\Project\Power_Grid\Case Files\Json files"):
            if file_name.endswith(".json"):
                Json = file_name
        input_directory = os.path.dirname(os.path.realpath('__file__'))
        net = pp.from_json(os.path.join(input_directory, 'Case Files/Json files/' + Json))
        warnings.filterwarnings('ignore')
        return net
    
    def Excel_reader(self):
       for file_name in os.listdir("G:\Final-Project\Grids and Networks\Power_Grid\Case Files\Excel files"):
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

# Edit the case file calues if the user decides to make changes
class CaseFileEditor():
    
    def __init__(self, net):
        # Defined supported elements
        self.net = net
        self.grid_elements = []
        self.buses = self.net.bus
        self.loads = self.net.load
        self.lines = self.net.line
        self.trafos = self.net.trafo
        self.generators = self.net.gen
        self.switches = self.net.switch
        self.storages = self.net.storage
        self.ext_grids = self.net.ext_grid
        self.Excel_file = None
        
    def grid_element_detector(self):
        # Try to find the supported elements in the case files if they are available
        if self.buses.empty:
            pass
        else:
            self.grid_elements.append("BUS")

        if self.generators.empty:
            pass
        else:
            self.grid_elements.append("GEN")
            
        if self.loads.empty:
            pass
        else:
            self.grid_elements.append("LOAD")
            
        if self.ext_grids.empty:
            pass
        else:
            self.grid_elements.append("EXT_GRID")
            
        if self.lines.empty:
            pass
        else:
            self.grid_elements.append("LINE")
        
        if self.trafos.empty:
            pass
        else:
            self.grid_elements.append("TRAFO")
 
        if self.switches.empty:
            pass
        else:
            self.grid_elements.append("SWITCH")
        
        if self.storages.empty:
            pass
        else:
            self.grid_elements.append("STORAGE")
        return self.grid_elements
        
    def grid_elements_analyzer_editor(self, elem_name):
        # Ask how many elements user wants to edit
        elem_number = Notification.element_edit_select(self, elem_name)
        # Make a loop based on the entered number and detect the selected elements
        for i in range(elem_number):
            elem_name = Notification.element_ask(self, i)
            
            if elem_name == "bus":
                edit_method = Notification.edit_interface(self)
                # Export all the existing data of the element in an excel file
                if edit_method == "1":
                    with pd.ExcelWriter("Exports/Excel/bus.xlsx") as excel_bus:
                        self.buses.to_excel(excel_bus)
                    process = Notification.Excel_export(self)
                    if process == "1":
                        # Load and updated all the entered values from the file
                        updated_bus_values = pd.read_excel("Exports/Excel/bus.xlsx", index_col=0)
                        for i in range(len(self.buses)):
                            self.buses.loc[i] = updated_bus_values.loc[i].values
                # Export all the existing data of the element in an excel file
                elif edit_method == "2":
                    self.buses.to_csv('Exports/CSV/bus.csv')
                    process = Notification.CSV_export(self)
                    if process == "1":
                        # Load and updated all the entered values from the file
                        updated_bus_values = pd.read_csv("Exports/CSV/bus.csv", index_col=0)
                        for i in range(len(self.buses)):
                            self.buses.loc[i] = updated_bus_values.loc[i].values
                            self.net.bus = self.buses

            if elem_name == "gen":
                edit_method = Notification.edit_interface(self)
                if edit_method == "1":
                    with pd.ExcelWriter("Exports/Excel/gen.xlsx") as excel_gen:
                        self.generators.to_excel(excel_gen)
                    process = Notification.Excel_export(self)
                    if process == "1":
                        updated_gen_values = pd.read_excel("Exports/Excel/gen.xlsx", index_col=0)
                        for i in range(len(self.generators)):
                            self.generators.loc[i] = updated_gen_values.loc[i].values
                elif edit_method == "2":
                    self.generators.to_csv('Exports/CSV/gen.csv')
                    process = Notification.CSV_export(self)
                    if process == "1":
                        updated_gen_values = pd.read_csv("Exports/CSV/gen.csv", index_col=0)
                        for i in range(len(self.generators)):
                            self.generators.loc[i] = updated_gen_values.loc[i].values
                            self.net.gen = self.generators

            if elem_name == "load":
                edit_method = Notification.edit_interface(self)
                if edit_method == "1":
                    with pd.ExcelWriter("Exports/Excel/load.xlsx") as excel_load:
                        self.loads.to_excel(excel_load)
                    process = Notification.Excel_export(self)
                    if process == "1":
                        updated_load_values = pd.read_excel("Exports/Excel/load.xlsx", index_col=0)
                        for i in range(len(self.loads)):
                            self.loads.loc[i] = updated_load_values.loc[i].values
                elif edit_method == "2":
                    self.loads.to_csv('Exports/CSV/load.csv')
                    process = Notification.CSV_export(self)
                    if process == "1":
                        updated_load_values = pd.read_csv("Exports/CSV/load.csv", index_col=0)
                        for i in range(len(self.loads)):
                            self.loads.loc[i] = updated_load_values.loc[i].values
                            self.net.load = self.loads

            if elem_name == "ext_grid":
                edit_method = Notification.edit_interface(self)
                if edit_method == "1":
                    with pd.ExcelWriter("Exports/Excel/ext_grid.xlsx") as excel_ext_grid:
                        self.ext_grids.to_excel(excel_ext_grid)
                    process = Notification.Excel_export(self)
                    if process == "1":
                        updated_ext_grid_values = pd.read_excel("Exports/Excel/ext_grid.xlsx", index_col=0)
                        for i in range(len(self.ext_grids)):
                            self.ext_grids.loc[i] = updated_ext_grid_values.loc[i].values
                elif edit_method == "2":
                    self.ext_grids.to_csv('Exports/CSV/ext_grid.csv')
                    process = Notification.CSV_export(self)
                    if process == "1":
                        updated_ext_grid_values = pd.read_csv("Exports/CSV/ext_grid.csv", index_col=0)
                        for i in range(len(self.ext_grids)):
                            self.ext_grids.loc[i] = updated_ext_grid_values.loc[i].values
                            self.net.ext_grid = self.ext_grids

            if elem_name == "line":
                edit_method = Notification.edit_interface(self)
                if edit_method == "1":
                    with pd.ExcelWriter("Exports/Excel/line.xlsx") as excel_line:
                        self.lines.to_excel(excel_line)
                    process = Notification.Excel_export(self)
                    if process == "1":
                        updated_line_values = pd.read_excel("Exports/Excel/line.xlsx", index_col=0)
                        for i in range(len(self.lines)):
                            self.lines.loc[i] = updated_line_values.loc[i].values
                elif edit_method == "2":
                    self.lines.to_csv('Exports/CSV/line.csv')
                    process = Notification.CSV_export(self)
                    if process == "1":
                        updated_line_values = pd.read_csv("Exports/CSV/line.csv", index_col=0)
                        for i in range(len(self.lines)):
                            self.lines.loc[i] = updated_line_values.loc[i].values
                            self.net.line = self.lines

            if elem_name == "trafo":
                edit_method = Notification.edit_interface(self)
                if edit_method == "1":
                    with pd.ExcelWriter("Exports/Excel/trafo.xlsx") as excel_trafo:
                        self.trafos.to_excel(excel_trafo)
                    process = Notification.Excel_export(self)
                    if process == "1":
                        updated_trafo_values = pd.read_excel("Exports/Excel/trafo.xlsx", index_col=0)
                        for i in range(len(self.trafos)):
                            self.trafos.loc[i] = updated_trafo_values.loc[i].values
                elif edit_method == "2":
                    self.trafos.to_csv('Exports/CSV/trafo.csv')
                    process = Notification.CSV_export(self)
                    if process == "1":
                        updated_trafo_values = pd.read_csv("Exports/CSV/trafo.csv", index_col=0)
                        for i in range(len(self.trafos)):
                            self.trafos.loc[i] = updated_trafo_values.loc[i].values
                            self.net.trafo = self.trafos

            if elem_name == "switch":
                edit_method = Notification.edit_interface(self)
                if edit_method == "1":
                    with pd.ExcelWriter("Exports/Excel/switch.xlsx") as excel_switch:
                        self.switches.to_excel(excel_switch)
                    process = Notification.Excel_export(self)
                    if process == "1":
                        updated_switch_values = pd.read_excel("Exports/Excel/switch.xlsx", index_col=0)
                        for i in range(len(self.switches)):
                            self.switches.loc[i] = updated_switch_values.loc[i].values
                elif edit_method == "2":
                    self.switches.to_csv('Exports/CSV/switch.csv')
                    process = Notification.CSV_export(self)
                    if process == "1":
                        updated_switch_values = pd.read_csv("Exports/CSV/switch.csv", index_col=0)
                        for i in range(len(self.switches)):
                            self.switches.loc[i] = updated_switch_values.loc[i].values
                            self.net.switch = self.switches

            if elem_name == "storage":
                edit_method = Notification.edit_interface(self)
                if edit_method == "1":
                    with pd.ExcelWriter("Exports/Excel/storage.xlsx") as excel_storage:
                        self.storages.to_excel(excel_storage)
                    process = Notification.Excel_export(self)
                    if process == "1":
                        updated_storage_values = pd.read_excel("Exports/Excel/storage.xlsx", index_col=0)
                        for i in range(len(self.storages)):
                            self.storages.loc[i] = updated_storage_values.loc[i].values
                elif edit_method == "2":
                    self.storages.to_csv('Exports/CSV/storage.csv')
                    process = Notification.CSV_export(self)
                    if process == "1":
                        updated_storage_values = pd.read_csv("Exports/CSV/storage.csv", index_col=0)
                        for i in range(len(self.storages)):
                            self.storages.loc[i] = updated_storage_values.loc[i].values
                            self.net.storage = self.storages 
            print("   ")
            print("Values of the chosen elements have been updated successfully")
            print(self.net)  

#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#
#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~# 
#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#~~~#  

class Excel_grid_creator():
    # Create a power grid from an excel file
    def __init__(self, net):
        self.Excel_file = CaseFileReader.Excel_reader(self)
        self.sheets = self.Excel_file.sheet_names
        self.grid_elem = {"buses" : []}
        self.net = net
        
    def Excel_file_analyzer(self):
        # Detect the name of the sheets and create the elements
        for i in range(len(self.sheets)):
            if self.sheets[i] == "bus":
                excel = pd.read_excel(self.Excel_file, sheet_name = self.sheets[i], index_col = 0)
                for bus in excel.index:
                    globals()["bus" + str(bus)] = pp.create_bus(self.net, vn_kv = excel.at[bus, "vn_kv"], in_service = excel.at[bus, "in_service"],  name = excel.at[bus, "name"])
                    self.grid_elem["buses"].append(excel.at[bus, "name"])
                                       
            if self.sheets[i] == "ext_grid":
                excel = pd.read_excel(self.Excel_file, sheet_name = self.sheets[i], index_col = 0)
                for ext in excel.index:
                    bus_external = excel.at[ext, "bus"]
                    if bus_external in self.grid_elem["buses"]:
                        ext_bus = globals()["bus" + str(ext)]
                        globals()["ext_grid" + str(ext)] = pp.create_ext_grid(self.net, bus = ext_bus , vm_pu = excel.at[ext, "vm_pu"],
                                                                              in_service = excel.at[ext, "in_service"], name = excel.at[ext, "name"])
            if self.sheets[i] == "load":
                excel = pd.read_excel(self.Excel_file, sheet_name = self.sheets[i], index_col = 0)
                for load in excel.index:
                    bus_load = excel.at[load, "bus"]
                    if bus_load in self.grid_elem["buses"]:
                        load_bus = globals()["bus" + str(load)]
                        globals()["load" + str(load)] = pp.create_load(self.net, bus = load_bus, q_kvar = excel.at[load, "q_kvar"], in_service = excel.at[load, "in_service"],
                                                                       p_mw = excel.at[load, "p_mw"], name = excel.at[load, "name"])
            if self.sheets[i] == "trafo":
                excel = pd.read_excel(self.Excel_file, sheet_name = self.sheets[i], index_col = 0) 
                for trafo in excel.index:
                    for high in excel.index:
                        t_hv_bus = excel.at[trafo, "hv_bus"]
                        if t_hv_bus in self.grid_elem["buses"]:
                            hv = globals()["bus" + str(high)]  
                        else:
                            pass
                    for low in excel.index:
                        t_lv_bus = excel.at[trafo, "lv_bus"]
                        if t_lv_bus in self.grid_elem["buses"]:
                            lv = globals()["bus" + str(low)]  
                        else:
                            pass    
                    globals()["trafo" + str(trafo)] = pp.create_transformer(self.net, hv_bus = hv, lv_bus = lv, in_service = excel.at[trafo, "in_service"],
                                                                            std_type = excel.at[trafo, "std_type"], name = excel.at[trafo, "name"])
            if self.sheets[i] == "line":
                excel = pd.read_excel(self.Excel_file, sheet_name = self.sheets[i], index_col = 0)            
                for line in excel.index:
                    for b_from in excel.index:
                        bus_f = excel.at[line, "from_bus"]
                        if bus_f in self.grid_elem["buses"]:
                            b_f = globals()["bus" + str(b_from)] 
                        else:
                            pass
                    for b_to in excel.index:
                        bus_t = excel.at[line, "to_bus"]
                        if bus_t in self.grid_elem["buses"]:
                            b_t = globals()["bus" + str(b_to)] 
                        else:
                            pass                  
                    globals()["Line" + str(line)] = pp.create_line(self.net, from_bus = b_f, to_bus = b_t, length_km = excel.at[line, "length_km"], in_service = excel.at[line, "in_service"],
                                                                   std_type = excel.at[line, "std_type"], name = excel.at[line, "name"] )
            if self.sheets[i] == "gen":
                excel = pd.read_excel(self.Excel_file, sheet_name = self.sheets[i], index_col = 0)
                for gen in excel.index:
                    gen_load = excel.at[gen, "bus"]
                    if gen_load in self.grid_elem["buses"]:
                        bus_gen = globals()["bus" + str(gen)]
                        globals()["gen" + str(gen)] = pp.create_gen(self.net, bus = bus_gen, p_mw = excel.at[gen, "p_mw"], in_service = excel.at[gen, "in_service"],
                                                                    vm_pu = excel.at[gen, "vm_pu"], name = excel.at[gen, "name"])   
            if self.sheets[i] == "storage":
                excel = pd.read_excel(self.Excel_file, sheet_name = self.sheets[i], index_col = 0)            
                for storage in excel.index:
                    stor_bus = excel.at[storage, "bus"]
                    if stor_bus in self.grid_elem["buses"]:
                        storag_bus = globals()["bus" + str(storage)]
                    else:
                        pass               
                    globals()["storage" + str(storage)] = pp.create_storage(self.net, bus = storag_bus, p_kw = excel.at[storage, "p_kw"], max_e_kwh = excel.at[storage, "max_e_kwh"],
                                                                            p_mw = excel.at[storage, "p_mw"], max_e_mwh = excel.at[storage, "max_e_mwh"], name = excel.at[storage, "name"])
        print(self.net)
        return self.net