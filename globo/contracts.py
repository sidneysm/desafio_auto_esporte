from scrapy.contracts import Contract
from scrapy.exceptions import ContractFail


class HasItemContract(Contract):

    name = 'has_itens'

    def post_process(self, output):
        if 'item' not in output[0]['feed'][0]:
            raise ContractFail('Não nenhum item na saída')


class HasTitleItem(Contract):

    name = 'has_title'

    def post_process(self, output):
        if 'title' not in output[0]['feed'][0]['item']:
            raise ContractFail('Não há título no primeiro item da saída')


class HasLinkItem(Contract):

    name = 'has_link'

    def post_process(self, output):
        if 'link' not in output[0]['feed'][0]['item']:
            raise ContractFail('Não há link no primeiro item da saída')


class HasDescriptionItem(Contract):

    name = 'has_description'

    def post_process(self, output):
        if 'description' not in output[0]['feed'][0]['item']:
            raise ContractFail('Não há descrição no primeiro item da saída')


class HasDescriptionSomething(Contract):

    name = 'has_description_something'

    def post_process(self, output):
        desc = output[0]['feed'][0]['item']['description']
        if len(desc) < 1:
            raise ContractFail('A descrição ficou vazia')
