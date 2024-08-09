from flask import Blueprint, request, jsonify
from utils.event_log_utils import EventLogUtils
import pm4py

performance_analysis_bp = Blueprint('performance_analysis', __name__)

@performance_analysis_bp.route('/analyze_performance', methods=['POST'])
def analyze_performance():
    data = request.json
    log = EventLogUtils.load_event_log(data['xes_path'])
    # Example performance analysis, can be extended with specific requirements
    performance = pm4py.algo.filtering.log.attributes.log_filter.apply(log, 'concept:name', values=['A', 'B'])
    return jsonify({'performance': str(performance)})
