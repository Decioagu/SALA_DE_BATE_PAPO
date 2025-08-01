from django.views.generic import TemplateView
from django.utils.safestring import mark_safe #21 Converter strings em HTML seguro
import json #21 Módulo json para manipulação de dados JSON

#21 Importa as views genéricas do Django
class IndexView(TemplateView):
    template_name = 'index.html'

#21 Define a view para a página inicial
class SalaView(TemplateView):
    template_name = 'sala.html'

    #21 Método para passar o nome da sala como contexto para o template
    def get_context_data(self, **kwargs):
        context = super(SalaView, self).get_context_data(**kwargs)
        context['nome_sala_json'] = mark_safe(
            json.dumps(self.kwargs['nome_sala']) #21 Converte o nome da sala para JSON seguro
        )
        return context

'''
O que é mark_safe?
    No Django, toda string passada para o template é automaticamente escapada para evitar
    ataques XSS (Cross-Site Scripting).
    Ou seja, se você passar <b>Olá</b> para o template, o Django renderiza como texto literal:

➡️  Isso é uma proteção automática para que ninguém insira código malicioso no HTML.
✅  Se você tem certeza absoluta que uma string é segura e quer que o Django não escape ela, 
    você usa mark_safe().
'''