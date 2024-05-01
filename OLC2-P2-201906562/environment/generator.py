
class Generator:
    def __init__(self, Tepm, lvl, ContFlot, ContStr):
        self.Temporal = 0x10000000 + Tepm
        self.ContTemp = 0; 
        self.Label = 0 + lvl
        self.CrtlFloat = 0 + ContFlot
        self.CrtlString = 0 + ContStr
        self.Code = []
        self.Data = []
        self.FinalCode = []
        self.Natives = []
        self.FuncCode = []
        self.TempList = []
        self.PrintStringFlag = True
        self.ConcatStringFlag = True
        self.BreakLabel = ""
        self.ContinueLabel = ""
        self.MainCode = False

    def get_code(self):
        return self.Code
    
    def get_finalCOde(self):
        return self.FinalCode

    def get_data(self):
        return self.Data
    
    def get_contemp(self):
        return self.ContTemp
    
    def get_contlvl(self):
        return self.Label
    
    def get_conflo(self):
        return self.CrtlFloat
    
    def get_constr(self):
        return self.CrtlString

    def get_final_code(self):
        self.add_headers()
        self.add_footers()
        outstring = "".join(self.Code)

        return outstring

    def get_temps(self):
        return self.TempList

    def add_break(self, lvl):
        self.BreakLabel = lvl

    def add_code(self, code):
        self.Code.append(code)
    
    def add_data_code(self, code):
        self.Data.append(code)

    def add_continue(self, lvl):
        self.ContinueLabel = lvl

    def new_temp(self):
        self.Temporal += 4
        self.ContTemp += 0
        return self.Temporal
    
    def new_string(self):
        self.CrtlString += 1
        return self.CrtlString
    
    def new_float(self):
        self.CrtlFloat += 1
        return self.CrtlFloat

    def new_label(self):
        temp = self.Label
        self.Label += 1
        return "L" + str(temp)

    def add_br(self):
        self.Code.append("\n")

    def comment(self, txt):
        self.Code.append(f"### {txt} \n")

    def variable_data(self, name, type, value):
        self.Data.append(f"{name}: .{type} {value} \n")

    def add_and(self, left, right, inter):
        self.Code.append(f"\tand {left}, {right}, {inter}\n")
   
    def add_or(self, left, right, inter):
        self.Code.append(f"\tor {left}, {right}, {inter}\n")
   
    def add_seqz(self, left, right):
        self.Code.append(f"\tseqz {left}, {right}\n")

    def add_addi(self, left, right, inter):
        self.Code.append(f"\taddi {left}, {right}, {inter}\n")

    def add_li(self, left, right):
        self.Code.append(f"\tli {left}, {right}\n")

    def add_lb(self, left, right):
        self.Code.append(f"\tlb {left}, {right}\n")

    def add_la(self, left, right):
        self.Code.append(f"\tla {left}, {right}\n")

    def add_lw(self, left, right):
        self.Code.append(f"\tlw {left}, {right}\n")

    def add_sw(self, left, right):
        self.Code.append(f"\tsw {left}, {right}\n")

    def add_sb(self, left, right):
        self.Code.append(f"\tsb {left}, {right}\n")
    
    def add_flw(self, left, right):
        self.Code.append(f"\tflw {left}, {right}, t0\n") 
    
    def add_fgts(self, target, left, right):
        self.Code.append(f"\tfgt.s {target}, {left}, {right}\n")
    
    def add_fges(self, target, left, right):
        self.Code.append(f"\tfge.s {target}, {left}, {right}\n")   
    
    def add_fles(self, target, left, right):
        self.Code.append(f"\tfle.s {target}, {left}, {right}\n")
    
    def add_feqs(self, target, left, right):
        self.Code.append(f"\tfeq.s {target}, {left}, {right}\n")
    
    def add_flts(self, target, left, right):
        self.Code.append(f"\tflt.s {target}, {left}, {right}\n")
    
    def add_fsw(self, left, right):
        self.Code.append(f"\tfsw {left}, {right}, t0\n")
    
    def add_fcvtsw(self, left, right):
        self.Code.append(f"\tfcvt.s.w {left}, {right}\n")

    def add_slli(self, target, left, right):
        self.Code.append(f"\tslli {target}, {left}, {right}\n")
    
    def add_slt(self, target, left, right):
        self.Code.append(f"\tslt {target}, {left}, {right}\n")

    def add_blt(self, left, right, target):
        self.Code.append(f"\tblt {left}, {right}, {target}\n")

    def add_bgt(self, left, right, target):
        self.Code.append(f"\tbgt {left}, {right}, {target}\n")

    def add_bge(self, left, right, target):
        self.Code.append(f"\tbge {left}, {right}, {target}\n")

    def add_ble(self, left, right, target):
        self.Code.append(f"\tble {left}, {right}, {target}\n")

    def add_blez(self, left, right, target):
        self.Code.append(f"\tblez {left}, {right}, {target}\n")

    def add_beq(self, left, right, target):
        self.Code.append(f"\tbeq {left}, {right}, {target}\n")

    def add_bne(self, left, right, target):
        self.Code.append(f"\tbne {left}, {right}, {target}\n")
    
    def add_beqz(self, left, target):
        self.Code.append(f"\tbeqz {left}, {target}\n")

    def add_jump(self, lvl):
        self.Code.append(f"\tj {lvl}\n")

    def new_body_label(self, lvl):
        self.Code.append(f"{lvl}:\n")

    def add_move(self, left, right):
        self.Code.append(f"\tmv {left}, {right}\n")

    def add_operation(self, operation, target, left, right):
        self.Code.append(f"\t{operation} {target}, {left}, {right}\n")

    def add_system_call(self):
        self.Code.append('\tecall\n')

    def add_headers(self):
        self.Code.insert(0,'\n.text\n.globl _start\n\n_start:\n')
        self.Data.insert(0,'msg_true: .asciz \"true\"\n')
        self.Data.insert(0,'msg_false: .asciz \"false\"\n')
        self.Data.insert(0,'msg_null: .asciz \"null\"\n')
        self.Data.insert(0,'.data\n')
        self.Code[:0] = self.Data
            
    def add_footers(self):
        self.Code.append('\n\tli a0, 0\n')
        self.Code.append('\tli a7, 93\n')
        self.Code.append('\tecall\n')