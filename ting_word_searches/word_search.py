def exists_word(word, instance):
    for i in range(0, len(instance)):
        file = {
            "palavra": word,
            "arquivo": instance.search(i)['nome_do_arquivo'],
            "ocorrencias": []
        }
        for index in range(0, len(instance.search(i)['linhas_do_arquivo'])):
            row = instance.search(i)['linhas_do_arquivo'][index]
            if word.lower() in row.lower():
                file['ocorrencias'].append({"linha": i + 1})

        print(len(file['ocorrencias']))

        result = []
        if len(file['ocorrencias']) > 0:
            result.append(file)

    return result


def search_by_word(word, instance):
    for i in range(0, len(instance)):
        file = {
            "palavra": word,
            "arquivo": instance.search(i)['nome_do_arquivo'],
            "ocorrencias": []
        }
        for index in range(0, len(instance.search(i)['linhas_do_arquivo'])):
            row = instance.search(i)['linhas_do_arquivo'][index]
            if word.lower() in row.lower():
                file['ocorrencias'].append({"linha": i + 1, "conteudo": row})

        print(len(file['ocorrencias']))

        result = []
        if len(file['ocorrencias']) > 0:
            result.append(file)

    return result
