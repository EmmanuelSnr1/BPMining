from flask import Blueprint, request, jsonify
from utils.event_log_utils import EventLogUtils
import pm4py

petri_nets_tools_bp = Blueprint('petri_nets_tools', __name__)

@petri_nets_tools_bp.route('/analyze_petri_net', methods=['POST'])
def analyze_petri_net():
    data = request.json
    log = EventLogUtils.load_event_log(data['xes_path'])
    net, initial_marking, final_marking = pm4py.discover_petri_net_inductive(log)
    analysis = pm4py.algo.analysis.petrinet.factory.apply(net, initial_marking)
    return jsonify({'analysis': str(analysis)})
