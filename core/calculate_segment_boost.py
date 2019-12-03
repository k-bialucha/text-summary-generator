def calculate_segment_boost(index, total_length, segment_boost):
    position = index / total_length

    for boost in segment_boost:
        start_pos = boost[0] / 100
        end_pos = boost[1] / 100
        boost_factor = boost[2] / 100

        is_position_in_segment = position >= start_pos and position <= end_pos

        if is_position_in_segment:
            return 1 + boost_factor

    return 1
