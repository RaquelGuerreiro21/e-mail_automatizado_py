# e-Email Scheduler com Anexo
Este projeto é um script Python que automatiza o envio de emails com um anexo específico em uma data e hora predefinidas. Utiliza as bibliotecas yagmail para envio de emails e schedule para agendamento de tarefas. O objetivo deste script é enviar um email com uma planilha em anexo toda segunda-feira às 16:00.

Configurações
Certifique-se de configurar corretamente as variáveis antes de executar o script:

EMAIL_REMETENTE: O endereço de email que enviará as mensagens.
SENHA: A senha do email remetente.
DESTINATARIOS: Lista de destinatários do email.
DESTINATARIOS_CC: Lista de destinatários em cópia.
CAMINHO_PLANILHA: O caminho para o arquivo da planilha que será anexada ao email.
Dependências
As seguintes bibliotecas Python são necessárias para executar este script:

yagmail
schedule
Você pode instalá-las usando pip:


Copiar código
pip install yagmail schedule

# Funcionamento
O script coleta a data atual e formata-a para ser usada no assunto do email.
Conecta-se ao servidor de email usando as credenciais fornecidas.
Envia um email com o assunto, corpo e anexo especificados.
O agendamento é configurado para enviar o email toda segunda-feira às 16:00.
O script permanece em execução, verificando a cada minuto se há alguma tarefa pendente para ser executada.
Para executar o script, basta rodar:


código:
python nome_do_script.py

Certifique-se de que o script esteja em um ambiente que permita a execução contínua, como um servidor ou uma máquina configurada para isso.

# Contribuição
Para contribuir com este projeto, sinta-se à vontade para abrir um pull request ou relatar problemas no repositório.

Espero que este README forneça uma compreensão clara de como configurar e executar o script de agendamento de email com anexo.






