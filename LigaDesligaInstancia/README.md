Utiliza função lambda e Cloud Whatch para ligar e desligar instancias fora do horario comercial.
As instancias estarão disponiveis de segunda a sexta das 8:00 as 18:00
O banco de dados e o serviço de log de temperatura e umidade funcionarão normalmente 24x7.

Etapas

IAM
1-Criar Politica para o serviço
2- json
3-
---
{
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Allow",
        "Action": [
          "logs:CreateLogGroup",
          "logs:CreateLogStream",
          "logs:PutLogEvents"
        ],
        "Resource": "arn:aws:logs:*:*:*"
      },
      {
        "Effect": "Allow",
        "Action": [
          "ec2:Start*",
          "ec2:Stop*"
        ],
        "Resource": "*"
      }
    ]
  }
---
IAM
1-Criar função para o lambda acessar o EC2
2-Adicionar politica criada à nova função

Lambda
1-Criar Função liga ec2
2-copiar codigo para o campo da função
3-deploy
4-editar tempo da função para 15s
5-testar

lamba
1-adicionar gatilho
2-clouwhatch event
3-Na Descrição da regra, adicionar expressão da cron de ligar de segunda a sexta as 8am


