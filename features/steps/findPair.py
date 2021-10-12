from behave import *
import subprocess


@given('подготовили текстовый файл КонституцияРФ.txt')
def step_impl(context):
    pass


@when('ищем пару слов "{firstWord}" и "{secondWord}" на расстоянии "{dist}" в текстовом файле "{file}"')
def step_impl(context, firstWord, secondWord, dist, file):
    context.answer = subprocess.check_output(f"./count_pairs.exe features/materials/{file} {firstWord} {secondWord} {dist}", shell=True)


@when('запускаем приложение count_pairs.exe с недостаточным числом аргументов')
def step_impl(context):
    context.answer = subprocess.check_output(f"./count_pairs.exe features/materials/КонституцияРФ.txt", shell=True)


@when('запускаем приложение count_pairs.exe более чем с четырьмя аргументами')
def step_impl(context):
    context.answer = subprocess.check_output(f"./count_pairs.exe features/materials/КонституцияРФ.txt права обязанности конституция 4", shell=True)


@then('получаем сообщение о невозможности открыть файл')
def step_impl(context):
    assert context.answer == b'Incorrect file name\n'


@then('получаем сообщение о неправильном количестве аргументов')
def step_impl(context):
    assert context.answer == b"Incorrect number of arguments\n"


@then('получаем сообщение о проблеме во время конвертирования и информацией о пойманном исключении')
def step_impl(context):
    assert context.answer == b'Error while converting char * to std::wstring\n'


@then('находим "{num}" "{pairs}" в текстовом файле')
def step_impl(context, num, pairs):
    assert context.answer == bytes(num + "\n", encoding = 'utf-8')


@then('не находим такую пару в текстовом файле')
def step_impl(context):
    print(context.answer)
    assert context.answer == bytes("0\n", encoding = 'utf-8')

