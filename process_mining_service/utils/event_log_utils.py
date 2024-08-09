import pm4py
from pm4py.objects.log.importer.xes import importer as xes_importer
from pm4py.objects.log.exporter.csv import exporter as csv_exporter

class EventLogUtils:
    @staticmethod
    def load_event_log(file_path):
        log = xes_importer.apply(file_path)
        return log

    @staticmethod
    def get_number_of_traces(log):
        return len(log)

    @staticmethod
    def get_number_of_events(trace):
        return len(trace)

    @staticmethod
    def get_trace_name(trace):
        return trace.attributes.get('concept:name', 'Unnamed Trace')

    @staticmethod
    def export_log_to_csv(log, file_path):
        csv_exporter.apply(log, file_path)
