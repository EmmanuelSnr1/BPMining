from flask import Blueprint, request, jsonify
from utils.event_log_utils import EventLogUtils
import pm4py

conformance_checking_bp = Blueprint('conformance_checking', __name__)

@conformance_checking_bp.route('/check_conformance', methods=['POST'])
def check_conformance():
    data = request.json
    log = EventLogUtils.load_event_log(data['xes_path'])
    net = data['net']
    initial_marking = data['initial_marking']
    final_marking = data['final_marking']
    alignments = pm4py.algo.conformance.alignments.factory.apply(log, net, initial_marking, final_marking)
    return jsonify({'alignments': str(alignments)})
