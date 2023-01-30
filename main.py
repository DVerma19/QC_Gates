from flask import Flask, render_template, request
from qiskit import *
import json, requests
from flaskwebgui import FlaskUI
from qiskit.circuit.library import *
from qiskit.circuit import Parameter
from matplotlib import pyplot as plt
import io
import random
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from qiskit.visualization import plot_histogram, plot_bloch_multivector

app = Flask(__name__)


@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

## Example Gates

def c3sx_example():
    test_qc = QuantumCircuit(4)
    test_qc.append(C3SXGate(), [0,1,2,3])
    fig = test_qc.draw(output='mpl')
    fig.savefig('./static/images/c3sx_qc.png')
    

def c3x_example():
    test_qc = QuantumCircuit(5)
    test = C3XGate()
    test_qc.append(test, [3,2,1,4])
    fig = test_qc.draw(output='mpl')
    fig.savefig('./static/images/c3x_qc.png')

def c4x_example():
    test_qc = QuantumCircuit(5)
    test = C4XGate()
    test_qc.append(test, [3,2,0,4,1])
    fig = test_qc.draw(output='mpl')
    fig.savefig('./static/images/c4x_qc.png')

def ccx_example():
    test_qc= QuantumCircuit(3)
    test = CCXGate()
    test_qc.append(test, [0,1,2])
    fig = test_qc.draw(output='mpl')
    fig.savefig('./static/images/ccx_qc.png')

def ccz_example():
    test_qc = QuantumCircuit(3)
    test = CCZGate()
    test_qc.append(test, [2,1,0])
    fig = test_qc.draw(output='mpl')
    fig.savefig('./static/images/ccz_qc.png')

def ch_example():
    test_qc = QuantumCircuit(2)
    test_qc.cx(0,1)
    test_qc.cx(1,0)
    fig = test_qc.draw(output='mpl')
    fig.savefig('./static/images/ch_qc.png')

def cphase_example():
    theta = Parameter('θ')
    test_qc = QuantumCircuit(3)
    test = CPhaseGate(theta)
    test_qc.append(test, [[0,1], [2]])
    fig = test_qc.draw(output='mpl')
    fig.savefig('./static/images/cphase_qc.png')

def crx_example():
    theta = Parameter('θ')
    test_qc= QuantumCircuit(5)
    test = CRXGate(theta)
    test_qc.append(test, [[0,3,4], [2]])
    fig = test_qc.draw(output='mpl')
    fig.savefig('./static/images/crx_qc.png')

def cry_example():
    theta = Parameter('θ')
    test_qc= QuantumCircuit(3)
    test = CRYGate(theta)
    test_qc.append(test, [[0,2], [1]])
    fig = test_qc.draw(output='mpl')
    fig.savefig('./static/images/cry_qc.png')


def crz_example():
    theta = Parameter('θ')
    test_qc= QuantumCircuit(5)
    test = CRZGate(theta)
    test_qc.append(test, [[0,3,4], [1]])
    fig = test_qc.draw(output='mpl')
    fig.savefig('./static/images/crz_qc.png')

def cs_example():
    test_qc = QuantumCircuit(4)
    test = CSGate()
    test_qc.append(test, [[1,2], [0,3]])
    fig = test_qc.draw(output='mpl')
    fig.savefig('./static/images/cs_qc.png')

def csx_example():
    test_qc = QuantumCircuit(4)
    test = CSXGate()
    test_qc.append(test, [[1,2], [0,3]])
    fig = test_qc.draw(output='mpl')
    fig.savefig('./static/images/csx_qc.png')

def csdg_example():
    test_qc = QuantumCircuit(3)
    test = CSdgGate()
    test_qc.append(test, [[1,2], [0,1]])
    fig = test_qc.draw(output='mpl')
    fig.savefig('./static/images/csdg_qc.png')

def cswap_example():
    test_qc = QuantumCircuit(4)
    test = CSwapGate()
    test_qc.append(test, [2,0,3])
    fig = test_qc.draw(output='mpl')
    fig.savefig('./static/images/cswap_qc.png')

def cu1_example():
    theta = Parameter('θ')
    test_qc = QuantumCircuit(3)
    test = CU1Gate(theta)
    test_qc.append(test, [2,0])
    fig = test_qc.draw(output='mpl')
    fig.savefig('./static/images/cu1_qc.png')

def cu3_example():
    theta = Parameter('θ')
    phi = Parameter('ϕ')
    lamda = Parameter('λ')
    test_qc = QuantumCircuit(4)
    test = CU3Gate(theta, phi, lamda)
    test_qc.append(test, [3,1])
    fig = test_qc.draw(output='mpl')
    fig.savefig('./static/images/cu3_qc.png')

def cu_example():
    theta = Parameter('θ')
    phi = Parameter('ϕ')
    lamda = Parameter('λ')
    gamma = Parameter('γ')
    test_qc = QuantumCircuit(4)
    test = CUGate(theta, phi, lamda, gamma)
    test_qc.append(test, [3,1])
    fig = test_qc.draw(output='mpl')
    fig.savefig('./static/images/cu_qc.png')

def cx_example():
    test_qc = QuantumCircuit(4)
    test = CXGate()
    test_qc.append(test, [[1,3], [2]])
    fig = test_qc.draw(output='mpl')
    fig.savefig('./static/images/cx_qc.png')

def cy_example():
    test_qc = QuantumCircuit(4)
    test = CXGate()
    test_qc.append(test, [[1,3], [2]])
    fig = test_qc.draw(output='mpl')
    fig.savefig('./static/images/cy_qc.png')

def cz_example():
    test_qc = QuantumCircuit(4)
    test = CXGate()
    test_qc.append(test, [[1,3], [2]])
    fig = test_qc.draw(output='mpl')
    fig.savefig('./static/images/cz_qc.png')

def h_example():
    test_qc = QuantumCircuit(4)
    test = HGate()
    test_qc.append(test, [[0]])
    fig = test_qc.draw(output='mpl')
    fig.savefig('./static/images/h_qc.png')

def i_example():
    test_qc = QuantumCircuit(4)
    test = IGate()
    test_qc.append(test, [[0,2]])
    fig = test_qc.draw(output='mpl')
    fig.savefig('./static/images/i_qc.png')

def mcphase_example():
    test_qc = QuantumCircuit(4)
    test = MCPhaseGate(90, 2)
    test_qc.append(test, [0,1,2])
    fig = test_qc.draw(output='mpl')
    fig.savefig('./static/images/mcphase_qc.png')

def mcu1_example():
    test_qc = QuantumCircuit(4)
    test = MCU1Gate(90, 2)
    test_qc.append(test, [1,2,3])
    fig = test_qc.draw(output='mpl')
    fig.savefig('./static/images/mcu1_qc.png')

def ms_example():
    test_qc = QuantumCircuit(5)
    test = MSGate(2,90)
    test_qc.append(test, [0,3])
    fig = test_qc.draw(output='mpl')
    fig.savefig('./static/images/ms_qc.png')

def phase_example():
    test_qc = QuantumCircuit(5)
    test = PhaseGate(90)
    test_qc.append(test, [[4,2]])
    fig = test_qc.draw(output='mpl')
    fig.savefig('./static/images/phase_qc.png')

def rc3x_example():
    test_qc = QuantumCircuit(5)
    test = RC3XGate()
    test_qc.append(test, [0,1,2,4])
    fig = test_qc.draw(output='mpl')
    fig.savefig('./static/images/rc3x_qc.png')

def rccx_example():
    test_qc = QuantumCircuit(5)
    test = RCCXGate()
    test_qc.append(test, [0,1,4])
    fig = test_qc.draw(output='mpl')
    fig.savefig('./static/images/rccx_qc.png')

def r_example():
    test_qc = QuantumCircuit(5)
    test = RGate(90,75)
    test_qc.append(test, [[0,1,2]])
    fig = test_qc.draw(output='mpl')
    fig.savefig('./static/images/r_qc.png')

def rx_example():
    test_qc = QuantumCircuit(5)
    test = RXGate(90)
    test_qc.append(test, [[0,1,2]])
    fig = test_qc.draw(output='mpl')
    fig.savefig('./static/images/rx_qc.png')

def rxx_example():
    test_qc = QuantumCircuit(5)
    test = RXXGate(90)
    test_qc.append(test, [[0,1], [3,2]])
    fig = test_qc.draw(output='mpl')
    fig.savefig('./static/images/rxx_qc.png')

def ry_example():
    test_qc = QuantumCircuit(5)
    test = RYGate(90)
    test_qc.append(test, [[0,1,2]])
    fig = test_qc.draw(output='mpl')
    fig.savefig('./static/images/ry_qc.png')

def ryy_example():
    test_qc = QuantumCircuit(5)
    test = RYYGate(90)
    test_qc.append(test, [[3,1], [2,0]])
    fig = test_qc.draw(output='mpl')
    fig.savefig('./static/images/ryy_qc.png')

def rz_example():
    test_qc = QuantumCircuit(5)
    test = RZGate(75)
    test_qc.append(test, [[0,2,4]])
    fig = test_qc.draw(output='mpl')
    fig.savefig('./static/images/rz_qc.png')

def rzx_example():
    test_qc = QuantumCircuit(5)
    test = RZXGate(90)
    test_qc.append(test, [[0,4], [2,2]])
    fig = test_qc.draw(output='mpl')
    fig.savefig('./static/images/rzx_qc.png')

def rzz_example():
    test_qc = QuantumCircuit(5)
    test = RZZGate(90)
    test_qc.append(test, [[2,4], [1,3]])
    fig = test_qc.draw(output='mpl')
    fig.savefig('./static/images/rzz_qc.png')

def s_example():
    test_qc = QuantumCircuit(3)
    test = SGate()
    test_qc.append(test, [[0,1]])
    fig = test_qc.draw(output='mpl')
    fig.savefig('./static/images/s_qc.png')

def sx_example():
    test_qc = QuantumCircuit(3)
    test = SXGate()
    test_qc.append(test, [[0,2]])
    fig = test_qc.draw(output='mpl')
    fig.savefig('./static/images/sx_qc.png')

def sxdg_example():
    test_qc = QuantumCircuit(3)
    test = SXdgGate()
    test_qc.append(test, [[1,2]])
    fig = test_qc.draw(output='mpl')
    fig.savefig('./static/images/sxdg_qc.png')

def swap_example():
    test_qc = QuantumCircuit(5)
    test = SwapGate()
    test_qc.append(test, [[1,2], [3,3]])
    fig = test_qc.draw(output='mpl')
    fig.savefig('./static/images/swap_qc.png')

def t_example():
    test_qc = QuantumCircuit(3)
    test = TGate()
    test_qc.append(test, [[2,1]])
    fig = test_qc.draw(output='mpl')
    fig.savefig('./static/images/t_qc.png')

def tdg_example():
    test_qc = QuantumCircuit(4)
    test = TdgGate()
    test_qc.append(test, [[1,3]])
    fig = test_qc.draw(output='mpl')
    fig.savefig('./static/images/tdg_qc.png')

def x_example():
    test_qc = QuantumCircuit(4)
    test = XGate()
    test_qc.append(test, [[2,3]])
    fig = test_qc.draw(output='mpl')
    fig.savefig('./static/images/x_qc.png')

def y_example():
    test_qc = QuantumCircuit(3)
    test = YGate()
    test_qc.append(test, [[0,2]])
    fig = test_qc.draw(output='mpl')
    fig.savefig('./static/images/y_qc.png')


def z_example():
    test_qc = QuantumCircuit(3)
    test = ZGate()
    test_qc.append(test, [[0,1]])
    fig = test_qc.draw(output='mpl')
    fig.savefig('./static/images/z_qc.png')

## Main Gate Functions

def c3sx_gate_func(gate, qc):
    list = []
    split = gate.split(',')
    for x in split:
        list.append(int(x))
    qc.append(C3SXGate(), list)
    fig = qc.draw(output='mpl')
    fig.savefig('./static/images/qc.png')

def c3x_gate_func(gate, qc):
    list = []
    split = gate.split(',')
    for x in split:
        list.append(int(x))
    qc.append(C3XGate(), list)
    fig = qc.draw(output='mpl')
    fig.savefig('./static/images/qc.png')

def c4x_gate_func(gate, qc):
    list = []
    split = gate.split(',')
    for x in split:
        list.append(int(x))
    qc.append(C4XGate(), list)
    fig = qc.draw(output='mpl')
    fig.savefig('./static/images/qc.png')

def ccx_gate_func(gate, qc):
    list = []
    split = gate.split(',')
    for x in split:
        list.append(int(x))
    qc.append(CCXGate(), list)
    fig = qc.draw(output='mpl')
    fig.savefig('./static/images/qc.png')

def ccz_gate_func(gate, qc):
    list = []
    split = gate.split(',')
    for x in split:
        list.append(int(x))
    qc.append(CCZGate(), list)
    fig = qc.draw(output='mpl')
    fig.savefig('./static/images/qc.png')

def ch_gate_func(gate_one, gate_two, qc):
    list_one = []
    split_one = gate_one.split(',')
    list_two = []
    split_two = gate_two.split(',')

    for x in split_one:
        list_one.append(int(x))
    for x in split_two:
        list_two.append(int(x))

    qc.append(CHGate(), [list_one, list_two])
    fig = qc.draw(output='mpl')
    fig.savefig('./static/images/qc.png')

def cphase_gate_func(gate_one, gate_two, qc):
    theta = Parameter('θ')
    list_one = []
    split_one = gate_one.split(',')
    list_two = []
    split_two = gate_two.split(',')

    for x in split_one:
        list_one.append(int(x))
    for x in split_two:
        list_two.append(int(x))

    qc.append(CPhaseGate(90), [list_one, list_two])
    fig = qc.draw(output='mpl')
    fig.savefig('./static/images/qc.png')

def crx_gate_func(gate_one, gate_two, qc):
    phi = Parameter('phi')
    list_one = []
    split_one = gate_one.split(',')
    list_two = []
    split_two = gate_two.split(',')

    for x in split_one:
        list_one.append(int(x))
    for x in split_two:
        list_two.append(int(x))

    qc.append(CRXGate(90), [list_one, list_two])
    fig = qc.draw(output='mpl')
    fig.savefig('./static/images/qc.png')
    print(qc)

def cry_gate_func(gate_one, gate_two, qc):
    omega = Parameter('omega')
    list_one = []
    split_one = gate_one.split(',')
    list_two = []
    split_two = gate_two.split(',')

    for x in split_one:
        list_one.append(int(x))
    for x in split_two:
        list_two.append(int(x))

    qc.append(CRYGate(90), [list_one, list_two])
    fig = qc.draw(output='mpl')
    fig.savefig('./static/images/qc.png')
    print(qc)

def crz_gate_func(gate_one, gate_two, qc):
    list_one = []
    split_one = gate_one.split(',')
    list_two = []
    split_two = gate_two.split(',')

    for x in split_one:
        list_one.append(int(x))
    for x in split_two:
        list_two.append(int(x))

    qc.append(CRZGate(90), [list_one, list_two])
    fig = qc.draw(output='mpl')
    fig.savefig('./static/images/qc.png')
    print(qc)

def cs_gate_func(gate_one, gate_two, qc):
    list_one = []
    split_one = gate_one.split(',')
    list_two = []
    split_two = gate_two.split(',')

    for x in split_one:
        list_one.append(int(x))
    for x in split_two:
        list_two.append(int(x))

    qc.append(CSGate(), [list_one, list_two])
    fig = qc.draw(output='mpl')
    fig.savefig('./static/images/qc.png')
    print(qc)

def csx_gate_func(gate_one, gate_two, qc):
    list_one = []
    split_one = gate_one.split(',')
    list_two = []
    split_two = gate_two.split(',')

    for x in split_one:
        list_one.append(int(x))
    for x in split_two:
        list_two.append(int(x))

    qc.append(CSXGate(), [list_one, list_two])
    fig = qc.draw(output='mpl')
    fig.savefig('./static/images/qc.png')
    print(qc)

def csdg_gate_func(gate_one, gate_two, qc):
    list_one = []
    split_one = gate_one.split(',')
    list_two = []
    split_two = gate_two.split(',')

    for x in split_one:
        list_one.append(int(x))
    for x in split_two:
        list_two.append(int(x))

    qc.append(CSdgGate(), [list_one, list_two])
    fig = qc.draw(output='mpl')
    fig.savefig('./static/images/qc.png')
    print(qc)

def cswap_gate_func(gate, qc):
    list = []
    split = gate.split(',')
    for x in split:
        list.append(int(x))
    qc.append(CSwapGate(), list)
    fig = qc.draw(output='mpl')
    fig.savefig('./static/images/qc.png')
    print(qc)

def cu1_gate_func(gate, qc):
    list = []
    split = gate.split(',')
   
    for x in split:
        list.append(int(x))
    
    qc.append(CU1Gate(90), list)
    fig = qc.draw(output='mpl')
    fig.savefig('./static/images/qc.png')
    print(qc)

def cu3_gate_func(gate, qc):
    list = []
    split = gate.split(',')
   
    for x in split:
        list.append(int(x))
    
    qc.append(CU3Gate(90, 75, 45), list)
    fig = qc.draw(output='mpl')
    fig.savefig('./static/images/qc.png')
    print(qc)

def cu_gate_func(gate,qc):
    list = []
    split = gate.split(',')

    for x in split:
        list.append(int(x))

    qc.append(CUGate(90, 75, 45, 30), list)
    fig = qc.draw(output='mpl')
    fig.savefig('./static/images/qc.png')
    print(qc)

def cx_gate_func(gate_one, gate_two, qc):
    list_one = []
    split_one = gate_one.split(',')
    list_two = []
    split_two = gate_two.split(',')

    for x in split_one:
        list_one.append(int(x))
    for x in split_two:
        list_two.append(int(x))

    qc.append(CXGate(), [list_one, list_two])
    fig = qc.draw(output='mpl')
    fig.savefig('./static/images/qc.png')
    print(qc)

def cy_gate_func(gate_one, gate_two, qc):
    list_one = []
    split_one = gate_one.split(',')
    list_two = []
    split_two = gate_two.split(',')

    for x in split_one:
        list_one.append(int(x))
    for x in split_two:
        list_two.append(int(x))

    qc.append(CYGate(), [list_one, list_two])
    fig = qc.draw(output='mpl')
    fig.savefig('./static/images/qc.png')
    print(qc)

def cz_gate_func(gate_one, gate_two, qc):
    list_one = []
    split_one = gate_one.split(',')
    list_two = []
    split_two = gate_two.split(',')

    for x in split_one:
        list_one.append(int(x))
    for x in split_two:
        list_two.append(int(x))

    qc.append(CZGate(), [list_one, list_two])
    fig = qc.draw(output='mpl')
    fig.savefig('./static/images/qc.png')
    print(qc)


def h_gate_func(gate,qc):
    list = []
    split = gate.split(',')

    for x in split:
        list.append(int(x))

    qc.append(HGate(), [list])
    fig = qc.draw(output='mpl')
    fig.savefig('./static/images/qc.png')
    print(qc)


def i_gate_func(gate,qc):
    list = []
    split = gate.split(',')

    for x in split:
        list.append(int(x))

    qc.append(IGate(), [list])
    fig = qc.draw(output='mpl')
    fig.savefig('./static/images/qc.png')
    print(qc)

def mcphase_gate_func(cbit,gate,qc):
    list = []
    split = gate.split(',')

    for x in split:
        list.append(int(x))
    
    qc.append(MCPhaseGate(90, int(cbit)), list)
    fig = qc.draw(output='mpl')
    fig.savefig('./static/images/qc.png')
    print(qc)

def mcu1_gate_func(cbit,gate,qc):
    list = []
    split = gate.split(',')

    for x in split:
        list.append(int(x))
    
    qc.append(MCU1Gate(90, int(cbit)), list)
    fig = qc.draw(output='mpl')
    fig.savefig('./static/images/qc.png')
    print(qc)


def s_gate_func(gate,qc):
    list = []
    split = gate.split(',')

    for x in split:
        list.append(int(x))

    qc.append(SGate(), [list])
    fig = qc.draw(output='mpl')
    fig.savefig('./static/images/qc.png')
    print(qc)

def x_gate_func(gate,qc):
    list = []
    split = gate.split(',')

    for y in split:
        list.append(int(y))

    qc.append(XGate(), [list])
    fig = qc.draw(output='mpl')
    fig.savefig('./static/images/qc.png')
    print(qc)

def y_gate_func(gate,qc):
    list = []
    split = gate.split(',')

    for x in split:
        list.append(int(x))

    qc.append(YGate(), [list])
    fig = qc.draw(output='mpl')
    fig.savefig('./static/images/qc.png')
    print(qc)

def z_gate_func(gate,qc):
    list = []
    split = gate.split(',')

    for x in split:
        list.append(int(x))

    qc.append(ZGate(), [list])
    fig = qc.draw(output='mpl')
    fig.savefig('./static/images/qc.png')
    print(qc)




@app.route('/')
def index():
    global c3sx_list
    c3sx_list = []

    global steps_instance
    steps_instance = 0
    
    
    ## Gate Example Functions Run
    c3sx_example()
    c3x_example()
    c4x_example()
    ccx_example()
    ccz_example()
    ch_example()
    cphase_example()
    crx_example()
    cry_example()
    crz_example()
    cs_example()
    csx_example()
    csdg_example()
    cswap_example()
    cu1_example()
    cu3_example()
    cu_example()
    cx_example()
    cy_example()
    cz_example()
    h_example()
    i_example()
    mcphase_example()
    mcu1_example()
    ms_example()
    phase_example()
    rc3x_example()
    rccx_example()
    r_example()
    rx_example()
    rxx_example()
    ry_example()
    ryy_example()
    rz_example()
    rzx_example()
    rzz_example()
    s_example()
    sx_example()
    sxdg_example()
    swap_example()
    t_example()
    tdg_example()
    x_example()
    y_example()
    z_example()

    return render_template('index.html')

@app.route('/input_qbits', methods=['POST'])
def input_qbits():
    
    global qc
    global qbit
    global circ
    global user_code
    global control_h_example_qc
    global c3sx_list
    global c3sx_example
    global c3x_example
    global c4x_example
    global ccx_example
    global ccz_example
    global cphase_example
    global crx_example
    global cry_example
    global crz_example
    global cs_example
    global csx_example
    global csdg_example
    global cswap_example
    global cu1_example
    global cu3_example
    global cu_example

    global steps
    global step_details
    steps = []
    step_details = []

    qbit = request.form['qbit_number_circuit']

    if(len(qbit) == 0):
        error = "Enter an Integer"
        return render_template("index.html", qbit=qbit, error=error)
    
    elif(int(qbit) <= 0):
        error = "Enter an input greater than 0"
        return render_template("index.html", qbit=qbit, error=error)

    else:
        qbit = int(qbit)


    qc = 0
    circ = QuantumRegister(qbit)
    qc = QuantumCircuit(circ)
    fig = qc.draw(output='mpl')
    fig.savefig('./static/images/qc.png')
    
    return render_template("index.html", qc=qc, qbit=qbit, url="./static/images/qc.png")

@app.route('/gates_to_circuit', methods=['POST'])
def gates_to_circuit():
    global qc
    global qbit
    global applied_gates_information
    global steps_instance
    applied_gates_information = "Gates have been applied!"
    global c3sx_list
    global c3sx_i

    global display_flag

    c3sx_gate = request.form['C3SX_input']
    c3x_gate = request.form['C3X_input']
    c4x_gate = request.form['C4X_input']
    ccx_gate = request.form['CCX_input']
    ccz_gate = request.form['CCZ_input']
    ch_gate_one = request.form['CH_input_one']
    ch_gate_two = request.form['CH_input_two']
    cphase_gate_one = request.form['CPhase_input_one']
    cphase_gate_two = request.form['CPhase_input_two']
    crx_gate_one = request.form['CRX_input_one']
    crx_gate_two = request.form['CRX_input_two']
    cry_gate_one = request.form['CRY_input_one']
    cry_gate_two = request.form['CRY_input_two']
    crz_gate_one = request.form['CRZ_input_one']
    crz_gate_two = request.form['CRZ_input_two']
    cs_gate_one = request.form['CS_input_one']
    cs_gate_two = request.form['CS_input_two']
    csx_gate_one = request.form['CSX_input_one']
    csx_gate_two = request.form['CSX_input_two']
    csdg_gate_one = request.form['CSdg_input_one']
    csdg_gate_two = request.form['CSdg_input_two']
    cswap_gate = request.form['CSwap_input']
    cu1_gate = request.form['CU1_input']
    cu3_gate = request.form['CU3_input']
    cu_gate = request.form['CU_input']
    cx_gate_one = request.form['CX_input_one']
    cx_gate_two = request.form['CX_input_two']
    cy_gate_one = request.form['CY_input_one']
    cy_gate_two = request.form['CY_input_two']
    cz_gate_one = request.form['CZ_input_one']
    cz_gate_two = request.form['CZ_input_two']
    h_gate = request.form['h_input']
    i_gate = request.form['i_input']
    mcphase_gate_cbit = request.form['mcphase_control_bits_input']
    mcphase_gate = request.form['mcphase_input']
    s_gate = request.form['s_input']
    x_gate = request.form['x_input']
    y_gate = request.form['y_input']
    z_gate = request.form['z_input']
    
    

    if(c3sx_gate):
        c3sx_gate_func(c3sx_gate, qc)
        steps.append(qc.data[steps_instance][0].name)
        step_details.append(qc.data[steps_instance])
        steps_instance += 1

    if(c3x_gate):
        c3x_gate_func(c3x_gate, qc)
        steps.append(qc.data[steps_instance][0].name)
        step_details.append(qc.data[steps_instance])
        steps_instance += 1



    if(c4x_gate):
        c4x_gate_func(c4x_gate, qc)
        steps.append(qc.data[steps_instance][0].name)
        steps_instance += 1
        

    if(ccx_gate):
       ccx_gate_func(ccx_gate, qc)
       steps.append(qc.data[steps_instance][0].name)
       steps_instance += 1

    if(ccz_gate):
        ccz_gate_func(ccz_gate, qc)
        steps.append(qc.data[steps_instance][0].name)
        steps_instance += 1


    if(ch_gate_one and ch_gate_two):
        ch_gate_func(ch_gate_one,ch_gate_two,qc)
        steps.append(qc.data[steps_instance][0].name)
        steps_instance += 1


    if(cphase_gate_one and cphase_gate_two):
        cphase_gate_func(cphase_gate_one,cphase_gate_two,qc)
        steps.append(qc.data[steps_instance][0].name)
        steps_instance += 1


    if(crx_gate_one and crx_gate_two):
        crx_gate_func(crx_gate_one,crx_gate_two,qc)
        steps.append(qc.data[steps_instance][0].name)
        steps_instance += 1

    if(cry_gate_one and cry_gate_two):
        cry_gate_func(cry_gate_one,cry_gate_two,qc)
        steps.append(qc.data[steps_instance][0].name)
        steps_instance += 1


    if(crz_gate_one and crz_gate_two):
        crz_gate_func(crz_gate_one,crz_gate_two,qc)
        steps.append(qc.data[steps_instance][0].name)
        steps_instance += 1


    if(cs_gate_one and cs_gate_two):
        cs_gate_func(cs_gate_one, cs_gate_two,qc)
        steps.append(qc.data[steps_instance][0].name)
        steps_instance += 1


    if(csx_gate_one and csx_gate_two):
        csx_gate_func(csx_gate_one, csx_gate_two, qc)
        steps.append(qc.data[steps_instance][0].name)
        steps_instance += 1

    
    if(csdg_gate_one and csdg_gate_two):
        csdg_gate_func(csdg_gate_one, csdg_gate_two, qc)
        steps.append(qc.data[steps_instance][0].name)
        steps_instance += 1

    
    if(cswap_gate):
       cswap_gate_func(cswap_gate, qc)
       steps.append(qc.data[steps_instance][0].name)
       steps_instance += 1

    
    if(cu1_gate):
        cu1_gate_func(cu1_gate, qc)
        steps.append(qc.data[steps_instance][0].name)
        steps_instance += 1
    
    if(cu3_gate):
        cu3_gate_func(cu3_gate, qc)
        steps.append(qc.data[steps_instance][0].name)
        steps_instance += 1

    if(cu_gate):
        cu_gate_func(cu_gate, qc)
        steps.append(qc.data[steps_instance][0].name)
        steps_instance += 1

    if(cx_gate_one and cx_gate_two):
        cx_gate_func(cx_gate_one, cx_gate_two, qc)
        steps.append(qc.data[steps_instance][0].name)
        steps_instance += 1

    if(cy_gate_one and cy_gate_two):
        cx_gate_func(cy_gate_one, cy_gate_two, qc)
        steps.append(qc.data[steps_instance][0].name)
        steps_instance += 1
    
    if(cz_gate_one and cz_gate_two):
        cx_gate_func(cz_gate_one, cz_gate_two, qc)
        steps.append(qc.data[steps_instance][0].name)
        steps_instance += 1

    if(h_gate):
        h_gate_func(h_gate, qc)
        steps.append(qc.data[steps_instance][0].name)
        steps_instance += 1

    if(i_gate):
        i_gate_func(i_gate, qc)
        steps.append(qc.data[steps_instance][0].name)
        steps_instance += 1
    
    if(mcphase_gate_cbit and mcphase_gate):
        mcphase_gate_func(mcphase_gate_cbit, mcphase_gate, qc)
        steps.append(qc.data[steps_instance][0].name)
        steps_instance += 1

    if(s_gate):
        s_gate_func(s_gate, qc)
        steps.append(qc.data[steps_instance][0].name)
        steps_instance += 1

    if(x_gate):
        x_gate_func(x_gate, qc)
        steps.append(qc.data[steps_instance][0].name)
        steps_instance += 1

    if(y_gate):
        y_gate_func(y_gate, qc)
        steps.append(qc.data[steps_instance][0].name)
        steps_instance += 1

    if(z_gate):
        z_gate_func(z_gate, qc)
        steps.append(qc.data[steps_instance][0].name)
        steps_instance += 1

    print()
    global length_steps
    length_steps = len(steps)

    display_flag = "Test Value to display"
    
    return render_template('index.html', url="./static/images/qc.png", qc=qc,qbit=qbit, applied_gates_information=applied_gates_information, steps=steps, length_steps=length_steps,display_flag=display_flag)

@app.route('/measure_circuit')
def measure_circuit():
    global qc
    global steps
    global length_steps
    global steps_instance
    global display_flag
    global display_flag_vol

    backend = BasicAer.get_backend('qasm_simulator')
    qc.measure_all()
    result = backend.run(transpile(qc, backend), shots=1024).result()
    counts  = result.get_counts(qc)
    fig = plot_histogram(counts)
    fig.savefig('./static/images/plot.png')

    display_flag_vol = "Display Vol"

    backend = BasicAer.get_backend('statevector_simulator')
    result = backend.run(transpile(qc, backend)).result()
    psi  = result.get_statevector(qc)
    fig = plot_bloch_multivector(psi)
    fig.savefig('./static/images/bloch_sphere.png')
    print(qc)
    print(counts)
    qc.remove_final_measurements()
    print(qc)
    return render_template('index.html', qc=qc, qbit=qbit, url="./static/images/qc.png", length_steps=length_steps, plot_url="./static/images/plot.png", plot='plot', sphere_url="./static/images/bloch_sphere.png", steps=steps, display_flag=display_flag, display_flag_vol=display_flag_vol)

@app.route('/qc_gate_delete', methods=['POST'])
def qc_gate_delete():
    global qc
    global steps
    global length_steps
    global steps_instance
    global display_flag
    global display_flag_vol

    display_flag = "Test Value to display"
    test_list = []
    categories = request.form.getlist('gates_deletion')

    for x in (categories):
        for y in sorted(steps):
            if str(x.replace("`", "")) == str(y):
                qc.data.pop(steps.index(y))
                steps.pop(steps.index(y))
                fig = qc.draw(output='mpl')
                fig.savefig('./static/images/qc.png')
                steps_instance -=1
    

    return render_template('index.html', qc=qc, qbit=qbit, url="./static/images/qc.png", length_steps=length_steps, plot_url="./static/images/plot.png", sphere_url="./static/images/bloch_sphere.png", steps=steps, display_flag=display_flag, display_flag_vol=display_flag_vol)

def start_flask(**server_kwargs):
    app = server_kwargs.pop("app", None)
    server_kwargs.pop("debug", None)

    try:
        import waitress

        waitress.serve(app, **server_kwargs)
    except:
        app.run(**server_kwargs)


if __name__ == "__main__":
    # app.run(debug=True)

    # FlaskUI(
    #     app=app,
    #     server="flask",
    #     width=1920,
    #     height=1090,
    #     port=8080
    # ).run()

    app.run(port=8080)