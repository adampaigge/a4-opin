import datetime
import json
import time
import uuid

import requests
from django import forms
from django.conf import settings
from requests.auth import HTTPBasicAuth


def send_to_flashpoll(data):
    if 'current_preview' in data:
        if 'save_draft' in data and data['current_preview'] == 'True':
            # Handling unpublish
            url_poll = '{base_url}/poll/{poll_id}/opin/stop'.format(
                base_url=settings.FLASHPOLL_BACK_URL,
                poll_id=data['module_settings-key']
            )
            # Handle delete
            headers = {'Content-type': 'application/json'}
            requests.delete(url_poll,
                            headers=headers,
                            auth=HTTPBasicAuth(
                                settings.FLASHPOLL_BACK_USER,
                                settings.FLASHPOLL_BACK_PASSWORD))
        else:
            startTime = time.mktime(datetime.datetime.strptime(
                data['module_settings-startTime'],
                "%d/%m/%Y %H:%M").timetuple())
            endTime = time.mktime(datetime.datetime.strptime(
                data['module_settings-endTime'],
                "%d/%m/%Y %H:%M").timetuple())
            jsonGenerator = {}
            jsonGenerator['title'] = data['module_settings-title']
            jsonGenerator['shortDescription'] = data[
                'module_settings-shortDescription']
            jsonGenerator['longDescription'] = data[
                'module_settings-longDescription']
            jsonGenerator['concludeMessage'] = data[
                'module_settings-concludeMessage']
            jsonGenerator['descriptionMediaURLs'] = [""]
            jsonGenerator['keywords'] = []
            jsonGenerator['resultVisibility'] = 0
            jsonGenerator['startTime'] = startTime
            jsonGenerator['endTime'] = endTime
            jsonGenerator['preview'] = 'save_draft' not in data
            # context
            jsonGenerator['lab'] = 'opin'
            jsonGenerator['domain'] = 'opin'
            jsonGenerator['campaign'] = 'default'
            # location
            jsonGenerator['geofenceLocation'] = data[
                'module_settings-geofenceLocation']
            jsonGenerator['geofenceRadius'] = 0
            jsonGenerator['geofenceId'] = ''
            # questions
            q = 1
            questions = []
            question_key = "module_settings-question_"+str(q)+"_questionType"
            while question_key in data:
                question = {}
                question['questionText'] = data[
                    "module_settings-question_"+str(q)+"_questionText"]
                question['orderId'] = q
                question['questionType'] = data[
                    "module_settings-question_"+str(q)+"_questionType"]
                if "module_settings-question_"+str(q)+"_mandatory" in data:
                    question['mandatory'] = True
                else:
                    question['mandatory'] = False
                question['mediaURLs'] = [""]
                # answers
                a = 1
                answers = []
                answer_key = "module_settings-question_" + \
                    str(q)+"_choice_"+str(a)+"_answerText"
                while answer_key in data:
                    answer = {}
                    answer['answerText'] = data[
                        "module_settings-question_"
                        + str(q)
                        + "_choice_"+str(a)
                        + "_answerText"
                    ]
                    answer['orderId'] = a
                    answer['mediaURL'] = ''
                    if (data["module_settings-question_"
                             + str(q)
                             +
                             "_questionType"] == "FREETEXT"):
                        answer['freetextAnswer'] = True
                    else:
                        answer['freetextAnswer'] = False
                    answers.append(answer)
                    a = a + 1
                    answer_key = "module_settings-question_" + \
                        str(q)+"_choice_"+str(a)+"_answerText"
                question['answers'] = answers
                questions.append(question)
                q = q + 1
                question_key = "module_settings-question_" + \
                    str(q)+"_questionType"
            jsonGenerator['questions'] = questions
            json_data = json.dumps(jsonGenerator)
            url_poll = '{base_url}/poll/{poll_id}/opin'.format(
                base_url=settings.FLASHPOLL_BACK_URL,
                poll_id=data['module_settings-key']
            )
            # Handle post
            headers = {'Content-type': 'application/json'}
            requests.post(url_poll,
                          data=json_data,
                          headers=headers,
                          auth=HTTPBasicAuth(settings.FLASHPOLL_BACK_USER,
                                             settings.FLASHPOLL_BACK_PASSWORD))


def fp_context_data_for_create_view(context, view):
    pollid = str(uuid.uuid4())
    context['pollid'] = pollid
    context['module_settings'] = view.kwargs['module_settings']

    return context


def fp_context_data_for_update_view(context, view):
    context['pollid'] = view.kwargs['pollid']
    context['module_settings'] = view.kwargs['module_settings']

    url_poll = '{base_url}/poll/{poll_id}'.format(
        base_url=settings.FLASHPOLL_BACK_URL,
        poll_id=context['pollid']
    )

    headers = {'Content-type': 'application/json'}
    res = requests.get(url_poll,
                       headers=headers,
                       auth=HTTPBasicAuth(settings.FLASHPOLL_BACK_USER,
                                          settings.FLASHPOLL_BACK_PASSWORD
                                          ))
    context['poll'] = json.loads(res.text)

    url_poll = '{base_url}/poll/{poll_id}/result'.format(
        base_url=settings.FLASHPOLL_BACK_URL,
        poll_id=context['pollid']
    )

    headers = {'Content-type': 'application/json'}
    res = requests.get(url_poll,
                       headers=headers,
                       auth=HTTPBasicAuth(settings.FLASHPOLL_BACK_USER,
                                          settings.FLASHPOLL_BACK_PASSWORD
                                          ))
    context['pollresult'] = json.loads(res.text)

    return context


def fp_context_data(module_settings):
    data = dict(module_settings.data)
    # case submitted
    if ('save_draft' in data) or ('publish' in data):
        jsonGenerator = {}
        jsonGenerator['title'] = data['module_settings-title']
        jsonGenerator['shortDescription'] = data[
            'module_settings-shortDescription']
        jsonGenerator['longDescription'] = data[
            'module_settings-longDescription']
        jsonGenerator['concludeMessage'] = data[
            'module_settings-concludeMessage']
        jsonGenerator['descriptionMediaURLs'] = [""]
        jsonGenerator['keywords'] = []
        jsonGenerator['resultVisibility'] = 0
        if (data['module_settings-startTime'] != ['']
                and data['module_settings-endTime'] != ['']):
            startTime = time.mktime(datetime.datetime.strptime(
                data['module_settings-startTime'][0],
                "%d/%m/%Y %H:%M").timetuple())
            endTime = time.mktime(datetime.datetime.strptime(
                data['module_settings-endTime'][0],
                "%d/%m/%Y %H:%M").timetuple())
            jsonGenerator['startTime'] = startTime
            jsonGenerator['endTime'] = endTime
        else:
            jsonGenerator['startTime'] = data['module_settings-startTime']
            jsonGenerator['endTime'] = data['module_settings-endTime']

        # location
        jsonGenerator['geofenceLocation'] = data[
            'module_settings-geofenceLocation']
        # questions
        q = 1
        questions = []
        question_key = "module_settings-question_"+str(q)+"_questionType"
        while question_key in data:
            question = {}
            question['questionText'] = data[
                "module_settings-question_"+str(q)+"_questionText"]
            question['orderId'] = q
            question['questionType'] = data[
                "module_settings-question_"+str(q)+"_questionType"]

            if "module_settings-question_"+str(q)+"_mandatory" in data:
                question['mandatory'] = True
            else:
                question['mandatory'] = False
            question['mediaURLs'] = [""]

            # answers
            a = 1
            answers = []
            answer_key = "module_settings-question_" + \
                str(q)+"_choice_"+str(a)+"_answerText"
            while answer_key in data:
                answer = {}
                answer['answerText'] = data[
                    "module_settings-question_"
                    + str(q)
                    + "_choice_"
                    + str(a)
                    + "_answerText"]
                answer['orderId'] = a
                answer['mediaURL'] = ''
                if (data[
                        "module_settings-question_"
                        + str(q)
                        + "_questionType"] == "FREETEXT"):
                    answer['freetextAnswer'] = True
                else:
                    answer['freetextAnswer'] = False

                answers.append(answer)
                a = a + 1
                answer_key = "module_settings-question_" + \
                    str(q)+"_choice_"+str(a)+"_answerText"

            question['answers'] = answers
            questions.append(question)
            q = q + 1
            question_key = "module_settings-question_"+str(q)+"_questionType"

        jsonGenerator['questions'] = questions
        poll = jsonGenerator
        module_settings.data._mutable = True
        module_settings.data['module_settings-poll'] = json.dumps(poll)

    else:
        # case edit
        if 'key' in module_settings.initial:
            pollid = module_settings.initial['key']
            if pollid:
                url_poll = '{base_url}/poll/{poll_id}'.format(
                    base_url=settings.FLASHPOLL_BACK_URL,
                    poll_id=pollid
                )

                # Handle get
                headers = {'Content-type': 'application/json'}
                response = requests.get(
                    url_poll,
                    headers=headers,
                    auth=HTTPBasicAuth(settings.FLASHPOLL_BACK_USER,
                                       settings.FLASHPOLL_BACK_PASSWORD))
                poll = json.loads(response.text)
                poll = get_ordered_poll(poll)

        else:
            # case create
            poll = {
                'keywords': [''],
                'shortDescription': '',
                'geofenceLocation': '', 'title': '',
                'concludeMessage': '',
                'questions': [
                    {
                        'questionText': '',
                        'mediaURLs': [''],
                        'orderId': 1,
                        'mandatory': True,
                        'questionType': 'CHECKBOX',
                        'answers': [
                            {
                                'freetextAnswer': False,
                                'orderId': 1,
                                'answerText': '',
                                'mediaURL': ''
                            },
                            {
                                'freetextAnswer': False,
                                'orderId': 2,
                                'answerText': '',
                                'mediaURL': ''
                            }
                        ]
                    }],
                'endTime': '',
                'longDescription': '',
                'startTime': '',
                'descriptionMediaURLs': ['']
            }

    module_settings.fields['poll'] = forms.CharField(
        widget=forms.Textarea)
    module_settings.initial['poll'] = json.dumps(poll)
    # description
    module_settings.fields['title'] = forms.CharField(
        label='Title', max_length=800)
    module_settings.initial['title'] = poll['title']
    module_settings.fields['shortDescription'] = forms.CharField(
        widget=forms.Textarea, label='Subtitle')
    module_settings.initial['shortDescription'] = poll['shortDescription']
    module_settings.fields['longDescription'] = forms.CharField(
        widget=forms.Textarea, label='Long description', required=False)
    module_settings.initial['longDescription'] = poll['longDescription']
    module_settings.fields['concludeMessage'] = forms.CharField(
        label='Conclude message', required=False, max_length=300)
    module_settings.initial['concludeMessage'] = poll['concludeMessage']
    module_settings.fields['startTime'] = forms.CharField(
        label='Start time', required=True)
    module_settings.initial['startTime'] = poll['startTime']
    module_settings.fields['endTime'] = forms.CharField(
        label='End time', required=True)
    module_settings.initial['endTime'] = poll['endTime']

    module_settings.fields['geofenceLocation'] = forms.CharField(
        widget=forms.Textarea, label='Location', required=True)
    module_settings.initial['geofenceLocation'] = poll['geofenceLocation']
    # questions
    for question in poll['questions']:
        q = question['orderId']
        module_settings.fields[
            'question_'+str(q)+'_questionText'] = forms.CharField(
                label='Question '+str(q), max_length=800)
        module_settings.initial[
            'question_'+str(q)+'_questionText'] = question['questionText']
        module_settings.fields['question_'
                               + str(q)
                               + '_questionType'] = forms.ChoiceField(
            label='Type', widget=forms.Select(), choices=(
                [('CHECKBOX', 'MULTIPLE'),
                 ('RADIO', 'SINGLE'),
                 ('FREETEXT', 'OPEN'),
                 ('ORDER', 'RANKING'), ]), initial='3', required=True)
        module_settings.initial[
            'question_'+str(q)+'_questionType'] = question['questionType']
        module_settings.fields[
            'question_'+str(q)+'_mandatory'] = forms.BooleanField(
                label='Mandatory', required=False)
        module_settings.initial[
            'question_'+str(q)+'_mandatory'] = question['mandatory']

        for answer in question['answers']:
            a = answer['orderId']
            module_settings.fields[
                'question_'
                + str(q) +
                '_choice_'
                + str(a)
                + '_answerText'] = forms.CharField(
                    label='Choice '+str(a), max_length=800)
            module_settings.initial[
                'question_'
                + str(q)
                + '_choice_'
                + str(a)
                + '_answerText'] = answer['answerText']


def get_ordered_poll(poll):
    for question in poll['questions']:
        answers = []
        for orderid in range(1, len(question['answers'])+1):
            answer = get_elt_at(question['answers'], orderid)
            answers.append(answer)

        question['answers'] = answers
    # questions
    questions = []
    for orderid in range(1, len(poll['questions'])+1):
        question = get_elt_at(poll['questions'], orderid)
        questions.append(question)

    poll['questions'] = questions

    return poll


def get_elt_at(list, orderid):
    for elt in list:
        if elt['orderId'] == orderid:
            return elt

    return None
