from flask import Blueprint, request, jsonify
import pm4py

process_discovery_bp = Blueprint('process_discovery', __name__)

@process_discovery_bp.route('/inductive', methods=['POST'])
def discover_process_using_inductive():
    data = request.json 
    log = pm4py.read_xes(data['xes_path'])
    net, initial_marking, final_marking = pm4py.discover_petri_net_inductive(log)
    return jsonify({'net': str(net), 'initial_marking': str(initial_marking), 'final_marking': str(final_marking)})

@process_discovery_bp.route('/alpha', methods=['POST'])
def discover_process_using_alpha():
    data = request.json
    log = pm4py.read_xes(data['xes_path'])
    net, initial_marking, final_marking = pm4py.discover_petri_net_alpha(log)
    return jsonify({'net': str(net), 'initial_marking': str(initial_marking), 'final_marking': str(final_marking)})

@process_discovery_bp.route('/heuristics', methods=['POST'])
def discover_process_using_heuristics():
    data = request.json
    log = pm4py.read_xes(data['xes_path'])
    heu_net = pm4py.discover_heuristics_net(log)
    return jsonify({'heuristics_net': str(heu_net)})
