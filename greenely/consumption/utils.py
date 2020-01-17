from datetime import datetime, timedelta
from .default_values import (RESOLUTION_LIST, DAY, MONTH, START, COUNT,
                             RESOLUTION)
from .errors import (RESOLUTION_INVALID, START_INVALID, COUNT_INVALID,
                     INPUT_DATA_NOT_COMPLETE)
from .models import days, months


def validate_data_inputs(resolution, start, count):
    """
    This method check the validation of query parameters
    :param resolution: 
    :param start: 
    :param count: 
    :return: 
    """
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
    """
    This method make the queryset based on the user inputs
    :param resolution: 
    :param start: 
    :param count: 
    :param user: 
    :return: 
    """

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
    """
    retrieve the data of the user consumption
    :param request: 
    :return: 
    """
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
    """
    Make a uniform error format for the bad requests
    :param errors_lis: 
    :param request_path: 
    :return: 
    """
    errs = {'errors': errors_lis, 'source': {'pointer': request_path}}
    return errs


def serialize_data_output(queryset):
    """
    Make the output response based on requirements
    :param queryset: 
    :return: 
    """
    output = {'data': []}
    for item in queryset:
        data_item = [item.timestamp.date(), item.consumption, item.temperature]
        output['data'].append(data_item)
    return output


def retrieve_limit(request):
    """
    Create limit response based on the requirements
    :param request: 
    :return: 
    """
    user = request.user
    output = {"limits": {}}
    output["limits"]["months"] = {}
    output["limits"]["months"]["timestamp"] = {}
    output["limits"]["months"]["consumption"] = {}
    output["limits"]["months"]["temperature"] = {}
    if months.objects.filter(user_id=user.id).count() > 0:
        output["limits"]["months"]["timestamp"][
            "minimum"] = months.objects.filter(user_id=user.id).order_by(
                'timestamp').first().timestamp.date()
        output["limits"]["months"]["timestamp"][
            "maximum"] = months.objects.filter(
                user_id=user.id).order_by('timestamp').last().timestamp.date()
        output["limits"]["months"]["consumption"][
            "minimum"] = months.objects.filter(
                user_id=user.id).order_by('consumption').first().consumption
        output["limits"]["months"]["consumption"][
            "maximum"] = months.objects.filter(
                user_id=user.id).order_by('consumption').last().consumption
        output["limits"]["months"]["temperature"][
            "minimum"] = months.objects.filter(
                user_id=user.id).order_by('temperature').first().temperature
        output["limits"]["months"]["temperature"][
            "maximum"] = months.objects.filter(
                user_id=user.id).order_by('temperature').last().temperature
    output["limits"]["days"] = {}
    output["limits"]["days"]["timestamp"] = {}
    output["limits"]["days"]["consumption"] = {}
    output["limits"]["days"]["temperature"] = {}
    if days.objects.filter(user_id=user.id).count() > 0:
        output["limits"]["days"]["timestamp"]["minimum"] = days.objects.filter(
            user_id=user.id).order_by('timestamp').first().timestamp.date()
        output["limits"]["days"]["timestamp"]["maximum"] = days.objects.filter(
            user_id=user.id).order_by('timestamp').last().timestamp.date()

        output["limits"]["days"]["consumption"][
            "minimum"] = days.objects.filter(
                user_id=user.id).order_by('consumption').first().consumption
        output["limits"]["days"]["consumption"][
            "maximum"] = days.objects.filter(
                user_id=user.id).order_by('consumption').last().consumption

        output["limits"]["days"]["temperature"][
            "minimum"] = days.objects.filter(
                user_id=user.id).order_by('temperature').first().temperature
        output["limits"]["days"]["temperature"][
            "maximum"] = days.objects.filter(
                user_id=user.id).order_by('temperature').last().temperature
    return output
