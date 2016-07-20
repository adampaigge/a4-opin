#!/bin/sh

set -e -v

if [ -n ${TRAVIS_SSH_SECRET} ]; then
    SSH_ID_ARG="-i ${HOME}/id_rsa"
    cat <<EOF | openssl enc -d -pass env:TRAVIS_SSH_SECRET -a -out ~/id_rsa
LS0tLS1CRUdJTiBSU0EgUFJJVkFURSBLRVktLS0tLQpNSUlFb3dJQkFBS0NBUUVB
b0o0V3QrWUs0MHprTmliMS94Qk96d0s1bWtJak5kM1pISkxvbEM4cFZGY2FSMHpa
CnRUM0FzK1NVTnRCZmVKOW5sQ25ZNDVpUmJ5aFdyZ1l2U1p3UnZTTDUvelE5a0hn
Z09DOHBjRUR4V3o3SGlaYUcKdlAxUkFBQWkyUkV0RWV6VVdLS3hXUnVubVAwS0tj
SEFESDNvTjYwMy82YnFoK0xSbmV3WVcvbnczaDBSUVpsTApmZlNHUzBrN3NneE5P
Q2h3ajQzWnBkNDhpVkdLYWRVZEdjTjhzZlltL3RoK0VySm9xYVZWWFhnS3phNjNq
c2dMCkFaWHE1KzlMZEgvL3hUcEIvSEhuWk9EUXdkNWFSOWdLbG1PRzc4U1F1aG02
SGVSTS9FWS9wbTBnVEc4aWV3aHIKOW54OEFhWEp2TExhQm95bjU5Q1VoM3pjNDZG
dHA1dEFLRS9UT1FJREFRQUJBb0lCQUhkbHphR2JJcERod2V2MwpmbnJEVnJKUVpr
U2owYVRqYTlmdjVYRHl0aGg2UDVDdE1sR212QzkrUmllUk1zZHFTQWMrTEhyVUda
aTJOZWxiCnM1OVdvMkVrTlE5ZmVEeUM4QUNVSG92UjJ4bG5TOUdkMGo5L1Y4MVdU
SkZzVVVLMytRcUN0cTkwL1Z1ZkR3VUgKZ0lwSXRtMWRHUG0welRlQ2h5eU1LM2VF
RDJnc3FmNVdLWmdlZzBFZ3o3ZnBpRVMzQWF3UEw1UkVHWlpGRG0yQQpZZm4yNUZK
TkVCUnczUXZXYXRWRmJoSHJ3VDdQVk9KV3YxRXZrUTloY0tlUFdWNTU2SHhYSWk0
RS9XNktCNERCCmZ0dHFlYWFZYW1vQkRRaDhHQ3MydUxVRTdEMTAwRXVRQTIzenQ0
em5QV1BSbVhkSkhEdFpJaDFDeFlXc1hnQkUKTE5MSFhHRUNnWUVBelBzWmFvUEth
WExEQjZFbzY4ZjQzdzM0K1Fpd01VU2Mva1JhOUJzWkhlVWZyeEpXMzhnMApwV1hV
Y0hXdHQybzNsS0xMcXJBSnVaVERxT3BlV3F3WFEzSkZmVGZXcUFkMDd2MUROSEhz
VFpZTXNweTEwM0JYCkpISlJxVlczRG0zOUdoWWNOV3RBU1hqdklhc3NreCtiNS9G
THQ4cE1sVFRXbEx1d1VtaklxazBDZ1lFQXlKaEQKSjg4N2w5eG00WGZpaDBWZncw
Tk1SNm1DVjFndENPYTdQM3V6MlMweng2d1pjTkxINGVtQnZZZW1rN0ZtaUhkSwph
OXU0clkxaE5rUU41end6TjBJTWpzNU5IaVhLTUtUMzBRL0QvWE9QaHVwa0FDL1V6
dlc1cStuZ3lMMzU1b0orCnBZNDJ2QzhJT0FyalNocFVJKy9rRDA3NG9OZTg0Y25J
TXlCcDZwMENnWUVBbWcxbERwNDVzNEppZlF0cjI3Z1EKbkdLOTZUdlVYMUszd29q
UTZvQ3JJY0tmUzA0M0tEd3BCTjFCQ2J3SGNMOU5RbElQU3hxK1ZGRXZzM1Znc0Rp
Qgp5MWpJVE5GNGJCUWVsN2FUbVlpOUZacGR0S2IrS0FoWUZiWXRGVnlzRlJZb2tF
QnB0dVFDRHJYcTBwejVCU0ZPClpNVCtLUVRMQmFBT1hQMnFDR1ZqMmtrQ2dZQnIv
TlJDVFNUR3h5YzNnQU9hVVBXUnQ5d0x4Q3hmK3g4YmFLTXIKTk53SU1YWnJxckZ6
ZEhXWW44MXhpK0pZSml1TmtiS2x4LzV1cCtyS2ZPNkRLbnhqNWhHK216OFcyTDgx
V3NueQphU3RZZVdxdDllYnAxdFlZcUY1Uk56SUV2NGtWMS9CNERjeFhtSFl6UFdG
STFrMnZud2hHV1h3dGtwYWpjcTV0Ckg2a0ZYUUtCZ0ZJSWNsQ1lJSHVTZ0tkbVZa
dzcveXppUHVFSTZjaUdnTTV3TVBqNnZQUmlJMkh6bVBTelR0U28Kc3c2cjFDK3J3
Y0NMYlFJSDQrMEd1Sy9JcDhoWDB1VUxxdlZLeG9DWG04MGJTampPWDVVSkltaElW
cUROd0FSTQpDTTR2TXYyNU50cWhZOXdyVTVlK1RUWk5WbUNCZk5Lcy9GTlh2Y01C
ZG5rY1JsSnJsSmpUCi0tLS0tRU5EIFJTQSBQUklWQVRFIEtFWS0tLS0tCg==
EOF
    chmod 600 ~/id_rsa
fi

ssh -p 22036 ${SSH_ID_ARG} build@benhabib.liqd.net deploy euth_wagtail master dev
