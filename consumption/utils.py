from datetime import datetime, timedelta
from .default_values import (RESOLUTION_LIST, DAY, MONTH, START, COUNT,
                             RESOLUTION)
from .errors import (RESOLUTION_INVALID, START_INVALID, COUNT_INVALID,
                     INPUT_DATA_NOT_COMPLETE)
from .models import days, months


def validate_data_inputs(resolution, start, count):
    errors = []
    if resolution not in RESOLUTION_LIST:
        errors.append(RESOLUTION_INVALID)
    try:
        start = datetime.strptime(start, '%Y-%m-%d')
    except:
        errors.append(START_INVALID)
    if not count.isdigit():
        errors.append(COUNT_INVALID)
    return errors, start


def get_queryset(resolution, start, count, user):

    if resolution == DAY:
        queryset = days.objects.filter(
            user_id=user.id,
            timestamp__range=[start, start + timedelta(days=int(count))])
    elif resolution == MONTH:
        queryset = months.objects.filter(
            user_id=user.id,
            timestamp__range=[start, start + timedelta(days=int(count) * 31)])
    else:
        queryset = False
    return queryset


def retrieve_data(request):
    errors = []
    resolution = request.GET.get(RESOLUTION)
    start = request.GET.get(START)
    count = request.GET.get(COUNT)
    if resolution and start and count:
        errors, start = validate_data_inputs(resolution, start, count)
    else:
        errors.append(INPUT_DATA_NOT_COMPLETE)
    if errors:
        return errors, False
    user = request.user
    queryset = get_queryset(resolution, start, count, user)
    if len(errors) == 0:
        return errors, queryset
    return errors, False


def make_errors_format(errors_lis, request_path):
    errs = {'errors': errors_lis, 'source': {'pointer': request_path}}
    return errs
