def get_ranges(intervals: list[int]) -> list[int]:
    """
    Предобрадотка временных интервалов, исключение пересечений
    """
    n = len(intervals)
    if n == 0:
        return []
    ranges = [intervals[0], intervals[1]]
    for i in range(2, n, 2):
        start = intervals[i]
        end = intervals[i + 1]
        if start > ranges[-1]:
            ranges.append(start)
            ranges.append(end)
        else:
            ranges[-1] = max(ranges[-1], end)
    return ranges


def appearance(intervals: dict[str, list[int]]) -> int:
    total_time = 0
    ranges_pupil = get_ranges(intervals["pupil"])
    ranges_tutor = get_ranges(intervals["tutor"])
    n = len(ranges_pupil)
    m = len(ranges_tutor)

    i = 0
    j = 0
    lesson_start, lesson_end = intervals["lesson"]
    while i <= n - 2 and j <= m - 2:
        p_start, p_end = ranges_pupil[i], ranges_pupil[i + 1]
        t_start, t_end = ranges_tutor[j], ranges_tutor[j + 1]
        if p_start > lesson_end or t_start > lesson_end:
            break
        if p_end < lesson_start:
            i += 2
            continue
        if t_end < lesson_start:
            j += 2
            continue
        if p_end < t_start:
            i += 2
        elif t_end < p_start:
            j += 2
        else:
            left_border = max(p_start, t_start, lesson_start)
            right_border = min(p_end, t_end, lesson_end)
            total_time += right_border - left_border
            if p_end < t_end:
                i += 2
            else:
                j += 2
    return total_time
