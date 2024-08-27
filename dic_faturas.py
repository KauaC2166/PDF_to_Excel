import PyPDF2
import datetime

ex_faturas = {
    # 1
    "fatura_EXP_048-24": {
        "doc": PyPDF2.PdfReader(open("faturas/FATURA_EXP_048-KEMIN/Commercial-Invoice-EXP-048-24.pdf", "rb")).pages[0].extract_text(),
        "numero_fatura": "EXP 048-24",
        "data": datetime.datetime(2024, 4, 17),
        "importador": "DSM NUTRITIONAL PRODUCTS URUGUAY SA",
        "exportador": "KEMIN DO BRASIL LTDA",
        "incoterm": "EXW"
    },
    # 2
    "packing_list_EXP 048-23": {
        "doc": PyPDF2.PdfReader(open("faturas/FATURA_EXP_048-KEMIN/Packing-List-EXP-048-24.pdf", "rb")).pages[0].extract_text(),
        "numero_fatura": "EXP 048-23",
        "data": datetime.datetime(2024, 4, 17),
        "importador": "DSM NUTRITIONAL PRODUCTS URUGUAY SA",
        "exportador": "KEMIN DO BRASIL LTDA",
        "incoterm": ""
    },
    # 3
    "fatura_003.24_ALM": {
        "doc": PyPDF2.PdfReader(open("faturas/FATURA_003.24_ALM-NORFRUIT/INVOICE-ALMAR-S.R.L.-003.24pdf.pdf", "rb")).pages[0].extract_text(),
        "numero_fatura": "003.24 ALM",
        "data": datetime.datetime(2024, 4, 25),
        "importador": "ALMAR S.R.L.",
        "exportador": "Norfruit Nordeste Frutas LTDA",
        "incoterm": "FCA"
    },
    # 4
    "packing_list": {
        "doc": PyPDF2.PdfReader(open("faturas/FATURA_003.24_ALM-NORFRUIT/PACKING-LIST-ALMAR-S.R.L..pdf", "rb")).pages[0].extract_text(),
        "numero_fatura": "",
        "data": datetime.datetime(2024, 4, 25),
        "importador": "Almar S.R.L",
        "exportador": "Norfruit Nordeste Frutas LTDA",
        "incoterm": ""
    },
    # 5
    "fatura_10741F": {
        "doc": PyPDF2.PdfReader(open("faturas/FATURA_10741_F-FRIVATTI/Comercial-Invoice-10741F.pdf", "rb")).pages[0].extract_text(),
        "numero_fatura": "10741F",
        "data": datetime.datetime(2024, 4, 16),
        "importador": "M. GUILLEN S.A.S",
        "exportador": "FRIVATTI",
        "incoterm": "FCA"
    },
    # 6
    "packing_list_10741F": {
        "doc": PyPDF2.PdfReader(open("faturas/FATURA_10741_F-FRIVATTI/Packing-List-10741F.pdf", "rb")).pages[0].extract_text(),
        "numero_fatura": "10741F",
        "data": datetime.datetime(2024, 4, 16),
        "importador": "M. GUILLEN S.A.S",
        "exportador": "FRIVATTI",
        "incoterm": ""
    },
    # 7
    "fatura_10742F": {
        "doc": PyPDF2.PdfReader(open("faturas/FATURA_10742_F-FRIVATTI/Comercial-Invoice-10742F.pdf", "rb")).pages[0].extract_text(),
        "numero_fatura": "10742F",
        "data": datetime.datetime(2024, 4, 1),
        "importador": "M. GUILLEN S.A.S",
        "exportador": "FRIVATTI",
        "incoterm": "CIP"
    },
    # 8
    "packing_list_10742F": {
        "doc": PyPDF2.PdfReader(open("faturas/FATURA_10742_F-FRIVATTI/Packing-List-10742F.pdf", "rb")).pages[0].extract_text(),
        "numero_fatura": "10742F",
        "data": datetime.datetime(2024, 4, 1),
        "importador": "M. GUILLEN S.A.S",
        "exportador": "FRIVATTI",
        "incoterm": "CIP"
    },
    # 9
    "fatura_10747F": {
        "doc": PyPDF2.PdfReader(open("faturas/FATURA_10747_F-FRIVATTI/Comercial-Invoice-10747F.pdf", "rb")).pages[0].extract_text(),
        "numero_fatura": "10747F",
        "data": datetime.datetime(2024, 4, 16),
        "importador": "COPAYAN S.A",
        "exportador": "FRIVATTI",
        "incoterm": "CIP"
    },
    # 10
    "packing_list_10747F": {
        "doc": PyPDF2.PdfReader(open("faturas/FATURA_10747_F-FRIVATTI/Packing-List-10747F.pdf", "rb")).pages[0].extract_text(),
        "numero_fatura": "10747F",
        "data": datetime.datetime(2024, 4, 16),
        "importador": "COPAYAN S.A",
        "exportador": "FRIVATTI",
        "incoterm": "CIP"
    },
    # 11
    "fatura_54561506-2": {
        "doc": PyPDF2.PdfReader(open("faturas/FATURA_54561506-2-JBS-ABASTO/54561506-2-fatura.pdf", "rb")).pages[0].extract_text(),
        "numero_fatura": "54561506-2",
        "data": datetime.datetime(2024, 4, 5),
        "importador": "ABASTO DE CARNES SATURNO SA",
        "exportador": "JBS S/A",
        "incoterm": "FCA"
    },
    # 12
    "fatura_54990663-5": {
        "doc": PyPDF2.PdfReader(open("faturas/FATURA_54990663-5-JBS-ST_CLARA/54990663-5-Fatura.pdf", "rb")).pages[0].extract_text(),
        "numero_fatura": "54990663-5",
        "data": datetime.datetime(2024, 3, 22),
        "importador": "SANTA CLARA SRL",
        "exportador": "JBS S/A",
        "incoterm": "FCA"
    },
    # 13
    "fatura_55219293-1": {
        "doc": PyPDF2.PdfReader(open("faturas/FATURA_55219293-1-JBS-COPAYAN/55219293-1-Fatura.pdf", "rb")).pages[0].extract_text(),
        "numero_fatura": "55219293-1",
        "data": datetime.datetime(2024, 3, 24),
        "importador": "COPAYAN S.A.",
        "exportador": "JBS S/A",
        "incoterm": "FCA"
    },
    # 14
    "fatura_55285736-1": {
        "doc": PyPDF2.PdfReader(open("faturas/FATURA_55285736-1-JBS-MAUFE/55285736-1-Fatura.pdf", "rb")).pages[0].extract_text(),
        "numero_fatura": "55285736-1",
        "data": datetime.datetime(2024, 3, 27),
        "importador": "MAUFE SRL",
        "exportador": "JBS S/A",
        "incoterm": "FCA"
    },
    # 15
    "fatura_AS_167/2024": {
        "doc": PyPDF2.PdfReader(open("faturas/FATURA_AS_167-ASTRA/AS-167-2024-FT.pdf", "rb")).pages[0].extract_text(),
        "numero_fatura": "AS 167/2024",
        "data": datetime.datetime(2024, 4, 2),
        "importador": "SANTA CLARA SRL",
        "exportador": "FRIGORIFICO ASTRA DO PARANA LTDA",
        "incoterm": "FCA"
    },
    # 16
    "fatura_AS_168/2024": {
        "doc": PyPDF2.PdfReader(open("faturas/FATURA_AS_168-ASTRA/AS-168-2024-FT.pdf", "rb")).pages[0].extract_text(),
        "numero_fatura": "AS 168/2024",
        "data": datetime.datetime(2024, 4, 12),
        "importador": "SANTA CLARA SRL",
        "exportador": "FRIGORIFICO ASTRA DO PARANA LTDA",
        "incoterm": "FCA"
    },
    # 17
    "fatura_AS_293/2024": {
        "doc": PyPDF2.PdfReader(open("faturas/FATURA_AS_293-ASTRA/AS-293-2024-FT.pdf", "rb")).pages[0].extract_text(),
        "numero_fatura": "AS 293/2024",
        "data": datetime.datetime(2024, 4, 17),
        "importador": "SANTA CLARA SRL",
        "exportador": "FRIGORIFICO ASTRA DO PARANA LTDA",
        "incoterm": "FCA"
    },
    # 18
    "fatura_CC_0448/2024": {
        "doc": PyPDF2.PdfReader(open("faturas/FATURA_CC_0448-CITRUS/CC-0448-2024-FATURA.pdf", "rb")).pages[0].extract_text(),
        "numero_fatura": "CC 0448 / 2024",
        "data": datetime.datetime(2024, 4, 12),
        "importador": "CONAPROLE",
        "exportador": "CITRUS COMMODITIES S.A.",
        "incoterm": "CFR"
    },
    # 19
    "fatura_PO_495221": {
        "doc": PyPDF2.PdfReader(open("faturas/FATURA_PO_495221-FRIBAL/Fatura-PO-495221-Abrogo.pdf", "rb")).pages[0].extract_text(),
        "numero_fatura": "PO 495221",
        "data": datetime.datetime(2024, 4, 9),
        "importador": "PARKER - MIGLIORINI INTERNATIONAL - GmbH",
        "exportador": "Fribal",
        "incoterm": "FCA"
    },
    # 20
    "fatura_PO_495491": {
        "doc": PyPDF2.PdfReader(open("faturas/FATURA_PO_495491-FRIBAL/Fatura-PO-495491-Delgon.pdf", "rb")).pages[0].extract_text(),
        "numero_fatura": "PO 495491",
        "data": datetime.datetime(2024, 4, 9),
        "importador": "PARKER - MIGLIORINI INTERNATIONAL - GmbH",
        "exportador": "Fribal",
        "incoterm": "FCA"
    },
    # 21
    "fatura_PO_496475": {
        "doc": PyPDF2.PdfReader(open("faturas/FATURA_PO_496475-FRIBAL/Fatura-PO-496475-Abrogo.pdf", "rb")).pages[0].extract_text(),
        "numero_fatura": "PO 496475",
        "data": datetime.datetime(2024, 4, 24),
        "importador": "PARKER - MIGLIORINI INTERNATIONAL - GmbH",
        "exportador": "Fribal",
        "incoterm": "FCA"
    }
}

'''

            "doc": PyPDF2.PdfReader(open("faturas/** PASTA **/** NOME DO ARQUIVO **", "rb")),
            "numero_fatura": "",
            "data": datetime.datetime(),
            "importador": "",
            "exportador": "",
            "incoterm": ""

'''