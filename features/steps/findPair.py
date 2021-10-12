from behave import *
import subprocess


@given('подготовили текстовый файл КонституцияРФ.txt')
def step_impl(context):
    pass


@when('ищем пару слов {firstWord} и {secondWord} на расстоянии {dist} в текстовом файле {file}')
def step_impl(context, firstWord, secondWord, dist, file):
    context.answer = subprocess.check_output(f"./count_pairs.exe {file[1:-1]} {firstWord[1:-1]} {secondWord[1:-1]} {dist[1:-1]}", shell=True)


@when('запускаем приложение count_pairs.exe с недостаточным числом аргументов')
def step_impl(context):
    context.answer = subprocess.check_output(f"./count_pairs.exe КонституцияРФ.txt", shell=True)


@then('получаем сообщение о невозможности открыть файл')
def step_impl(context):
    assert context.answer == b'Incorrect file name\n'


@then('получаем сообщение о недостаточном количестве аргументов')
def step_impl(context):
    assert context.answer == b"Incorrect number of arguments\n"


@then('получаем сообщение о проблеме во время конвертирования и информацией о пойманном исключении')
def step_impl(context):
    assert context.answer == b'Error while converting char * to std::wstring\n'


@then('находим {num} {pairs} в текстовом файле')
def step_impl(context, num, pairs):
    assert context.answer == bytes(num[1:-1] + "\n", encoding = 'utf-8')


@then('не находим такую пару в текстовом файле')
def step_impl(context):
    print(context.answer)
    assert context.answer == bytes("0\n", encoding = 'utf-8')

