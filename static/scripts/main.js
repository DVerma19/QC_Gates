window.onload = () => {
    let qbit_div = document.getElementById('quantum_circuit')
    let qbit_qc_div = document.getElementById('qbit_to_quantum_circuit')
    let qbit_qc_pre = document.getElementById('qbit_quantum_circuit_holder')
    let applied_gates_information = document.getElementById('applied_gates_information')
    let display_flag_p = document.getElementById('display_flag_p')
    let measure_values_div = document.getElementById('measure_values')
    let bloch_sphere_img = document.getElementById('bloch_sphere')
    let plot_graph_img = document.getElementById('plot_graph')
    let display_flag_vol_p = document.getElementById('display_flag_vol_p')

    if(qbit_qc_pre.innerText.length > 0) {
        qbit_div.classList.toggle('fade')
        qbit_qc_div.classList.toggle('fade')
        qbit_qc_div.style.top = "-150px"
        ufade_qbit_to_qc()
    }
    else {qbit_div.style.display = "block"}

    if(applied_gates_information.innerText.length > 0) {
        display_fade_checkbox_gate()
    }

    check_qbit_input(event)

    if(display_flag_p.innerText.length > 0) {
        measure_values_div.style.display = "block"
    }
    
    if(display_flag_vol_p.innerText.length > 0){
        bloch_sphere_img.style.display = "block";
        plot_graph_img.style.display = "block";
    }
}

// Function to Check Qbit Input
function check_qbit_input(event) {
    event.preventDefault()
    let qbit_div_input = document.getElementById('qbit_number_circuit').innerText;
    let qbit_div = document.getElementById('qbit_number_circuit')

    if(qbit_div_input != '' && qbit_div_input != null)
    {
        if(parseInt(qbit_div_input) <= 0) {qbit_div.style.border = "2px solid red"}
    }

}
function fade_qbit() {
    check_qbit_input()
    let qbit_div = document.getElementById('quantum_circuit')
    qbit_div.classList.toggle('fade')
    qbit_div.style.maxHeight = 0;
}

function ufade_qbit_to_qc() {
    let qbit_qc_div = document.getElementById('qbit_to_quantum_circuit')
    var op = 0.1;
    var timer = setInterval(function () {
        if (op >= 1){
            clearInterval(timer);
        }
        qbit_qc_div.style.opacity = op;
        qbit_qc_div.style.filter = 'alpha(opacity=' + op * 100 + ")";
        op += op * 0.1;
    }, 15);

}

function display_fade_checkbox_gate() {
    let checkbox_gate_div = document.getElementById('checkbox_gate_div');

    let qbit_val = parseInt(document.getElementById('qbit_value').innerText)
    if(qbit_val < 5){
        document.getElementById('C4XGate').disabled = true
    }
    if(qbit_val < 4) {
        if(qbit_val >= 3) {
            document.getElementById('C3SXGate').disabled = true
            document.getElementById('C3XGate').disabled = true
            document.getElementById('C4XGate').disabled = true
        }
        if(qbit_val < 3){
            document.getElementById('CCXGate').disabled = true
            document.getElementById('CCZGate').disabled = true
            document.getElementById('CSwapGate').disabled = true
            document.getElementById('C3SXGate').disabled = true
            document.getElementById('C3XGate').disabled = true
            document.getElementById('C4XGate').disabled = true
        }
    }
    checkbox_gate_div.style.display = "block";
    unfade_checkbox_gates();
    checkbox_gate_div.style.top = "-120px"
    

}

function unfade_checkbox_gates() {
    let checkbox_gate_div = document.getElementById('checkbox_gate_div')
    var op = 0.1;
    var timer = setInterval(function () {
        if (op >= 1){
            clearInterval(timer);
        }
        checkbox_gate_div.style.opacity = op;
        checkbox_gate_div.style.filter = 'alpha(opacity=' + op * 100 + ")";
        op += op * 0.1;
    }, 15);

}

function checkbox_gates_submit() {
    let c3sx_gate = document.getElementById('C3SXGate')
    let c3x_gate = document.getElementById('C3XGate')
    let c4x_gate = document.getElementById('C4XGate')
    let ccx_gate = document.getElementById('CCXGate')
    let ccz_gate = document.getElementById('CCZGate')
    let ch_gate = document.getElementById('CHGate')
    let cphase_gate = document.getElementById('CPhaseGate')
    let crx_gate = document.getElementById('CRXGate')
    let cry_gate = document.getElementById('CRYGate')
    let crz_gate = document.getElementById('CRZGate')
    let cs_gate = document.getElementById('CSGate')
    let csx_gate = document.getElementById('CSXGate')
    let csdg_gate = document.getElementById('CSdgGate')
    let cswap_gate = document.getElementById('CSwapGate')
    let cu1_gate = document.getElementById('CU1Gate')
    let cu3_gate = document.getElementById('CU3Gate')
    let cu_gate = document.getElementById('CUGate')
    let cx_gate = document.getElementById('CXGate')
    let cy_gate = document.getElementById('CYGate')
    let cz_gate = document.getElementById('CZGate')
    let h_gate = document.getElementById('HGate')
    let i_gate = document.getElementById('IGate')
    let mcphase_gate = document.getElementById('MCPhaseGate')
    let mcu1_gate = document.getElementById('MCU1Gate')
    let s_gate = document.getElementById('SGate')
    let x_gate = document.getElementById('XGate')
    let y_gate = document.getElementById('YGate')
    let z_gate = document.getElementById('ZGate')

    var gate_list = [c3sx_gate, c3x_gate, c4x_gate, ccx_gate, ccz_gate, ch_gate, cphase_gate, crx_gate, cry_gate, crz_gate, cs_gate, csx_gate,
        csdg_gate, cswap_gate, cu1_gate, cu3_gate, cu_gate, cx_gate, cy_gate, cz_gate, h_gate, i_gate, mcphase_gate, mcu1_gate,
         s_gate, x_gate, y_gate, z_gate]
    
        
        let checked_gates = []
        let divtest = document.getElementById('measure_values')
        divtest.innerHTML = ""
        
    for(let g = 0; g < gate_list.length; g++) {     
        let submit_gates_to_circuit_form_div = document.getElementById('submit_gates_to_circuit_form_div');
        submit_gates_to_circuit_form_div.style.display = 'block'
        let circuit_gate_applier = document.getElementById('circuit_gate_applier');
        circuit_gate_applier.style.display = "block"

        if( gate_list[g].checked) {
            document.getElementById(gate_list[g].id + '_div').style.display = "block";
            checked_gates.push(gate_list[g].id)              
        }
        else{
            document.getElementById(gate_list[g].id + '_div').style.display = "none";

        }
        
    }

    console.log(checked_gates)

    // for(let w = 0; w < checked_gates.length; w++) {
        
    //     var gates_div = document.createElement('div')
    //     gates_div.id = checked_gates[w] + '_div'

    //     var heading = document.createElement('h2')
    //     heading.innerText = checked_gates[w]
        
        

    //     checked_gates[w] = checked_gates[w].replace("Gate", "")
    //     var input = document.createElement('input')
    //     input.id = checked_gates[w] +  '_input'
    //     input.type = "text"

    //     var btn = document.createElement('button')
    //     main_function = checked_gates[w] + '_show'
    //     btn.id = main_function

    //     gates_div.append(heading)
    //     gates_div.append(input)
    //     gates_div.append(btn)
    //     divtest.append(gates_div)
    // }
    
}