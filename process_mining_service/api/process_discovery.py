from flask import Blueprint, request, jsonify
import pm4py
from utils.helpers import create_error_response  # Adjust import according to your project structure

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

