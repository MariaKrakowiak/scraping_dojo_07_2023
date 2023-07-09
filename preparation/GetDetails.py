def retrieve_authors(data, authors):
    """
    Retrieve author's name and surname, append to list.
    :param data:
    :param authors:
    :return:
    """
    for d in data:
        authors.append(d['author']['name'].encode('ascii', 'ignore').decode('utf-8'))


def retrieve_tags(data, tags):
    """
    Retrieve tags and append to list.
    :param data:
    :param tags:
    :return:
    """
    for d in data:
        tags.append(d['tags'])


def retrieve_texts(data, texts):
    """
    Retrieve text (quote), append to list.
    :param data:
    :param texts:
    :return:
    """
    for d in data:
        texts.append(d['text'].encode('ascii', 'ignore').decode('utf-8'))


def retrieve_list_of_dict(authors_list, tags_list, texts_list):
    """
    Retrieve the list of dictionaries for each page.
    :param authors_list:
    :param tags_list:
    :param texts_list:
    :return:
    """
    return [{'text': texts_list[i],
             'by': authors_list[i],
             'tags': tags_list[i]} for i in range(len(texts_list))]
