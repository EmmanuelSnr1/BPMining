from flask import Blueprint, request, jsonify
import pm4py
from pm4py.statistics.traces.generic.log import case_statistics
from pm4py.statistics.end_activities.log import get as get_end_activities
from pm4py.statistics.start_activities.log import get as get_start_activities
from pm4py.statistics.variants.log import get as variants_module
from utils.helpers import create_error_response

overview_bp = Blueprint('overview', __name__)

@overview_bp.route('/process_overview', methods=['POST'])
def process_overview():
    data = request.json
    if 'xes_path' not in data:
        return create_error_response('xes_path not found in request', 400)

    xes_path = data['xes_path']

    try:
        # Load the event log
        event_log = pm4py.read_xes(xes_path)

        # 1. Number of Events
        num_events = sum([len(trace) for trace in event_log])

        # 2. Number of Cases (Traces)
        num_cases = len(event_log)

        # 3. Number of Unique Activities (Ensure events are dictionaries)
        activities = set()
        for trace in event_log:
            for event in trace:
                if isinstance(event, dict) and "concept:name" in event:
                    activities.add(event["concept:name"])
        
        num_activities = len(activities)

        # 4. Throughput Time (Per Case)
        case_durations = case_statistics.get_all_case_durations(event_log)
        average_throughput_time = sum(case_durations) / len(case_durations) if case_durations else 0

        # 5. Variants (Unique Process Paths)
        variants = variants_module.get_variants(event_log)  # Ensure correct usage of the method
        num_variants = len(variants)
        top_variants = sorted(variants.items(), key=lambda x: len(x[1]), reverse=True)[:3]

        # 6. Start and End Activities
        start_activities = get_start_activities.get_start_activities(event_log)  # Correct call from the module
        end_activities = get_end_activities.get_end_activities(event_log)  # Correct call from the module

        # Build the response JSON
        overview_data = {
            'num_events': num_events,
            'num_cases': num_cases,
            'num_activities': num_activities,
            'average_throughput_time': average_throughput_time,
            'num_variants': num_variants,
            'top_variants': [
                {"variant": variant, "num_cases": len(cases)}
                for variant, cases in top_variants
            ],
            'start_activities': start_activities,
            'end_activities': end_activities
        }

        return jsonify(overview_data)

    except Exception as e:
        return create_error_response(f"Error processing process overview: {str(e)}", 500)