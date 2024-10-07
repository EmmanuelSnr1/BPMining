from flask import Blueprint, request, jsonify
import pm4py
import xmltodict
from utils.helpers import create_error_response 
import io
import tempfile
import os
from pm4py.objects.bpmn.exporter import exporter as bpmn_exporter
from pm4py.algo.discovery.dfg import algorithm as dfg_algorithm  # Correct import



process_discovery_bp = Blueprint('process_discovery', __name__)

@process_discovery_bp.route('/inductive', methods=['POST'])
def discover_process_using_inductive():
    data = request.json
    if 'xes_path' not in data:
        return create_error_response('xes_path not found in request', 400)
    try:
        log = pm4py.read_xes(data['xes_path'])
        net, initial_marking, final_marking = pm4py.discover_petri_net_inductive(log)
        return jsonify({'net': str(net), 'initial_marking': str(initial_marking), 'final_marking': str(final_marking)})
    except Exception as e:
        return create_error_response(f"Error processing inductive discovery: {str(e)}", 500)

@process_discovery_bp.route('/alpha', methods=['POST'])
def discover_process_using_alpha():
    data = request.json
    if 'xes_path' not in data:
        return create_error_response('xes_path not found in request', 400)
    try:
        log = pm4py.read_xes(data['xes_path'])
        net, initial_marking, final_marking = pm4py.discover_petri_net_alpha(log)
        return jsonify({'net': str(net), 'initial_marking': str(initial_marking), 'final_marking': str(final_marking)})
    except Exception as e:
        return create_error_response(f"Error processing alpha discovery: {str(e)}", 500)

@process_discovery_bp.route('/heuristics', methods=['POST'])
def discover_process_using_heuristics():
    data = request.json
    if 'xes_path' not in data:
        return create_error_response('xes_path not found in request', 400)
    try:
        log = pm4py.read_xes(data['xes_path'])
        heu_net = pm4py.discover_heuristics_net(log)
        return jsonify({'heuristics_net': str(heu_net)})
    except Exception as e:
        return create_error_response(f"Error processing heuristics discovery: {str(e)}", 500)
# Discover Directly Follows Graph (DFG)
@process_discovery_bp.route('/dfg', methods=['POST'])
def discover_directly_follows_graph():
    data = request.json
    if 'xes_path' not in data:
        return create_error_response('xes_path not found in request', 400)
    try:
        # Read the log file
        log = pm4py.read_xes(data['xes_path'])
        
        # Discover the Directly Follows Graph (DFG) using the correct method
        dfg = dfg_algorithm.apply(log)
        
        # Convert the DFG to a JSON-friendly format
        dfg_json = convert_to_dfg_json(dfg)
        
        return jsonify({'directly_follows_graph': dfg_json})
    except Exception as e:
        return create_error_response(f"Error processing DFG discovery: {str(e)}", 500)


def convert_to_dfg_json(dfg):
    # Convert DFG to a list of edges and their frequencies
    dfg_edges = [{"source": str(source), "target": str(target), "frequency": frequency}
                 for (source, target), frequency in dfg.items()]

    # Convert the DFG to a JSON-friendly structure
    return {"edges": dfg_edges}
# Addition of BPMN Just for visualisation. 

# Discover BPMN model using Inductive Miner
@process_discovery_bp.route('/bpmn/inductive', methods=['POST'])
def discover_bpmn_using_inductive():
    data = request.json
    if 'xes_path' not in data:
        return create_error_response('xes_path not found in request', 400)
    try:
        # Read the log file
        log = pm4py.read_xes(data['xes_path'])
        
        # Discover the BPMN process model using the inductive miner
        bpmn_model = pm4py.discover_bpmn_inductive(log)
        
        # Convert the BPMN model to a JSON-friendly format
        bpmn_json = convert_to_bpmn_json(bpmn_model)
        
        return jsonify({'bpmn_model': bpmn_json})
    except Exception as e:
        return create_error_response(f"Error processing BPMN inductive discovery: {str(e)}", 500)


def convert_to_bpmn_json(bpmn_model):
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".bpmn") as temp_file:
        temp_file_path = temp_file.name

    try:
        # Export the BPMN model to the temporary file
        bpmn_exporter.apply(bpmn_model, temp_file_path)

        # Read the BPMN XML from the file
        with open(temp_file_path, 'r', encoding='utf-8') as f:
            bpmn_xml = f.read()

        # Convert the BPMN XML string to a JSON-friendly Python dictionary
        bpmn_dict = xmltodict.parse(bpmn_xml)

        # Return the JSON-friendly dict
        return bpmn_dict

    finally:
        # Clean up the temporary file
        os.remove(temp_file_path)

