from flask import Flask, Blueprint, request, jsonify
import pm4py
import pandas as pd
import logging

performance_analysis_bp = Blueprint('performance_analysis', __name__)
logging.basicConfig(level=logging.INFO)

def read_log_file(xes_path):
    try:
        if xes_path.endswith('.xes'):
            log = pm4py.read_xes(xes_path)
        elif xes_path.endswith('.csv'):
            df = pd.read_csv(xes_path)
            log = pm4py.convert_to_event_log(df)
        else:
            raise ValueError("Unsupported file format")
        return log
    except Exception as e:
        logging.error(f"Error reading log file: {e}")
        raise

@performance_analysis_bp.route('/case_duration', methods=['POST'])
def analyze_case_duration():
    data = request.json
    if 'xes_path' not in data:
        return jsonify({'error': 'xes_path not found in request'}), 400
    
    try:
        log = read_log_file(data['xes_path'])
        case_durations = pm4py.statistics.traces.generic.log.case_statistics.get_all_case_durations(log)
        logging.info(f"Case durations: {case_durations}")
        
        if isinstance(case_durations, list) and all(isinstance(duration, float) for duration in case_durations):
            performance_map = {str(index): duration for index, duration in enumerate(case_durations)}
        else:
            performance_map = {case['case_id']: case['duration'] for case in case_durations}

        return jsonify({'performance_map': performance_map})
    
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return jsonify({'error': 'An error occurred while processing the request'}), 500

@performance_analysis_bp.route('/frequency', methods=['POST'])
def analyze_frequency():
    data = request.json
    if 'xes_path' not in data:
        return jsonify({'error': 'xes_path not found in request'}), 400
    
    try:
        log = read_log_file(data['xes_path'])
    
        from pm4py.statistics.variants.log import get as variants_get
        variants = variants_get.get_variants(log)
        
        logging.info(f"Variants: {variants}")
        
        # Convert tuple keys to string for compatibility
        frequency_map = {str(variant): len(variants[variant]) for variant in variants}
        
        return jsonify({'frequency_map': frequency_map})
    
    except Exception as e:
        logging.error(f"Error analyzing frequency: {e}")
        return jsonify({'error': 'An error occurred while processing the request'}), 500
@performance_analysis_bp.route('/resource_utilization', methods=['POST'])
def analyze_resource_utilization(): 
    data = request.json
    if 'xes_path' not in data:
        return jsonify({'error': 'xes_path not found in request'}), 400
    
    try:
        log = read_log_file(data['xes_path'])
        
        from pm4py.statistics.attributes.log import get as attributes_get
        resource_utilization = attributes_get.get_attribute_values(log, attribute_key='org:resource')
        
        logging.info(f"Resource Utilization: {resource_utilization}")
        
        utilization_map = {resource: utilization for resource, utilization in resource_utilization.items()}
        
        return jsonify({'utilization_map': utilization_map})
    
    except Exception as e:
        logging.error(f"Error analyzing resource utilization: {e}")
        return jsonify({'error': 'An error occurred while processing the request'}), 500

@performance_analysis_bp.route('/bottlenecks', methods=['POST'])
def analyze_bottlenecks():
    data = request.json
    if 'xes_path' not in data:
        return jsonify({'error': 'xes_path not found in request'}), 400
    
    try:
        # Read the log file into a DataFrame
        log = read_log_file(data['xes_path'])
        
        # Check the structure of the DataFrame
        logging.info(f"Log type: {type(log)}")
        if isinstance(log, pd.DataFrame):
            logging.info(f"Log DataFrame head:\n{log.head()}")
        else:
            logging.error("Log data is not in the expected DataFrame format.")
            return jsonify({'error': 'Log data is not in the expected format'}), 500
        
        # Ensure the DataFrame contains the necessary columns
        required_columns = ['concept:name', 'time:timestamp']
        if not all(col in log.columns for col in required_columns):
            logging.error(f"Missing required columns: {required_columns}")
            return jsonify({'error': f"Log DataFrame missing required columns: {required_columns}"}), 500
        
        # Convert the 'time:timestamp' column to datetime if it isn't already
        if not pd.api.types.is_datetime64_any_dtype(log['time:timestamp']):
            log['time:timestamp'] = pd.to_datetime(log['time:timestamp'])
        
        # Sort the DataFrame by trace and timestamp to ensure events are in the correct order
        log = log.sort_values(by=['concept:name', 'time:timestamp'])
        
        # Calculate durations between subsequent events within the same trace
        log['duration'] = log.groupby('concept:name')['time:timestamp'].diff().dt.total_seconds()
        
        # Calculate the average duration for each event type
        average_durations = log.groupby('concept:name')['duration'].mean().dropna()
        
        # Identify potential bottlenecks (e.g., average duration > 1 hour)
        threshold = 3600  # 1 hour in seconds
        bottlenecks = average_durations[average_durations > threshold].to_dict()
        
        logging.info(f"Average durations:\n{average_durations}")
        logging.info(f"Bottlenecks: {bottlenecks}")

        return jsonify({'bottlenecks': bottlenecks})
    
    except Exception as e:
        logging.error(f"Error analyzing bottlenecks: {e}")
        return jsonify({'error': 'An error occurred while processing the request'}), 500