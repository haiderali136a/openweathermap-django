def compare_weather_conditions(weather_details: dict, expected_output: str) -> bool:
    if 'temperature' in expected_output:
        if 'less than' in expected_output:
            expected_temperature = expected_output.split('less than')[1].strip().split(' ')[0]
            try:
                expected_temperature = int(expected_temperature)
                if expected_temperature < weather_details['main']['temp']:
                    return True
            except Exception as e:
                pass
        elif 'higher than' in expected_output:
            expected_temperature = expected_output.split('higher than')[1].strip().split(' ')[0]
            try:
                expected_temperature = int(expected_temperature)
                if weather_details['main']['temp'] > expected_temperature:
                    return True
            except Exception as e:
                pass
        else:
            expected_temperature = expected_output.split('temperature')[1].strip().split(' ')[0]
            try:
                expected_temperature = int(expected_temperature)
                if weather_details['main']['temp'] == expected_temperature:
                    return True
            except Exception as e:
                pass
    else:
        if weather_details['weather']['description'] == expected_output:
            return True
        else:
            return False
