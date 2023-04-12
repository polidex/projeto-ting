from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    for i in range(0, len(instance)):
        if path_file == instance.search(i)['nome_do_arquivo']:
            return None

    result = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(txt_importer(path_file)),
        'linhas_do_arquivo': txt_importer(path_file)
    }
    instance.enqueue(result)
    sys.stdout.write(str(result))


def remove(instance):
    if len(instance) == 0:
        sys.stdout.write('Não há elementos\n')
    else:
        value = instance.dequeue()
        sys.stdout.write(
            f'Arquivo {value["nome_do_arquivo"]} removido com sucesso\n')


def file_metadata(instance, position):
    try:
        value = instance.search(position)
        sys.stdout.write(str(value))
    except IndexError:
        sys.stderr.write('Posição inválida')
