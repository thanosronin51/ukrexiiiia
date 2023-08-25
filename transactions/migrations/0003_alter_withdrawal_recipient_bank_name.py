# Generated by Django 4.2.3 on 2023-08-19 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0002_remove_payment_proof_of_pay'),
    ]

    operations = [
        migrations.AlterField(
            model_name='withdrawal',
            name='recipient_bank_name',
            field=models.CharField(choices=[('ABC International Bank Plc', 'ABC International Bank Plc'), ('BANKA INTESA SANPAOLO', 'BANKA INTESA SANPAOLO'), ('Bank of America', 'Bank of America'), ('Citibank', 'Citibank'), ('JPMorgan Chase', 'JPMorgan Chase'), ('Wells Fargo', 'Wells Fargo'), ('Barclays', 'Barclays'), ('HSBC', 'HSBC'), ('Lloyds Banking Group', 'Lloyds Banking Group'), ('Royal Bank of Scotland', 'Royal Bank of Scotland'), ('Standard Chartered', 'Standard Chartered'), ('UBS', 'UBS'), ('Credit Suisse', 'Credit Suisse'), ('Deutsche Bank', 'Deutsche Bank'), ('Societe Generale', 'Societe Generale'), ('BNP Paribas', 'BNP Paribas'), ('ING Group', 'ING Group'), ('Rabobank', 'Rabobank'), ('Santander', 'Santander'), ('BBVA', 'BBVA'), ('CaixaBank', 'CaixaBank'), ('Itau Unibanco', 'Itau Unibanco'), ('Bradesco', 'Bradesco'), ('Bank of China', 'Bank of China'), ('Industrial and Commercial Bank of China', 'Industrial and Commercial Bank of China'), ('China Construction Bank', 'China Construction Bank'), ('Agricultural Bank of China', 'Agricultural Bank of China'), ('Bank of Communications', 'Bank of Communications'), ('Mitsubishi UFJ Financial Group', 'Mitsubishi UFJ Financial Group'), ('Sumitomo Mitsui Financial Group', 'Sumitomo Mitsui Financial Group'), ('Mizuho Financial Group', 'Mizuho Financial Group'), ('Nomura Holdings', 'Nomura Holdings'), ('Resona Holdings', 'Resona Holdings'), ('Sberbank', 'Sberbank'), ('VTB Bank', 'VTB Bank'), ('Gazprombank', 'Gazprombank'), ('Alfa-Bank', 'Alfa-Bank'), ('Promsvyazbank', 'Promsvyazbank'), ('Rosbank', 'Rosbank'), ('Korea Development Bank', 'Korea Development Bank'), ('KB Financial Group', 'KB Financial Group'), ('Shinhan Financial Group', 'Shinhan Financial Group'), ('Woori Financial Group', 'Woori Financial Group'), ('Hana Financial Group', 'Hana Financial Group'), ('NongHyup Financial Group', 'NongHyup Financial Group'), ('Bank Mandiri', 'Bank Mandiri'), ('Bank Central Asia', 'Bank Central Asia'), ('Bank Rakyat Indonesia', 'Bank Rakyat Indonesia'), ('Bank Negara Indonesia', 'Bank Negara Indonesia'), ('OCBC Bank', 'OCBC Bank'), ('DBS Bank', 'DBS Bank'), ('United Overseas Bank', 'United Overseas Bank'), ('Bangkok Bank', 'Bangkok Bank'), ('Siam Commercial Bank', 'Siam Commercial Bank'), ('Kasikornbank', 'Kasikornbank'), ('Krung Thai Bank', 'Krung Thai Bank'), ('TMB Bank', 'TMB Bank'), ('Standard Bank Group', 'Standard Bank Group'), ('FirstRand Bank', 'FirstRand Bank'), ('Nedbank', 'Nedbank'), ('Investec', 'Investec'), ('Capitec Bank', 'Capitec Bank'), ('Bank of Montreal', 'Bank of Montreal'), ('Toronto-Dominion Bank', 'Toronto-Dominion Bank'), ('Royal Bank of Canada', 'Royal Bank of Canada'), ('Scotiabank', 'Scotiabank'), ('National Australia Bank', 'National Australia Bank'), ('Australia and New Zealand Banking Group', 'Australia and New Zealand Banking Group'), ('Commonwealth Bank', 'Commonwealth Bank'), ('Westpac Banking Corporation', 'Westpac Banking Corporation'), ('National Bank of Australia', 'National Bank of Australia'), ('BNZ', 'BNZ'), ('ASB Bank', 'ASB Bank'), ('Kiwibank', 'Kiwibank'), ('Bank of New Zealand', 'Bank of New Zealand'), ('Banco Santander', 'Banco Santander'), ('BBVA', 'BBVA'), ('CaixaBank', 'CaixaBank'), ('Bankia', 'Bankia'), ('Banco Sabadell', 'Banco Sabadell'), ('ING Group', 'ING Group'), ('ABN AMRO', 'ABN AMRO'), ('Rabobank', 'Rabobank'), ('SNS Bank', 'SNS Bank'), ('Banco de Chile', 'Banco de Chile'), ('BancoEstado', 'BancoEstado'), ('Santander Chile', 'Santander Chile'), ('Banco de Crédito e Inversiones', 'Banco de Crédito e Inversiones'), ('Banco Santander (Mexico)', 'Banco Santander (Mexico)'), ('BBVA Bancomer', 'BBVA Bancomer'), ('Banorte', 'Banorte'), ('HSBC Mexico', 'HSBC Mexico'), ('Citigroup', 'Citigroup'), ('JPMorgan Chase', 'JPMorgan Chase'), ('Bank of America', 'Bank of America'), ('Wells Fargo', 'Wells Fargo'), ('TD Bank', 'TD Bank'), ('Scotiabank', 'Scotiabank'), ('Morgan Stanley', 'Morgan Stanley'), ('Goldman Sachs', 'Goldman Sachs'), ('BNY Mellon', 'BNY Mellon'), ('State Street Corporation', 'State Street Corporation'), ('Northern Trust', 'Northern Trust'), ('PNC Financial Services', 'PNC Financial Services'), ('Capital One', 'Capital One'), ('Fifth Third Bancorp', 'Fifth Third Bancorp'), ('SunTrust Banks', 'SunTrust Banks'), ('KeyCorp', 'KeyCorp'), ('American Express', 'American Express'), ('Discover Financial', 'Discover Financial'), ('BB&T Corporation', 'BB&T Corporation'), ('Regions Financial Corporation', 'Regions Financial Corporation'), ('Huntington Bancshares', 'Huntington Bancshares'), ('Ally Financial', 'Ally Financial'), ('First Republic Bank', 'First Republic Bank'), ('Synchrony Financial', 'Synchrony Financial'), ('USAA', 'USAA'), ('Comerica', 'Comerica'), ('Zions Bancorp', 'Zions Bancorp'), ('SVB Financial Group', 'SVB Financial Group'), ('E*TRADE', 'E*TRADE'), ('Ameriprise Financial', 'Ameriprise Financial'), ('Raymond James Financial', 'Raymond James Financial'), ('LPL Financial', 'LPL Financial'), ('Stifel Financial', 'Stifel Financial'), ('Janney Montgomery Scott', 'Janney Montgomery Scott'), ('Jefferies Financial Group', 'Jefferies Financial Group'), ('Robert W. Baird', 'Robert W. Baird'), ('Cowen Group', 'Cowen Group'), ('Evercore', 'Evercore'), ('Houlihan Lokey', 'Houlihan Lokey'), ('Moelis & Company', 'Moelis & Company'), ('Oppenheimer Holdings', 'Oppenheimer Holdings'), ('Piper Sandler', 'Piper Sandler'), ('RBC Capital Markets', 'RBC Capital Markets'), ('Stephens Inc.', 'Stephens Inc.'), ('SunTrust Robinson Humphrey', 'SunTrust Robinson Humphrey'), ('William Blair & Company', 'William Blair & Company'), ('M&T Bank', 'M&T Bank'), ('Associated Banc-Corp', 'Associated Banc-Corp'), ('TCF Financial Corporation', 'TCF Financial Corporation'), ('First Horizon National Corporation', 'First Horizon National Corporation'), ('Commerce Bancshares', 'Commerce Bancshares'), ('Popular, Inc.', 'Popular, Inc.'), ('BOK Financial Corporation', 'BOK Financial Corporation'), ('Synovus', 'Synovus'), ('Hancock Whitney Corporation', 'Hancock Whitney Corporation'), ('Cathay Bank', 'Cathay Bank'), ('East West Bank', 'East West Bank'), ('First Citizens BancShares', 'First Citizens BancShares'), ('Webster Financial Corporation', 'Webster Financial Corporation'), ('City National Bank', 'City National Bank'), ('Wintrust Financial Corporation', 'Wintrust Financial Corporation'), ('Texas Capital Bancshares', 'Texas Capital Bancshares'), ('Signature Bank', 'Signature Bank'), ('New York Community Bancorp', 'New York Community Bancorp'), ('F.N.B. Corporation', 'F.N.B. Corporation'), ('First Hawaiian Bank', 'First Hawaiian Bank'), ('Huntington Bancshares', 'Huntington Bancshares'), ('Bank of the West', 'Bank of the West'), ('CIT Group', 'CIT Group'), ('NBT Bancorp', 'NBT Bancorp'), ('PacWest Bancorp', 'PacWest Bancorp'), ('Western Alliance Bancorporation', 'Western Alliance Bancorporation'), ('Greenhill & Co.', 'Greenhill & Co.'), ('PJT Partners', 'PJT Partners'), ('Houlihan Lokey', 'Houlihan Lokey'), ('Moelis & Company', 'Moelis & Company'), ('Centerview Partners', 'Centerview Partners'), ('Qatalyst Partners', 'Qatalyst Partners'), ('Guggenheim Partners', 'Guggenheim Partners'), ('Moelis & Company', 'Moelis & Company'), ('Evercore', 'Evercore'), ('Rothschild & Co', 'Rothschild & Co'), ('Greenhill & Co.', 'Greenhill & Co.')], default='', max_length=200),
        ),
    ]
