import json
import ast


def db_to_json(data: list):
    """Converts values from the database to JSON."""

    def _convert_json_strings(data_dict):
        for key, value in data_dict.items():
            if isinstance(value, str):
                try:
                    parsed_value = ast.literal_eval(value)
                    if isinstance(parsed_value, (list, dict)):
                        data_dict[key] = parsed_value
                except (ValueError, SyntaxError):
                    pass
            elif isinstance(value, dict):
                _convert_json_strings(value)

    for item in data:
        _convert_json_strings(item)

    return data
