from flask import Blueprint, request, jsonify
from utils.event_log_utils import EventLogUtils
import pm4py

process_enhancement_bp = Blueprint('process_enhancement', __name__)

@process_enhancement_bp.route('/enhance_process', methods=['POST'])
def enhance_process():
    data = request.json
    log = EventLogUtils.load_event_log(data['xes_path'])
    # Example process enhancement, can be extended with specific requirements
    enhanced_log = pm4py.algo.enhancement.sna.factory.apply(log)
    return jsonify({'enhanced_log': str(enhanced_log)})
